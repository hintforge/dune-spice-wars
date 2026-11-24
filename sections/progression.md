# Dune: Spice Wars -- Progression, unlocks and cross-mode differences

**status:** research-integrated
**last_reconciled:** 2026-11-07
**patch note:** current patch v2.2.8.33026 (2026-11-06) wins. Patch ledger from the Steam news feed: after v2.2.5.32923 (2024-12-12) the only posts are v2.2.7.32974 (2025-07-09), v2.2.8.33019 (2026-10-21) and v2.2.8.33026 (2026-11-06). Their text changes no free-faction unit stat, economy number, Development, Resolution or Conquest rule. The one Vernius change among them is in v2.2.7 (2025-07-09): the Harmless Gadget treaty no longer breaks when entering conflict with Vernius (P3 correction of the P2 reading that nothing after v2.2.5 touched Vernius). v2.2.7 also fixed nuke-silo, assassin, Fremen Research Station and Chani bugs; v2.2.8.33019 added a 1-slot district for Conquest Fremen main bases, spectating and a lobby leaver icon, two exploit fixes and modding hooks; v2.2.8.33026 fixed one memory leak. A version v2.2.6.32935 existed by 2025-04-21 (a player screenshot) but has no Steam post, so its contents are unknown.

The match-by-match gates are in `sections/solo_skirmish.md` (skirmish and standard multiplayer), `sections/conquest.md` and `sections/multiplayer.md`. This file holds what unlocks what, how the modes differ and the common failures.

## Which first-pass numbers still hold

Economy outputs, unit stats, Landsraad rules, CHOAM rules and Hegemony thresholds are unchanged as far as the posts after v2.2.5 reveal (the 2025-07-09 post changes only a Vernius treaty). Duneopedia's Hawk and Spire values equal the August 2024 official notes, so it is at least as new as 2024-08-22. Two Duneopedia numbers disagree with the March 2024 changelist (Border Defense, Energy Efficiency; `items/developments.md`). The v2.2.6 contents are unknown, so "holds" means "no later note found".

_source: https://steamstore-a.akamaihd.net/news/externalpost/steam_community_announcements/1848664643345529 , https://steamstore-a.akamaihd.net/news/externalpost/steam_community_announcements/1847286114027994 , https://steamstore-a.akamaihd.net/news/externalpost/steam_community_announcements/1803527891922277 , https://dune-spice-wars.github.io/duneopedia/units.html 2026-11-07 · capture: web_fetch · confidence: medium · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_ [Confirmed: 2 sources, 1 language]

## Unlock-dependency table

Rows where no source states the condition read "unlock: unknown".

| Unlockable | Condition | Cost | Mode | Unlocks or needed for | Patch | tier |
|---|---|---|---|---|---|---|
| Atreides, Harkonnen, Smugglers, Fremen, Corrino, Ecaz | none: free | free | all | Conquest availability by date (`sections/conquest.md`) | current | none |
| House Vernius of Ix | paid DLC (USD 12.99 on 2026-11-07); playable only with it; appears as an opponent for all (2024-03-07) | paid | all | its own tree, 5 achievements, patents and obfuscation (`factions/vernius.md`) | current | dlc:vernius |
| Vernius patents | 5,000 Hegemony | 600 Solari to file; rivals pay 500 each | all | Patent Troll; one free skip of a development prerequisite | 2024-03-20 | dlc:vernius |
| Vernius obfuscation | 10,000 Hegemony | 20 Standing | all | one researched development has no effect for any faction | 2024-03-07 | dlc:vernius |
| Vernius Neural Node | exactly one connected neighbouring region; no development needed | 50 Plascrete (Duneopedia) and, per video guides, 3 Standing | all | the Nodal Network, tethering; without it a village is at -50% | undated; 2024-06 | dlc:vernius |
| Vernius Harmless Gadget treaty | Heretical Computing; offered to a faction in truce | 100 Solari; the accepting faction loses 10 Standing | all | an Analytical Machine for the receiver; Information with Holistic Thinking for Vernius | 2025-07-09 | dlc:vernius |
| Heroes (2 per faction) | 10,000 Hegemony; one pick, the other cannot be recruited that game | free first pick; re-buy 1,000 Solari + 30 Standing (Fremen: 150 Authority) | all | Favoritism, Ghola Hero, Hero Slayer | 2024-03-07; later hero reworks exist | progression |
| Elite unit | 5,000 Hegemony | unit cost | all | air units and major buildings at the same threshold | 2024-03-07 | progression |
| Headquarters building | 2,500 Hegemony | building cost | all | first-pass fact, no P2 source | current | progression |
| Dune Governorship Charter | other factions: 450 Standing and one held Charter (one exception, in the claim below the table); Fremen: map control, allied Sietches, intact Sietches; won by vote | votes (Influence) | skirmish, MP, Conquest goal | Political victory; Governor | 2024-08-01; v2.2.6 | late-game |
| Charters (5) | eligibility only (since 2023-06-22) | votes | all | each Charter's perk | current | progression |
| Council Representative | replaces the Governorship when Political victory is off; Fremen not eligible | none | all | none | 2024-08-22 | late-game |
| Voting right | Standing 100 or more | none | all | votes (`sections/landsraad.md`) | current | progression |
| CHOAM ownership bonuses | own 10% and 30% of CHOAM Shares | Solari to buy shares | all | CHOAM Market; 50% is the Economic victory | 2023-06-22; 2024-11-18 | progression |
| Developments | capture the first village | Knowledge (formula in `items/developments.md`) | all | the shared tree | current | none |
| Armory gear slot 1 | Survival Training (Military tier 1) | gear free to install; 1,000 Solari to swap or remove (500 since 2024-08-01) | all | gear per unit (`items/gear.md`); Shiny New Gear, Ready to Rumble | 2024-03-07; current status unverified | progression |
| Armory gear slot 2 | Army Logistics (Atreides, Ecaz trees); Harkonnen, Smugglers, Corrino, Fremen use a unique Military development (`items/upgrades.md`) | Knowledge | all | extra gear per unit | Duneopedia undated | progression |
| Kanly Duel, five tutorials | available from the start | free | solo, multiplayer | Duelist, Back to School | current | none |
| Conquest | solo menu "New Game" | free | single player | passive bonuses, development assets | 2023-12-14 | none |
| Cosmetics (skins, banners) | unlock: unknown; none found in any source read | none found | none | the 102-achievement list contains no cosmetic reward text | none | none |
| Achievements | 102 in total: 85 base, 10 with Heroes of Dune, 7 with Community Update #4; 60 rare on the Steam page | none | all | `achievements.md` | current | none |

