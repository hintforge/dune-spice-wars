# Dune: Spice Wars -- Mechanics

**status:** research-integrated
**last_reconciled:** 2026-11-24
**patch note:** The current patch is v2.2.8.33026 (2026-11-06) and wins. The fan database Duneopedia (the main source for numbers below) carries no version stamp; its numbers match the v2.2.3 notes (2024-12-04) on every point checked. Facts from it are labelled "consistent with v2.2.3": changes in v2.2.4 to v2.2.8.33026 are not itemised in the notes except where listed below, and none of those notes changes a stat listed here. P2 re-checked this (`sections/progression.md`): no Steam post after v2.2.5 changes a stat, economy number or rule here, and Duneopedia's Hawk and Spire values equal the August 2024 notes. A v2.2.6 (2025) exists with no post, so its contents are unknown. P3 re-checked Vernius: the 2025-07-09 post (v2.2.7.32974) is the one post after v2.2.5 that changes a Vernius rule (the Harmless Gadget treaty); see `factions/vernius.md`.
**source run:** P1 and P2 were each a single deep-research run (one tool each), so no fact here is corroborated across research tools; confidence is `medium` unless two independent publications agree and no patch caveat applies.

## Terms used in this guide

- **Hegemony:** a faction's overall power score. 30,000 wins. Thresholds of 2,500, 5,000 and 10,000 unlock buildings, elite units and heroes.
- **Landsraad Standing:** political reputation, 0 to 500. Separate from Hegemony and from Influence.
- **Influence:** spendable resource that buys votes in the Landsraad Council and raises Charter priority.
- **Landsraad Council:** a vote that convenes every 20 days on three proposed Resolutions.
- **Resolution:** a one-off council vote item (non-Charter). **Charter:** a standing grant won by a council vote and held until revoked or re-voted.
- **CHOAM:** the trading company; players buy and sell CHOAM Shares, and Spice converts to Solari at a CHOAM rate.
- **District:** the bonus tier earned in a Village or Main Base when buildings of one category (Economy, Military, Statecraft) are completed.
- **Operation:** an espionage mission launched with Intel. **Sietch:** a neutral Fremen settlement any faction can ally with; different from the playable Fremen faction.

## Economy and resources

Spice converts to Solari; Plascrete builds; Manpower recruits; Water supplies villages and units; Authority annexes villages; Knowledge researches; Influence buys votes; Intel funds operations; Fuel Cells run vehicles.

| Resource | Rule | tier |
|---|---|---|
| Spice | Stockpile cap 3,000 (6,000 with a CHOAM Branch). Converts to Solari at 1.5 to 2.5 per Spice, recalculated each Spice Tax cycle. Spice Tax is due every 25 days; missing it costs -20 Landsraad Standing. Harvesters on Spice Fields are attacked by Sandworms. | none |
| Solari | Main Base gives +30. Deficit: -50% Knowledge, -100% Agent recruitment speed, -5 Landsraad Standing. | none |
| Plascrete | Main Base +30; cap 5,000. Deficit: +50% building Solari upkeep, -50% construction speed. | none |
| Manpower | Main Base +4; cap 500. Deficit: -100% unit health regeneration. | none |
| Fuel Cells | Main Base +10. Fremen cannot obtain them (their major buildings use extra Water instead). For House Vernius's Fuel Cell rules see `factions/vernius.md`. | none |
| Water | Main Base +20. Village buildings consume 2, major buildings 3 (Fremen 10). Deficit: +50% Supply drain, -50% Manpower production, unrest and rebellion. | none |
| Authority | Main Base +4; cap 500. Comes from Arrakis Infiltration; used to take Villages. | none |
| Intel | Cap 1,000. Comes from Agents and Data Centers; funds Operations. | none |
| Command Points | Main Base 22. Raised mainly by military Developments. | none |
| Hegemony gain | +600 per village on a medium map (+1,000 on a small map), +1,000 per Special Region, +1,000 per Spice Tax payment, +300 per Event. | progression |

_source: https://dune-spice-wars.github.io/duneopedia/arrakis 2026-11-07 · capture: web_fetch · confidence: medium · enemy-tier: 1 · puzzle-tier: 1 · category: mainline · spoiler: progression_ [Single source -- verify · class:community-wiki]

The Spice Tax is a Hegemony source as well as a Standing cost: each payment gives +1,000 Hegemony. Mainstream English guides miss this. [patch: consistent with v2.2.3]

_source: https://dune-spice-wars.github.io/duneopedia/arrakis 2026-11-07 · capture: web_fetch · confidence: medium · enemy-tier: 1 · puzzle-tier: 1 · category: mainline · spoiler: progression_ [Single source -- verify · class:community-wiki]

The Fandom wiki's Resolutions page lists a "Land Sale" resolution that pays 10,000 Solari for abandoning a village, an exploit-shaped option.

_source: https://dunespicewars.fandom.com/wiki/Resolutions 2026-11-07 · capture: web_fetch · confidence: medium · enemy-tier: 1 · puzzle-tier: 1 · category: mainline · spoiler: progression_ [Single source -- verify · class:community-wiki]

Auto-Recall on harvesters gives -5% Spice and tries to pull a harvester out when a Sandworm attacks (it can still die). With no Ornithopter watching, "Greed" mode gives +150% Spice during the attack but may lose the harvester. [patch: consistent with v2.2.3]

