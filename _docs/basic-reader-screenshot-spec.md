# Basic Reader — Screenshot Spec

## App Store Required Sizes

| Device | Resolution | Simulator to use |
|---|---|---|
| iPhone 16 Pro Max | 1320 × 2868 px | iPhone 16 Pro Max |
| iPad Pro 13" (M4) | 2064 × 2752 px | iPad Pro 13-inch (M4) |
| Mac (optional) | 2560 × 1600 px | Mac, window at 1280×800 scaled 2x |

Apple requires at least iPhone screenshots. iPad and Mac are separate slots in
App Store Connect — if you don't upload them, the iPhone screenshots are stretched
to fill, which looks bad. Upload all three.

Shoot in **dark mode** to match the app's aesthetic and your site.

---

## iPhone Screenshots (1320 × 2868)

Shoot in order — App Store shows them left to right.

### 1. Hero — Feed List
**Screen:** Main sidebar + article list, a feed open with 8–10 articles visible.
**What to show:** Folder structure in sidebar, unread counts, article titles.
**Callout:** "Your feeds. No clutter."

### 2. Reading View
**Screen:** An article open full-screen in the in-app browser or reader view.
**What to show:** Clean article text, no chrome getting in the way.
**Callout:** "Read without leaving the app."

### 3. Semantic Search
**Screen:** Search screen with a query typed and results showing — ideally results
that demonstrate semantic matching (e.g. query "climate" returning articles
that say "global warming" or "carbon emissions").
**Callout:** "Search finds what you mean."

### 4. Filter Rules
**Screen:** Filter rules list with 2–3 active rules visible (wildcard + regex).
**What to show:** Rule name, pattern, scope (global/feed/folder), match target.
**Callout:** "Kill the noise. Keep what matters."

### 5. iCloud Sync / Settings
**Screen:** Settings screen showing iCloud sync status as active.
**What to show:** The sync row confirming it's on and working.
**Callout:** "Syncs across all your devices. No account needed."

---

## iPad Screenshots (2064 × 2752)

iPad gets its own slot in App Store Connect. The three-column layout is your
biggest differentiator on this platform — make it the hero.

### 1. Three-Column Hero
**Screen:** Full three-column layout — sidebar with folders, article list in the
middle, article open on the right.
**What to show:** As much content visible as possible. Dark mode. Unread badges.
**Callout:** "Built for iPad."

### 2. Filter Rules (iPad)
**Screen:** Filter rules screen in the settings panel alongside the article list.
**Callout:** "Powerful filters. Included."

### 3. Search (iPad)
**Screen:** Search active with results, showing the wider layout.
**Callout:** "On-device semantic search."

---

## Mac Screenshots (optional but recommended)

Mac is a separate App Store page. Worth doing — it signals the app is a real
Mac app, not an afterthought.

### 1. Three-Column Window
**Screen:** Full app window at ~1280×800, three-column layout, a feed open.
Put it on a plain dark desktop background (System Settings → Wallpaper → Color).
**Callout:** "At home on Mac, too."

### 2. Menu Bar / Keyboard Nav
**Screen:** An article open, showing the menu bar and native Mac chrome.
**Callout:** "Native. Not just stretched."

---

## Figma Setup

1. Download **Facebook Design iOS 18 device frames** (free, google "facebook design
   iOS frames figma community") or search Figma Community for "iOS 18 mockup".
2. For iPad, search "iPad Pro M4 mockup figma".
3. For Mac, search "MacBook Pro mockup figma" — use a space grey / dark skin.
4. Background color: `#0f0f11` (matches the site) or a subtle gradient from
   `#0f0f11` to `#1a1a1f`.
5. Callout text: use **SF Pro Display** (or Inter as a stand-in) at ~52–64pt,
   white, above the device frame.
6. Export each at **1x** — simulator screenshots are already retina resolution.

---

## Simulator Tips

- **Cmd+S** in Simulator saves a screenshot to your Desktop.
- Set the simulator to **100% scale** (Window → Physical Size) before shooting
  so you get the full native resolution.
- Turn off the simulator's device bezel via **Features → Show Device Bezel** if
  you want a clean screen-only crop to paste into Figma frames.
- Use **Cmd+Shift+H** to go home, **Cmd+L** to lock — useful for resetting state
  between shots.
- For the iPad three-column shot, rotate to landscape if it gives you a better
  layout: **Hardware → Rotate Left/Right**.

---

## Shoot Order (fastest workflow)

1. iPhone simulator: all 5 screens in one session, dark mode on
2. iPad simulator: 3 screens
3. Mac: 2 screens (run the actual app, not simulator)
4. Drop all into Figma, frame up, add callouts
5. Export and upload to App Store Connect

Total time estimate: ~2–3 hours including Figma work.
