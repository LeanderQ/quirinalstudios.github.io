# Dice With the Universe — App Store Copy

Last updated: October 2026

Written from the product page (`dice-with-the-universe/index.html`) and checked
against the game's code and data in October 2026 — see the verification list at
the bottom.

---

## App Name

```
Dice With the Universe
```

## Subtitle (30 chars max)

```
Physics Farkle vs. History
```

26 characters. Alternate (29): `A Farkle Journey Through Time`

## Promotional Text (170 chars max)

```
Roll physics-driven dice against 15 of history's greatest minds. Push your luck, beat the bosses, and build a dice collection worthy of the ages.
```

145 characters. Promotional text can be changed any time without a new build.

## Category

Primary: Games. Suggested game subcategories (up to two allowed): Board, Strategy.
There is no Dice subcategory; confirm the exact options in App Store Connect.

## Keywords (100 chars max)

```
push,luck,risk,campaign,boss,single,player,offline,strategy,d20,d12,tabletop,3d,ancient,casual
```

94 characters. Words excluded because they are already indexed from the name,
subtitle, or category: dice, universe, farkle, physics, history, games.

---

## Description

```
God doesn't play dice with the universe. You do.

Roll real, physics-driven dice against 15 of history's greatest minds, from ancient shamans to a rogue AI, in a Farkle strategy game where every roll is a gamble and every opponent has their own idea of risk.

Free to play through the first period. A one-time purchase unlocks the full campaign and Quick Game.

--- PUSH YOUR LUCK ---

Farkle is simple to learn and hard to master. Roll, set aside your scoring dice, then decide: bank your points, or risk it all for one more throw? Bank too early and you fall behind. Push too far and you lose everything.

Every roll is real. Dice tumble, bounce, and settle using full 3D physics, with no canned animations and no predetermined outcomes.

--- RIVALS WITH PERSONALITY ---

Each opponent has their own risk tolerance and banking threshold. Genghis Khan takes bigger risks than Leonardo da Vinci. Learn how they think, then use it against them.

--- A JOURNEY THROUGH 15 PERIODS OF HISTORY ---

ORIGINS
Sit across the table from a Shaman, a Grain Keeper, Hammurabi, Akhenaten, and Qin Shi Huang. Civilization is young and the stakes are everything.

EXPANSION
Caesar, Hypatia, Genghis Khan, Zheng He, and da Vinci. The world is getting bigger, and so is what you stand to lose.

RECKONING
Louverture, Tesla, Franklin, an AI Architect, and the Last Council. The universe is watching. What will your dice say about you?

Your choices across all 15 periods shape three narrative axes in each era, and each era ends with its own reckoning. Twenty-seven ways to end the story.

--- BOSS FIGHTS AND A DICE COLLECTION ---

Every period ends with a boss who plays harder and smarter. Beat them and claim one of their dice as your own.

Unlock D4s, D8s, D12s, D20s, and more along the way. Mix and match six dice into your personal loadout and build a collection worthy of the ages.

--- A WORLD THAT SHIFTS AS YOU GO ---

Music and visual themes change with every era, from ceremonial drums to synthesized tension.

Ready to roll against history?
```

---

## Notes

- Avoid Unicode box-drawing characters (── etc.) in the description; App Store
  Connect rejects them. Plain `---` dividers and plain hyphens are safe.
- Do not add "Yahtzee" to the keywords. It is a trademark and Apple can reject
  or pull listings that use another company's marks.
- The description now says the game is free through the first period with a
  one-time purchase for the full campaign and Quick Game, matching the in-app
  unlock (`full_campaign_unlock`). Keep this in step with the product page and
  FAQ, which still only mention a possible human-art in-app purchase.
- The keyword `roguelike` was removed (the game isn't one; irrelevant keywords can
  be flagged). `risk` replaced it.
- The FAQ discloses that the current artwork is AI-assisted. The description
  doesn't mention it, so check that App Store Connect's own questionnaires
  answer consistently with the FAQ.

## Verification (checked against the game, October 2026)

- [x] Full 3D physics dice (DiceCreator `PhysicsDie`); outcomes come from the physics, not a script
- [x] 15 periods in three eras, with the opponent names listed per era
- [x] A boss ends each period and awards one of its dice
- [x] D4, D8, D12, D20 unlocks, and a loadout of six dice
- [x] Per-opponent risk tolerance and banking threshold (e.g. Genghis Khan banks at 350 with
      risk 0.45; Leonardo da Vinci at 300 with risk 0.3), hence "takes bigger risks"
- [x] Music changes per period and the visual themes change per era
- [x] 27 endings (3 x 3 x 3 archetype combinations)
- [x] Three narrative axes per era, nine in total (the old sentence named three of them
      as if they were the only three)
- [ ] Platform: the copy never names one. The page says iPhone only; the app also runs
      on iPad in compatibility mode.
- [ ] Re-read the final text in App Store Connect against the age-rating and privacy
      answers, and against the AI-assisted-artwork disclosure in the FAQ.