_source: https://steamstore-a.akamaihd.net/news/externalpost/steam_community_announcements/5679673637652411956 , https://steamstore-a.akamaihd.net/news/externalpost/steam_community_announcements/5679673637652411370 , https://dune-spice-wars.github.io/duneopedia/vernius.html , https://www.youtube.com/watch?v=fcAqG6QYj4U , https://www.reddit.com/r/Dunespicewars/comments/1k0j6ot/you_always_benefit_more_than_vernius_from/ , https://steamstore-a.akamaihd.net/news/externalpost/steam_community_announcements/5963413728335113504 , https://steamstore-a.akamaihd.net/news/externalpost/steam_community_announcements/1783238125343186 , https://docs.google.com/document/d/1LOwlJxOl1-0WhCfDtR5rmxcoiG30G8nzNREUZxs6Ch4 , https://truesteamachievements.com/game/Dune-Spice-Wars/achievements 2026-11-07 · capture: web_fetch · confidence: medium · enemy-tier: 2 · puzzle-tier: 2 · category: mainline · spoiler: late-game_ [Single source -- verify · class:official-pr]

An Atreides at 10,000 Hegemony needs only the Standing for the Dune Governorship Charter, with no held Charter.

_source: https://dune-spice-wars.github.io/duneopedia/atreides 2026-11-07 · capture: web_fetch · confidence: medium · enemy-tier: 2 · puzzle-tier: 2 · category: mainline · spoiler: late-game_ [Single source -- verify · class:community-wiki]

Conquest unlockables (Fremen friendship, Fremen unity and Faufreluche corruption tiers, passive bonuses, development assets) are in `sections/conquest.md`. A Research Treaty (needs Lay of the Land or Advanced Engineering) and an Embassy district (Diplomatic Maneuvers) are Development-gated.

_source: https://dune-spice-wars.github.io/duneopedia/developments.html 2026-11-07 · capture: web_fetch · confidence: medium · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_ [Single source -- verify · class:community-wiki]

> **Cross-system dependency** -- see `dependencies.md` DEP-002.
> **Cross-system dependency** -- see `dependencies.md` DEP-003.
> **Cross-system dependency** -- see `dependencies.md` DEP-004.
> **Cross-system dependency** -- see `dependencies.md` DEP-005.
> **Cross-system dependency** -- see `dependencies.md` DEP-011.
> **Cross-system dependency** -- see `dependencies.md` DEP-012.

## Cross-mode differences

| System | Skirmish and multiplayer | Conquest | tier |
|---|---|---|---|
| Heroes | free at 10,000 Hegemony in every mode (2024-03-07) | same unlock; the Hired Help and Incursion missions give a designated hero at the start | progression |
| Charters | eligibility only since 2023-06-22 | Atreides' trait gives a random greater Charter at the start; Smuggler corruption at 100% ignores Standing for the advanced Charter | progression |
| Governorship | one of four victory toggles | one of several optional goals; Pressure must stay under 100% | late-game |
| Sandworms | the lobby setting Sandworm activity; "greed mode" abuse reduced 2023-12-14 | no per-run setting found | none |
| Fremen main base | 5 building slots in the 2024-03-07 notes (one 2-slot and one 3-slot district), plus a 1-slot district added 2024-08-01 | Conquest Fremen main bases got a 1-slot district in v2.2.8.33019 "to match Sietch Tabr" | none |
| Voting timers (human players) | Slow: 1 min 30 s phases and 5 min vote; Fast: 30 s and 45 s | whether the AI-only voting in Conquest differs is not stated in any source read | none |
| Higher AI difficulty | a 2025 forum thread says the AI starts with CHOAM shares, always pays tax and builds instantly | a Conquest win on Insane is the achievement Golden Path | progression |