_source: https://dune-spice-wars.github.io/duneopedia/arrakis , https://steamcommunity.com/sharedfiles/filedetails/?id=3058990585 2026-11-07 · capture: web_fetch · confidence: medium · enemy-tier: 1 · puzzle-tier: 1 · category: mainline · spoiler: progression_ [Confirmed: 2 sources, 1 language]

Spice Addict ("have 5,000 Spice in stockpile") is impossible without the CHOAM Branch Main Base building, because the Spice stockpile cap is 3,000 (6,000 with the branch). Exception to "just stockpile it". [patch: consistent with v2.2.3]

_source: https://dune-spice-wars.github.io/duneopedia/arrakis , https://steamcommunity.com/stats/1605220/achievements 2026-11-07 · capture: web_fetch · confidence: medium · enemy-tier: 1 · puzzle-tier: 1 · category: mainline · spoiler: progression · achievement: SpiceAddict · achievement-hidden: no · trigger_type: threshold_ [Confirmed: 2 sources, 1 language]

> **Cross-system dependency** -- see `dependencies.md` DEP-006.

## Villages, districts and buildings

Villages: after beating the militia the capture options are Annex (spend Authority), Pillage (plunder, mostly Solari) and Liberate (only on enemy villages). Standard factions have 5 building slots (2 unlocked; extra slots cost 100, 200, 400 Plascrete); Corrino has 6 (3 unlocked); Fremen have 4 (2 unlocked; 100, 200). Each village has 2 random traits. Neutral villages farther from the Main Base have stronger militia. [patch: consistent with v2.2.3]

_source: https://dune-spice-wars.github.io/duneopedia/arrakis , https://dune-spice-wars.github.io/duneopedia/buildings 2026-11-07 · capture: web_fetch · confidence: medium · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_ [Single source -- verify · class:community-wiki]

Village traits (24 listed): Analysts, Bartering Customs, Connections, Data Brokers, Desert Miners, Former Smugglers, Former Soldiers, Glass Sculptors, Handymen, Hardworkers, Industrious, Ingenious Mind, Local Sourcing, Plunderers, Scavenger Network, Scientists, Scholarly, Strong Network, Strong-Willed, Versatile, Water Traders, Way of the Desert, Well Diggers, Youthful Eagerness.

_source: https://dune-spice-wars.github.io/duneopedia/arrakis 2026-11-07 · capture: web_fetch · confidence: medium · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_ [Single source -- verify · class:community-wiki]

Special Regions (15 listed; "all or some spawn randomly"): Acid Lakes, Crescent Ridge, Great Volcano, Imperial Basin, Moon Dew Vale, Mount Idaho, Observatory Mountain, Polar Sink (always the map centre), Sand Fall, Shield Wall, Space Wreck, The Desolation (cannot be owned), Well of Riches, White Rift, Worm Nest. Each owned region gives +1,000 Hegemony; annexing costs +30 Authority. Examples: Polar Sink allows a Water Extractor (+25 Water); Great Volcano allows a Fuel Cell Factory (+100%) and Fremen Ceremonial Caves; Mount Idaho gives +200% Plascrete Factory output; The Desolation gives -40% ground unit health daily and +400% Supply drain. [patch: consistent with v2.2.3]

_source: https://dune-spice-wars.github.io/duneopedia/arrakis 2026-11-07 · capture: web_fetch · confidence: medium · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_ [Single source -- verify · class:community-wiki]

Districts: a district bonus activates when the buildings of one category in a Village or Main Base are completed. Fremen Conquest main bases get a 1-slot district (Conquest only, v2.2.8.33019); Community Update #3 gave Fremen +1 Main Base building slot, forming a new 1-slot district. Blue (Statecraft) district bonuses 2 and 3 were buffed in v2.2.2 (+3 Influence and +5 Intel; 150 votes or 150 max Influence).

_source: https://steamstore-a.akamaihd.net/news/externalpost/steam_community_announcements/1847286114027994 , https://steamstore-a.akamaihd.net/news/externalpost/steam_community_announcements/5963413728335113504 , https://steamstore-a.akamaihd.net/news/externalpost/steam_community_announcements/1783872412139437 2026-11-07 · capture: web_fetch · confidence: medium · enemy-tier: 1 · puzzle-tier: 1 · category: mainline · spoiler: progression_ [Single source -- verify · class:official-pr]

Barracks gives gear customisation and +30% Experience gains. The Armory has a second gear slot unlocked by one specific Military development per faction (see `items/upgrades.md`).

_source: https://dune-spice-wars.github.io/duneopedia/buildings 2026-11-07 · capture: web_fetch · confidence: medium · enemy-tier: 1 · puzzle-tier: 1 · category: mainline · spoiler: progression_ [Single source -- verify · class:community-wiki]

## Spice harvesting

Harvesters on Spice Fields are attacked by Sandworms. The Worm Nest special region makes military units attract Sandworms 50% faster and gives +25% regional Spice. The Decoy Thumper operation calls a Sandworm to a region. Drones are Mechanical and "do not attract Sandworms". Fremen harvest with mobile Harvesting Teams (see `factions/fremen.md`). Steam's store text warns players to scan the landscape for wormsign or risk losing troops and harvesters.

