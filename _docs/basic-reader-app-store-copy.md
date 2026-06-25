# Basic Reader — App Store Copy

Last updated: June 2026

---

## App Name

```
Basic Reader
```

## Subtitle (30 chars max)

```
RSS & Atom. No Subscription.
```

## Keywords (100 chars max)

```
rss,feed reader,atom,news reader,rss reader,feedly,inoreader,opml,podcast,no subscription
```

91 characters. Words excluded (already indexed via name/subtitle): basic, reader, articles.

---

## Description

```
Basic Reader is a fast, focused RSS reader for iPhone, iPad, and Mac. No subscription. No account. No nonsense.

Most RSS apps have turned into subscription businesses — charging $8-10/month for features that should come standard. Basic Reader ships everything included, for a one-time price.

--- WHAT'S INCLUDED ---

Smart Search
Search across all your articles instantly. Results are re-ranked using an on-device AI model for semantic relevance — so you find what you mean, not just what you typed. Nothing leaves your device.

iCloud Sync
Feeds, folders, filter rules, read status, starred articles, and preferences sync automatically across all your devices via iCloud. No account needed beyond your Apple ID.

Content Filter Rules
Hide the noise with wildcard or regex filters, scoped to any feed, folder, or globally — applied against titles, summaries, or both. A filter indicator shows when rules are active.

Folders & Organization
Group feeds into collapsible folders with drag-and-drop reordering. Unread counts appear at a glance on every feed, folder, and your app icon badge.

Background Refresh
Your feeds update automatically on a configurable schedule. Pull to refresh any time.

OPML Import & Export
Bring your subscriptions in from any other reader. Take them out just as easily. Your data is never held hostage.

Swipe Gestures
Swipe to mark articles read or unread without opening them. Accidentally marked everything read? Shake to undo.

Stars & Favorites
Star any article to save it for later, accessible across all your feeds.

Privacy Controls
Control image loading per-feed to block tracking pixels and reduce data usage. No analytics SDKs. No backend. We never see what you read.

iPhone, iPad & Mac
Built natively in SwiftUI. A clean adaptive layout on iPhone, a full three-column view on iPad and Mac.

Full Accessibility
VoiceOver, Dynamic Type, and Reduce Motion support — built in from day one.

--- NO SUBSCRIPTION. EVER. ---

Basic Reader is a one-time purchase. Existing features will never be paywalled or removed. If new features are added at a cost, everything you already have stays exactly as it is.
```

---

## Notes

- Avoid Unicode box-drawing characters (── etc.) — App Store Connect rejects them.
- `podcast` keyword is a stretch; remove if Apple flags it during review, or once you confirm you don't support audio enclosures.
- Add `widgets`, `shortcuts` to keywords when those features ship.
- The semantic search copy ("on-device AI model") is accurate — NLContextualEmbedding (BERT) via Apple's NaturalLanguage framework, verified in SearchService.swift.
- Atom support confirmed in RSSParser.swift — handles `entry`, `summary`, `content`, `published`, `updated`, `id`.
