# Basic Reader — App Store Copy

Last updated: August 2026 (free download + one-time unlock model)

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
Basic Reader is a fast, focused RSS reader for iPhone, iPad, and Mac. No account. No nonsense.

Most RSS apps have turned into subscription businesses — charging $8-10/month for features that should come standard. Basic Reader is free to download and free to use for reading your feeds. When you're ready for more, a single one-time purchase unlocks the full feature set — and it's yours for good. No subscription. Ever.

--- FREE ---

Feeds & Folders
Subscribe to any RSS or Atom feed. Group them into collapsible folders with drag-and-drop reordering. Unread counts appear at a glance on every feed, folder, and your app icon badge.

Background Refresh
Your feeds update automatically on a configurable schedule. Pull to refresh any time.

OPML Import & Export
Bring your subscriptions in from any other reader. Take them out just as easily. Your data is never held hostage.

Swipe Gestures
Swipe to mark articles read or unread without opening them. Accidentally marked everything read? Shake to undo.

Star Favorites
Star any article to save it for later, accessible across all your feeds.

Privacy Controls
Control image loading and Javascript to block tracking pixels and reduce data usage. No analytics SDKs. No backend. We never see what you read.

iPhone, iPad & Mac
Built natively in SwiftUI. A clean adaptive layout on iPhone, a full three-column view on iPad and Mac.

Full Accessibility
VoiceOver, Dynamic Type, and Reduce Motion support — built in from day one.

--- UNLOCK THE FULL VERSION ---

One time purchase. No subscription, no recurring fee, no tiers to upgrade later. Unlocks:

Smart Search
Search across all your articles instantly. Results are re-ranked using an on-device AI model for semantic relevance — so you find what you mean, not just what you typed. Nothing leaves your device.

iCloud Sync
Feeds, folders, filter rules, read status, starred articles, and preferences sync automatically across all your devices via iCloud. No account needed beyond your Apple ID.

Content Filter Rules
Hide the noise with wildcard, regex, or semantic filters that match by topic — not just exact words.

Timeline
A single combined view of every article from every feed, in one place.

Article View Styles
Customize how articles are displayed for a more comfortable reading experience.

--- NO SUBSCRIPTION. EVER. ---

The unlock is a one-time purchase. Whatever it includes today stays yours — nothing you've already unlocked will ever be paywalled again or moved behind a new tier.
```

2,499 characters — well under the 4,000 char limit.

---

## Notes

- Model change (August 2026): Basic Reader shipped its original App Store copy describing
  a single one-time purchase for everything. Before public launch, the app moved to a
  free-download-plus-one-time-unlock model (StoreKit product
  `com.quirinalstudios.basicreader.core`, entitlement `.full`). This description reflects
  that: the FREE section lists features with no gating; UNLOCK THE FULL VERSION lists the
  five features gated behind `PremiumFeature` — Semantic Search, Content Filters, iCloud
  Sync, Article View Styles, Timeline. Since this changed pre-launch, it does not conflict
  with the "existing features never paywalled" promise — nothing shipped to users has been
  taken away or re-gated.
- JavaScript toggle claim confirmed: `SettingsView.swift` has "Allow JavaScript in
  Articles" (`allowJavaScript` AppStorage key, off by default), wired into the in-app
  browser's WKWebView content preferences.
- Semantic filter rules claim confirmed: filter matching now includes an embedding-based
  semantic path in addition to wildcard/regex (see `SemanticMatcher.swift` and the filter
  pipeline redesign commits from August 2026).
- Avoid Unicode box-drawing characters (── etc.) — App Store Connect rejects them. Plain
  `---` dashes and em dashes (—) are fine.
- `podcast` keyword is a stretch; remove if Apple flags it during review, or once you confirm you don't support audio enclosures.
- Add `widgets`, `shortcuts` to keywords when those features ship.
- The semantic search copy ("on-device AI model") is accurate — NLContextualEmbedding (BERT) via Apple's NaturalLanguage framework, verified in SearchService.swift.
- Atom support confirmed in RSSParser.swift — handles `entry`, `summary`, `content`, `published`, `updated`, `id`.
