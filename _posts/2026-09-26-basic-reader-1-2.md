---
title: "Basic Reader 1.2: feed previews, sharing from Safari, and feed health"
seo_title: "Basic Reader 1.2: Feed Previews and Safari Sharing"
date: 2026-09-26 09:00:00 -0400
categories: [basic-reader]
---
Feed previews, sharing from Safari, feed health indicators, and a round of speed and image fixes. What's new since 1.1:

### Feed Health (Full only)

Feeds that stop updating now show a warning icon. Long-press or right-click a feed to see "Feed Health": how many fetches have failed in a row, the error, and when it last worked.

### Feed Preview

Before you subscribe, Add Feed now shows the feed's title, description, article count, and a few sample headlines, so you can check it's the right feed before committing.

### Share from Safari (Full only)

You can now add a feed straight from Safari (or other apps) via the Share Sheet. It works even if you share a normal webpage, not just a raw feed link: it will try to find the feed automatically.

### Faster scrolling with images

If you use the Compact or Card article list styles, scrolling through feeds with lots of images should feel noticeably smoother, especially with a large number of feeds.

### Fixed: some feeds never showing images

A few feeds (xkcd was one) never loaded a thumbnail in the article list even with images enabled. Should be fixed now. Please check if any feed you know was affected looks right.

### Fixed: a feed silently stuck for weeks

If any feed's "Updated" timestamp looked stuck far in the past, that should now resolve itself on the next refresh.

### General speed improvements

Various fixes to reduce lag, especially for anyone with a large number of feeds (about 90 or more).
