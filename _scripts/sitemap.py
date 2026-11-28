#!/usr/bin/env python3
"""Builds sitemap.xml from the site's pages, and reports changed pages to IndexNow.

    python3 _scripts/sitemap.py                      rewrite sitemap.xml
    python3 _scripts/sitemap.py --ping BEFORE AFTER  send pages changed between two commits
    add --dry-run to --ping to print the request instead of sending it

A page is listed if it declares a canonical URL; news posts come from _posts/.
lastmod is the date of the last commit that changed the page's own source.
"""
import datetime
import glob
import json
import os
import re
import subprocess
import sys
import urllib.request

HOST = 'quirinalstudios.com'
BASE = f'https://{HOST}'
KEY = '140b345f3264d63e8a93eec3ad5b1afe'  # public by design: IndexNow reads it back from /<key>.txt


def git(*args):
    return subprocess.check_output(['git', *args], text=True).strip()


def modified(path):
    """UTC date of the last change; today for a change not yet committed."""
    if git('status', '--porcelain', '--', path):
        return datetime.datetime.now(datetime.timezone.utc).date().isoformat()
    stamp = int(git('log', '-1', '--format=%ct', '--', path))
    return datetime.datetime.fromtimestamp(stamp, datetime.timezone.utc).date().isoformat()


def pages():
    """Maps each public URL to the source files whose changes alter it."""
    found = {}
    for path in git('ls-files', '--cached', '--others', '--exclude-standard', '*.html').split('\n'):
        if path.startswith('_') or not os.path.exists(path):
            continue
        match = re.search(r'<link rel="canonical" href="(%s/[^"{]*)"' % re.escape(BASE),
                          open(path, encoding='utf-8').read())
        if match:
            found[match.group(1)] = [path]

    now = datetime.datetime.now(datetime.timezone.utc)
    for path in sorted(glob.glob('_posts/*.md')):
        name = re.match(r'_posts/(\d{4})-(\d{2})-\d{2}-(.+)\.md$', path)
        front = open(path, encoding='utf-8').read().split('---')[1]
        date = re.search(r'^date:\s*(\S+ \S+ [+-]\d{4})', front, re.M)
        if date and datetime.datetime.strptime(date.group(1), '%Y-%m-%d %H:%M:%S %z') > now:
            continue  # Jekyll does not publish future posts
        year, month, slug = name.groups()
        found[f'{BASE}/news/{year}/{month}/{slug}/'] = [path]
        # The news list and the app's page both list this post.
        categories = re.search(r'^categories:\s*\[(.*?)\]', front, re.M)
        listings = ['news'] + [c.strip() for c in categories.group(1).split(',')] if categories else ['news']
        for listing in listings:
            if f'{BASE}/{listing}/' in found:
                found[f'{BASE}/{listing}/'].append(path)
    return found


def write_sitemap():
    lines = ['<?xml version="1.0" encoding="UTF-8"?>',
             '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for url, sources in sorted(pages().items()):
        lines.append(f'  <url><loc>{url}</loc><lastmod>{max(map(modified, sources))}</lastmod></url>')
    lines.append('</urlset>')
    with open('sitemap.xml', 'w', encoding='utf-8') as out:
        out.write('\n'.join(lines) + '\n')
    print(f'sitemap.xml: {len(lines) - 3} pages')


def ping(before, after, dry_run):
    try:
        changed = set(git('diff', '--name-only', before, after).split('\n'))
    except subprocess.CalledProcessError:
        changed = None  # no usable earlier commit: send everything
    everything = changed is None or bool(changed & {'_layouts/post.html', '_config.yml'})
    urls = sorted(url for url, sources in pages().items() if everything or changed & set(sources))
    if not urls:
        print('IndexNow: no page changed')
        return
    body = {'host': HOST, 'key': KEY, 'keyLocation': f'{BASE}/{KEY}.txt', 'urlList': urls}
    if dry_run:
        print(json.dumps(body, indent=2))
        return
    request = urllib.request.Request('https://api.indexnow.org/indexnow', json.dumps(body).encode(),
                                     {'Content-Type': 'application/json; charset=utf-8'})
    with urllib.request.urlopen(request, timeout=30) as response:
        print(f'IndexNow: HTTP {response.status} for {len(urls)} pages')


if __name__ == '__main__':
    os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
    if '--ping' in sys.argv:
        start = sys.argv.index('--ping') + 1
        ping(sys.argv[start], sys.argv[start + 1], '--dry-run' in sys.argv)
    else:
        write_sitemap()