_source: https://dune-spice-wars.github.io/duneopedia/arrakis , https://dune-spice-wars.github.io/duneopedia/gameplay , https://dune-spice-wars.github.io/duneopedia/atreides , https://store.steampowered.com/api/appdetails?appids=1605220 2026-11-07 · capture: web_fetch · confidence: medium · enemy-tier: 1 · puzzle-tier: 0 · category: mainline · spoiler: none_ [Confirmed: 2 sources, 1 language]

Fremen only: Thumpers allow wormriding, and at 5,000 Hegemony thumpers are generated passively. Community Update #4: the Sandworm moves at speed 25 (was 15) during wormriding.

_source: https://steamstore-a.akamaihd.net/news/externalpost/steam_community_announcements/1783238125343186 , https://dune-spice-wars.github.io/duneopedia/fremen 2026-11-07 · capture: web_fetch · confidence: medium · enemy-tier: 1 · puzzle-tier: 1 · category: mainline · spoiler: progression_ [Confirmed: 2 sources, 1 language]

## Military and units

Command Points cap armies. Supply (range from your territory) drains outside territory; Water raises non-mechanical Supply range. Each faction fields 3 basic ground units. Per-faction stats are in `factions/`.

_source: https://dune-spice-wars.github.io/duneopedia/arrakis , https://dune-spice-wars.github.io/duneopedia/atreides 2026-11-07 · capture: web_fetch · confidence: medium · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_ [Single source -- verify · class:community-wiki]

Beyond the 3 basic ground units, each faction also fields 1 drone (needs Mechanization), 1 elite ground unit (5,000 Hegemony), 2 spaceships (Spacing Guild Branch required; Fremen use a Recycling Plant) and 2 heroes (10,000 Hegemony).

_source: https://dune-spice-wars.github.io/duneopedia/arrakis , https://dune-spice-wars.github.io/duneopedia/atreides 2026-11-07 · capture: web_fetch · confidence: medium · enemy-tier: 1 · puzzle-tier: 1 · category: mainline · spoiler: progression_ [Single source -- verify · class:community-wiki]

Neutral and enemy-AI units (HP / Power / Armor). [patch: consistent with v2.2.3]

| Unit | Stats | tier |
|---|---|---|
| Militia | 300 / 11 / 4 | none |
| Ranged Militia | 250 / 12 | none |
| Demolition Militia | 250 / 6 | none |
| Heavy Militia | 400 / 13 / 6 | none |
| Raider (local raiders) | 300 / 14 / 4 | none |
| Raider Artificer | stats not captured | none |
| Ranged Raider | 300 / 18 | none |
| Renegade | 600 / 17 / 6 | none |
| Demolition Renegade | 400 / 28 | none |
| Renegade Drone, Renegade Ship | stats not captured | none |

_source: https://dune-spice-wars.github.io/duneopedia/units 2026-11-07 · capture: web_fetch · confidence: medium · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_ [Single source -- verify · class:community-wiki]

Hireling and neutral-style units. [patch: consistent with v2.2.3]

| Unit | Rule | tier |
|---|---|---|
| Ornithopter | 300 Solari; you start with 1 | none |
| Mercenary | 800 Solari; needs 10% of CHOAM Shares; lasts 20 days; 300 HP, 15 Power | progression |
| Assassin | 200 Intel; needs the Spying Logistic development; kills one non-mechanical unit then disbands | progression |

_source: https://dune-spice-wars.github.io/duneopedia/units 2026-11-07 · capture: web_fetch · confidence: medium · enemy-tier: 1 · puzzle-tier: 1 · category: mainline · spoiler: progression_ [Single source -- verify · class:community-wiki]

Combat rework of 2024-03-07 (Heroes of Dune update): armor can no longer be shredded, but every faction has a flat armor-reducing unit and a unit built for high armor; elite units arrive at 5,000 Hegemony; gear is free to install and costs Solari only to remove or swap; Rally Points can be placed anywhere inside Airfield range (Fremen use unpillaged allied Sietches); stealthy units are now detected only by Probe Setup, a Monitoring Station village building, or a rare gear or hero effect. This is the likely reason pre-2024-03 unit and stealth guides are wrong on the current patch. Flat armor reducers named in the same notes: the Atreides Heavy Weapon Squad (-2 armor on its target), the Ecaz Squire (-2), the Harkonnen Combat Probe (nearby enemies -2); the Smuggler Sniper and the Ecaz Musketeer carry "Armor Penetration". Open question: Duneopedia (undated, at least as new as 2024-08-22) still lists "Demolition: Area damage; 30% chance to destroy Armor" for several units and "50% Armor destroy chance" for the Altar's siege weapons, while no patch note after 2024-03-07 mentions Demolition. Whether the 30% is live is unverified and is not stated here as a rule (`sections/conflicts.md`).

_source: https://steamstore-a.akamaihd.net/news/externalpost/steam_community_announcements/5679673637652411956 , https://dune-spice-wars.github.io/duneopedia/units 2026-11-07 · capture: web_fetch · confidence: low · enemy-tier: 1 · puzzle-tier: 1 · category: mainline · spoiler: progression_ [Contradicted across sources -- see notes]

## Espionage and operations

