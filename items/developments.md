# Dune: Spice Wars -- Shared Development tree

**status:** research-integrated
**last_reconciled:** 2026-11-07
**patch note:** the node list and prerequisites come from Duneopedia (undated; its unit data equals the August 2024 notes, so it is at least as new as 2024-08-22) and agree with the Fandom node list. The cost formula is Fandom's. No Steam patch note after v2.2.5 changes a Development, but v2.2.6.32935 (2025) has no post, so its contents are unknown. Current patch v2.2.8.33026 wins; where a number comes from an older note it says so.

The Developments window opens once the first village is captured. There are four categories (Economy, Military, Statecraft, Expansion) with 9 shared nodes each, 36 in total, in four tiers. Each faction replaces some of these nodes with unique ones (unique nodes: `items/upgrades.md`).

_source: https://dune-spice-wars.github.io/duneopedia/developments.html , https://dunespicewars.fandom.com/wiki/Developments 2026-11-07 · capture: web_fetch · confidence: medium · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_ [Confirmed: 2 sources, 1 language]

## Cost of a Development

The first Knowledge cost of a tier-t node with nothing yet researched is 10 x (1.036^(t+1) - 1) / 0.036: tier 1 = 20.36, tier 2 = about 31.1, tier 3 = about 42.2, tier 4 = about 53.7. Each later node multiplies its cost by 1.036 for every Development already researched. There is no per-node cost table; the cost is this formula. A completed 1-slot district in the matching category cuts that category's step cost by 15% (the v2.0 Heroes update changed 20% to 15%). Research Treaties cut the cost of the partner's techs by 20%. Resolutions can cut or raise a category's speed by 50% (`sections/landsraad.md`). [patch: the 15% rule is from 2024-03-07 and Fandom's text matches it; the 1.036 base is unverified for the current patch]

_source: https://dunespicewars.fandom.com/wiki/Developments , https://steamstore-a.akamaihd.net/news/externalpost/steam_community_announcements/5679673637652411956 2026-11-07 · capture: web_fetch · confidence: medium · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_ [Single source -- verify · class:community-wiki]

## The 36 shared nodes

Tier is the row of the tree. "Needs" is the single prerequisite node.

| Category | Tier | Node | Needs | Main effects | tier |
|---|---|---|---|---|---|
| Economy | 1 | Composite Materials | none | +10 Plascrete; unlocks Maintenance Center | none |
| Economy | 2 | Modular Parts | Composite Materials | +1 max crew; Spice Silos; Harvester Works | none |
| Economy | 2 | Advanced Engineering | Composite Materials | +2% village output per building; Mason Guild; Trade Agreement | none |
| Economy | 3 | CHOAM Integration | Modular Parts | CHOAM branch; +1 CHOAM agent slot (the exchange-rate part of the effect text is garbled in the source) | none |
| Economy | 3 | Insulated Valley | Advanced Engineering | -30% building upkeep in low-wind regions; -1 Water | none |
| Economy | 3 | Geothermal Condensers | Advanced Engineering | fuel-cell factory +10 Solari, +5 Water | none |
| Economy | 3 | Riches of Arrakis | Advanced Engineering | +10 Solari and +2% per special region | none |
| Economy | 4 | Crew Training Program | CHOAM Integration | +2 crew; +20% spice | none |
| Economy | 4 | CHOAM Support | CHOAM Integration | -15% share buy price; +0.1 exchange rate per 5% owned | none |
| Military | 1 | Survival Training | none | unlocks the Armory; Military Base | none |
| Military | 2 | Army Logistics | Survival Training | +10 Water; second gear slot | none |
| Military | 2 | Mechanization | Survival Training | Support Drone | none |
| Military | 2 | Recruitment Initiative | Survival Training | +5 command points; +20% manpower; Command Post | none |
| Military | 3 | Energy Efficiency | Mechanization | +50% fuel cell output; Fusion Plant | none |
| Military | 3 | Parallel Training | Recruitment Initiative | +2 training slots; Military Academy | none |
| Military | 4 | Parts Production | Energy Efficiency | +20% mechanical unit HP, regeneration | none |
| Military | 4 | Military Propaganda | Parallel Training | +10 command points | none |
| Military | 4 | Siege Incentives | Parallel Training | +50% damage to main bases | none |
| Statecraft | 1 | Intelligence Network | none | +10 Standing per council on a chosen result; +100% agent speed | none |
| Statecraft | 2 | Diplomatic Maneuvers | Intelligence Network | House Gifts; Political Agreement; Embassy district | none |
| Statecraft | 2 | Spying Logistic | Intelligence Network | Assassins; +200% agent speed; Intelligence Agency | none |
| Statecraft | 3 | Counter Measures | Diplomatic Maneuvers | Landsraad Guard per 100 Influence; +1 counter-intelligence agent | none |
| Statecraft | 3 | Landsraad Support | Diplomatic Maneuvers | +50 max Influence per agent; +1 Landsraad slot | none |
| Statecraft | 3 | Stealth Gear | Spying Logistic | refund 20% Intel; -50% detection | none |
| Statecraft | 3 | Nefarious Contracts | Spying Logistic | -50% Assassin cost; +1 cell | none |
| Statecraft | 4 | Insider Trading | Landsraad Support | -20% sell price; 1 Influence per share (the v2.2.4 value) | none |
| Statecraft | 4 | Spying Mastery | Stealth Gear | +5 max agents (10 to 15) | none |
| Expansion | 1 | Local Dialect Studies | none | -15% annex Authority; +1 Water per village | none |
| Expansion | 2 | Lay of the Land | Local Dialect Studies | +0.5 Knowledge per village; Research Agreement | none |
| Expansion | 2 | Local Hubs | Local Dialect Studies | -15% village building cost; Investment Office | none |
| Expansion | 2 | Native Customs | Local Dialect Studies | +20% Authority from agents; -30% annex cost with a revealed Sietch | none |
| Expansion | 3 | Civilian Defense Force | Local Hubs | +1 militia slot; +150 militia HP | none |
| Expansion | 3 | Outpost Logistics | Native Customs | -30% annex penalty; +1 Arrakis agent slot | none |
| Expansion | 3 | Valuable Trinkets | Native Customs | +100% Sietch trade; Crafts Workshop | none |
| Expansion | 4 | Border Defense | Civilian Defense Force | +1 missile battery; +30% power; militia armor (see the conflict below) | none |
| Expansion | 4 | Wonders of the Desert | Valuable Trinkets | +30% special-region output | none |

