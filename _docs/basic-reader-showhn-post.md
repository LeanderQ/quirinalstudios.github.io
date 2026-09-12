# Basic Reader — Show HN Launch Post

Last updated: September 2026

Draft for a Show HN submission. Checked against the official guidelines at
https://news.ycombinator.com/showhn.html before writing:

- Must link to something people can actually interact with — submit the App
  Store link as the URL, not the marketing site (which would read as a
  landing page).
- "You must be available to discuss and respond to comments" is an explicit
  rule, not just a norm — be ready to actually answer replies after posting.
- Must be non-trivial, personally created work — the post leans into the
  Claude-assisted learning story honestly, but grounds it in real technical
  depth so it doesn't read as "prompted an app into existence."
- No soliciting upvotes, no signup walls — none included here.

---

## Title

```
Show HN: Basic Reader – an RSS reader I taught myself iOS dev to build, with Claude
```

## URL to submit

```
https://apps.apple.com/app/id6781077283
```

## First-comment text (post as a reply to your own submission)

```
Hi HN — I'm the author. Basic Reader is an RSS/Atom reader for iPhone, iPad, and Mac, and it's also how I taught myself iOS development.

I used NetNewsWire for years and genuinely love it — it's a big part of why I still believe in RSS as a format. But I kept wanting filter rules that weren't there, and eventually "I wish this existed" turned into "let me see if I can build it." I'd written very little Swift before starting; I built it by pairing with Claude, treating it less like a code generator and more like a very patient senior engineer I could ask "why" until I actually understood the answer.

A few of the more interesting technical bits:

- Zero third-party dependencies. Feed parsing, networking, and search are all built on Apple's own frameworks.
- On-device semantic search using NLContextualEmbedding (a BERT-based model via the NaturalLanguage framework). It's a two-phase search: instant word-match results on every keystroke, then a 300ms-debounced semantic re-rank via cosine similarity over Accelerate. Nothing leaves the device.
- The filter engine (wildcard/regex/semantic rules, scoped to a feed, folder, or globally) went through a few rearchitectures once I had enough articles to notice it doing full-table rescans on every toggle. It now maintains a persisted per-article rule-mask index instead of recomputing visibility from scratch.
- Sync is SwiftData mirrored through CloudKit — no account system, just your existing Apple ID.
- Mac isn't a stretched iPad UI — it's Mac Catalyst with a real three-column layout, full keyboard shortcuts, and right-click context menus.
- Privacy is architectural, not a policy promise: no analytics SDKs, no backend servers at all — so there's genuinely nothing of yours for me to see. You can also disable image loading and JavaScript per-feed, which kills tracking pixels and most fingerprinting vectors in the in-app browser.

It's free to download and use for reading; a single one-time purchase (no subscription) unlocks search, filters, sync, and a couple of other things.

Happy to go into more detail on any of this — the semantic filter matching in particular went through a lot of iteration and I'd be curious what this crowd thinks of the approach.
```

## Notes before posting

- Be actually available to respond to comments for at least the first
  several hours after posting — this is a stated rule, not optional.
- The NetNewsWire mention is framed as admiration plus a specific gap
  (filter rules), not a knock on the app — keep it that way in any edits.
- Double-check the App Store link still resolves before submitting.
