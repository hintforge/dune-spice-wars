# Dune: Spice Wars -- Conquest campaign

**status:** research-integrated
**last_reconciled:** 2026-11-24
**patch note:** current patch v2.2.8.33026 wins. Most rules here come from one Korean-language page (NamuWiki, machine-translated to English, page modified 2026-08-07; the P2 capture was cut off at 45,000 of 51,646 characters, so its region list is missing) plus official notes; the Steam beginner guide (2024-03) confirms the Pressure bar and the Fremen relationship bar. The Namu page was modified 2026-08-07 but still prints the pre-2024-11-18 territory goal of 8, so it does not reflect every patch change; where the two disagree the dated official note wins (the Great-House territory goal is 10). No Steam note since 2024-12-12 changes a Conquest rule except the Fremen main-base district of v2.2.8.33019. The Vernius Conquest (P3) has its full treatment in `factions/vernius.md`.

## Flow

Conquest is the campaign-like mode, single player (the unofficial CoopQuest mod adds co-op). It is entered from the solo menu "New Game" (renamed 2023-12-14). Choose a Great House (or Fremen or Smugglers since 2024-11-18) and a difficulty. A generated map of Arrakis appears with two random rival factions. Choose a faction trait: since 2023-12-14 the first one is picked after the first mission, not at the start. Two to three random border territories are pinned and you attack one; each territory has a main mission and secondary objectives. Pick two councilors before each mission. After success choose one passive bonus; the Pressure gauge then updates and the map shows the rivals' gains. A run takes about 10 to 12 hours (the developer says about 10).

_source: https://en.namu.wiki/w/Dune:%20Spice%20Wars/%EC%A0%95%EB%B3%B5%20%EB%AA%A8%EB%93%9C , https://steamcommunity.com/sharedfiles/filedetails/?id=3058990585 , https://steamstore-a.akamaihd.net/news/externalpost/steam_community_announcements/5124581515254875112 , https://docs.google.com/document/d/1ZXpuWBrSc2Zp64P02O7baujPmmeAeJyYV84W4GORpys 2026-11-07 · capture: web_fetch · confidence: medium · enemy-tier: 1 · puzzle-tier: 1 · category: mainline · spoiler: progression_ [Single source -- verify · class:community-wiki]

Conquest can be played as Atreides, Harkonnen, Corrino, Ecaz, Smugglers or Fremen, and as House Vernius of Ix with the paid DLC (Vernius can also appear as a random rival without it). The Steam beginner guide (March 2024) still said Smugglers and Fremen were excluded; Community Update #4 superseded that. Smugglers and Fremen are the "third force": they cannot be picked as a rival target in a house run. [translated from: Korean for the Namu page]

_source: https://steamstore-a.akamaihd.net/news/externalpost/steam_community_announcements/1783238125343186 , https://en.namu.wiki/w/Dune:%20Spice%20Wars/%EC%A0%95%EB%B3%B5%20%EB%AA%A8%EB%93%9C 2026-11-07 · capture: web_fetch · confidence: high · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_ [Confirmed: 2 sources, 2 languages]

Availability by date: Atreides, Harkonnen and Corrino with the Conquest Update (2023-06-22); Ecaz with 1.0 (2023-09-14); Smugglers and Fremen with Community Update #4 (2024-11-18, with seven new achievements).

_source: https://steamstore-a.akamaihd.net/news/externalpost/steam_community_announcements/1783238125343186 , https://steamstore-a.akamaihd.net/news/externalpost/steam_community_announcements/5124581515254875112 , https://steamstore-a.akamaihd.net/news/externalpost/steam_community_announcements/5141476355678693098 2026-11-07 · capture: web_fetch · confidence: medium · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_ [Single source -- verify · class:official-pr]

## Win condition

