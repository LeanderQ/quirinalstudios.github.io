# News post template

Copy the block below into `_posts/YYYY-MM-DD-short-name.md`.

```markdown
---
title: "Headline shown on the page and in the feeds"
seo_title: "Browser and search title, 30-60 characters"
meta_description: "What the reader gets on this page, in 110-160 characters, without marketing adjectives."
date: YYYY-MM-DD 09:00:00 -0500
categories: [basic-reader]
---
Opening paragraph. It is used as the feed summary.
```

- `categories`: `basic-reader` or `dice-with-the-universe`, which selects the app feed.
- `date`: use the real release date. A date in the future keeps the post unpublished. Use `-0400` during daylight saving time.
- Include `seo_title` and `meta_description` on every post.