Agents: the first agent starts recruiting after the first village capture, 10 days by default, later agents progressively slower. Default cap 10 (15 with Spying Mastery); up to 3 agents per spying field (Harkonnen +1 slot). [patch: consistent with v2.2.3]

_source: https://dune-spice-wars.github.io/duneopedia/gameplay 2026-11-07 · capture: web_fetch · confidence: medium · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_ [Single source -- verify · class:community-wiki]

Agent traits (14): Artist, Bene Gesserit, Brainwashed, Charismatic, Council Agent, Engineer, Fremen Sibling, Ghost, Intendant, Mentat, Merchant, Psychologist, Recruiter, Suk Doctor. [patch: consistent with v2.2.3]

_source: https://dune-spice-wars.github.io/duneopedia/gameplay 2026-11-07 · capture: web_fetch · confidence: medium · enemy-tier: 1 · puzzle-tier: 1 · category: mainline · spoiler: progression_ [Single source -- verify · class:community-wiki]

Assignments: Enemy Faction +3 Intel; Arrakis +1 Authority; Spacing Guild +1 Manpower; CHOAM +10 Solari; Landsraad +1 Influence; Counterintelligence (1% daily capture chance, 10% detect, 10% capture-on-detect). Intelligence levels per field: L1 reveals borders, village production, councilors, development counts and unlocks Infiltration Cells; L2 reveals Main Base buildings, units and agents; L3 unlocks Assassination. [patch: consistent with v2.2.3]

_source: https://dune-spice-wars.github.io/duneopedia/gameplay 2026-11-07 · capture: web_fetch · confidence: medium · enemy-tier: 1 · puzzle-tier: 1 · category: mainline · spoiler: progression_ [Single source -- verify · class:community-wiki]

Operations take 3 days to prepare. Difficulty Easy, Medium, Hard, Epic, Special carries complication chances of 0, 5, 10, 15, 0% per day, a 30% detection chance and 0, 20, 40, 60% capture-on-detection (Easy to Epic). Exception to "operations are risk-free if easy": Easy operations have 30% detection but 0% capture; the risk rises with difficulty. Common operations: Probe Setup (50 Intel), Defense Sabotage, Leave Order, Supply Drop, Scavenger Team (100 Intel, Easy); Decoy Thumper, EMP Bomb (200 Intel + 200 Solari, Medium); Administrative Burden, Defense Breaches (500 + 500, Hard). Each free faction has three unique operations (Easy, Medium, Hard), listed in `factions/`. Community Update #3 changed EMP Bomb to -50% attack speed and -20% speed for mechanical units, removing -50% power, and made Defense Breaches stop stacking.

_source: https://dune-spice-wars.github.io/duneopedia/gameplay , https://steamstore-a.akamaihd.net/news/externalpost/steam_community_announcements/5963413728335113504 2026-11-07 · capture: web_fetch · confidence: medium · enemy-tier: 1 · puzzle-tier: 1 · category: mainline · spoiler: progression_ [Confirmed: 2 sources, 1 language]

Assassination chain: Infiltration Cells (100 Intel, needs target level 1), Cell Search (200 Solari), Assassination (500 Intel + 1,000 Solari; needs Target faction level 3 and level 1 in Arrakis, Spacing Guild, CHOAM and Landsraad) removes the target leader, and a successful assassination can win the game. Community Update #3 added "Assassination tips" (on by default). Since v2.2.3 the Imperial Intelligence resolution blocks new Infiltration Cells.

_source: https://dune-spice-wars.github.io/duneopedia/gameplay , https://steamstore-a.akamaihd.net/news/externalpost/steam_community_announcements/5963413728335113504 , https://steamstore-a.akamaihd.net/news/externalpost/steam_community_announcements/1784506359205976 2026-11-07 · capture: web_fetch · confidence: medium · enemy-tier: 2 · puzzle-tier: 2 · category: mainline · spoiler: late-game_ [Confirmed: 2 sources, 1 language]

## Landsraad, council and CHOAM

The Council convenes every 20 days with three Resolutions; only one Charter is held at a time; minimum Charter priority is 50, and spending Influence raises a Charter's priority (10 Influence gives +20 at best, +1 at worst). The first Charter win pays 2,000 Solari + 20 Standing. You cannot be eligible at the first Council. [patch: Fandom page consistent with v2.2.3/v2.2.4]

_source: https://dunespicewars.fandom.com/wiki/Charter 2026-11-07 · capture: web_fetch · confidence: medium · enemy-tier: 1 · puzzle-tier: 1 · category: mainline · spoiler: progression_ [Single source -- verify · class:community-wiki]

