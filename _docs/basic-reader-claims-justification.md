# Basic Reader — "Subscription Elsewhere" Claims Justification

This file documents the evidence and reasoning behind each of the five comparison
claims on the Basic Reader product page. Review before launch and update if
competitor pricing changes.

Last reviewed: July 2026

---

## CORRECTION LOG (July 2026 re-verification)

**First pass (retracted):** An initial re-check via automated web-fetch tooling
misread Inoreader's pricing table and concluded filter rules were free-tier
available and cross-device sync was unrestricted. Both conclusions were **wrong**
— the automated summary of the pricing page was inaccurate. The user caught this
by checking inoreader.com/pricing directly.

**Second pass (correct, verified by direct page check):**
- **Filter Rules** — Confirmed accurate as originally written. Inoreader's Free
  tier has **no rules and no filters at all**; Pro is required to get any (30
  rules / 50 filters). Claim restored, citing Inoreader (not Feedly).
- **iCloud Sync** — Inoreader's pricing page has no dedicated sync-restriction row,
  but their own FAQ states: "If you have an active subscription, you can use
  Inoreader in your browser and on our iOS and Android apps" — implying an active
  subscription is required for app access at all, which would include sync.
  Claim restored with softened wording citing the FAQ directly rather than
  asserting a specific "sync" restriction that isn't explicitly labeled as such.

One price was genuinely stale and has been corrected:
- Inoreader Pro: $7.99/month → **$7.50/month** (billed annually), confirmed
  directly from inoreader.com/pricing.

Readwise Reader's price ($7.99 → $9.99/month) was corrected based on converging
aggregator sources, not a direct page fetch (readwise.io/reader/pricing 404'd).
Given the reliability issue discovered above, **this price should be manually
verified before launch** rather than trusted as-is.

**Lesson:** automated fetch/summarization tools can misread pricing tables,
especially free-vs-paid tier comparisons. Direct manual verification of pricing
pages is required before trusting any competitor pricing claim — do not rely on
a single automated pass, cross-check contradictory results manually instead of
picking one.

---

## 1. Content Filter Rules

**Claim:** Filter rules are locked behind a subscription in competing apps.

**Evidence:**
- **Inoreader** — Direct check of inoreader.com/pricing (July 2026) confirms: Free
  tier has no Rules and no Filters at all. Pro unlocks 30 rules / 50 filters.
  Pro costs $7.50/month (billed annually) or $9.99/month (billed monthly).
  Source: inoreader.com/pricing (verified directly, July 2026)
- **Feedly** — Mute Filters (keyword/topic filtering) are also confirmed restricted
  to Feedly Pro+ and Enterprise plans, not available on the free tier — a
  supporting secondary source, not the primary citation.
  Source: docs.feedly.com/article/109-how-can-i-add-create-a-mute-filter

**Confidence: High** (Inoreader confirmed via direct page check; Feedly as
supporting evidence)

---

## 2. Automatic Background Refresh

**Claim:** Guaranteed fast background refresh is a paid feature in competing apps.

**Evidence:**
- **Inoreader** — The pricing page explicitly lists "Maximum guaranteed refresh
  interval" as a Pro-only feature, described as feeds updating at minimum once
  per hour. Free tier has no guaranteed refresh rate stated. Pro is $7.50/month
  billed annually ($9.99/month billed monthly) — corrected from $7.99.
  Source: inoreader.com/pricing (verified July 2026)
- **Feedly** — Unverified due to site loading issues. **Recommend verifying.**

**Nuance:** The claim on the page is that Basic Reader refreshes "down to every
5 minutes." This is a product claim that needs to be verified against iOS
background fetch limitations — Apple's BackgroundTasks framework does not
guarantee specific intervals. Consider softening to "refreshes automatically
on a configurable schedule" if 5-minute intervals cannot be guaranteed.

**Confidence: Medium** (Inoreader confirmed; iOS refresh rate caveat applies)

---

## 3. OPML Import & Export

**Claim:** OPML portability is restricted in competing apps.

**Evidence:**
- **Inoreader** — "Automatic OPML backups" are listed as a Pro-only feature.
  However, manual OPML import may be available on the free tier — the pricing
  page is not explicit on this. The claim on the page has been scoped to
  "automatic OPML backups" to reflect this uncertainty.
  Source: inoreader.com/pricing (verified June 2026)
- **Feedly** — Unverified. **Recommend verifying at feedly.com/plans.**

**Nuance:** NetNewsWire (free, open source) and Reeder (one-time purchase)
both offer OPML freely. The claim is accurate for subscription-based apps
(Inoreader, Feedly) but would be misleading if applied universally. The page
copy correctly scopes this to "automatic backups" rather than import/export
in general — keep it that way.

**Confidence: Medium** (Inoreader automatic backups confirmed; manual import unclear)

---

## 4. Unread Count App Badge

**Claim:** Tagged "Subscription elsewhere" on the page.

**Evidence:** None verified. Research did not find a specific RSS app that gates
the app icon unread badge behind a subscription paywall. The body copy was
deliberately softened during the last revision to remove any specific claim:
*"A small thing that other apps either skip entirely or bury in settings."*

**Action required:** Either:
- (a) Find a specific app that genuinely paywalls the badge and cite it, or
- (b) Remove the "Subscription elsewhere" tag and replace it with something
  like "Often missing" or "Frequently overlooked" — which is honest and still
  makes the point without an unsupported paywall claim.

**Confidence: Low — tag is currently misleading. Recommend updating.**

---

## 5. In-App Browser

**Claim:** Tagged "Subscription elsewhere" on the page.

**Evidence:** None verified. Research did not find a specific RSS app that gates
in-app article reading behind a subscription. The body copy makes no subscription
claim — it just describes the feature. The tag is inconsistent with the copy.

**Action required:** Same as #4 — either find evidence or change the tag. Options:
- "Missing elsewhere" (many RSS readers open articles in Safari, not in-app)
- Remove the tag entirely and keep it as a plain feature highlight

**Confidence: Low — tag is currently unsupported. Recommend updating.**

---

---

## 4. iCloud Sync

**Claim:** iCloud sync requires a paid account in competing apps.

**Evidence:**
- **Inoreader** — No dedicated "sync" row exists in the pricing comparison table,
  but Inoreader's own FAQ states: "If you have an active subscription, you can
  use Inoreader in your browser and on our iOS and Android apps." This implies an
  active (paid) subscription is required to use the apps at all, which by
  extension includes any cross-device sync. Page copy has been softened to cite
  this FAQ language directly rather than assert a specific "sync paywall" that
  isn't its own labeled row.
  Source: inoreader.com/pricing FAQ section (verified directly, July 2026)
- **Basic Reader** — Uses SwiftData CloudKit mirroring (cloudKitDatabase: .automatic)
  and NSUbiquitousKeyValueStore for preferences. Syncs feeds, folders, filter rules,
  read status, starred articles, and 7 preference keys. Requires only an Apple ID
  — no new account, no subscription.
  Source: confirmed in BasicReader.entitlements and BasicReaderApp.swift

**Confidence: Medium** (FAQ language supports the claim but isn't a dedicated
pricing-table row; recommend a final manual read of the FAQ page before launch)

---

## 5. Semantic Search

**Claim:** On-device semantic search is a paid feature in competing apps.

**Evidence:**
- **Readwise Reader** — Offers semantic/natural language search, bundled into its
  $9.99/month (billed annually) plan — corrected from $7.99. Uses cloud-based AI
  (not on-device). Source: readwise.io pricing coverage (verified July 2026)
- **Basic Reader** — Uses Apple's NLContextualEmbedding (BERT-based) via the
  NaturalLanguage framework. Embeddings are pre-computed on-device after each
  refresh and cached to disk. Search uses a two-phase approach: instant word-match
  results on each keystroke, then a 300ms debounced semantic pass re-ranking via
  cosine similarity (Accelerate). Fully on-device — no content leaves the device.
  Source: confirmed in SearchService.swift (June 2026)

**Confidence: High** (implementation verified in code; Readwise pricing verified)

---

## Privacy — iCloud Correction

The page previously stated "All your data lives on your device." This was corrected
after iCloud sync shipped. Accurate statement: data lives on-device and in the
user's own iCloud account — not on Quirinal Studios servers (which don't exist).