_source: https://dune-spice-wars.github.io/duneopedia/developments.html 2026-11-07 · capture: web_fetch · confidence: medium · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_ [Single source -- verify · class:community-wiki]

Two values disagree with the 2024-03-07 Heroes of Dune changelist: Border Defense militia armor is +4 in Duneopedia and +2 in the changelist, and Energy Efficiency is +50% in Duneopedia and +30% in the changelist. P3 found a second publisher for the +30%: a French video guide (2024-03-30) says Energy Efficiency gives "-1 Fuel Cell for mechanical units, plus 30%" and is "almost mandatory". Duneopedia is undated but agrees with the 2024-08 notes on other points, so it may be newer than both; no patch note changes Energy Efficiency, so the current value is unverified. The later value was not found. Insider Trading's 1 Influence per share matches the 2024-12-10 note.

_source: https://dune-spice-wars.github.io/duneopedia/developments.html , https://docs.google.com/document/d/1kgajYkMYh6QC1wzq8RQfmYiiNiTF7-svVo3t1nQmE0I , https://www.youtube.com/watch?v=ZFNAL3cVmoM 2026-11-07 · capture: web_fetch · confidence: low · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_ [Contradicted across sources -- see notes]

## Second Armory gear slot

Army Logistics (Military tier 2, needs Survival Training) unlocks the second gear slot. In Duneopedia's faction data it exists only in the Atreides and Ecaz Military trees (Duneopedia lists it as one of the 36 shared nodes, so whether "shared" is right for it is unclear). The other four free factions have their own unique Military development for the second slot (`items/upgrades.md`). The Ecaz double-source bug was fixed 2023-12-14. [patch: Duneopedia undated; current status unverified]

_source: https://dune-spice-wars.github.io/duneopedia/developments.html , https://docs.google.com/document/d/1ZXpuWBrSc2Zp64P02O7baujPmmeAeJyYV84W4GORpys 2026-11-07 · capture: web_fetch · confidence: medium · enemy-tier: 1 · puzzle-tier: 1 · category: mainline · spoiler: progression_ [Single source -- verify · class:community-wiki]

> **Cross-system dependency** -- see `dependencies.md` DEP-012.

## Faction-unique replacement nodes seen in P2

Atreides: Local Community, Urban Planning, Post-Trauma Reintegration, Atreides Sympathizers, Sustainable Spying, Veteran Militia. Ecaz: Inspiring Standard, Logistical Flourish. Harkonnen: Work Ethics, Cruel Reputation, Landsraad Whispers, Enhanced Questioning. (Full unique lists per faction: `items/upgrades.md`.)

_source: https://dune-spice-wars.github.io/duneopedia/developments.html 2026-11-07 · capture: web_fetch · confidence: medium · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_ [Single source -- verify · class:community-wiki]

Vernius (paid DLC, P3): Technological Exchange, Heretical Computing, Holistic Thinking, Physical Wiring, Sequential Thinking, Neural Tropism, Automated Defenses, Entropic Engineering, Spice Enlightenment, Water Batteries, Guild Collaboration, Automated Manufacture. Water Batteries replaces Army Logistics as the second-Armory-slot development, which answers part of the Army Logistics scope question for Vernius only (`items/upgrades.md`, `factions/vernius.md`).

_source: https://dune-spice-wars.github.io/duneopedia/vernius.html , https://steamstore-a.akamaihd.net/news/externalpost/steam_community_announcements/5679673637652411370 2026-11-07 · capture: web_fetch · confidence: high · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: dlc:vernius · entity: vernius_ [Confirmed: 2 sources, 1 language]

> see factions/vernius.md for full summary

## Development achievements

Economist, Logistician, Analyst and Sociologist read "Research all [Economy / Military / Statecraft ("Political" in Steam's text) / Expansion] Developments". No source gives the node count behind each achievement, and whether the faction-unique replacement nodes count towards "all" is unknown. The entries are in `achievements.md`.

_source: https://truesteamachievements.com/game/Dune-Spice-Wars/achievements 2026-11-07 · capture: web_fetch · confidence: medium · enemy-tier: 1 · puzzle-tier: 1 · category: mainline · spoiler: progression_ [Single source -- verify · class:editorial-en]