Standing tiers and losses. [patch: consistent with v2.2.3; Community Update #4 raised the 30% CHOAM-ownership bonus to +200 max Influence]

| Standing | Effect | tier |
|---|---|---|
| 0-99 Pariah | no vote, -3 Influence production, +300% share buying cost; a Landsraad Guard attacks your Main Base every 20 days | progression |
| 100-199 Low | -2 Influence production, +100% share buying cost (Fandom, P2) | progression |
| 200-299 Medium | no listed effect; dropping below 250 risks losing Charters | progression |
| 300-399 High | +100 max Influence, +1 production, -10% buy cost | progression |
| 400-500 Very High | +200 max Influence, +2 production, -15% buy cost | progression |
| Losses | missed Spice Tax -20; betraying a Truce -100; using Nuclear Warheads -500; recruiting a Hero Ghola -30 | progression |

_source: https://dune-spice-wars.github.io/duneopedia/arrakis , https://dunespicewars.fandom.com/wiki/Landsraad_Standing , https://steamstore-a.akamaihd.net/news/externalpost/steam_community_announcements/1783238125343186 2026-11-07 · capture: web_fetch · confidence: medium · enemy-tier: 1 · puzzle-tier: 1 · category: mainline · spoiler: progression_ [Confirmed: 2 sources, 1 language]

Gains, the full list of losses and the voting rules are in `sections/landsraad.md`. The Fandom "Landsraad Standing" page was read in P2 and agrees with the tier numbers above; Fandom labels its own gain and loss lists "incomplete".

Charters (five). Common Charters need 250 Standing plus the stated condition. Water Seller's Union condition was 50 Water production and became 70 in v2.2.2 (official).

| Charter | Condition | Effect | tier |
|---|---|---|---|
| Speaker of the Council | 250 Standing + 600 Influence spent on votes | reroll 1 resolution per council | progression |
| Judge of the Council | 250 Standing + 2,000 military Experience | trains Landsraad Guards/Judges | progression |
| Water Seller's Union | 250 Standing + 70 Water production | +2 Solari per positive Water | progression |
| Eye of the Council | 250 Standing + 7 assigned Agents | +2 extra Agents with traits | progression |
| Dune Governorship | 450 Standing + hold 1 Charter (one exception, in the claim below the table) | +300 max Influence, +3 Influence production; first election pays 10,000 Solari and guarantees "Loss of Rights" on the next council | late-game |

_source: https://dunespicewars.fandom.com/wiki/Charter 2026-11-07 · capture: web_fetch · confidence: medium · enemy-tier: 2 · puzzle-tier: 2 · category: mainline · spoiler: late-game_ [Single source -- verify · class:community-wiki]

An Atreides at 10,000 Hegemony needs only the Standing for the Dune Governorship, with no held Charter.

_source: https://dune-spice-wars.github.io/duneopedia/atreides 2026-11-07 · capture: web_fetch · confidence: medium · enemy-tier: 2 · puzzle-tier: 2 · category: mainline · spoiler: late-game_ [Single source -- verify · class:community-wiki]

Water Seller's Union Charter needs 70 Water production (was 50 before v2.2.2).

_source: https://steamstore-a.akamaihd.net/news/externalpost/steam_community_announcements/1783872412139437 , https://dunespicewars.fandom.com/wiki/Charter 2026-11-07 · capture: web_fetch · confidence: high · enemy-tier: 1 · puzzle-tier: 1 · category: mainline · spoiler: progression_ [Confirmed: 2 sources, 1 language]

Dune Governorship, Political victory length: Fandom says the Governor must hold the title 30 days; Duneopedia says 45 days; the 2023-24 Steam beginner guide says 30; three 2022 early-access pages say 60. The only official statement (2022-07-29) says the time was "slightly increased to allow for 2 Landsraad voting phases" and gives no number, and no source gives the value on v2.2.8.33026. Unresolved; do not state any number as fact. The full source table is in `sections/landsraad.md`.

_source: https://dunespicewars.fandom.com/wiki/Charter , https://dune-spice-wars.github.io/duneopedia/gameplay , https://steamcommunity.com/sharedfiles/filedetails/?id=3058990585 , https://steamstore-a.akamaihd.net/news/externalpost/steam_community_announcements/4587497456683917161 , https://gamerant.com/dune-spice-wars-win-conditions-victory-how/ 2026-11-07 · capture: web_fetch · confidence: low · enemy-tier: 2 · puzzle-tier: 2 · category: mainline · spoiler: late-game_ [Contradicted across sources -- see notes]

Fremen Governorship condition: control 20% of the map, ally all non-devastated Sietches, and keep at least 75% of Sietches non-devastated. Community Update #3 states this as "1/5 of the map, ally all non-devastated sietches, at least 3/4 not devastated".

_source: https://dunespicewars.fandom.com/wiki/Charter , https://steamstore-a.akamaihd.net/news/externalpost/steam_community_announcements/5963413728335113504 2026-11-07 · capture: web_fetch · confidence: high · enemy-tier: 2 · puzzle-tier: 2 · category: mainline · spoiler: late-game_ [Confirmed: 2 sources, 1 language]

Resolutions: the Fandom wiki lists 38 non-Charter resolutions (Agenda Contracts to War of Assassins), each with an effect and whether it affects one faction or all. Official reworks in v2.2.3: Portfolio Scrutiny (cannot buy shares; selling pays 3 Hegemony per share), CHOAM Dilution (20% of owned shares destroyed), Sale Incentive (CHOAM ownership bonuses blocked; lose 20 Solari per share at the next council), Labor Rights (+100% military unit upkeep), Imperial Intelligence (also blocks new Infiltration Cells); share price effects of buying and selling are 50% stronger. Community Update #4: Landsraad Support gives 5 Punishers, Spacing Guild Resources gives +10 Armor. The Fandom text matches these exactly.

_source: https://dunespicewars.fandom.com/wiki/Resolutions , https://steamstore-a.akamaihd.net/news/externalpost/steam_community_announcements/1784506359205976 , https://steamstore-a.akamaihd.net/news/externalpost/steam_community_announcements/1783238125343186 2026-11-07 · capture: web_fetch · confidence: high · enemy-tier: 1 · puzzle-tier: 1 · category: mainline · spoiler: progression_ [Confirmed: 2 sources, 1 language]

Voting phase rules (v2.2.4, 2024-12-10): other factions' Influence, Solari and CHOAM ownership are hidden during voting; CHOAM Shares cannot be bought during voting; selling shares no longer lowers the price instantly (applied at the end of the council); Insider Trading gives +1 Influence per share sold (was +2 from Community Update #4), and with Insider Trading, selling during voting pays 50% less Solari. Current: 1 (v2.2.4, unchanged in the later notes read).

_source: https://steamstore-a.akamaihd.net/news/externalpost/steam_community_announcements/1785321795762338 , https://steamstore-a.akamaihd.net/news/externalpost/steam_community_announcements/1783238125343186 2026-11-07 · capture: web_fetch · confidence: medium · enemy-tier: 1 · puzzle-tier: 1 · category: mainline · spoiler: progression_ [Single source -- verify · class:official-pr]

Timers: v2.2.3 (2024-12-04) made "Slow" the multiplayer default Landsraad timer and lengthened preliminary phases. P2 filled in the numbers: Slow gives preliminary phases of up to 1 min 30 s each and a vote of up to 5 min; Fast gives 30 s and 45 s. [patch: 2024-12-04; unchanged in the later notes read]

_source: https://steamstore-a.akamaihd.net/news/externalpost/steam_community_announcements/1784506359205976 2026-11-07 · capture: web_fetch · confidence: medium · enemy-tier: 1 · puzzle-tier: 1 · category: mainline · spoiler: progression_ [Single source -- verify · class:official-pr]

CHOAM: owning more than 50% of CHOAM Shares is the Economic victory (the achievement text says "more than half"). Owning 10% of Shares allows hiring Mercenaries. CHOAM opens about one month into a game.

_source: https://dune-spice-wars.github.io/duneopedia/gameplay , https://vandal.elespanol.com/logros/pc/dune-spice-wars/111674 , https://dune-spice-wars.github.io/duneopedia/units 2026-11-07 · capture: web_fetch · confidence: medium · enemy-tier: 2 · puzzle-tier: 2 · category: mainline · spoiler: late-game_ [Confirmed: 2 sources, 1 language]

> **Cross-system dependency** -- see `dependencies.md` DEP-002.
> **Cross-system dependency** -- see `dependencies.md` DEP-003.
> **Cross-system dependency** -- see `dependencies.md` DEP-007.
> **Cross-system dependency** -- see `dependencies.md` PON-001.
> **Cross-system dependency** -- see `dependencies.md` PON-003.

## Alliances, treaties and Sietches

Sietches spawn randomly and are invisible until detected. They raid nearby player villages (more often at low relation) and trade 10 Water for a Sietch-specific resource; relation rises with trade; at relation 100 you may ally the Sietch for one trait. Fremen can ally Sietches outside their territory. 12 Sietch traits: Arrakis Heart, Commercial Hub, Helping Hand, Tool Makers, Arrakis Harvesters, Heralds of Revolution, Scouts of Secret Paths, Training Grounds, Arrakis Collectors, Fremen Agents, Fremen Brotherhood, Fremen Scientists. Relation 100 comes from trade, territory control and an assigned agent; an ally is lost if the Sietch is pillaged. [patch: consistent with v2.2.3]

_source: https://dune-spice-wars.github.io/duneopedia/arrakis , https://steamcommunity.com/sharedfiles/filedetails/?id=3058990585 2026-11-07 · capture: web_fetch · confidence: medium · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_ [Confirmed: 2 sources, 1 language]

Since v2.2.3 every Sietch has an integrated missile battery that only targets flying units engaged with its militia; flying units no longer trigger a Sietch attack. Community Update #3 made pillaged ("devastated") Sietches unbuildable for Fremen unless repopulated at large cost.

_source: https://steamstore-a.akamaihd.net/news/externalpost/steam_community_announcements/1784506359205976 , https://steamstore-a.akamaihd.net/news/externalpost/steam_community_announcements/5963413728335113504 2026-11-07 · capture: web_fetch · confidence: medium · enemy-tier: 1 · puzzle-tier: 1 · category: mainline · spoiler: progression_ [Single source -- verify · class:official-pr]

Truces: betraying a Truce costs -100 Standing; Lawful Aggression (achievement) ends a Truce legally by spending Influence, avoiding that cost. The exact Influence price was not found in P1 or P2. "First Step" needs the other faction (human or AI) to accept a proposed Truce. Whether Ecaz can break a Truce is disputed (see `factions/ecaz.md`; the dated official note says it can since 2024-11-18). Each active Truce gives Standing every council (`sections/landsraad.md`).

_source: https://dune-spice-wars.github.io/duneopedia/arrakis , https://www.wemod.com/cheats/dune-spice-wars-trainers/achievements 2026-11-07 · capture: web_fetch · confidence: medium · enemy-tier: 1 · puzzle-tier: 1 · category: mainline · spoiler: progression_ [Confirmed: 2 sources, 1 language]

> **Cross-system dependency** -- see `dependencies.md` DEP-001.
> **Cross-system dependency** -- see `dependencies.md` DEP-009.

## Heroes

Heroes unlock at 10,000 Hegemony, cost 1,000 Solari (Fremen Chani and Otheym: 1,000 Solari + 150 Authority; whether the first pick is free is an open conflict in `sections/conflicts.md`), take 15 days to recruit and have 20 Solari upkeep. When a hero dies you may bring it back as a Ghola at a cost to both your bank account and your reputation (-30 Standing). The Heroes of Dune update shipped as a free update on 2024-03-07 alongside the paid DLC. Each hero has a global effect, local effects and one active skill. 12 heroes in the six free factions, 2 per faction; hero detail is in `factions/`.

_source: https://dune-spice-wars.github.io/duneopedia/arrakis , https://steamstore-a.akamaihd.net/news/externalpost/steam_community_announcements/5679673637652411956 , https://steamcommunity.com/stats/1605220/achievements 2026-11-07 · capture: web_fetch · confidence: medium · enemy-tier: 1 · puzzle-tier: 1 · category: mainline · spoiler: progression_ [Confirmed: 3 sources, 1 language]

Councilors are not heroes: two are chosen at game start from four per faction, and heroes (two per faction) are separate. The rosters are in `items/abilities.md`.

_source: https://dune-spice-wars.github.io/duneopedia/harkonnen , https://dune-spice-wars.github.io/duneopedia/arrakis 2026-11-07 · capture: web_fetch · confidence: medium · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_ [Single source -- verify · class:community-wiki]

> **Cross-system dependency** -- see `dependencies.md` DEP-005.

## Research

The Developments window becomes available once the first village is captured. Roughly 75% of all developments is typical in a normal game. Each faction has unique developments (counts per faction in `items/upgrades.md`); the 36 shared nodes, their prerequisites and the Knowledge cost formula are in `items/developments.md`, and the Armory gear options are in `items/gear.md`.

_source: https://steamcommunity.com/sharedfiles/filedetails/?id=3058990585 2026-11-07 · capture: web_fetch · confidence: medium · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_ [Single source -- verify · class:forum]

> **Cross-system dependency** -- see `dependencies.md` DEP-012.

## Victory conditions

How a match is won in skirmish and multiplayer (Conquest uses a different rule set: `sections/conquest.md`). Steam achievements pair with them: Hegemon (Hegemony), Governor (Governorship), Conqueror (destroy the last base), Assassin (assassinate the last opponent), Magnate (more than half of CHOAM).

_source: https://vandal.elespanol.com/logros/pc/dune-spice-wars/111674 , https://www.wemod.com/cheats/dune-spice-wars-trainers/achievements 2026-11-07 · capture: web_fetch · confidence: medium · enemy-tier: 2 · puzzle-tier: 2 · category: mainline · spoiler: late-game_ [Confirmed: 2 sources, 1 language]

| Victory | Condition | tier |
|---|---|---|
| Domination | eliminate all opposing factions by destroying Main Bases or by Assassination (two routes to one victory type) | late-game |
| Hegemony | reach 30,000 Hegemony | late-game |
| Political | be Governor of Dune (Charter) for a disputed number of days: 45 per Duneopedia, 30 per Fandom and the Steam guide, 60 in 2022 pages (see `sections/landsraad.md`) | late-game |
| Economic | hold more than 50% of CHOAM Shares | late-game |

_source: https://dune-spice-wars.github.io/duneopedia/gameplay , https://dunespicewars.fandom.com/wiki/Charter 2026-11-07 · capture: web_fetch · confidence: medium · enemy-tier: 2 · puzzle-tier: 2 · category: mainline · spoiler: late-game_ [Contradicted across sources -- see notes]

Hegemony victory (30,000) is stated by three sources and is called the easiest overall by the Steam beginner guide and a Steam discussion. Several posters note any faction can win by any route.

_source: https://dune-spice-wars.github.io/duneopedia/arrakis , https://steamcommunity.com/sharedfiles/filedetails/?id=3058990585 , https://steamstore-a.akamaihd.net/news/externalpost/steam_community_announcements/5124581515254875112 2026-11-07 · capture: web_fetch · confidence: high · enemy-tier: 2 · puzzle-tier: 2 · category: mainline · spoiler: late-game_ [Confirmed: 3 sources, 1 language]

Victory progress cards appear when someone is close to Hegemony, Economic or Political victory; the Conquest Update added a "Victory screen" button after a game.

_source: https://steamcommunity.com/sharedfiles/filedetails/?id=3058990585 , https://steamstore-a.akamaihd.net/news/externalpost/steam_community_announcements/5124581515254875112 2026-11-07 · capture: web_fetch · confidence: medium · enemy-tier: 1 · puzzle-tier: 1 · category: mainline · spoiler: progression_ [Confirmed: 2 sources, 1 language]

## Hazards

Sandworms, storms and Sietch raids are the map hazards, configurable in the lobby (`settings.md`). Storms hurt units (mostly air), cut village production and block building in a hit village. Sandworm behaviour for harvesters and wormriding is under "Spice harvesting" above.

_source: https://steamcommunity.com/sharedfiles/filedetails/?id=3058990585 , https://steamstore-a.akamaihd.net/news/externalpost/steam_community_announcements/6214419350719070750 2026-11-07 · capture: web_fetch · confidence: medium · enemy-tier: 1 · puzzle-tier: 0 · category: mainline · spoiler: none_ [Confirmed: 2 sources, 1 language]

## Game modes

Five modes and a tutorial set; detail lives in `sections/`. Skirmish (Battle of Arrakis against AI), multiplayer (the same ruleset against humans) and Conquest (different rules, objectives and map) are separate: the Conquest Pressure meter, passive bonuses and mission types do not exist in Battle of Arrakis. Maps are procedurally generated: Steam's 1.0 FAQ says "procedural maps and scenarios" for Conquest, and French and Korean sources agree. Localization-mechanism class: none (confirmed).

_source: https://steamstore-a.akamaihd.net/news/externalpost/steam_community_announcements/5141476355678693098 , https://www.phonandroid.com/test-dune-spice-wars-un-excellent-jeu-de-strategie-epice-et-tout.html , https://en.namu.wiki/w/Dune:%20Spice%20Wars/%EC%A0%95%EB%B3%B5%20%EB%AA%A8%EB%93%9C 2026-11-07 · capture: web_fetch · confidence: high · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_ [Confirmed: 3 sources, 3 languages]

## Notable changes by patch (official notes unless stated)

Current patch v2.2.8.33026 (2026-11-06). The Steam news feed shows no patch note between 2024-12-12 and 2025-07-09, nor between 2025-07-09 and 2026-10-21. A version v2.2.6.32935 existed by 2025-04-21 (shown in a player screenshot) but has no Steam post, so its contents are unknown.

| Patch (date) | Change that matters | tier |
|---|---|---|
| Heroes of Dune (2024-03-07) | heroes (2 per faction at 10k Hegemony), combat/stealth/Intel rework, new councilors; Vernius appears as an opposing faction in every mode | progression |
| Community Update #3 (2024-08-01) | spectators; devastated Sietch rework; spaceship rebalance; Landsraad Judge units 40 to 25 Influence; gear swap cost 1000 to 500 Solari; Atreides/Harkonnen/Smuggler/Fremen/Ecaz tweaks | progression |
| Community Update #4 (2024-11-18) | Smugglers and Fremen playable in Conquest; six new map types; Statistics screen; Insider Trading 2 Influence per share and no CHOAM sell cooldown; Iakin rework; Ecaz can break truce | progression |
| v2.2.1 (2024-11-20) | Fremen Conquest easier; units attack villages once militia are defeated; crash fixes | progression |
| v2.2.2 (2024-11-26) | blue district bonuses 2 and 3 buffed; Water Seller 50 to 70 Water; Random map; hide-version option | progression |
| v2.2.3 (2024-12-04) | CHOAM/Council resolution reworks; Sietch missile battery; Duncan rework; many gear changes; "Slow" default | progression |
| v2.2.4 (2024-12-10) | voting hides rivals' Influence/Solari/CHOAM; no share buying while voting; Insider Trading +1 Influence | progression |
| v2.2.5 (2024-12-12) | Fremen Mobile Turret holds position; Defender of the Law fix | progression |
| v2.2.7.32974 (2025-07-09) | nuke-loading cancel/duplicate fix; devastated village buildings untargetable; assassin limits; Peaceful annex interrupted by nuclear devastation; Fremen Research Station parity; Contraband quest rewards; Sanya hidden bonus removed; disconnect handling; Vernius Harmless Gadget treaty no longer breaks when entering conflict with Vernius | progression |
| v2.2.8.33019 (2026-10-21) | Fremen Conquest 1-slot district; P2P spectators; early-leaver lobby icon; Concord Chamber infinite-Solari and Landsraad Immunity exploits fixed; hotkey options scroll fix; modding hooks; in-game /enableCheats (disables achievements) | progression |
| v2.2.8.33026 (2026-11-06) | memory leak fix, DirectX renderer, zooming to tactical view | none |

_source: https://steamstore-a.akamaihd.net/news/externalpost/steam_community_announcements/1848664643345529 , https://steamstore-a.akamaihd.net/news/externalpost/steam_community_announcements/1847286114027994 , https://steamstore-a.akamaihd.net/news/externalpost/steam_community_announcements/1803527891922277 , https://steamstore-a.akamaihd.net/news/externalpost/steam_community_announcements/1785774543521852 , https://steamstore-a.akamaihd.net/news/externalpost/steam_community_announcements/1785321795762338 , https://steamstore-a.akamaihd.net/news/externalpost/steam_community_announcements/1784506359205976 , https://steamstore-a.akamaihd.net/news/externalpost/steam_community_announcements/1783872412139437 , https://steamstore-a.akamaihd.net/news/externalpost/steam_community_announcements/1783872411945343 , https://steamstore-a.akamaihd.net/news/externalpost/steam_community_announcements/1783238125343186 , https://steamstore-a.akamaihd.net/news/externalpost/steam_community_announcements/5963413728335113504 , https://steamstore-a.akamaihd.net/news/externalpost/steam_community_announcements/5679673637652411956 2026-11-07 · capture: web_fetch · confidence: medium · enemy-tier: 1 · puzzle-tier: 1 · category: mainline · spoiler: progression_ [Single source -- verify · class:official-pr]
