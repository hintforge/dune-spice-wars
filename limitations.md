# Dune: Spice Wars -- Limitations & Blocked Sources

Sources I found that look useful but couldn't fully fetch -- paywalls, Cloudflare, age gates, video-only content, etc. URLs preserved so the player (or another contributor) can open them in a real browser.

## How to read this file
- Each entry: topic, URL, block type, what I could glean, best alternative I did get to.
- Each per-topic file (in `factions/`, `items/`, `sections/`) also lists its own blocked sources at the bottom -- the player rarely needs to come hunting here.
- This file is the catch-all for sources that didn't fit a specific topic.

## Block types
- **paywall** -- content gated behind a subscription or article limit
- **cloudflare** -- Cloudflare bot challenge / 403 / 503 from WebFetch
- **video-only** -- YouTube or other video where the answer is shown visually; no readable text equivalent
- **age-gate** -- content blocked behind age verification
- **cookie-wall** -- popup or consent flow that broke the fetch
- **search-snippet-only** -- search engine returned a snippet but the page itself wasn't reachable
- **dead-link** -- URL was in another source but no longer resolves

- **robots-restriction** -- the external research runtime reports a robots access restriction
- **terms-restriction** -- a stated retrieval restriction was reported; preserve the actual evidence
- **javascript-dependent** -- useful content requires page execution the available tool did not perform
- **login-required** -- a signed-in session is required
- **access-not-checked** -- no content/access check was performed; never call this robots-blocked

## Companion tools

For every useful map, tracker, database or completion tool supplied, recalled or found:

- Name and URL if verified (otherwise mark unknown/unverified)
- Apparent coverage, evidence for it, and uncertainty; unread coverage is not confirmed game data
- Reason not read, access-check result, policy evidence if available, and check date
- How a person could use it, best readable alternative, and wider-spoiler warning where relevant

Merge repeated URLs with dated evidence retained. Read tools can also be recorded here when they offer a useful location fallback. Record an honest empty statement when no candidates were found; do not imply exhaustive discovery.

