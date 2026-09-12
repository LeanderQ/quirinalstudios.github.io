# Basic Reader — r/rss Launch Post

Last updated: September 2026

Draft for a launch announcement text post on r/rss. Written in "I'm the
solo developer" voice rather than ad copy, per that subreddit's usual
tolerance for self-promotion when it's transparent and informative.

---

## Title

```
I built a subscription-free RSS reader for iPhone/iPad/Mac — free to download, one-time purchase unlocks the rest
```

## Body

```
Hey r/rss — I'm the solo developer behind Basic Reader, an RSS/Atom reader for iPhone, iPad, and Mac that just launched on the App Store.

I built this because I got tired of watching RSS apps turn into $8–10/month subscriptions for things that used to just be... a feature of the app. So Basic Reader works differently:

Free to download, free to use for reading feeds:
- Feeds & folders with drag-and-drop organization
- Background refresh on a configurable schedule
- OPML import/export (bring your subscriptions in, take them out any time)
- Swipe gestures, starring, privacy controls for image/script loading
- Full VoiceOver, Dynamic Type, and Reduce Motion support

A single one-time purchase (no subscription, ever) unlocks:
- On-device semantic search — finds articles by meaning, not just keyword matches, and nothing leaves your device
- iCloud sync across your devices
- Filter rules — wildcard, regex, and semantic/topic-based filtering
- Timeline — one combined view of every article from every feed
- Additional article view styles (list/compact/card)

No analytics SDKs, no backend servers — I don't have the infrastructure to see what you read even if I wanted to. Your data lives on-device or in your own iCloud account.

It's on iPhone, iPad, and Mac (Catalyst) with a proper three-column layout on iPad/Mac, not just a stretched phone UI.

Link: https://apps.apple.com/app/id6781077283

Happy to answer questions about feed format support, the search implementation, or anything else — this sub is a big part of why I wanted to build something that doesn't nickel-and-dime RSS readers specifically.
```

---

## Notes before posting

- Check r/rss's sidebar/wiki rules on self-promotion first — some subreddits
  require a minimum account age, a "verified developer" flair, or cap how
  often you can post your own project.
- Confirm whether the sub prefers a text post or a link post.
- Be ready to answer follow-up questions in the comments about feed format
  support (RSS + Atom, confirmed in RSSParser.swift) and the on-device
  semantic search implementation (NLContextualEmbedding via Apple's
  NaturalLanguage framework).
