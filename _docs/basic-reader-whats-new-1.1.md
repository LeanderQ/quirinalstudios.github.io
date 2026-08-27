# Basic Reader — What's New (1.1)

Last updated: August 2026

Scope: commits after the `MARKETING_VERSION = 1.1` bump (`2f633e5`, merged in
`995a74e`) through current `HEAD` (`80ed9c7`) in the BasicReader repo. Article
View Styles and the one-time-unlock/StoreKit paywall itself were merged
*before* that bump, so they're technically part of 1.0, not new in this
release — but see the caveat below.

---

## Mac App Store / App Store release notes text

```
What's New in 1.1

• Timeline — see every unread article from every feed in one combined view.
• Article View Styles — browse your feeds as a list, compact thumbnails, or full image cards.
• Smarter Filter Rules — rules now understand meaning, not just exact words. Semantic matching catches near-misses that wildcard and regex rules used to let through.
• Faster filtering — rule matching is significantly quicker, especially in large libraries.
• Fixed a bug where iCloud sync could silently stop working after a fresh install.
• Fixed a mis-sized tap target on the filter rule toggle and a flickering issue in folder filters.
```

---

## Source commits

- **Timeline**: `d183df2` — "Add Timeline: a paywalled all-feeds view" (after
  the 1.1 bump)
- **Article View Styles**: `006cfcf` — "Add paywalled article view styles and
  fix share-badge image detection" (before the 1.1 bump — included here at
  the user's request since the app hasn't actually shipped to the App Store
  yet, so the 1.0/1.1 boundary is an internal marker rather than a real prior
  release)
- **Semantic filter matching**: `f3b98e5`, `5625797`, `5f1d42a`, `1d7360a`,
  and related commits — SemanticMatcher, contextual-embedding path, word-
  embedding query expansion, wired into the filter pipeline
- **Faster filtering**: `2297256`, `dc0ca26`, `83a75b1`, `5e59ce4`, `ec7ab7f`
  and the broader FilterIndex rearchitecture (persisted masks, per-article
  rule masks, incremental drain)
- **iCloud sync fix**: `7a16f78` — "Fix silent CloudKit sync failures and the
  read-sync entitlement race"
- **UI fixes**: `c3fb571` — "Give filter rule toggle its own tap target";
  folder-filter-flickering fix (PR #123); `304da5e` — "Stop the filter index
  from flashing already-matched articles visible"

## Not included (internal/non-user-facing)

Strict-concurrency warning fixes, ReDoS probe timing changes, dedup/migration
cleanup, CI bump to Xcode 26.6, ContentView split, and other refactor/test
commits in the same range — no user-visible effect, left out of release
notes.

## To do before submitting

- [ ] Re-confirm the 1.0/1.1 boundary against whatever build was actually
      submitted to App Store Connect, if any — this doc assumes the git
      version bump as the dividing line, which may not match a real prior
      submission.
- [ ] Trim/adjust wording to fit whatever character limit the target store
      listing enforces for release notes (Apple's limit is generous — 4,000
      chars — so no trimming should be needed).