Checked by P1 on 2026-11-07 (one deep-research run; discovery is not exhaustive). None found is a faction planner or build-order calculator. No replay or statistics sites were found; the in-game Statistics screen (Community Update #4) is the nearest. Spice Wars skirmish and multiplayer maps are generated, so a fixed location tracker does not apply.

| Tool | Coverage | Access status (2026-11-07) | Notes |
|---|---|---|---|
| Duneopedia, https://dune-spice-wars.github.io/duneopedia | factions, units, buildings, Developments, councilors, Arrakis, Gameplay (operations); Resolutions, Charters, Events and points of interest still marked "TO DO" | read, 200 OK | undated, community-run; matches v2.2.3; this guide's main number source |
| Dune: Spice Wars Wiki (Fandom), https://dunespicewars.fandom.com | about 257 pages: Charter, Resolutions, units, Developments | read for 2 pages (Charter, Resolutions); home page title redirects | CC-BY-SA; date per page unknown |
| NamuWiki Conquest page, https://en.namu.wiki/w/Dune:%20Spice%20Wars/%EC%A0%95%EB%B3%B5%20%EB%AA%A8%EB%93%9C | Conquest rules, regions, missions, bonuses | read (page modified 2026-08-07) | Korean, machine-translated |
| minmax.wiki, https://minmax.wiki/dune-spice-wars | wiki shell with no articles | read; empty | not useful |
| Nexus Mods listing, https://www.nexusmods.com/games/dunespicewars/mods | 9 mods: CoopQuest, Quinn's Faction Toolkit, Bene Tleilaxu Faction, Quinn's Unofficial Patcher, Music Mod, Infinite Solari, QuinnQuest, Dyaus Anchor (7-faction mod), Community Patch (P2P multiplayer rebalance) | listing read; mod pages not opened | modding class; mod text is not game fact |
| WeMod trainer page, https://www.wemod.com/cheats/dune-spice-wars-trainers/achievements | achievements list with global percentages (95 of 102); cheats | achievements page read | trainer itself not run |
| dunespicewars.github.io | factions, units, buildings (recalled by the brief) | 404, GitHub Pages site not found | not usable |
| dunespicewars.wiki.gg | unknown | 401 Not Authorized | not usable |
| SteamDB | patch notes | not fetched | not read |
| Dune: Mod Wars Discord, r/dunebasebuilds | mod help; shared base layouts | not read | mentioned in a Reddit post |
| TrueAchievements / TrophiesHunter | Xbox achievement list (26 per VGTimes Windows 10 page) | search result only | the Xbox list is a different count |

## Entries

### Steam Community achievements page -- achievement list
- Source: https://steamcommunity.com/stats/1605220/achievements
- Block type: javascript-dependent (the visible page text loads only part of the list for an unsigned-in reader, but the page data carries all 102 names)
- Why I think it has the answer: it is Steam's own canonical list (102 achievements, 60 rare)
- What I could glean: all 102 display names and hidden flags (none hidden), with global completion percentages from Steam's keyless percentages endpoint
- Best alternative I did get to: the full list in the stub list in `achievements.md`; trigger conditions are the part still not researched

### gamesplanet.com -- achievement list
- Source: https://us.gamesplanet.com/community/dune-spice-wars-steam-key--5533-1/achievements
- Block type: cloudflare
- Why I think it has the answer: a search result described it as a Steam achievement listing (it states 103, one more than Steam)
- What I could glean before the block: nothing beyond the search snippet
- Best alternative I did get to: Steam Community page above; in P2 the trigger text for the 7 Conquest achievements was read on TrueSteamAchievements instead (still blocked 2026-11-07 for Gamesplanet)

### trophieshunter.com -- achievement list
- Source: https://trophieshunter.com/games/dune-spice-wars-pc-xbox-series/achievements/full-house
- Block type: cloudflare
- Why I think it has the answer: per-achievement pages for the PC and Xbox lists
- What I could glean before the block: nothing
- Best alternative I did get to: Steam Community page above

### P1 (2026-11-07): sources found but not read

- Gamesplanet achievements page, https://us.gamesplanet.com/community/dune-spice-wars-steam-key--5533-1/achievements -- cloudflare; trigger text for 7 Conquest achievements (named in `achievements.md`) came only from a search-tool summary in P1; P2 read the same triggers on TrueSteamAchievements, so those 7 entries are now resolved but keep `hidden: unknown`. The Gamesplanet page states 103 lines, one more than Steam, and is still unread.
- SteamHunters and completionist.me achievement lists -- cloudflare, blocked 2026-11-07.
- GameStar review (German) -- cloudflare, blocked 2026-11-07.
- dunespicewars.com Conquest and other posts -- HTTP 403 on both fetch tools; official announcement text.
- Google Docs full changelists linked from the Conquest Update and Heroes of Dune posts -- fetch returned an unrelated summary; unverified.
- Steam guide "Spice addiction guide... Insane" (id 2809136076) -- not fetched; Fremen Insane strategy.
- 2022 faction guides (The Gamer Fremen, Cultured Vultures, GameSkinny, GamePressure faction pages, wotpack.ru, Gamersky/Bilibili zones) -- not fetched; they predate the 2024-03 rework.
- Fandom pages for Landsraad Standing and Developments -- read in P2; the Fandom unit pages are still unread (Duneopedia covers units).
- Reddit threads (Vernius, "Community Multiplayer Rebalance Mod", "1.0 House Harkonnen Guide", "Harkonnen conquest bonuses are insane", "New Content?") -- titles seen only.
- YouTube: two gameplay videos loaded but no transcript could be extracted; no video segment was transcribed.
- Steam news archive 2022 to 2023 (Line in the Sand, Air & Sand, Community Updates #1 and #2, Ecaz introduction) -- titles and dates only.

### P1 (2026-11-07): gaps and open conflicts

- Not covered after P1 and P2: default hotkey letters (images); graphics and audio option lists; Events and points-of-interest lists; the exact appearance conditions of 35 Resolutions; the Influence price of ending a Truce; the zone adjacency graph of the 26 Conquest regions; per-house ownership of the 42 passive bonuses; Corrino unit gear. (Closed by P2: the shared Development tree and its cost formula, the Atreides and Ecaz second-slot development, Armory gear for five factions, the 38 Resolutions and Standing, Conquest starting traits for every house, the seven blocked Conquest achievement triggers.)
- Open source conflicts (with every value and source): see `sections/conflicts.md`. That file holds each conflict at its own spoiler tier, so no disputed value is written here untagged. P2 resolved two P1 conflicts (Hawk and Spire stats) from dated official notes.
- Unverified: the month Corrino (free update, 2022-09 per a news-list entry) and Ecaz (with 1.0) arrived; whether the Shiny New Gear and Interstellar Transit achievements trigger as described after the 2024-03 rework and for Fremen; the "True Friendship" achievement (in older lists, not among Steam's 102); what Steam patch v2.2.6.32935 changed (it has no post); whether Gamesplanet's 103 achievement titles (one more than Steam) are a real extra.
- Discovery limit: P1 and P2 were each one deep-research run (one tool each). No fact was corroborated by a second research tool, and P2's own cross-check was by publication, not by tool.

### P2 (2026-11-07): sources found but not read, and tools

- Gamesplanet and TrophiesHunter achievement pages -- HTTP 403 (blocked 2026-11-07). The trigger text P1 could not read was taken from TrueSteamAchievements instead. A person can open both in a browser.
- SteamHunters, completionist.me, dunespicewars.com, gamestar.de -- not attempted in P2 (P1 recorded Cloudflare or 403 blocks).
- Four developer changelists linked from Steam posts and exported through their public Google Docs links but not read in P2: Air and Sand (2022-11), Corrino (2022-09), the 1.0 release list (2023-09, holds the Ecaz bonuses) and the November 2023 list. They would fill the earliest Ecaz and Corrino rules and Corrino gear. The Corrino section of the Heroes of Dune changelist was also not read.
- The NamuWiki Conquest page: the P2 capture stopped at 45,000 of 51,646 characters, so its "Arrakis Global List" section (regions and resources) and its footnotes are missing.
- Search-tool summaries only (not counted): TV Tropes, GameRiv and GamePretty, for the Governorship length (their figures are not counted as sources; the length conflict is in `sections/conflicts.md`).
- r/Dunespicewars threads listed by title only (the Vernius guide was read in P3): a Vernius guide, a Harkonnen tricks thread, a House Moritani thread, Quinn's patch threads, and two threads on a late-game victory type not appearing or not working. Reddit reads in P2 used the RSS reader only, so comment sets may be partial.
- No video was transcribed in P2 (no transcript tool).
- Known tools after P2: Duneopedia (units, buildings, Developments with prerequisites, Arrakis, gameplay; Resolutions and Charters marked "TO DO"; undated); the Fandom wiki (Landsraad Standing, Resolutions, Developments node list and Charter read; 257 pages); NamuWiki Conquest page (see above); TrueSteamAchievements (102 achievements with trigger text; readable); the unofficial QuinnQuest and Quinn's Unofficial Patch mods discussed on r/Dunespicewars in 2025-08 and 2026-10 (community balance mods, not game rules). No faction planner, build-order tool or unlock tracker beyond Duneopedia was found; the search was not exhaustive.

### P3 (2026-11-07): House Vernius of Ix -- sources not read, tools, gaps

- One deep-research run (no second tool, so nothing is corroborated across research tools). It read the full NamuWiki Conquest page (51,570 characters), which answers the P2 gap about the nine Vernius traits; its region adjacency graph and per-house passive-bonus ownership are still not in any extract used.
- Steam Community thread "Vernius Suck", https://steamcommunity.com/app/1605220/discussions/0/4363500868530352166 -- read only through a fetch-tool summary, not verbatim (April 2024: standing and design opinions). A person can open it in a browser.
- Reddit threads, titles only: https://www.reddit.com/r/Dunespicewars/comments/1bdrgqg/is_house_vernius_underpowered/ (2024-03-13), https://www.reddit.com/r/Dunespicewars/comments/1jnpxjr/i_must_not_be_smart_enough_for_vernius/ (rate-limited, cited for two small claims and never read), /1m2jah5/ (Dune Circuit community mod), /1i9yim6/, /1lsxdbc/ (multiplayer tips) and the QuinnQuest threads. The Reddit reader returned coverage "unknown" on every thread read and the browser fetch was refused (challenge) on two. A signed-in browser can read the full comment trees.
- YouTube: four Vernius videos were transcribed (DuneBro 2024-03-12, Daevohk 2024-06-18, Jinshe in French 2024-03-30, Noteau in French 2024-05-11), the last three by keyword windows only. Found but not transcribed: DuneBro beginners guide (2024-03-08, captions saved), Grayzo (2025-08-22), a French overview and a councilors guide for all factions.
- Not read: Steam news before 2024-02 and the DLC's own store HTML page (the store API text was used), the contents and price of "The Ixian Edition" bundle. No Chinese or Russian Vernius strategy page was found; the localized store texts (French, German, Russian, Simplified Chinese) were used for the non-English check. German press (Gameswelt) was read through a fetch-tool summary.
- Companion tools after P3: Duneopedia (Vernius councilors, 9 units, a 36-node tree with unique markers, Neural Node, undated; its "Faction Bonuses" block for Vernius is wrong and is not used); the older fan database dunespicewars.github.io is a 404; the Dune Circuit Community Mod and QuinnQuest threads change numbers and are not planners; three auto-generated guide sites (gleetron, fusa-ap5, ifrriqog on pages.dev) are unreliable and were not fetched. No planner, build-order tool, Vernius map or collectible tracker exists for this game.
- Gaps (no readable source states them): development costs and tier positions; S-Vault building costs and upkeep; councilor unlock conditions; node count, per-region and distance limits, and whether an enemy captures a node; numeric tether ranges; what happens at 0 Fuel Cells without Water Batteries and whether units consume Fuel Cells per day; whether the first hero pick is free; Vernius's own Conquest win goals and any stage plan; whether a non-owner can join a lobby with a Vernius player; whether Vernius can earn the Scrappers achievement; the role of the Experimental Alloy Furnace; whether obfuscation can be broken or differs by mode; unlock conditions and Intel costs of Ambient Connection, Empirical Data and Hidden Backdoor; what v2.2.6.32935 changed for Vernius. Disputed values: `sections/conflicts.md`.

## Always-blocked categories

- **Generated map layouts.** Skirmish and multiplayer maps are generated, so no source can give fixed coordinates for resource spots or villages; the guide teaches how to read them, not where they are.
- **Save-file field meanings.** No published description of the game's save format was found, and this guide ships no save reader. Any future reader must treat every save field as a candidate until a before/after pair proves it.
- **Game files.** The install is a single packed archive; the game's own text and data tables cannot be read without extraction, which setup does not do.