Achieve two of three goals while Pressure is under 100%. Great Houses: capture rival capital 1; capture rival capital 2; own 10 or more cumulative territories (the working value since Community Update #4, 2024-11-18; the Namu page still prints 8, see the territory-goal paragraph below); or ally the Fremen (friendship 100%). Fremen: capture two rival capitals; liberate more than 7 occupied spice regions; Fremen unity 100%. Smugglers: capture a Great House capital; use development assets in allied land 12 times; ally the Fremen; Faufreluche corruption 100%.

_source: https://en.namu.wiki/w/Dune:%20Spice%20Wars/%EC%A0%95%EB%B3%B5%20%EB%AA%A8%EB%93%9C , https://steamstore-a.akamaihd.net/news/externalpost/steam_community_announcements/1783238125343186 2026-11-07 · capture: web_fetch · confidence: medium · enemy-tier: 2 · puzzle-tier: 2 · category: mainline · spoiler: late-game_ [Single source -- verify · class:community-wiki]

The Namu page lists four lines for what it calls "two of three" goals; how the lines group into three goals is not stated, so the grouping above is a reading of the page, not a rule.

_source: https://en.namu.wiki/w/Dune:%20Spice%20Wars/%EC%A0%95%EB%B3%B5%20%EB%AA%A8%EB%93%9C 2026-11-07 · capture: web_fetch · confidence: low · enemy-tier: 2 · puzzle-tier: 2 · category: mainline · spoiler: late-game_ [Hypothesis -- unverified]

Territory goal: 10 owned territories is the working value. Community Update #4 (2024-11-18) says "8 -> 10 controlled territory to validate the conquest objective in great houses conquests", and no later change was found. NamuWiki (page modified 2026-08-07) still prints 8, which is the pre-2024-11-18 value and may simply be stale; the P2 research also read the same official note as raising the Water Gift objective from 8 to 10 territories, so whether the note means the win goal, the Water Gift objective or both is not confirmed. A 2025-07 player run ended on 9 territories with a Fremen-alliance goal. The disputed 8 is kept in `sections/conflicts.md`.

_source: https://en.namu.wiki/w/Dune:%20Spice%20Wars/%EC%A0%95%EB%B3%B5%20%EB%AA%A8%EB%93%9C , https://steamstore-a.akamaihd.net/news/externalpost/steam_community_announcements/1783238125343186 , https://www.reddit.com/r/Dunespicewars/comments/1lsxdbc/am_i_ready_for_multiplayer_any_tips/ 2026-11-07 · capture: web_fetch · confidence: low · enemy-tier: 2 · puzzle-tier: 2 · category: mainline · spoiler: late-game_ [Contradicted across sources -- see notes]

## Pressure gauge (the loss timer)

+3% per owned territory each time a zone is occupied. Above 50% the AI prioritises attacking you. At 100% after the post-mission bonus pick you lose even if the victory conditions are met. A Pressure-reduction secondary mission slows it; hard difficulty makes secondary objectives harder. Every slow mission raises Pressure; the latest safe point is while Pressure is under 50%. Mainstream Steam guides describe the bar but not the automatic loss at 100%. Pressure-cutting rewards: a successful Agony defence cuts 15%, a capital-siege secondary objective cuts 20%, and the first Ancient Sietch goal cuts 5%.

_source: https://en.namu.wiki/w/Dune:%20Spice%20Wars/%EC%A0%95%EB%B3%B5%20%EB%AA%A8%EB%93%9C , https://steamcommunity.com/sharedfiles/filedetails/?id=3058990585 2026-11-07 · capture: web_fetch · confidence: medium · enemy-tier: 2 · puzzle-tier: 2 · category: mainline · spoiler: late-game · missable: yes_ [Single source -- verify · class:community-wiki]

> **Cross-system dependency** -- see `dependencies.md` PON-002.

## Decisions that cannot be undone

A failed mission is not replayed: the result is applied, neutral territory passes to whoever won it, and Pressure jumps. The page advises restarting the run if a loss looks likely. Any territory lost, any passive bonus chosen and the Ancient Sietch choice (protect or plunder) cannot be undone. Mission choice is limited to the pinned border territories.

_source: https://en.namu.wiki/w/Dune:%20Spice%20Wars/%EC%A0%95%EB%B3%B5%20%EB%AA%A8%EB%93%9C 2026-11-07 · capture: web_fetch · confidence: medium · enemy-tier: 1 · puzzle-tier: 1 · category: mainline · spoiler: progression · missable: yes_ [Single source -- verify · class:community-wiki]

The first mission is most likely Skirmish (won by any victory type: Hegemony, Political or Economic), per the page; "most likely" is the page's hedge.

_source: https://en.namu.wiki/w/Dune:%20Spice%20Wars/%EC%A0%95%EB%B3%B5%20%EB%AA%A8%EB%93%9C 2026-11-07 · capture: web_fetch · confidence: low · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_ [Single source -- verify · class:community-wiki]

## Capital sieges

Unlocked only after quick successive wins (an adjacent capital; 2 or more of Incursion, Assault, Hired Help, Cutting the Head Off; the defender failing twice). The activation rule is a community guess; the Namu page was edited 2026-08-07 and still says no official rule exists, and no Steam post states one. The reward for each secondary objective is 5 development assets and -20% Pressure; success removes the rival from Arrakis permanently. Siege names match the achievement names.

_source: https://en.namu.wiki/w/Dune:%20Spice%20Wars/%EC%A0%95%EB%B3%B5%20%EB%AA%A8%EB%93%9C 2026-11-07 · capture: web_fetch · confidence: low · enemy-tier: 2 · puzzle-tier: 2 · category: mainline · spoiler: late-game_ [Hypothesis -- unverified]

| Siege | Rival | Defender | Attacker bonus and side objective | tier |
|---|---|---|---|---|
| Siege of Arrakeen | Atreides | all heroes, all councilors and buildings; the command-centre shield gives +60 defence and allows no direct attacks or operations until it is lifted | +10 max command points and 3 agents; the Shield Block operation needs Atreides Intel level 3 and level 1 on the other, and removes the shield for 1 day; secondary: destroy Arrakeen within 15 days of the first shield block | late-game |
| The Fortress | Harkonnen | very fast troop replenishment; two missile batteries in every enemy village (the page ties this to a Tier 4 expansion unlock; page text, not verified in game) | +10 command points; secondary: lose 20 or fewer troops | late-game |
| Downfall | Corrino | three Imperial Barges must all be destroyed; unaffiliated imperial troops raid | +10 command points; two Landsraad Judges kept after each positive agenda; secondary: 20,000 damage to the barges by Landsraad troops | late-game |
| The Red Exhibition | Ecaz | a Masterpiece in every village | +10 command points; secondary: destroy it without removing any Masterpiece | late-game |
| Singularity | Vernius (DLC) | 5 random developments patented at the start | +10 command points; secondary: destroy S-Bolt before Knowledge reaches 100 | dlc:vernius |

Result of any siege: the rival is permanently removed from Arrakis. A successful secondary objective gives +5 development assets and -20% Pressure.

_source: https://en.namu.wiki/w/Dune:%20Spice%20Wars/%EC%A0%95%EB%B3%B5%20%EB%AA%A8%EB%93%9C 2026-11-07 · capture: web_fetch · confidence: medium · enemy-tier: 2 · puzzle-tier: 2 · category: mainline · spoiler: late-game_ [Single source -- verify · class:community-wiki]

> **Cross-system dependency** -- see `dependencies.md` SEQ-002.
> **Cross-system dependency** -- see `dependencies.md` SEQ-003.

## Main mission types (15)

Each run presents main mission types chosen per attacked territory, plus one siege mission per rival capital. Faction limits: the Namu page leaves its "who can play it" cells partly unlabelled. Official Community Update #4 says Fremen Conquest has 2 exclusive missions and Smugglers 1 (2024-11-18); the earlier reading that Sietch Rescue is Fremen-only and Spice Heist Smugglers-only fits that but is not confirmed. [location inventory incomplete]

| Mission | Goal and special rules | Win or loss | tier |
|---|---|---|---|
| Skirmish | win by Hegemony, Political or Economic victory first; usually the first mission | win: first victory; loss: an AI wins | none |
| Strategic Expansion | reach a set Hegemony before the rival | win: threshold first | progression |
| Famous Summit | the same; summit regions (likely Idaho Mountains and the Great Crater) pay 100 Hegemony per day when held | win: threshold first | progression |
| Extend Your Grasp | occupy a set number of regions first; merging villages costs 60% less Authority | win: count first | progression |
| Hired Help | start with a hero, maxed units and 10,000 Solari; only mercenaries can be recruited; liberate set regions and defeat the rival's hero; needs 10% of CHOAM | win: objectives met | progression |
| Assault | destroy the rival outpost in a set number of days; unit upkeep -50%, +10 command points | win: destroyed in time (a 2024-12-12 fix covers its timer) | progression |
| Incursion | the same goal; start with a hero, recruit cost and time -50%, recovery +100%, -20 command points | win: destroyed in time | progression |
| Sietch Rescue (Fremen) | destroy the rival before a set number of Sietches are looted; a looted Sietch cannot be reassembled | loss: too many looted | progression |
| Spice Heist (Smugglers) | sabotage or block the rival's spice deal: 5 loading drones arriving completes the deal, killing 3 first blocks it (+500 spice each); no spice buildings, no liberating | win or loss by drone counts; fixed 2024-12-04 so it cannot target Vernius | progression |
| Fremen Uprising | destroy the rival outpost or liberate all villages in a set number of days; makes Fremen Resistance units; +20 Fremen friendship | win: objective met | progression |
| Ancient Sietch | ally N Sietches before the rivals, then protect (+30 friendship; failing still gives +20) or plunder (-30 friendship, +5 development assets); the first goal cuts Pressure 5% | branch: cannot be undone once chosen | progression |
| The Renegades | remove all rebel camps; unlocks the Spacing Guild branch and air units for the run; start with 2 fighter ships | win: all camps removed | progression |
| Cutting the Head Off | reach infiltration level 3 and assassinate in a set number of days; start with 2 Bene Gesserit agents | win: kill in time | late-game |
| Bailout | reach 30% of CHOAM first | win: 30% first | late-game |
| Agony | prepare 20 days, hold 30 days before reinforcements, then clear the rest; success cuts Pressure 15%; the secondary adds 3 development assets and 15% more | win: hold; loss: the territory is lost | late-game |

_source: https://en.namu.wiki/w/Dune:%20Spice%20Wars/%EC%A0%95%EB%B3%B5%20%EB%AA%A8%EB%93%9C , https://steamstore-a.akamaihd.net/news/externalpost/steam_community_announcements/1783238125343186 , https://steamstore-a.akamaihd.net/news/externalpost/steam_community_announcements/1784506359205976 2026-11-07 · capture: web_fetch · confidence: medium · enemy-tier: 2 · puzzle-tier: 2 · category: mainline · spoiler: late-game_ [Single source -- verify · class:community-wiki]

Secondary objectives named in the official notes: Water Gift, Guild Commission, Recycling Spree (the Fremen version), Spying Initiative (a bonus), Defender of the Law, Spice Heist sabotage, Land Grab, Dreamer's Den, Preacher's Burden, Disinterested Favor, Angel's Share. v2.2.5 made Defender of the Law spawn renegade bases at mission start so it is always possible; v2.2.2 made Guild Commission and Recycling Spree harder; Community Update #4 made Water Gift harder.

_source: https://steamstore-a.akamaihd.net/news/externalpost/steam_community_announcements/1785774543521852 , https://steamstore-a.akamaihd.net/news/externalpost/steam_community_announcements/1783872412139437 , https://steamstore-a.akamaihd.net/news/externalpost/steam_community_announcements/1783238125343186 2026-11-07 · capture: web_fetch · confidence: medium · enemy-tier: 1 · puzzle-tier: 1 · category: mainline · spoiler: progression_ [Single source -- verify · class:official-pr]

> **Cross-system dependency** -- see `dependencies.md` DEP-010.

## Starting traits per house

Each house has its own starting traits (Namu page, machine-translated; names are the page's English glosses). Whether a house gets all of its list at the start or earns them one per pick is not stated; the December 2023 note says the first bonus is picked after the first mission.

| House | Traits | Key lines | tier |
|---|---|---|---|
| Atreides (9) | Free Real-Estate, Friendly Reputation, Ginaz Swordmaster, Landsraad Network, Legitimate Claim, Military Prestige, Radiance of the Paragon, Respect from the Houses, Wounded Protection | first two buildings in peacefully annexed villages are free; +20 Standing per peaceful annex; a random greater Charter at the start; annex Influence cost -80% | progression |
| Harkonnen (9) | Alternative Facts, Assassin School, Educational Example, Frightening Tools, Omnipresent Fanaticism, Painful Lessons, Pragmatic Sacrifice, Thetical Opportunism, Virtual Tyranny | a free assassin each day if none; oppression costs -50% | progression |
| Corrino (9) | Administrative Redundancy, Imperial Gigantism, Mandatory Levies, Mentorship Program, Political Appropriation, Profitable Delegation, Strength in Numbers, Space Optimization, Spare Freighter | an extra imperial base; district bonuses doubled; +30% resources to all houses and Corrino takes 10% of Solari | progression |
| Ecaz (9) | Artful Display, Artistic Freedom, Fascinating Works, Favorite Candidate, Helpful Entourage, Lonely Quest, Knight of the Windmill, Political Duel, Virtuous Standing | start with a champion Knight and a Squire | progression |
| Smugglers (9 names listed; the page says 8) | Another Man's Treasure, Early Birds, Gigantic Water Tanks, Grocer Network, One-Armed Bandit, Rotten From the Inside, Street-Smart, Vanguard Outposts, Well-Traveled | start with 5 fuel cells and a Scavenging Drone | progression |
| Fremen (9) | Cleanup Crew, Deep Reserve, Drawing the Faithful, Little Drops, Manifest Legitimacy, Meaningful Symbols, Shared Purpose, The Land Provides, Wind from the South | natural resources revealed at the start | progression |
| Vernius (9) | Assisted Workforce, Exponential Growth, Inducement Awards, Intuitive Network, Parallel Processing, Randomized Trials, Recycled City, Sequential Trade, Serendipitous Research | Knowledge from developments and from connected Neural Nodes; 10,000 Solari the first time Knowledge reaches 50 and again at 100 (effects in `factions/vernius.md`) | dlc:vernius |

_source: https://en.namu.wiki/w/Dune:%20Spice%20Wars/%EC%A0%95%EB%B3%B5%20%EB%AA%A8%EB%93%9C , https://docs.google.com/document/d/1ZXpuWBrSc2Zp64P02O7baujPmmeAeJyYV84W4GORpys 2026-11-07 · capture: web_fetch · confidence: medium · enemy-tier: 1 · puzzle-tier: 1 · category: mainline · spoiler: progression_ [Single source -- verify · class:community-wiki]

Playing or fighting Vernius in Conquest: a DLC owner picks it in the faction list; as a rival it holds Scholar's Refuge, and the Singularity siege (row above) starts the defender with 5 random patented developments, all heroes, all councilors and its infrastructure. The Namu page gives no win goals by name for Vernius (probably the Great-House goals above), and no source gives a Vernius stage plan. The Hired Help mission that lacked a second phase against Vernius was fixed on 2024-11-18, and Spice Heist can no longer be given against Vernius (2024-12-04).

_source: https://en.namu.wiki/w/Dune:%20Spice%20Wars/%EC%A0%95%EB%B3%B5%20%EB%AA%A8%EB%93%9C , https://steamstore-a.akamaihd.net/news/externalpost/steam_community_announcements/1783238125343186 , https://steamstore-a.akamaihd.net/news/externalpost/steam_community_announcements/1784506359205976 2026-11-07 · capture: web_fetch · confidence: medium · enemy-tier: 2 · puzzle-tier: 2 · category: mainline · spoiler: dlc:vernius · entity: vernius_ [Single source -- verify · class:community-wiki] [translated from: Korean]

> see factions/vernius.md for full summary

## Passive bonuses

One passive bonus is picked after each success. The page lists 42 in all: 16 are flagged in the page as public and 26 are not, but the page's ownership column is blank, so which house owns which is unrecorded [unlock-chain incomplete -- condition unknown]. Grouping the 26 by house theme (Harkonnen units and oppression, Ecaz masterpieces and sanctuaries, Vernius neural nodes and tethers, Smugglers underworld headquarters, Corrino imperial bases) is a reading, not a source fact.

The 16 flagged public: Attentive Ears (+10% Intel); Economy Developments (start with two tier-2 Economy Developments); Elimination Network (an assassin on operation); Friendly Ambassadors (+10% Standing gain); Formation Template (-20% basic unit cost and time); Head Start (tier 1 in every tree); Intelligence Support (+2% attack per agent); Sapper's Brigade (+10% damage per agent on that faction); Military Developments; Plundering Mindset (+10% Solari from looting); Propaganda Network (+10% Authority); Recruit Formation (units start promoted); Statecraft Developments; Spying Initiative (+50% agent speed and +2 max agents; it was +5 before 2024-11-18); Spying Vanguard (start with 1 agent); Wordy Diplomats (+10% Influence).

The other 26 (names as machine-translated): Healthy Rations, Moral High Ground, Political Model, Wealth of Paragon, Minor Martyrdom, Sick Gambling, Secret Cabal, Talkative Survivors, Assault Formation, Expansion Taxes, Imperial Logistics, Structural Optimization, Defender of Arts, Luxury Garden, Resourcing Retreat, Tourney Culture, Culture of Curiosity, Maintenance Protocol, Research Grant, Serial Assembly, Dangerous Job, Distant Profits, Synergetic Advertising, Underworld Root, Early Reclaim, Holy Purpose.

_source: https://en.namu.wiki/w/Dune:%20Spice%20Wars/%EC%A0%95%EB%B3%B5%20%EB%AA%A8%EB%93%9C , https://steamstore-a.akamaihd.net/news/externalpost/steam_community_announcements/1783238125343186 2026-11-07 · capture: web_fetch · confidence: medium · enemy-tier: 1 · puzzle-tier: 1 · category: mainline · spoiler: progression_ [Single source -- verify · class:community-wiki]

Development assets: +5 for each capital-siege secondary objective, +3 for the Agony secondary, +5 for plundering at Ancient Sietch; they are spent on allied land (the Smuggler goal needs 12 uses).

_source: https://en.namu.wiki/w/Dune:%20Spice%20Wars/%EC%A0%95%EB%B3%B5%20%EB%AA%A8%EB%93%9C 2026-11-07 · capture: web_fetch · confidence: medium · enemy-tier: 2 · puzzle-tier: 2 · category: mainline · spoiler: late-game_ [Single source -- verify · class:community-wiki]

## Fremen friendship, Fremen unity, Faufreluche corruption

Fremen friendship (Great-House conquests). Gains: +3 for allying a Sietch, +10 for relevant secondary objectives, +20 Fremen Uprising, +30 protecting Ancient Sietch (+20 if the protection fails); losses: -4 for looting a Sietch, -30 for plundering Ancient Sietch.

| Friendship | Reward | tier |
|---|---|---|
| 25% Tolerance | the nearest village is revealed; 2 Warriors | progression |
| 50% Respect | all Spice revealed; 4 Infiltrators | progression |
| 75% Friendship | the Windtrap becomes buildable; 2 promoted Fedaykin | progression |
| 100% Alliance | build in allied Sietches, Ritual Caves, sandworm riding, the Fremen fixed as allies and joining capital sieges; this is a win-condition goal and the achievement Friendly Native | late-game |

_source: https://en.namu.wiki/w/Dune:%20Spice%20Wars/%EC%A0%95%EB%B3%B5%20%EB%AA%A8%EB%93%9C , https://truesteamachievements.com/game/Dune-Spice-Wars/achievements 2026-11-07 · capture: web_fetch · confidence: medium · enemy-tier: 2 · puzzle-tier: 2 · category: mainline · spoiler: late-game · missable: yes · entity: fremen_ [Single source -- verify · class:community-wiki]

> see factions/fremen.md for full summary

Fremen unity (Fremen conquest). Gains: +1, +3 or +6 for Sietch events by tier, +10 for side missions.

| Unity | Reward | tier |
|---|---|---|
| 25% Hopeful Followers | thumpers +2; 2 Warriors | progression |
| 50% | manpower +3 and authority +3 | progression |
| 75% | buildings in allied Sietches; 2 Fedaykin | progression |
| 100% United Brotherhood | thumper speed +200%; starts with 3 operations; a win-condition goal and the achievement United People | late-game |

_source: https://en.namu.wiki/w/Dune:%20Spice%20Wars/%EC%A0%95%EB%B3%B5%20%EB%AA%A8%EB%93%9C , https://truesteamachievements.com/game/Dune-Spice-Wars/achievements 2026-11-07 · capture: web_fetch · confidence: medium · enemy-tier: 2 · puzzle-tier: 2 · category: mainline · spoiler: late-game · missable: yes · entity: fremen_ [Single source -- verify · class:community-wiki]

> see factions/fremen.md for full summary

Faufreluche corruption (Smuggler conquest). Gains: +5 for the bribe operation, +10 for each of two secondary objectives, +30 for the Spice Heist sabotage.

| Corruption | Reward | tier |
|---|---|---|
| 25% | information never below level 1; 2 legionaries | progression |
| 50% | bribes give 10% of the house's CHOAM stock; 4 mercenaries | progression |
| 75% | houses lose 100 base votes; a Landsraad Guard and 2 Judges | progression |
| 100% | information floor level 2; ignores Standing for the advanced Charter; a win-condition goal and the achievement Corrupted Nobility | late-game |

_source: https://en.namu.wiki/w/Dune:%20Spice%20Wars/%EC%A0%95%EB%B3%B5%20%EB%AA%A8%EB%93%9C , https://truesteamachievements.com/game/Dune-Spice-Wars/achievements 2026-11-07 · capture: web_fetch · confidence: medium · enemy-tier: 2 · puzzle-tier: 2 · category: mainline · spoiler: late-game · missable: yes · entity: smugglers_ [Single source -- verify · class:community-wiki]

> see factions/smugglers.md for full summary

## Run end and Conquest achievements

House-win achievements: The Duke of Caladan (Atreides), The Baron of Giedi Prime (Harkonnen), The Emperor of Salusa Secundus (Corrino), The Archduchess of Ecaz (Ecaz), The Liberator of Dune and The Godfather of Arrakis (the two other house wins; the P2 text lists them in the house-win group without saying which of the Fremen and the Smugglers each belongs to). There are also eliminate-a-house achievements, Kwisatz Haderach (win a Conquest in under 4 in-game years; "in-game" is unconfirmed), Golden Path (win a Conquest on Insane) and Plans within Plans (a secondary-objective achievement whose trigger text was not given). Entries: `achievements.md`.

_source: https://truesteamachievements.com/game/Dune-Spice-Wars/achievements 2026-11-07 · capture: web_fetch · confidence: medium · enemy-tier: 2 · puzzle-tier: 2 · category: mainline · spoiler: late-game_ [Single source -- verify · class:editorial-en]

The house-win achievement for the paid DLC is The Earl of Ix (win a Conquest as Vernius); its entry is resolved in `achievements.md` (P3).

_source: https://truesteamachievements.com/game/Dune-Spice-Wars/achievements 2026-11-07 · capture: web_fetch · confidence: medium · enemy-tier: 2 · puzzle-tier: 2 · category: mainline · spoiler: dlc:vernius_ [Single source -- verify · class:editorial-en]

> **Cross-system dependency** -- see `dependencies.md` SEQ-001.

## Conquest regions

Conquest uses a fixed list of 26 named regions (positions shift slightly each run, resources are randomised): five capitals (Plains of Arrakeen, Carthag's Rift, Emperor's Landing, Heart of the Forest, and Scholar's Refuge which is the Vernius DLC capital) and 21 others: North Pole, Mount Idaho Range, Volcanic Range, Pasty Mesa, Broken Land, Hagga Basin, Imperial Basin, Plaster Basin, The Great Flat, Funeral Plain, Erg Habbanya, Erg Sihaya, Great Erg, Minor Erg, False Wall West, False Wall East, False Wall South, Harg Pass, Wind Pass, Grosse Valley, Cielago Depression. Some names are the page's English renderings and may differ in game. The adjacency of the regions was not published in any readable source, and the P2 capture lost the page's "Arrakis Global List" section (regions and resources): the node list is known, the edges are not. [location inventory incomplete]

_source: https://en.namu.wiki/w/Dune:%20Spice%20Wars/%EC%A0%95%EB%B3%B5%20%EB%AA%A8%EB%93%9C 2026-11-07 · capture: web_fetch · confidence: medium · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: progression_ [Single source -- verify · class:community-wiki]

## Reception

A German review (2023-09) says Conquest "is not a gripping campaign with connected missions" and that the heroes appear "without any introduction"; a French review calls it "clearly the most interesting" mode. These are opinions, not facts.

_source: https://www.gameswelt.de/dune-spice-wars/test/test-ab-in-die-wueste-322455 , https://www.phonandroid.com/test-dune-spice-wars-un-excellent-jeu-de-strategie-epice-et-tout.html 2026-11-07 · capture: web_fetch · confidence: low · enemy-tier: 0 · puzzle-tier: 0 · category: lore · spoiler: none_ [Contradicted across sources -- see notes]