_source: https://steamstore-a.akamaihd.net/news/externalpost/steam_community_announcements/1847286114027994 , https://steamstore-a.akamaihd.net/news/externalpost/steam_community_announcements/1784506359205976 , https://steamstore-a.akamaihd.net/news/externalpost/steam_community_announcements/5963413728335113504 , https://docs.google.com/document/d/1LOwlJxOl1-0WhCfDtR5rmxcoiG30G8nzNREUZxs6Ch4 , https://en.namu.wiki/w/Dune:%20Spice%20Wars/%EC%A0%95%EB%B3%B5%20%EB%AA%A8%EB%93%9C , https://www.reddit.com/r/Dunespicewars/comments/1lsxdbc/am_i_ready_for_multiplayer_any_tips/ 2026-11-07 · capture: web_fetch · confidence: medium · enemy-tier: 2 · puzzle-tier: 2 · category: mainline · spoiler: late-game_ [Single source -- verify · class:official-pr]

> **Cross-system dependency** -- see `dependencies.md` DEP-001.
> **Cross-system dependency** -- see `dependencies.md` DEP-006.
> **Cross-system dependency** -- see `dependencies.md` PON-003.

## Common progression failures

| Failure | Mechanism | Fix | Patch | tier |
|---|---|---|---|---|
| Governorship won, then lost at the next council | a "Loss of Rights" vote revokes all Charters | out-vote it, hold the Speaker Charter to re-roll, or remove rivals who cannot vote | 2023-09 | late-game |
| The Fremen lead Hegemony first and get dog-piled | the whole lobby targets the leader | do not reach 20,000 first without defence; ambush and stealth economy | 2025-06 | late-game |
| Missing a Spice Tax payment | -20 Standing; an unpaid Influence deficit drains Standing 5 per day (2022 figure) | pay on the 25-day cycle | current for the -20; 2022 for the drain | none |
| Standing under 250 | Charters can be lost; under 100 there is no vote and Guards raid every 20 days | keep an Embassy and Truces, avoid betrayals (-100) | current | none |
| Conquest Pressure reaches 100% | +3% per territory, more on failed missions | take Pressure-cutting secondary objectives; avoid the slow Fremen-alliance route | patch unknown | progression |
| Spice Heist aimed at a faction that made it impossible | the mission could target a faction that blocked it | fixed 2024-12-04 | 2.2.3 | progression |
| Ignoring rare timed events | small tab notifications top left; ignoring detrimental ones can cause rebellion | choose in the events tab | 2022, pre-1.0 | none |

_source: https://www.reddit.com/r/Dunespicewars/comments/168vxtb/how_to_hold_governorship_for_30_days/ , https://www.reddit.com/r/Dunespicewars/comments/1lc1gkm/fremen_faction_requires_serious_buff_in/ , https://dunespicewars.fandom.com/wiki/Landsraad_Standing , https://www.gamepressure.com/dune-spice-wars/votes-and-influence/zbfca1 , https://en.namu.wiki/w/Dune:%20Spice%20Wars/%EC%A0%95%EB%B3%B5%20%EB%AA%A8%EB%93%9C , https://steamstore-a.akamaihd.net/news/externalpost/steam_community_announcements/1784506359205976 , https://steamcommunity.com/sharedfiles/filedetails/?id=2809136076 2026-11-07 · capture: web_fetch · confidence: medium · enemy-tier: 2 · puzzle-tier: 2 · category: mainline · spoiler: late-game_ [Single source -- verify · class:forum]

## Common-knowledge rules with documented exceptions

"Developments are researched with Knowledge": a Research Treaty instead cuts the partner's techs by 20%, and a completed district cuts the step cost by 15%. "You win Conquest with two of three goals": Pressure at 100% voids it. "A Truce means safe": Ecaz may break one (since 2024-11-18), and a betrayed Atreides gains extra Standing (the size of that bonus is not stated).

_source: https://dunespicewars.fandom.com/wiki/Developments , https://en.namu.wiki/w/Dune:%20Spice%20Wars/%EC%A0%95%EB%B3%B5%20%EB%AA%A8%EB%93%9C , https://steamstore-a.akamaihd.net/news/externalpost/steam_community_announcements/1783238125343186 2026-11-07 · capture: web_fetch · confidence: medium · enemy-tier: 2 · puzzle-tier: 2 · category: mainline · spoiler: late-game_ [Single source -- verify · class:community-wiki]
