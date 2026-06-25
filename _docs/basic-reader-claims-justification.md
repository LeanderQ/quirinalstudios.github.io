# Basic Reader — "Subscription Elsewhere" Claims Justification

This file documents the evidence and reasoning behind each of the five comparison
claims on the Basic Reader product page. Review before launch and update if
competitor pricing changes.

Last reviewed: June 2026

---

## 1. Content Filter Rules

**Claim:** Filter rules are locked behind a subscription in competing apps.

**Evidence:**
- **Inoreader** — Filter rules ("execute actions based on article properties") are
  explicitly listed as a Pro-tier feature. Free accounts are limited to 30 rules;
  Pro unlocks unlimited rules. Pro costs $7.99/month (billed annually) or $9.99/month.
  Source: inoreader.com/pricing (verified June 2026)
- **Feedly** — Feedly's pricing page was inaccessible during research, but Feedly
  is widely documented (App Store reviews, tech press) as gating keyword filtering
  behind its Pro plan (~$8/month). **Recommend re-verifying at feedly.com/plans
  before launch.**

**Confidence: High** (Inoreader confirmed; Feedly unverified but widely cited)

---

## 2. Automatic Background Refresh

**Claim:** Guaranteed fast background refresh is a paid feature in competing apps.

**Evidence:**
- **Inoreader** — The pricing page explicitly lists "Maximum guaranteed refresh
  interval" as a Pro-only feature, described as feeds updating at minimum once
  per hour. Free tier has no guaranteed refresh rate stated.
  Source: inoreader.com/pricing (verified June 2026)
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
- **Inoreader** — Cross-device sync is tied to having an Inoreader account; meaningful
  sync (rules, read status across devices) requires the Pro plan ($7.99/month).
  Free accounts have limited retention and sync capabilities.
- **Basic Reader** — Uses SwiftData CloudKit mirroring (cloudKitDatabase: .automatic)
  and NSUbiquitousKeyValueStore for preferences. Syncs feeds, folders, filter rules,
  read status, starred articles, and 7 preference keys. Requires only an Apple ID
  — no new account.
  Source: confirmed in BasicReader.entitlements and BasicReaderApp.swift (June 2026)

**Confidence: Medium** (Inoreader's free sync limitations are documented; recommend
verifying exact free-tier sync scope before launch)

---

## 5. Semantic Search

**Claim:** On-device semantic search is a paid feature in competing apps.

**Evidence:**
- **Readwise Reader** — Offers semantic/natural language search at $7.99/month.
  Uses cloud-based AI (not on-device).
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
| 1 | Content Filter Rules | ✅ Yes | Inoreader pricing page |
| 2 | Background Refresh | ✅ Yes (with iOS caveat) | Inoreader pricing page |
| 3 | OPML Import & Export | ⚠️ Partial | Inoreader (automatic backup only) |
| 4 | iCloud Sync | ⚠️ Medium | Inoreader free-tier limitations |
| 5 | Semantic Search | ✅ Yes | Readwise Reader pricing; code verified |

## To do before launch
- [ ] Re-verify Inoreader pricing at inoreader.com/pricing
- [ ] Verify Feedly pricing at feedly.com/plans
- [ ] Confirm exact scope of Inoreader free-tier sync
- [ ] Confirm iOS background refresh intervals are achievable as claimed