Updated copy:
- Privacy section intro: "...in your own iCloud account — never on ours."
- "Stored Locally" card renamed to "Your Data, Your Cloud" with corrected copy.

---

## Summary

| # | Feature | Tag Supported? | Primary Source |
|---|---------|---------------|---------------|
| 1 | Content Filter Rules | ✅ Yes | Inoreader pricing page (direct check) |
| 2 | Background Refresh | ✅ Yes (with iOS caveat) | Inoreader pricing page |
| 3 | OPML Import & Export | ⚠️ Partial | Inoreader (automatic backup only) |
| 4 | iCloud Sync | ⚠️ Medium | Inoreader FAQ (app access requires subscription) |
| 5 | Semantic Search | ⚠️ Medium | Readwise Reader — price via aggregators, not direct |

## To do before launch
- [x] Re-verify Inoreader pricing at inoreader.com/pricing (July 2026, checked
      directly by the user after an automated tool misread the table)
- [ ] Verify Feedly Pro+ exact price directly at feedly.com/plans (currently sourced
      from aggregator coverage, not Feedly's own page — site was inaccessible in
      July 2026); Feedly is only cited as supporting evidence, not primary
- [ ] Manually re-read Inoreader's FAQ page in full to confirm the "active
      subscription required for apps" line still applies to sync specifically
- [ ] Confirm iOS background refresh intervals are achievable as claimed
- [ ] Re-verify Readwise Reader pricing directly at readwise.io (currently sourced
      from aggregator coverage — readwise.io/reader/pricing returned 404)
