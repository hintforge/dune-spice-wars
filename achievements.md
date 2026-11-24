# Dune: Spice Wars -- Achievements

**status:** research-integrated
**last_reconciled:** 2026-11-24
**stub_source:** Steam Community achievements page, https://steamcommunity.com/stats/1605220/achievements (102 names; ids from Steam's global-percentages endpoint)
**stub_fetched:** 2026-11-07
**stub_count:** 102
**recount:** partial -- 26 of 102 names seen (live fetch 2026-11-07 of the Steam page, header "ACHIEVEMENTS (102)"); all 26 seen names match entries 1-26 of the platform order and the live total of 102 equals the corpus total. The other 76 names are marked `unverified against live platform list` (the page renders only the first 26 rows).

## Coverage

102 Steam achievements (60 rare); coverage is partially verified against live platform list (26 of 102); each of the other 76 entries carries the mark `unverified against live platform list`. The 95 `hidden: no` flags rest on the Stage 0 fetch of the achievement data embedded in the Steam Community page (a fetch-tool read of the page data, which marks none hidden); the Steam store API sample of 10 names agrees, and no hidden flag was checked beyond those, so "none hidden" is that page data's reading, not a confirmed fact for every row. The 7 Conquest rows whose triggers P1 knew only from a search-tool summary of a blocked page still carry `hidden: unknown` (no source read shows their hidden flag). P1 outcome: 90 resolved, 5 deferred, 7 unreachable. P2 outcome (2026-11-07): 97 resolved, 5 deferred, 0 unreachable. The 5 deferred were all paid-DLC House Vernius entries (deferred to P3). P3 outcome (2026-11-07): 102 resolved, 0 deferred, 0 unreachable; the five Vernius triggers are confirmed from TrueSteamAchievements (one more editorial page; WeMod republishes Steam's own text), still medium and single source; P3 found no base-game achievement text that names Vernius. The 7 former unreachable rows (the Conquest rows that carry `hidden: unknown`) now have trigger text from TrueSteamAchievements, a readable page (single source, medium): five carry a stated trigger; for two of them the page lists them only among the Conquest house wins, so which house each belongs to is low confidence. Resolved entries come from Vandal and WeMod, which both republish Steam's own text, so independence between them is limited; their rows are medium confidence even where two or three sources are named. Cheats (/enableCheats) and modified .cdb files disable achievements for that save. Triggers are paraphrased; names are verbatim.

## Genre vocabulary

- **class** -- bound to a faction's identity (win as it, or a faction-specific condition).
- **mission** -- bound to a Conquest mission or siege.
- **social**, **multiplayer** -- as in the conventional vocabulary (treaties, votes, Sietch bonds; multiplayer lobbies).

## Progression

Every player who plays long enough reaches these.

### Expansionist
- **id:** `Expansionist` · **hidden:** no · **trigger_type:** progression · **missable:** no · **ponr-window:** n/a · **vector-binding:** `mechanics.md` (Villages)
- **trigger:** take your first village. **prereqs:** capturing the first village also unlocks Developments.
_source: https://vandal.elespanol.com/logros/pc/dune-spice-wars/111674 , https://www.wemod.com/cheats/dune-spice-wars-trainers/achievements 2026-11-07 · capture: web_fetch · confidence: medium · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none · achievement: Expansionist · achievement-hidden: no · trigger_type: progression_ [Confirmed: 2 sources, 1 language]

### Defender
- **id:** `Defender` · **hidden:** no · **trigger_type:** progression · **missable:** no (repeatable) · **ponr-window:** n/a · **vector-binding:** `mechanics.md` (Sietches)
- **trigger:** defeat a raid aimed at you. **prereqs:** needs a Sietch raid or rebels.
_source: https://vandal.elespanol.com/logros/pc/dune-spice-wars/111674 , https://www.wemod.com/cheats/dune-spice-wars-trainers/achievements 2026-11-07 · capture: web_fetch · confidence: medium · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none · achievement: Defender · achievement-hidden: no · trigger_type: progression_ [Confirmed: 2 sources, 1 language]

### Regional Specialty
- **id:** `RegionalSpecialty` · **hidden:** no · **trigger_type:** progression · **missable:** no · **ponr-window:** n/a · **vector-binding:** `mechanics.md` (Villages)
- **trigger:** build a resource building that uses a local natural resource. **prereqs:** for example a Dew Collector, Windtrap or Processing Plant per region.
_source: https://vandal.elespanol.com/logros/pc/dune-spice-wars/111674 , https://www.wemod.com/cheats/dune-spice-wars-trainers/achievements 2026-11-07 · capture: web_fetch · confidence: medium · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none · achievement: RegionalSpecialty · achievement-hidden: no · trigger_type: progression_ [Confirmed: 2 sources, 1 language]

### Sly
- **id:** `Sly` · **hidden:** no · **trigger_type:** progression · **missable:** no · **ponr-window:** n/a · **vector-binding:** `mechanics.md` (Espionage)
- **trigger:** launch an operation. **prereqs:** needs Intel and an operation slot; any Easy operation counts.
_source: https://vandal.elespanol.com/logros/pc/dune-spice-wars/111674 , https://www.wemod.com/cheats/dune-spice-wars-trainers/achievements 2026-11-07 · capture: web_fetch · confidence: medium · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none · achievement: Sly · achievement-hidden: no · trigger_type: progression_ [Confirmed: 2 sources, 1 language]

### Spice Duty
- **id:** `SpiceDuty` · **hidden:** no · **trigger_type:** progression · **missable:** no · **ponr-window:** n/a · **vector-binding:** `mechanics.md` (Spice harvesting)
- **trigger:** assign a new crew to a Harvester or Harvesting Team. **prereqs:** needs a harvester.
_source: https://vandal.elespanol.com/logros/pc/dune-spice-wars/111674 , https://www.wemod.com/cheats/dune-spice-wars-trainers/achievements 2026-11-07 · capture: web_fetch · confidence: medium · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none · achievement: SpiceDuty · achievement-hidden: no · trigger_type: progression_ [Confirmed: 2 sources, 1 language]

### Legal Bond
- **id:** `LegalBond` · **hidden:** no · **trigger_type:** progression · **genre:** social · **missable:** no · **ponr-window:** n/a · **vector-binding:** `mechanics.md` (Alliances)
- **trigger:** sign a treaty. **prereqs:** a counterpart faction must accept.
_source: https://vandal.elespanol.com/logros/pc/dune-spice-wars/111674 , https://www.wemod.com/cheats/dune-spice-wars-trainers/achievements 2026-11-07 · capture: web_fetch · confidence: medium · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none · achievement: LegalBond · achievement-hidden: no · trigger_type: progression · genre: social_ [Confirmed: 2 sources, 1 language]

### Urban Planning
- **id:** `UrbanPlanning` · **hidden:** no · **trigger_type:** progression · **missable:** no · **ponr-window:** n/a · **vector-binding:** `mechanics.md` (Villages, districts)
- **trigger:** activate a district bonus. **prereqs:** complete a district row in a village or base.
_source: https://vandal.elespanol.com/logros/pc/dune-spice-wars/111674 , https://www.wemod.com/cheats/dune-spice-wars-trainers/achievements 2026-11-07 · capture: web_fetch · confidence: medium · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none · achievement: UrbanPlanning · achievement-hidden: no · trigger_type: progression_ [Confirmed: 2 sources, 1 language]

### Spy Master
- **id:** `SpyMaster` · **hidden:** no · **trigger_type:** progression · **missable:** no · **ponr-window:** n/a · **vector-binding:** `mechanics.md` (Espionage)
- **trigger:** reach infiltration level 3 in any field. **prereqs:** 3 agents on a field.
_source: https://steamcommunity.com/stats/1605220/achievements , https://www.wemod.com/cheats/dune-spice-wars-trainers/achievements , https://www.gamepressure.com/dune-spice-wars/trophies-achievements/z3fb9b 2026-11-07 · capture: web_fetch · confidence: medium · enemy-tier: 1 · puzzle-tier: 1 · category: mainline · spoiler: progression · achievement: SpyMaster · achievement-hidden: no · trigger_type: progression_ [Confirmed: 3 sources, 2 languages]

### Water Bond
- **id:** `WaterBond` · **hidden:** no · **trigger_type:** progression · **genre:** social · **missable:** no · **ponr-window:** n/a · **vector-binding:** `mechanics.md` (Sietches)
- **trigger:** ally a Sietch. **prereqs:** relation 100, plus an agent and territory.
_source: https://vandal.elespanol.com/logros/pc/dune-spice-wars/111674 , https://www.wemod.com/cheats/dune-spice-wars-trainers/achievements 2026-11-07 · capture: web_fetch · confidence: medium · enemy-tier: 1 · puzzle-tier: 1 · category: mainline · spoiler: progression · achievement: WaterBond · achievement-hidden: no · trigger_type: progression · genre: social_ [Confirmed: 2 sources, 1 language]

### Aggressor
- **id:** `Aggressor` · **hidden:** no · **trigger_type:** progression · **missable:** no · **ponr-window:** n/a · **vector-binding:** `mechanics.md` (Villages)
- **trigger:** capture a village owned by another faction. **prereqs:** militia defeated first; Atreides cannot pillage neutral villages but can annex.
_source: https://vandal.elespanol.com/logros/pc/dune-spice-wars/111674 , https://www.wemod.com/cheats/dune-spice-wars-trainers/achievements 2026-11-07 · capture: web_fetch · confidence: medium · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none · achievement: Aggressor · achievement-hidden: no · trigger_type: progression_ [Confirmed: 2 sources, 1 language]

### First Step
- **id:** `FirstStep` · **hidden:** no · **trigger_type:** progression · **genre:** social · **missable:** no · **ponr-window:** n/a · **vector-binding:** `mechanics.md` (Alliances)
- **trigger:** propose a Truce and have it accepted. **prereqs:** the other faction (human or AI) must accept.
_source: https://vandal.elespanol.com/logros/pc/dune-spice-wars/111674 , https://www.wemod.com/cheats/dune-spice-wars-trainers/achievements 2026-11-07 · capture: web_fetch · confidence: medium · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none · achievement: FirstStep · achievement-hidden: no · trigger_type: progression · genre: social_ [Confirmed: 2 sources, 1 language]

### Shiny New Gear
- **id:** `ShinyNewGear` · **hidden:** no · **trigger_type:** progression · **missable:** no · **ponr-window:** n/a · **vector-binding:** `items/gear.md`
- **trigger:** buy gear in the Barracks. **prereqs:** Barracks (Main Base) required. Since the 2024-03 rework made gear free to install, whether "buy" still triggers on install is unverified.
_source: https://vandal.elespanol.com/logros/pc/dune-spice-wars/111674 , https://www.wemod.com/cheats/dune-spice-wars-trainers/achievements 2026-11-07 · capture: web_fetch · confidence: medium · enemy-tier: 1 · puzzle-tier: 1 · category: mainline · spoiler: progression · achievement: ShinyNewGear · achievement-hidden: no · trigger_type: progression_ [Confirmed: 2 sources, 1 language]

### Honor of Duty
- **id:** `HonorOfDuty` · **hidden:** no · **trigger_type:** progression · **genre:** social · **missable:** no · **ponr-window:** n/a · **vector-binding:** `mechanics.md` (Landsraad)
- **trigger:** get elected to a Charter (Battle/MP). **prereqs:** 250 Standing for common Charters; not possible in the first Council.
_source: https://dunespicewars.fandom.com/wiki/Charter , https://vandal.elespanol.com/logros/pc/dune-spice-wars/111674 , https://www.wemod.com/cheats/dune-spice-wars-trainers/achievements 2026-11-07 · capture: web_fetch · confidence: medium · enemy-tier: 1 · puzzle-tier: 1 · category: mainline · spoiler: progression · achievement: HonorOfDuty · achievement-hidden: no · trigger_type: progression · genre: social_ [Confirmed: 3 sources, 1 language]

### Way of the Air
- **id:** `WayOfTheAir` · **hidden:** no · **trigger_type:** progression · **missable:** no · **ponr-window:** n/a · **vector-binding:** `mechanics.md` (Military)
- **trigger:** carry troops by shuttle. **prereqs:** an Airfield; the Main Base counts as one.
_source: https://vandal.elespanol.com/logros/pc/dune-spice-wars/111674 , https://www.wemod.com/cheats/dune-spice-wars-trainers/achievements 2026-11-07 · capture: web_fetch · confidence: medium · enemy-tier: 1 · puzzle-tier: 1 · category: mainline · spoiler: progression · achievement: WayOfTheAir · achievement-hidden: no · trigger_type: progression_ [Confirmed: 2 sources, 1 language]

### Back to School
- **id:** `WinTutorial` · **hidden:** no · **trigger_type:** progression · **missable:** no · **ponr-window:** n/a · **vector-binding:** `sections/solo_skirmish.md`
- **trigger:** complete a tutorial (any of the 5, single player).
_source: https://vandal.elespanol.com/logros/pc/dune-spice-wars/111674 , https://www.wemod.com/cheats/dune-spice-wars-trainers/achievements 2026-11-07 · capture: web_fetch · confidence: medium · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none · achievement: WinTutorial · achievement-hidden: no · trigger_type: progression_ [Confirmed: 2 sources, 1 language]

### Favoritism
- **id:** `Favoritism` · **hidden:** no · **trigger_type:** progression · **missable:** no · **ponr-window:** n/a · **vector-binding:** `items/abilities.md`
- **trigger:** choose a hero. **prereqs:** 10,000 Hegemony and 1,000 Solari.
_source: https://steamcommunity.com/stats/1605220/achievements , https://www.wemod.com/cheats/dune-spice-wars-trainers/achievements 2026-11-07 · capture: web_fetch · confidence: medium · enemy-tier: 1 · puzzle-tier: 1 · category: mainline · spoiler: progression · achievement: Favoritism · achievement-hidden: no · trigger_type: progression_ [Confirmed: 2 sources, 1 language]

### Interstellar Transit
- **id:** `InterstellarTransit` · **hidden:** no · **trigger_type:** progression · **missable:** no · **ponr-window:** n/a · **vector-binding:** `mechanics.md` (Military)
- **trigger:** build a Spacing Guild Branch. **prereqs:** 5,000 Hegemony. Fremen build a Recycling Plant instead; whether that counts is unverified.
_source: https://steamcommunity.com/stats/1605220/achievements , https://www.wemod.com/cheats/dune-spice-wars-trainers/achievements 2026-11-07 · capture: web_fetch · confidence: medium · enemy-tier: 1 · puzzle-tier: 1 · category: mainline · spoiler: progression · achievement: InterstellarTransit · achievement-hidden: no · trigger_type: progression_ [Confirmed: 2 sources, 1 language]

### Obliteration
- **id:** `Obliteration` · **hidden:** no · **trigger_type:** progression · **missable:** no · **ponr-window:** n/a · **vector-binding:** `mechanics.md` (Victory)
- **trigger:** destroy another player's base. **prereqs:** Main Base destruction.
_source: https://vandal.elespanol.com/logros/pc/dune-spice-wars/111674 , https://www.wemod.com/cheats/dune-spice-wars-trainers/achievements 2026-11-07 · capture: web_fetch · confidence: medium · enemy-tier: 1 · puzzle-tier: 1 · category: mainline · spoiler: progression · achievement: Obliteration · achievement-hidden: no · trigger_type: progression_ [Confirmed: 2 sources, 1 language]

### Bringing a Spaceship to a Knife Fight
- **id:** `SpaceshipToAKnifeFight` · **hidden:** no · **trigger_type:** progression · **missable:** no · **ponr-window:** n/a · **vector-binding:** `mechanics.md` (Military)
- **trigger:** recruit a Frigate. **prereqs:** Spacing Guild Branch and 100 Guild Favour (Fremen: 100 Machine Scraps at the Recycling Plant).
- **platform-list check:** this name was not among the 26 seen on the live Steam page (2026-11-07 recount); unverified against live platform list.
_source: https://dune-spice-wars.github.io/duneopedia/atreides , https://vandal.elespanol.com/logros/pc/dune-spice-wars/111674 , https://www.wemod.com/cheats/dune-spice-wars-trainers/achievements 2026-11-07 · capture: web_fetch · confidence: medium · enemy-tier: 1 · puzzle-tier: 1 · category: mainline · spoiler: progression · achievement: SpaceshipToAKnifeFight · achievement-hidden: no · trigger_type: progression_ [Confirmed: 3 sources, 1 language]

### Hero Slayer
- **id:** `HeroSlayer` · **hidden:** no · **trigger_type:** progression · **missable:** no · **ponr-window:** n/a · **vector-binding:** `items/abilities.md`
- **trigger:** kill an enemy hero. **prereqs:** the enemy must have a hero (10,000 Hegemony).
- **platform-list check:** this name was not among the 26 seen on the live Steam page (2026-11-07 recount); unverified against live platform list.
_source: https://www.wemod.com/cheats/dune-spice-wars-trainers/achievements , https://steamstore-a.akamaihd.net/news/externalpost/steam_community_announcements/5679673637652411956 2026-11-07 · capture: web_fetch · confidence: medium · enemy-tier: 1 · puzzle-tier: 1 · category: mainline · spoiler: progression · achievement: HeroSlayer · achievement-hidden: no · trigger_type: progression_ [Confirmed: 2 sources, 1 language]

### One in a million
- **id:** `OneInAMillion` · **hidden:** no · **trigger_type:** progression · **missable:** no · **ponr-window:** n/a · **vector-binding:** `mechanics.md` (Military)
- **trigger:** destroy a Frigate. **prereqs:** an enemy Frigate exists; Cronos and anti-air do air damage, and the Altar gives +100% against flyers.
- **platform-list check:** this name was not among the 26 seen on the live Steam page (2026-11-07 recount); unverified against live platform list.
_source: https://vandal.elespanol.com/logros/pc/dune-spice-wars/111674 , https://www.wemod.com/cheats/dune-spice-wars-trainers/achievements 2026-11-07 · capture: web_fetch · confidence: medium · enemy-tier: 1 · puzzle-tier: 1 · category: mainline · spoiler: progression · achievement: OneInAMillion · achievement-hidden: no · trigger_type: progression_ [Confirmed: 2 sources, 1 language]

### Killer
- **id:** `Killer` · **hidden:** no · **trigger_type:** progression · **missable:** no · **ponr-window:** n/a · **vector-binding:** `mechanics.md` (Espionage)
- **trigger:** assassinate an enemy leader. **prereqs:** level 3 on the Target faction and level 1 in each field; 500 Intel + 1,000 Solari.
- **platform-list check:** this name was not among the 26 seen on the live Steam page (2026-11-07 recount); unverified against live platform list.
_source: https://dune-spice-wars.github.io/duneopedia/gameplay , https://vandal.elespanol.com/logros/pc/dune-spice-wars/111674 , https://vgtimes.ru/games/dune-spice-wars/achievements-and-trophies/windows-10/ 2026-11-07 · capture: web_fetch · confidence: medium · enemy-tier: 1 · puzzle-tier: 1 · category: mainline · spoiler: progression · achievement: Killer · achievement-hidden: no · trigger_type: progression_ [Confirmed: 3 sources, 2 languages]

### Playing with Others
- **id:** `Multiplayer` · **hidden:** no · **trigger_type:** progression · **genre:** multiplayer · **missable:** no · **ponr-window:** n/a · **vector-binding:** `sections/multiplayer.md`
- **trigger:** finish a multiplayer game without forfeiting.
- **platform-list check:** this name was not among the 26 seen on the live Steam page (2026-11-07 recount); unverified against live platform list.
_source: https://vandal.elespanol.com/logros/pc/dune-spice-wars/111674 , https://www.wemod.com/cheats/dune-spice-wars-trainers/achievements 2026-11-07 · capture: web_fetch · confidence: medium · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none · achievement: Multiplayer · achievement-hidden: no · trigger_type: progression · genre: multiplayer_ [Confirmed: 2 sources, 1 language]

### Duelist
- **id:** `KanlyWin` · **hidden:** no · **trigger_type:** progression · **missable:** no · **ponr-window:** n/a · **vector-binding:** `sections/solo_skirmish.md` (Kanly)
- **trigger:** win a Kanly Duel (1v1).
- **platform-list check:** this name was not among the 26 seen on the live Steam page (2026-11-07 recount); unverified against live platform list.
_source: https://vandal.elespanol.com/logros/pc/dune-spice-wars/111674 , https://www.wemod.com/cheats/dune-spice-wars-trainers/achievements 2026-11-07 · capture: web_fetch · confidence: medium · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none · achievement: KanlyWin · achievement-hidden: no · trigger_type: progression_ [Confirmed: 2 sources, 1 language]

### Thrill of Victory
- **id:** `MultiplayerWin` · **hidden:** no · **trigger_type:** progression · **genre:** multiplayer · **missable:** no · **ponr-window:** n/a · **vector-binding:** `sections/multiplayer.md`
- **trigger:** win a standard multiplayer game with at least one other player.
- **platform-list check:** this name was not among the 26 seen on the live Steam page (2026-11-07 recount); unverified against live platform list.
_source: https://vandal.elespanol.com/logros/pc/dune-spice-wars/111674 , https://www.wemod.com/cheats/dune-spice-wars-trainers/achievements 2026-11-07 · capture: web_fetch · confidence: medium · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none · achievement: MultiplayerWin · achievement-hidden: no · trigger_type: progression · genre: multiplayer_ [Confirmed: 2 sources, 1 language]

## Branch

A faction pick, a victory route, or a campaign path excludes the others.

### Honorable Duke
- **id:** `WinAtreides` · **hidden:** no · **trigger_type:** branch · **genre:** class · **missable:** no · **ponr-window:** n/a · **vector-binding:** `factions/atreides.md`
- **trigger:** win as Atreides (solo or multiplayer).
- **platform-list check:** this name was not among the 26 seen on the live Steam page (2026-11-07 recount); unverified against live platform list.
_source: https://vandal.elespanol.com/logros/pc/dune-spice-wars/111674 , https://www.wemod.com/cheats/dune-spice-wars-trainers/achievements , https://vgtimes.ru/games/dune-spice-wars/achievements-and-trophies/windows-10/ 2026-11-07 · capture: web_fetch · confidence: medium · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none · achievement: WinAtreides · achievement-hidden: no · trigger_type: branch · genre: class · entity: atreides_ [Confirmed: 3 sources, 2 languages]

### Hegemon
- **id:** `Hegemon` · **hidden:** no · **trigger_type:** branch · **missable:** no · **ponr-window:** n/a · **vector-binding:** `mechanics.md` (Victory)
- **trigger:** win by Hegemony (30,000).
- **platform-list check:** this name was not among the 26 seen on the live Steam page (2026-11-07 recount); unverified against live platform list.
_source: https://vandal.elespanol.com/logros/pc/dune-spice-wars/111674 , https://www.wemod.com/cheats/dune-spice-wars-trainers/achievements , https://vgtimes.ru/games/dune-spice-wars/achievements-and-trophies/windows-10/ 2026-11-07 · capture: web_fetch · confidence: medium · enemy-tier: 2 · puzzle-tier: 2 · category: mainline · spoiler: late-game · achievement: Hegemon · achievement-hidden: no · trigger_type: branch_ [Confirmed: 3 sources, 2 languages]

### Disobeying The Form
> **Cross-system dependency** -- see `dependencies.md` PON-001.
- **id:** `UseAtomicsOnSomeoneElse` · **hidden:** no · **trigger_type:** branch · **missable:** no (but costly) · **ponr-window:** n/a · **vector-binding:** `mechanics.md` (Landsraad Standing losses)
- **trigger:** use atomics on someone else. **prereqs:** a Nuclear Silo (2,000 Solari + 1,000 Plascrete + 10 Fuel Cells, once per faction). Using Nuclear Warheads costs -500 Standing and rules out the Governorship in that game.
- **platform-list check:** this name was not among the 26 seen on the live Steam page (2026-11-07 recount); unverified against live platform list.
_source: https://dune-spice-wars.github.io/duneopedia/buildings , https://www.wemod.com/cheats/dune-spice-wars-trainers/achievements , https://steamcommunity.com/sharedfiles/filedetails/?id=3058990585 2026-11-07 · capture: web_fetch · confidence: medium · enemy-tier: 2 · puzzle-tier: 2 · category: mainline · spoiler: late-game · achievement: UseAtomicsOnSomeoneElse · achievement-hidden: no · trigger_type: branch_ [Confirmed: 3 sources, 1 language]

### Conqueror
- **id:** `Conqueror` · **hidden:** no · **trigger_type:** branch · **missable:** no · **ponr-window:** n/a · **vector-binding:** `mechanics.md` (Victory)
- **trigger:** win by destroying the last base.
- **platform-list check:** this name was not among the 26 seen on the live Steam page (2026-11-07 recount); unverified against live platform list.
_source: https://vandal.elespanol.com/logros/pc/dune-spice-wars/111674 , https://www.wemod.com/cheats/dune-spice-wars-trainers/achievements , https://gameplay.tips/guides/dune-spice-wars-100-full-achievement-guide.html 2026-11-07 · capture: web_fetch · confidence: medium · enemy-tier: 2 · puzzle-tier: 2 · category: mainline · spoiler: late-game · achievement: Conqueror · achievement-hidden: no · trigger_type: branch_ [Confirmed: 3 sources, 1 language]

### Visionary Rebel
- **id:** `WinFremen` · **hidden:** no · **trigger_type:** branch · **genre:** class · **missable:** no · **ponr-window:** n/a · **vector-binding:** `factions/fremen.md`
- **trigger:** win as Fremen.
- **platform-list check:** this name was not among the 26 seen on the live Steam page (2026-11-07 recount); unverified against live platform list.
_source: https://vandal.elespanol.com/logros/pc/dune-spice-wars/111674 , https://www.wemod.com/cheats/dune-spice-wars-trainers/achievements , https://vgtimes.ru/games/dune-spice-wars/achievements-and-trophies/windows-10/ 2026-11-07 · capture: web_fetch · confidence: medium · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none · achievement: WinFremen · achievement-hidden: no · trigger_type: branch · genre: class · entity: fremen_ [Confirmed: 3 sources, 2 languages]

### Governor
> **Cross-system dependency** -- see `dependencies.md` PON-001.
> **Cross-system dependency** -- see `dependencies.md` PON-003.
- **id:** `Governor` · **hidden:** no · **trigger_type:** branch · **missable:** no · **ponr-window:** n/a · **vector-binding:** `mechanics.md` (Landsraad, Victory)
- **trigger:** win through the Dune Governorship (Battle/MP). **prereqs:** 450 Standing and 1 Charter (an Atreides at 10,000 Hegemony needs only the Standing); hold the title for a disputed number of days (30, 45, or 60 in 2022 pages; unresolved, see `sections/landsraad.md`).
- **platform-list check:** this name was not among the 26 seen on the live Steam page (2026-11-07 recount); unverified against live platform list.
_source: https://dune-spice-wars.github.io/duneopedia/gameplay , https://dunespicewars.fandom.com/wiki/Charter , https://dune-spice-wars.github.io/duneopedia/atreides , https://vandal.elespanol.com/logros/pc/dune-spice-wars/111674 2026-11-07 · capture: web_fetch · confidence: low · enemy-tier: 2 · puzzle-tier: 2 · category: mainline · spoiler: late-game · achievement: Governor · achievement-hidden: no · trigger_type: branch_ [Contradicted across sources -- see notes]

### Dreaded Baron
- **id:** `WinHarkonnen` · **hidden:** no · **trigger_type:** branch · **genre:** class · **missable:** no · **ponr-window:** n/a · **vector-binding:** `factions/harkonnen.md`
- **trigger:** win as Harkonnen.
- **platform-list check:** this name was not among the 26 seen on the live Steam page (2026-11-07 recount); unverified against live platform list.
_source: https://vandal.elespanol.com/logros/pc/dune-spice-wars/111674 , https://www.wemod.com/cheats/dune-spice-wars-trainers/achievements , https://vgtimes.ru/games/dune-spice-wars/achievements-and-trophies/windows-10/ 2026-11-07 · capture: web_fetch · confidence: medium · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none · achievement: WinHarkonnen · achievement-hidden: no · trigger_type: branch · genre: class · entity: harkonnen_ [Confirmed: 3 sources, 2 languages]

### Ruthless Emperor
- **id:** `WinCorrino` · **hidden:** no · **trigger_type:** branch · **genre:** class · **missable:** no · **ponr-window:** n/a · **vector-binding:** `factions/corrino.md`
- **trigger:** win as Corrino.
- **platform-list check:** this name was not among the 26 seen on the live Steam page (2026-11-07 recount); unverified against live platform list.
_source: https://vandal.elespanol.com/logros/pc/dune-spice-wars/111674 , https://www.wemod.com/cheats/dune-spice-wars-trainers/achievements , https://vgtimes.ru/games/dune-spice-wars/achievements-and-trophies/windows-10/ 2026-11-07 · capture: web_fetch · confidence: medium · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none · achievement: WinCorrino · achievement-hidden: no · trigger_type: branch · genre: class · entity: corrino_ [Confirmed: 3 sources, 2 languages]

### Cunning Criminal
- **id:** `WinSmugglers` · **hidden:** no · **trigger_type:** branch · **genre:** class · **missable:** no · **ponr-window:** n/a · **vector-binding:** `factions/smugglers.md`
- **trigger:** win as Smugglers.
- **platform-list check:** this name was not among the 26 seen on the live Steam page (2026-11-07 recount); unverified against live platform list.
_source: https://vandal.elespanol.com/logros/pc/dune-spice-wars/111674 , https://www.wemod.com/cheats/dune-spice-wars-trainers/achievements , https://vgtimes.ru/games/dune-spice-wars/achievements-and-trophies/windows-10/ 2026-11-07 · capture: web_fetch · confidence: medium · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none · achievement: WinSmugglers · achievement-hidden: no · trigger_type: branch · genre: class · entity: smugglers_ [Confirmed: 3 sources, 2 languages]

### Magnate
- **id:** `Magnate` · **hidden:** no · **trigger_type:** branch · **missable:** no · **ponr-window:** n/a · **vector-binding:** `mechanics.md` (CHOAM, Victory)
- **trigger:** win by holding over half of CHOAM Shares. **prereqs:** CHOAM opens after about one month.
- **platform-list check:** this name was not among the 26 seen on the live Steam page (2026-11-07 recount); unverified against live platform list.
_source: https://vandal.elespanol.com/logros/pc/dune-spice-wars/111674 , https://www.wemod.com/cheats/dune-spice-wars-trainers/achievements , https://steamcommunity.com/sharedfiles/filedetails/?id=3058990585 2026-11-07 · capture: web_fetch · confidence: medium · enemy-tier: 2 · puzzle-tier: 2 · category: mainline · spoiler: late-game · achievement: Magnate · achievement-hidden: no · trigger_type: branch_ [Confirmed: 3 sources, 2 languages]

### The Duke of Caladan
- **id:** `ConquestWinAtreides` · **hidden:** no · **trigger_type:** branch · **genre:** class, mission · **missable:** scenario-locked · **ponr-window:** Pressure under 100% · **vector-binding:** `sections/conquest.md`
- **trigger:** win a Conquest as Atreides.
- **platform-list check:** this name was not among the 26 seen on the live Steam page (2026-11-07 recount); unverified against live platform list.
_source: https://vandal.elespanol.com/logros/pc/dune-spice-wars/111674 , https://www.wemod.com/cheats/dune-spice-wars-trainers/achievements 2026-11-07 · capture: web_fetch · confidence: medium · enemy-tier: 1 · puzzle-tier: 1 · category: mainline · spoiler: progression · achievement: ConquestWinAtreides · achievement-hidden: no · trigger_type: branch · genre: class, mission · entity: atreides_ [Confirmed: 2 sources, 1 language]

### Assassin
- **id:** `Assassin` · **hidden:** no · **trigger_type:** branch · **missable:** no · **ponr-window:** n/a · **vector-binding:** `mechanics.md` (Espionage, Victory)
- **trigger:** win by assassinating your last opponent.
- **platform-list check:** this name was not among the 26 seen on the live Steam page (2026-11-07 recount); unverified against live platform list.
_source: https://vandal.elespanol.com/logros/pc/dune-spice-wars/111674 , https://www.wemod.com/cheats/dune-spice-wars-trainers/achievements , https://vgtimes.ru/games/dune-spice-wars/achievements-and-trophies/windows-10/ 2026-11-07 · capture: web_fetch · confidence: medium · enemy-tier: 2 · puzzle-tier: 2 · category: mainline · spoiler: late-game · achievement: Assassin · achievement-hidden: no · trigger_type: branch_ [Confirmed: 3 sources, 2 languages]

### Refined Archduchess
- **id:** `WinEcaz` · **hidden:** no · **trigger_type:** branch · **genre:** class · **missable:** no · **ponr-window:** n/a · **vector-binding:** `factions/ecaz.md`
- **trigger:** win as Ecaz.
- **platform-list check:** this name was not among the 26 seen on the live Steam page (2026-11-07 recount); unverified against live platform list.
_source: https://vandal.elespanol.com/logros/pc/dune-spice-wars/111674 , https://www.wemod.com/cheats/dune-spice-wars-trainers/achievements 2026-11-07 · capture: web_fetch · confidence: medium · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none · achievement: WinEcaz · achievement-hidden: no · trigger_type: branch · genre: class · entity: ecaz_ [Confirmed: 2 sources, 1 language]

### Successful Betrayal
> **Cross-system dependency** -- see `dependencies.md` DEP-001.
- **id:** `SuccessfulBetrayal` · **hidden:** no · **trigger_type:** branch · **genre:** social · **missable:** no · **ponr-window:** n/a · **vector-binding:** `mechanics.md` (Alliances)
- **trigger:** eliminate a faction you betrayed within the last 20 days. **prereqs:** betrayal costs -100 Standing (Ecaz follow the Community Update #4 rule).
- **platform-list check:** this name was not among the 26 seen on the live Steam page (2026-11-07 recount); unverified against live platform list.
_source: https://vandal.elespanol.com/logros/pc/dune-spice-wars/111674 , https://www.wemod.com/cheats/dune-spice-wars-trainers/achievements 2026-11-07 · capture: web_fetch · confidence: medium · enemy-tier: 1 · puzzle-tier: 1 · category: mainline · spoiler: progression · achievement: SuccessfulBetrayal · achievement-hidden: no · trigger_type: branch · genre: social_ [Confirmed: 2 sources, 1 language]

### Distraction
- **id:** `Distraction` · **hidden:** no · **trigger_type:** branch · **genre:** social · **missable:** no · **ponr-window:** n/a · **vector-binding:** `mechanics.md` (Landsraad)
- **trigger:** win while a player you helped elect is Dune Governor (Battle/MP). **prereqs:** the Governor must be another faction; you vote them in.
- **platform-list check:** this name was not among the 26 seen on the live Steam page (2026-11-07 recount); unverified against live platform list.
_source: https://www.wemod.com/cheats/dune-spice-wars-trainers/achievements 2026-11-07 · capture: web_fetch · confidence: medium · enemy-tier: 2 · puzzle-tier: 2 · category: mainline · spoiler: late-game · achievement: Distraction · achievement-hidden: no · trigger_type: branch · genre: social_ [Single source -- verify · class:editorial-en]

### Friendly Native
> **Cross-system dependency** -- see `dependencies.md` DEP-010.
- **id:** `ConquestFriendlyNative` · **hidden:** unknown · **trigger_type:** branch · **genre:** mission, social · **missable:** scenario-locked · **ponr-window:** Pressure under 100% · **vector-binding:** `sections/conquest.md` (Fremen friendship)
- **trigger:** ally the Fremen in Conquest (TrueSteamAchievements, read in P2). **prereqs:** Fremen friendship 100% (`sections/conquest.md`).
- **platform-list check:** this name was not among the 26 seen on the live Steam page (2026-11-07 recount); unverified against live platform list.
_source: https://truesteamachievements.com/game/Dune-Spice-Wars/achievements , https://en.namu.wiki/w/Dune:%20Spice%20Wars/%EC%A0%95%EB%B3%B5%20%EB%AA%A8%EB%93%9C 2026-11-07 · capture: web_fetch · confidence: medium · enemy-tier: 2 · puzzle-tier: 2 · category: mainline · spoiler: late-game · achievement: ConquestFriendlyNative · achievement-hidden: unknown · trigger_type: branch · genre: mission, social · entity: fremen_ [Single source -- verify · class:editorial-en]

### The Emperor of Salusa Secundus
- **id:** `ConquestWinCorrino` · **hidden:** no · **trigger_type:** branch · **genre:** class, mission · **missable:** scenario-locked · **ponr-window:** Pressure under 100% · **vector-binding:** `sections/conquest.md`
- **trigger:** win a Conquest as Corrino.
- **platform-list check:** this name was not among the 26 seen on the live Steam page (2026-11-07 recount); unverified against live platform list.
_source: https://vandal.elespanol.com/logros/pc/dune-spice-wars/111674 , https://www.wemod.com/cheats/dune-spice-wars-trainers/achievements 2026-11-07 · capture: web_fetch · confidence: medium · enemy-tier: 1 · puzzle-tier: 1 · category: mainline · spoiler: progression · achievement: ConquestWinCorrino · achievement-hidden: no · trigger_type: branch · genre: class, mission · entity: corrino_ [Confirmed: 2 sources, 1 language]

### Clever Earl
- **id:** `WinVernius` · **hidden:** no · **trigger_type:** branch · **genre:** class · **missable:** no · **ponr-window:** n/a · **vector-binding:** `factions/vernius.md`
- **trigger:** win a game as House Vernius (any mode that has a normal win; no difficulty limit stated). **prereqs:** the paid DLC.
- **platform-list check:** this name was not among the 26 seen on the live Steam page (2026-11-07 recount); unverified against live platform list.
_source: https://www.wemod.com/cheats/dune-spice-wars-trainers/achievements , https://truesteamachievements.com/game/Dune-Spice-Wars/achievements 2026-11-07 · capture: web_fetch · confidence: medium · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: dlc:vernius · achievement: WinVernius · achievement-hidden: no · trigger_type: branch · genre: class · entity: vernius_ [Single source -- verify · class:editorial-en]

### The Baron of Giedi Prime
- **id:** `ConquestWinHarkonnen` · **hidden:** no · **trigger_type:** branch · **genre:** class, mission · **missable:** scenario-locked · **ponr-window:** Pressure under 100% · **vector-binding:** `sections/conquest.md`
- **trigger:** win a Conquest as Harkonnen.
- **platform-list check:** this name was not among the 26 seen on the live Steam page (2026-11-07 recount); unverified against live platform list.
_source: https://vandal.elespanol.com/logros/pc/dune-spice-wars/111674 , https://www.wemod.com/cheats/dune-spice-wars-trainers/achievements 2026-11-07 · capture: web_fetch · confidence: medium · enemy-tier: 1 · puzzle-tier: 1 · category: mainline · spoiler: progression · achievement: ConquestWinHarkonnen · achievement-hidden: no · trigger_type: branch · genre: class, mission · entity: harkonnen_ [Confirmed: 2 sources, 1 language]

### The Archduchess of Ecaz
- **id:** `ConquestWinEcaz` · **hidden:** no · **trigger_type:** branch · **genre:** class, mission · **missable:** scenario-locked · **ponr-window:** Pressure under 100% · **vector-binding:** `sections/conquest.md`
- **trigger:** win a Conquest as Ecaz.
- **platform-list check:** this name was not among the 26 seen on the live Steam page (2026-11-07 recount); unverified against live platform list.
_source: https://vandal.elespanol.com/logros/pc/dune-spice-wars/111674 , https://www.wemod.com/cheats/dune-spice-wars-trainers/achievements 2026-11-07 · capture: web_fetch · confidence: medium · enemy-tier: 1 · puzzle-tier: 1 · category: mainline · spoiler: progression · achievement: ConquestWinEcaz · achievement-hidden: no · trigger_type: branch · genre: class, mission · entity: ecaz_ [Confirmed: 2 sources, 1 language]

### United People
- **id:** `ConquestUnitedPeople` · **hidden:** unknown · **trigger_type:** branch · **genre:** mission · **missable:** scenario-locked · **ponr-window:** Pressure under 100% · **vector-binding:** `sections/conquest.md` (Fremen unity)
- **trigger:** unite the Fremen in Conquest (TrueSteamAchievements, read in P2). **prereqs:** Fremen unity 100% in a Fremen run (`sections/conquest.md`).
- **platform-list check:** this name was not among the 26 seen on the live Steam page (2026-11-07 recount); unverified against live platform list.
_source: https://truesteamachievements.com/game/Dune-Spice-Wars/achievements , https://en.namu.wiki/w/Dune:%20Spice%20Wars/%EC%A0%95%EB%B3%B5%20%EB%AA%A8%EB%93%9C 2026-11-07 · capture: web_fetch · confidence: medium · enemy-tier: 2 · puzzle-tier: 2 · category: mainline · spoiler: late-game · achievement: ConquestUnitedPeople · achievement-hidden: unknown · trigger_type: branch · genre: mission · entity: fremen_ [Single source -- verify · class:editorial-en]

### The Liberator of Dune
- **id:** `ConquestWinFremen` · **hidden:** unknown · **trigger_type:** branch · **genre:** class, mission · **missable:** scenario-locked · **ponr-window:** Pressure under 100% · **vector-binding:** `sections/conquest.md`
- **trigger:** win a Conquest as Fremen. TrueSteamAchievements lists this name among the Conquest house wins without naming the house; the Fremen reading rests on the P1 search summary of a blocked page and on the Fremen being the sixth playable house (low confidence on the house).
- **platform-list check:** this name was not among the 26 seen on the live Steam page (2026-11-07 recount); unverified against live platform list.
_source: https://truesteamachievements.com/game/Dune-Spice-Wars/achievements 2026-11-07 · capture: web_fetch · confidence: low · enemy-tier: 1 · puzzle-tier: 1 · category: mainline · spoiler: progression · achievement: ConquestWinFremen · achievement-hidden: unknown · trigger_type: branch · genre: class, mission · entity: fremen_ [Single source -- verify · class:editorial-en]

### The Earl of Ix
- **id:** `ConquestWinVernius` · **hidden:** no · **trigger_type:** branch · **genre:** class, mission · **missable:** scenario-locked · **ponr-window:** Pressure under 100% · **vector-binding:** `sections/conquest.md`, `factions/vernius.md`
- **trigger:** win a Conquest as House Vernius (no difficulty stated). **prereqs:** the paid DLC; Vernius's own Conquest win goals are not stated by any source read.
- **platform-list check:** this name was not among the 26 seen on the live Steam page (2026-11-07 recount); unverified against live platform list.
_source: https://www.wemod.com/cheats/dune-spice-wars-trainers/achievements , https://truesteamachievements.com/game/Dune-Spice-Wars/achievements 2026-11-07 · capture: web_fetch · confidence: medium · enemy-tier: 2 · puzzle-tier: 2 · category: mainline · spoiler: dlc:vernius · achievement: ConquestWinVernius · achievement-hidden: no · trigger_type: branch · genre: class, mission · entity: vernius_ [Single source -- verify · class:editorial-en]

### The Godfather of Arrakis
- **id:** `ConquestWinSmugglers` · **hidden:** unknown · **trigger_type:** branch · **genre:** class, mission · **missable:** scenario-locked · **ponr-window:** Pressure under 100% · **vector-binding:** `sections/conquest.md`
- **trigger:** win a Conquest as Smugglers. TrueSteamAchievements lists this name among the Conquest house wins without naming the house; the Smuggler reading rests on the P1 search summary of a blocked page and on the Smugglers being the other newly playable house (low confidence on the house).
- **platform-list check:** this name was not among the 26 seen on the live Steam page (2026-11-07 recount); unverified against live platform list.
_source: https://truesteamachievements.com/game/Dune-Spice-Wars/achievements 2026-11-07 · capture: web_fetch · confidence: low · enemy-tier: 1 · puzzle-tier: 1 · category: mainline · spoiler: progression · achievement: ConquestWinSmugglers · achievement-hidden: unknown · trigger_type: branch · genre: class, mission · entity: smugglers_ [Single source -- verify · class:editorial-en]

### Corrupted Nobility
- **id:** `ConquestCorruptedNobility` · **hidden:** unknown · **trigger_type:** branch · **genre:** class, mission · **missable:** scenario-locked · **ponr-window:** Pressure under 100% · **vector-binding:** `sections/conquest.md` (Faufreluche corruption)
- **trigger:** corrupt the Faufreluches in a Smuggler Conquest (TrueSteamAchievements, read in P2). **prereqs:** corruption 100% (`sections/conquest.md`).
- **platform-list check:** this name was not among the 26 seen on the live Steam page (2026-11-07 recount); unverified against live platform list.
_source: https://truesteamachievements.com/game/Dune-Spice-Wars/achievements , https://en.namu.wiki/w/Dune:%20Spice%20Wars/%EC%A0%95%EB%B3%B5%20%EB%AA%A8%EB%93%9C 2026-11-07 · capture: web_fetch · confidence: medium · enemy-tier: 2 · puzzle-tier: 2 · category: mainline · spoiler: late-game · achievement: ConquestCorruptedNobility · achievement-hidden: unknown · trigger_type: branch · genre: class, mission · entity: smugglers_ [Single source -- verify · class:editorial-en]

## Mastery

Skill-bound or restriction-bound challenges.

### Easy Win
- **id:** `WinEasy` · **hidden:** no · **trigger_type:** mastery · **missable:** only-on-difficulty · **ponr-window:** n/a · **vector-binding:** `sections/solo_skirmish.md`
- **trigger:** win on Easy or higher (solo), any victory type. A win on Insane also credits the lower ones (2022-23 tip; current patch unverified).
_source: https://vandal.elespanol.com/logros/pc/dune-spice-wars/111674 , https://www.wemod.com/cheats/dune-spice-wars-trainers/achievements , https://vgtimes.ru/games/dune-spice-wars/achievements-and-trophies/windows-10/ 2026-11-07 · capture: web_fetch · confidence: medium · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none · achievement: WinEasy · achievement-hidden: no · trigger_type: mastery_ [Confirmed: 3 sources, 2 languages]

### Plans within Plans
- **id:** `ConquestWinWithSecondaryObjective` · **hidden:** no · **trigger_type:** mastery · **genre:** mission · **missable:** yes · **ponr-window:** the secondary objective must be completed during that mission · **vector-binding:** `sections/conquest.md`
- **trigger:** win a Conquest mission with its secondary objective done.
- **platform-list check:** this name was not among the 26 seen on the live Steam page (2026-11-07 recount); unverified against live platform list.
_source: https://vandal.elespanol.com/logros/pc/dune-spice-wars/111674 , https://www.wemod.com/cheats/dune-spice-wars-trainers/achievements 2026-11-07 · capture: web_fetch · confidence: medium · enemy-tier: 1 · puzzle-tier: 1 · category: mainline · spoiler: progression · achievement: ConquestWinWithSecondaryObjective · achievement-hidden: no · trigger_type: mastery · genre: mission_ [Confirmed: 2 sources, 1 language]

### Desert Fighter
- **id:** `WinMedium` · **hidden:** no · **trigger_type:** mastery · **missable:** only-on-difficulty · **ponr-window:** n/a · **vector-binding:** `sections/solo_skirmish.md`
- **trigger:** win on Medium or higher (solo).
- **platform-list check:** this name was not among the 26 seen on the live Steam page (2026-11-07 recount); unverified against live platform list.
_source: https://vandal.elespanol.com/logros/pc/dune-spice-wars/111674 , https://www.wemod.com/cheats/dune-spice-wars-trainers/achievements , https://vgtimes.ru/games/dune-spice-wars/achievements-and-trophies/windows-10/ 2026-11-07 · capture: web_fetch · confidence: medium · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none · achievement: WinMedium · achievement-hidden: no · trigger_type: mastery_ [Confirmed: 3 sources, 2 languages]

### Strategist
- **id:** `WinHard` · **hidden:** no · **trigger_type:** mastery · **missable:** only-on-difficulty · **ponr-window:** n/a · **vector-binding:** `sections/solo_skirmish.md`
- **trigger:** win on Hard or higher (solo).
- **platform-list check:** this name was not among the 26 seen on the live Steam page (2026-11-07 recount); unverified against live platform list.
_source: https://vandal.elespanol.com/logros/pc/dune-spice-wars/111674 , https://www.wemod.com/cheats/dune-spice-wars-trainers/achievements , https://vgtimes.ru/games/dune-spice-wars/achievements-and-trophies/windows-10/ 2026-11-07 · capture: web_fetch · confidence: medium · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none · achievement: WinHard · achievement-hidden: no · trigger_type: mastery_ [Confirmed: 3 sources, 2 languages]

### Peaceful Dune
- **id:** `WinAtPeace` · **hidden:** no · **trigger_type:** mastery · **genre:** social, multiplayer · **missable:** yes · **ponr-window:** needs a 4-player lobby · **vector-binding:** `sections/multiplayer.md`
- **trigger:** win while in Truce with 3 living opponents for at least a month. **prereqs:** hold a Truce with all three rivals at once.
- **platform-list check:** this name was not among the 26 seen on the live Steam page (2026-11-07 recount); unverified against live platform list.
_source: https://vandal.elespanol.com/logros/pc/dune-spice-wars/111674 , https://www.wemod.com/cheats/dune-spice-wars-trainers/achievements 2026-11-07 · capture: web_fetch · confidence: medium · enemy-tier: 1 · puzzle-tier: 1 · category: mainline · spoiler: progression · achievement: WinAtPeace · achievement-hidden: no · trigger_type: mastery · genre: social, multiplayer_ [Confirmed: 2 sources, 1 language]

### One Against All
- **id:** `WinAtWar` · **hidden:** no · **trigger_type:** mastery · **genre:** multiplayer · **missable:** yes · **ponr-window:** needs a 4-player lobby · **vector-binding:** `sections/multiplayer.md`
- **trigger:** win while in Conflict with 3 living opponents for at least 3 months.
- **platform-list check:** this name was not among the 26 seen on the live Steam page (2026-11-07 recount); unverified against live platform list.
_source: https://vandal.elespanol.com/logros/pc/dune-spice-wars/111674 , https://www.wemod.com/cheats/dune-spice-wars-trainers/achievements 2026-11-07 · capture: web_fetch · confidence: medium · enemy-tier: 1 · puzzle-tier: 1 · category: mainline · spoiler: progression · achievement: WinAtWar · achievement-hidden: no · trigger_type: mastery · genre: multiplayer_ [Confirmed: 2 sources, 1 language]

### Prudent
- **id:** `WinNoLosses` · **hidden:** no · **trigger_type:** mastery · **missable:** yes (solo only) · **ponr-window:** the first permanent unit or village lost · **vector-binding:** `sections/solo_skirmish.md`
- **trigger:** win solo without losing or disbanding any permanent military unit or village (temporary units are not counted).
- **platform-list check:** this name was not among the 26 seen on the live Steam page (2026-11-07 recount); unverified against live platform list.
_source: https://vandal.elespanol.com/logros/pc/dune-spice-wars/111674 , https://www.wemod.com/cheats/dune-spice-wars-trainers/achievements 2026-11-07 · capture: web_fetch · confidence: medium · enemy-tier: 1 · puzzle-tier: 1 · category: mainline · spoiler: progression · achievement: WinNoLosses · achievement-hidden: no · trigger_type: mastery_ [Confirmed: 2 sources, 1 language]

### Master of Arrakis
- **id:** `WinInsane` · **hidden:** no · **trigger_type:** mastery · **missable:** only-on-difficulty · **ponr-window:** n/a · **vector-binding:** `sections/solo_skirmish.md`
- **trigger:** win on Insane (solo). It also unlocks the lower win achievements per an early-access-era tip.
- **platform-list check:** this name was not among the 26 seen on the live Steam page (2026-11-07 recount); unverified against live platform list.
_source: https://vandal.elespanol.com/logros/pc/dune-spice-wars/111674 , https://www.wemod.com/cheats/dune-spice-wars-trainers/achievements , https://vgtimes.ru/games/dune-spice-wars/achievements-and-trophies/windows-10/ 2026-11-07 · capture: web_fetch · confidence: medium · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none · achievement: WinInsane · achievement-hidden: no · trigger_type: mastery_ [Confirmed: 3 sources, 2 languages]

### Pariah
- **id:** `WinMonthPariah` · **hidden:** no · **trigger_type:** mastery · **missable:** yes (solo only) · **ponr-window:** Standing must stay under 100 for the month · **vector-binding:** `mechanics.md` (Standing)
- **trigger:** win solo while at Pariah Standing for at least a month. **prereqs:** Standing under 100; a Landsraad Guard attacks every 20 days.
- **platform-list check:** this name was not among the 26 seen on the live Steam page (2026-11-07 recount); unverified against live platform list.
_source: https://dune-spice-wars.github.io/duneopedia/arrakis , https://vandal.elespanol.com/logros/pc/dune-spice-wars/111674 , https://www.wemod.com/cheats/dune-spice-wars-trainers/achievements 2026-11-07 · capture: web_fetch · confidence: medium · enemy-tier: 1 · puzzle-tier: 1 · category: mainline · spoiler: progression · achievement: WinMonthPariah · achievement-hidden: no · trigger_type: mastery_ [Confirmed: 3 sources, 1 language]

### No Mercy for Traitors
- **id:** `NoMercy` · **hidden:** no · **trigger_type:** mastery · **genre:** social · **missable:** no · **ponr-window:** n/a · **vector-binding:** `mechanics.md` (Alliances)
- **trigger:** eliminate a faction that betrayed you within the last 20 days.
- **platform-list check:** this name was not among the 26 seen on the live Steam page (2026-11-07 recount); unverified against live platform list.
_source: https://vandal.elespanol.com/logros/pc/dune-spice-wars/111674 , https://www.wemod.com/cheats/dune-spice-wars-trainers/achievements 2026-11-07 · capture: web_fetch · confidence: medium · enemy-tier: 1 · puzzle-tier: 1 · category: mainline · spoiler: progression · achievement: NoMercy · achievement-hidden: no · trigger_type: mastery · genre: social_ [Confirmed: 2 sources, 1 language]

### No Offense
- **id:** `WinNoVillageAttacks` · **hidden:** no · **trigger_type:** mastery · **genre:** class · **missable:** yes · **ponr-window:** the first village attack · **vector-binding:** `factions/atreides.md`
- **trigger:** as Atreides, win without ever attacking a village. **prereqs:** Peaceful Annexation only; one player did it with CHOAM.
- **platform-list check:** this name was not among the 26 seen on the live Steam page (2026-11-07 recount); unverified against live platform list.
_source: https://dune-spice-wars.github.io/duneopedia/atreides , https://vandal.elespanol.com/logros/pc/dune-spice-wars/111674 , https://steamcommunity.com/app/1605220/discussions/0/6393481422733947450 2026-11-07 · capture: web_fetch · confidence: medium · enemy-tier: 1 · puzzle-tier: 1 · category: mainline · spoiler: progression · achievement: WinNoVillageAttacks · achievement-hidden: no · trigger_type: mastery · genre: class · entity: atreides_ [Confirmed: 3 sources, 1 language]

### Insanity
- **id:** `Insanity` · **hidden:** no · **trigger_type:** mastery · **missable:** only-on-difficulty · **ponr-window:** settings fixed at game start · **vector-binding:** `settings.md`, `sections/solo_skirmish.md`
- **trigger:** win against 3 Insane AIs, solo, with Sandworm, Storm, Neutral and Contract settings at maximum and all victory conditions on.
- **platform-list check:** this name was not among the 26 seen on the live Steam page (2026-11-07 recount); unverified against live platform list.
_source: https://vandal.elespanol.com/logros/pc/dune-spice-wars/111674 , https://www.wemod.com/cheats/dune-spice-wars-trainers/achievements 2026-11-07 · capture: web_fetch · confidence: medium · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none · achievement: Insanity · achievement-hidden: no · trigger_type: mastery_ [Confirmed: 2 sources, 1 language]

### Savage
- **id:** `WinNoDevs` · **hidden:** no · **trigger_type:** mastery · **missable:** yes (solo only) · **ponr-window:** the first Development researched · **vector-binding:** `sections/solo_skirmish.md`
- **trigger:** win solo without researching any development. Developments unlock after the first village capture, so avoid them.
- **platform-list check:** this name was not among the 26 seen on the live Steam page (2026-11-07 recount); unverified against live platform list.
_source: https://vandal.elespanol.com/logros/pc/dune-spice-wars/111674 , https://www.wemod.com/cheats/dune-spice-wars-trainers/achievements , https://vgtimes.ru/games/dune-spice-wars/achievements-and-trophies/windows-10/ 2026-11-07 · capture: web_fetch · confidence: medium · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none · achievement: WinNoDevs · achievement-hidden: no · trigger_type: mastery_ [Confirmed: 3 sources, 2 languages]

### Kwisatz Haderach
> **Cross-system dependency** -- see `dependencies.md` SEQ-001.
- **id:** `ConquestKwisatzHaderach` · **hidden:** unknown · **trigger_type:** mastery · **genre:** mission · **missable:** yes (time limit per run) · **ponr-window:** four years (in-game unconfirmed) · **vector-binding:** `sections/conquest.md`
- **trigger:** win a Conquest in under 4 years (TrueSteamAchievements, read in P2; "in-game" is not confirmed).
- **platform-list check:** this name was not among the 26 seen on the live Steam page (2026-11-07 recount); unverified against live platform list.
_source: https://truesteamachievements.com/game/Dune-Spice-Wars/achievements 2026-11-07 · capture: web_fetch · confidence: medium · enemy-tier: 2 · puzzle-tier: 2 · category: mainline · spoiler: late-game · achievement: ConquestKwisatzHaderach · achievement-hidden: unknown · trigger_type: mastery · genre: mission_ [Single source -- verify · class:editorial-en]

### Golden Path
- **id:** `ConquestGoldenPath` · **hidden:** unknown · **trigger_type:** mastery · **genre:** mission · **missable:** only-on-difficulty · **ponr-window:** difficulty chosen at run start · **vector-binding:** `sections/conquest.md`
- **trigger:** win a Conquest on Insane (TrueSteamAchievements, read in P2).
- **platform-list check:** this name was not among the 26 seen on the live Steam page (2026-11-07 recount); unverified against live platform list.
_source: https://truesteamachievements.com/game/Dune-Spice-Wars/achievements 2026-11-07 · capture: web_fetch · confidence: medium · enemy-tier: 1 · puzzle-tier: 1 · category: mainline · spoiler: progression · achievement: ConquestGoldenPath · achievement-hidden: unknown · trigger_type: mastery · genre: mission_ [Single source -- verify · class:editorial-en]

## Collection

A finite, named set completed in full.

### Economist
- **id:** `AllEconomicDevs` · **hidden:** no · **trigger_type:** collection · **missable:** no · **ponr-window:** n/a · **vector-binding:** `items/developments.md`
- **trigger:** research all Economy developments. About 75% of all developments is typical, so this needs every Economy node. The shared set is 9 nodes (`items/developments.md`); whether the faction-unique replacement nodes count towards "all" is unknown.
_source: https://vandal.elespanol.com/logros/pc/dune-spice-wars/111674 , https://www.wemod.com/cheats/dune-spice-wars-trainers/achievements , https://steamcommunity.com/sharedfiles/filedetails/?id=3058990585 2026-11-07 · capture: web_fetch · confidence: medium · enemy-tier: 1 · puzzle-tier: 1 · category: mainline · spoiler: progression · achievement: AllEconomicDevs · achievement-hidden: no · trigger_type: collection_ [Confirmed: 3 sources, 1 language]

### Logistician
- **id:** `AllMilitaryDevs` · **hidden:** no · **trigger_type:** collection · **missable:** no · **ponr-window:** n/a · **vector-binding:** `items/developments.md`
- **trigger:** research all Military developments. The shared set is 9 nodes (`items/developments.md`); whether the faction-unique replacement nodes count is unknown.
- **platform-list check:** this name was not among the 26 seen on the live Steam page (2026-11-07 recount); unverified against live platform list.
_source: https://vandal.elespanol.com/logros/pc/dune-spice-wars/111674 , https://www.wemod.com/cheats/dune-spice-wars-trainers/achievements , https://vgtimes.ru/games/dune-spice-wars/achievements-and-trophies/windows-10/ 2026-11-07 · capture: web_fetch · confidence: medium · enemy-tier: 1 · puzzle-tier: 1 · category: mainline · spoiler: progression · achievement: AllMilitaryDevs · achievement-hidden: no · trigger_type: collection_ [Confirmed: 3 sources, 2 languages]

### Sociologist
- **id:** `AllExpansionDevs` · **hidden:** no · **trigger_type:** collection · **missable:** no · **ponr-window:** n/a · **vector-binding:** `items/developments.md`
- **trigger:** research all Expansion developments. The shared set is 9 nodes (`items/developments.md`); whether the faction-unique replacement nodes count is unknown.
- **platform-list check:** this name was not among the 26 seen on the live Steam page (2026-11-07 recount); unverified against live platform list.
_source: https://vandal.elespanol.com/logros/pc/dune-spice-wars/111674 , https://www.wemod.com/cheats/dune-spice-wars-trainers/achievements , https://vgtimes.ru/games/dune-spice-wars/achievements-and-trophies/windows-10/ 2026-11-07 · capture: web_fetch · confidence: medium · enemy-tier: 1 · puzzle-tier: 1 · category: mainline · spoiler: progression · achievement: AllExpansionDevs · achievement-hidden: no · trigger_type: collection_ [Confirmed: 3 sources, 2 languages]

### Analyst
- **id:** `AllStatecraftDevs` · **hidden:** no · **trigger_type:** collection · **missable:** no · **ponr-window:** n/a · **vector-binding:** `items/developments.md`
- **trigger:** research all Political (Statecraft) developments. The shared set is 9 nodes (`items/developments.md`); whether the faction-unique replacement nodes count is unknown.
- **platform-list check:** this name was not among the 26 seen on the live Steam page (2026-11-07 recount); unverified against live platform list.
_source: https://vandal.elespanol.com/logros/pc/dune-spice-wars/111674 , https://www.wemod.com/cheats/dune-spice-wars-trainers/achievements , https://vgtimes.ru/games/dune-spice-wars/achievements-and-trophies/windows-10/ 2026-11-07 · capture: web_fetch · confidence: medium · enemy-tier: 1 · puzzle-tier: 1 · category: mainline · spoiler: progression · achievement: AllStatecraftDevs · achievement-hidden: no · trigger_type: collection_ [Confirmed: 3 sources, 2 languages]

### Ichwan Bedwine
- **id:** `AlliedAllSietches` · **hidden:** no · **trigger_type:** collection · **genre:** class, social · **missable:** no · **ponr-window:** n/a · **vector-binding:** `factions/fremen.md`
- **trigger:** as Fremen, ally every Sietch. **prereqs:** Fremen can ally Sietches outside their territory.
- **platform-list check:** this name was not among the 26 seen on the live Steam page (2026-11-07 recount); unverified against live platform list.
_source: https://dune-spice-wars.github.io/duneopedia/fremen , https://vandal.elespanol.com/logros/pc/dune-spice-wars/111674 , https://www.wemod.com/cheats/dune-spice-wars-trainers/achievements 2026-11-07 · capture: web_fetch · confidence: medium · enemy-tier: 1 · puzzle-tier: 1 · category: mainline · spoiler: progression · achievement: AlliedAllSietches · achievement-hidden: no · trigger_type: collection · genre: class, social · entity: fremen_ [Confirmed: 3 sources, 1 language]

### Landsraad's Favorite
> **Cross-system dependency** -- see `dependencies.md` DEP-007.
- **id:** `AllCharters` · **hidden:** no · **trigger_type:** collection · **genre:** class, social · **missable:** no · **ponr-window:** n/a · **vector-binding:** `factions/atreides.md`
- **trigger:** as Atreides, hold all Charters at the same time. **prereqs:** the Atreides 10,000 Hegemony perk skips Charter prerequisites except Standing.
- **platform-list check:** this name was not among the 26 seen on the live Steam page (2026-11-07 recount); unverified against live platform list.
_source: https://dune-spice-wars.github.io/duneopedia/atreides , https://vandal.elespanol.com/logros/pc/dune-spice-wars/111674 , https://www.wemod.com/cheats/dune-spice-wars-trainers/achievements 2026-11-07 · capture: web_fetch · confidence: medium · enemy-tier: 1 · puzzle-tier: 1 · category: mainline · spoiler: progression · achievement: AllCharters · achievement-hidden: no · trigger_type: collection · genre: class, social · entity: atreides_ [Confirmed: 3 sources, 1 language]

## Threshold

A count or amount reached, with no finite named set.

### Full House
- **id:** `FullHouse` · **hidden:** no · **trigger_type:** threshold · **missable:** no · **ponr-window:** n/a · **vector-binding:** `mechanics.md` (Villages, buildings)
- **trigger:** fill every slot in your Main Base.
_source: https://vandal.elespanol.com/logros/pc/dune-spice-wars/111674 , https://www.wemod.com/cheats/dune-spice-wars-trainers/achievements 2026-11-07 · capture: web_fetch · confidence: medium · enemy-tier: 1 · puzzle-tier: 1 · category: mainline · spoiler: progression · achievement: FullHouse · achievement-hidden: no · trigger_type: threshold_ [Confirmed: 2 sources, 1 language]

### Greatest House
- **id:** `GreatestHouse` · **hidden:** no · **trigger_type:** threshold · **genre:** social · **missable:** no · **ponr-window:** n/a · **vector-binding:** `mechanics.md` (Standing)
- **trigger:** reach 500 Landsraad Standing (not Fremen, who have no Standing). **prereqs:** the Embassy or Council Chamber helps.
_source: https://dune-spice-wars.github.io/duneopedia/arrakis , https://vandal.elespanol.com/logros/pc/dune-spice-wars/111674 , https://www.wemod.com/cheats/dune-spice-wars-trainers/achievements 2026-11-07 · capture: web_fetch · confidence: medium · enemy-tier: 1 · puzzle-tier: 1 · category: mainline · spoiler: progression · achievement: GreatestHouse · achievement-hidden: no · trigger_type: threshold · genre: social_ [Confirmed: 3 sources, 1 language]

### Landmarks
- **id:** `Landmarks` · **hidden:** no · **trigger_type:** threshold · **missable:** no · **ponr-window:** n/a · **vector-binding:** `mechanics.md` (Special Regions)
- **trigger:** control 4 special regions at once. **prereqs:** regions spawn at random; some maps have fewer.
_source: https://vandal.elespanol.com/logros/pc/dune-spice-wars/111674 , https://www.wemod.com/cheats/dune-spice-wars-trainers/achievements 2026-11-07 · capture: web_fetch · confidence: medium · enemy-tier: 1 · puzzle-tier: 1 · category: mainline · spoiler: progression · achievement: Landmarks · achievement-hidden: no · trigger_type: threshold_ [Confirmed: 2 sources, 1 language]

### Spice Addict
- **id:** `SpiceAddict` · **hidden:** no · **trigger_type:** threshold · **missable:** no · **ponr-window:** n/a · **vector-binding:** `mechanics.md` (Economy)
- **trigger:** hold 5,000 Spice at once. **prereqs:** a CHOAM Branch (raises the cap from 3,000 to 6,000).
_source: https://dune-spice-wars.github.io/duneopedia/arrakis , https://vandal.elespanol.com/logros/pc/dune-spice-wars/111674 , https://www.wemod.com/cheats/dune-spice-wars-trainers/achievements 2026-11-07 · capture: web_fetch · confidence: medium · enemy-tier: 1 · puzzle-tier: 1 · category: mainline · spoiler: progression · achievement: SpiceAddict · achievement-hidden: no · trigger_type: threshold_ [Confirmed: 3 sources, 1 language]

### Water Seller
- **id:** `WaterSeller` · **hidden:** no · **trigger_type:** threshold · **missable:** no · **ponr-window:** n/a · **vector-binding:** `mechanics.md` (Economy)
- **trigger:** have 100 net Water production. **prereqs:** big Water buildings (Polar Sink Extractor +25).
- **platform-list check:** this name was not among the 26 seen on the live Steam page (2026-11-07 recount); unverified against live platform list.
_source: https://dune-spice-wars.github.io/duneopedia/arrakis , https://vandal.elespanol.com/logros/pc/dune-spice-wars/111674 , https://www.wemod.com/cheats/dune-spice-wars-trainers/achievements 2026-11-07 · capture: web_fetch · confidence: medium · enemy-tier: 1 · puzzle-tier: 1 · category: mainline · spoiler: progression · achievement: WaterSeller · achievement-hidden: no · trigger_type: threshold_ [Confirmed: 3 sources, 2 languages]

### Ready to Rumble
- **id:** `ReadyToRumble` · **hidden:** no · **trigger_type:** threshold · **missable:** no · **ponr-window:** n/a · **vector-binding:** `items/gear.md`
- **trigger:** have 10 gear items equipped at once. **prereqs:** Barracks and the faction's second-gear-slot development (5 units x 2 slots).
- **platform-list check:** this name was not among the 26 seen on the live Steam page (2026-11-07 recount); unverified against live platform list.
_source: https://vandal.elespanol.com/logros/pc/dune-spice-wars/111674 , https://www.wemod.com/cheats/dune-spice-wars-trainers/achievements , https://steamcommunity.com/sharedfiles/filedetails/?id=3058990585 2026-11-07 · capture: web_fetch · confidence: medium · enemy-tier: 1 · puzzle-tier: 1 · category: mainline · spoiler: progression · achievement: ReadyToRumble · achievement-hidden: no · trigger_type: threshold_ [Confirmed: 3 sources, 1 language]

### Guild Lackey
- **id:** `GuildLackey` · **hidden:** no · **trigger_type:** threshold · **missable:** no · **ponr-window:** n/a · **vector-binding:** `mechanics.md` (Military)
- **trigger:** hold 500 Guild Favour. **prereqs:** a Spacing Guild Branch trading resources for Favour.
- **platform-list check:** this name was not among the 26 seen on the live Steam page (2026-11-07 recount); unverified against live platform list.
_source: https://vandal.elespanol.com/logros/pc/dune-spice-wars/111674 , https://www.wemod.com/cheats/dune-spice-wars-trainers/achievements 2026-11-07 · capture: web_fetch · confidence: medium · enemy-tier: 1 · puzzle-tier: 1 · category: mainline · spoiler: progression · achievement: GuildLackey · achievement-hidden: no · trigger_type: threshold_ [Confirmed: 2 sources, 1 language]

### Prom King
- **id:** `PromKing` · **hidden:** no · **trigger_type:** threshold · **genre:** social · **missable:** no · **ponr-window:** n/a · **vector-binding:** `mechanics.md` (Landsraad)
- **trigger:** be elected on a Resolution with at least 1,000 total votes (Battle/MP). **prereqs:** stack Influence, Standing tiers and Minor House votes.
- **platform-list check:** this name was not among the 26 seen on the live Steam page (2026-11-07 recount); unverified against live platform list.
_source: https://vandal.elespanol.com/logros/pc/dune-spice-wars/111674 , https://www.wemod.com/cheats/dune-spice-wars-trainers/achievements 2026-11-07 · capture: web_fetch · confidence: medium · enemy-tier: 1 · puzzle-tier: 1 · category: mainline · spoiler: progression · achievement: PromKing · achievement-hidden: no · trigger_type: threshold · genre: social_ [Confirmed: 2 sources, 1 language]

### Fully Furnished
- **id:** `FullyFurnished` · **hidden:** no · **trigger_type:** threshold · **genre:** class · **missable:** no · **ponr-window:** n/a · **vector-binding:** `factions/corrino.md`
- **trigger:** as Corrino, hold at least 12 Main Base buildings. **prereqs:** Corrino has extra building slots and Imperial Bases.
- **platform-list check:** this name was not among the 26 seen on the live Steam page (2026-11-07 recount); unverified against live platform list.
_source: https://dune-spice-wars.github.io/duneopedia/corrino , https://vandal.elespanol.com/logros/pc/dune-spice-wars/111674 , https://www.wemod.com/cheats/dune-spice-wars-trainers/achievements 2026-11-07 · capture: web_fetch · confidence: medium · enemy-tier: 1 · puzzle-tier: 1 · category: mainline · spoiler: progression · achievement: FullyFurnished · achievement-hidden: no · trigger_type: threshold · genre: class · entity: corrino_ [Confirmed: 2 sources, 1 language]

### Half a World
- **id:** `HalfAWorld` · **hidden:** no · **trigger_type:** threshold · **missable:** no · **ponr-window:** n/a · **vector-binding:** `mechanics.md` (Villages)
- **trigger:** control at least 30 regions. **prereqs:** a large map.
- **platform-list check:** this name was not among the 26 seen on the live Steam page (2026-11-07 recount); unverified against live platform list.
_source: https://vandal.elespanol.com/logros/pc/dune-spice-wars/111674 , https://www.wemod.com/cheats/dune-spice-wars-trainers/achievements , https://vgtimes.ru/games/dune-spice-wars/achievements-and-trophies/windows-10/ 2026-11-07 · capture: web_fetch · confidence: medium · enemy-tier: 1 · puzzle-tier: 1 · category: mainline · spoiler: progression · achievement: HalfAWorld · achievement-hidden: no · trigger_type: threshold_ [Confirmed: 3 sources, 2 languages]

### Sandlord
- **id:** `Sandlord` · **hidden:** no · **trigger_type:** threshold · **genre:** class · **missable:** no · **ponr-window:** n/a · **vector-binding:** `factions/fremen.md`
- **trigger:** as Fremen, control 2 Deep Deserts. **prereqs:** 5,000 Hegemony: surround a Deep Desert to control it.
- **platform-list check:** this name was not among the 26 seen on the live Steam page (2026-11-07 recount); unverified against live platform list.
_source: https://dune-spice-wars.github.io/duneopedia/fremen , https://vandal.elespanol.com/logros/pc/dune-spice-wars/111674 , https://www.wemod.com/cheats/dune-spice-wars-trainers/achievements 2026-11-07 · capture: web_fetch · confidence: medium · enemy-tier: 1 · puzzle-tier: 1 · category: mainline · spoiler: progression · achievement: Sandlord · achievement-hidden: no · trigger_type: threshold · genre: class · entity: fremen_ [Confirmed: 3 sources, 1 language]

### Underworld Empire
- **id:** `EveryStructureHasHeadquarters` · **hidden:** no · **trigger_type:** threshold · **genre:** class · **missable:** no · **ponr-window:** n/a · **vector-binding:** `factions/smugglers.md`
- **trigger:** as Smugglers, own an Underworld HQ in every enemy village and Main Base. **prereqs:** HQs need Authority; 10,000 Hegemony for Main Base HQs.
- **platform-list check:** this name was not among the 26 seen on the live Steam page (2026-11-07 recount); unverified against live platform list.
_source: https://dune-spice-wars.github.io/duneopedia/smugglers , https://vandal.elespanol.com/logros/pc/dune-spice-wars/111674 , https://www.wemod.com/cheats/dune-spice-wars-trainers/achievements 2026-11-07 · capture: web_fetch · confidence: medium · enemy-tier: 1 · puzzle-tier: 1 · category: mainline · spoiler: progression · achievement: EveryStructureHasHeadquarters · achievement-hidden: no · trigger_type: threshold · genre: class · entity: smugglers_ [Confirmed: 3 sources, 1 language]

### Heroic Champion
- **id:** `HeroicChampion` · **hidden:** no · **trigger_type:** threshold · **genre:** class · **missable:** no · **ponr-window:** n/a · **vector-binding:** `factions/ecaz.md`
- **trigger:** as Ecaz, have a Champion worth 5,000 Hegemony. **prereqs:** 5,000 Hegemony to name a Champion.
- **platform-list check:** this name was not among the 26 seen on the live Steam page (2026-11-07 recount); unverified against live platform list.
_source: https://vandal.elespanol.com/logros/pc/dune-spice-wars/111674 , https://www.wemod.com/cheats/dune-spice-wars-trainers/achievements 2026-11-07 · capture: web_fetch · confidence: medium · enemy-tier: 1 · puzzle-tier: 1 · category: mainline · spoiler: progression · achievement: HeroicChampion · achievement-hidden: no · trigger_type: threshold · genre: class · entity: ecaz_ [Confirmed: 2 sources, 1 language]

### Squeeze Hard
- **id:** `SingleVillageSpiceProd` · **hidden:** no · **trigger_type:** threshold · **genre:** class · **missable:** no · **ponr-window:** n/a · **vector-binding:** `factions/harkonnen.md`
- **trigger:** as Harkonnen, produce 250 Spice in one village. **prereqs:** Oppression doubles output for 2 days.
- **platform-list check:** this name was not among the 26 seen on the live Steam page (2026-11-07 recount); unverified against live platform list.
_source: https://dune-spice-wars.github.io/duneopedia/harkonnen , https://vandal.elespanol.com/logros/pc/dune-spice-wars/111674 , https://www.wemod.com/cheats/dune-spice-wars-trainers/achievements 2026-11-07 · capture: web_fetch · confidence: medium · enemy-tier: 1 · puzzle-tier: 1 · category: mainline · spoiler: progression · achievement: SingleVillageSpiceProd · achievement-hidden: no · trigger_type: threshold · genre: class · entity: harkonnen_ [Confirmed: 2 sources, 1 language]

### Recycling
- **id:** `Scrapers` · **hidden:** no · **trigger_type:** threshold · **genre:** class · **missable:** no · **ponr-window:** n/a · **vector-binding:** `factions/fremen.md`
- **trigger:** hold 500 Spaceship Parts. **prereqs:** the Fremen Recycling Plant trades resources for Machine Scraps and Spaceship Parts, so in practice this is a Fremen achievement.
- **platform-list check:** this name was not among the 26 seen on the live Steam page (2026-11-07 recount); unverified against live platform list.
_source: https://dune-spice-wars.github.io/duneopedia/fremen , https://vandal.elespanol.com/logros/pc/dune-spice-wars/111674 , https://www.wemod.com/cheats/dune-spice-wars-trainers/achievements 2026-11-07 · capture: web_fetch · confidence: medium · enemy-tier: 1 · puzzle-tier: 1 · category: mainline · spoiler: progression · achievement: Scrapers · achievement-hidden: no · trigger_type: threshold · genre: class · entity: fremen_ [Confirmed: 2 sources, 1 language]

### Awakening
- **id:** `Awakening` · **hidden:** no · **trigger_type:** threshold · **genre:** class · **missable:** no · **ponr-window:** n/a · **vector-binding:** `factions/vernius.md`
- **trigger:** with House Vernius, reach 100 Knowledge in a game. **prereqs:** the paid DLC; the Vernius Conquest trait Inducement Awards pays 10,000 Solari at 50 and at 100 Knowledge.
- **platform-list check:** this name was not among the 26 seen on the live Steam page (2026-11-07 recount); unverified against live platform list.
_source: https://www.wemod.com/cheats/dune-spice-wars-trainers/achievements , https://truesteamachievements.com/game/Dune-Spice-Wars/achievements 2026-11-07 · capture: web_fetch · confidence: medium · enemy-tier: 1 · puzzle-tier: 1 · category: mainline · spoiler: dlc:vernius · achievement: Awakening · achievement-hidden: no · trigger_type: threshold · genre: class · entity: vernius_ [Single source -- verify · class:editorial-en]

### Patent Troll
> **Cross-system dependency** -- see `dependencies.md` DEP-011.
- **id:** `PatentTroll` · **hidden:** no · **trigger_type:** threshold · **genre:** class · **missable:** no · **ponr-window:** n/a · **vector-binding:** `factions/vernius.md`
- **trigger:** with House Vernius, gain 5,000 Solari through patents in a single game (at least 10 sales at 500 Solari each). **prereqs:** the paid DLC and 5,000 Hegemony; the achievement could unlock for the wrong faction until the 2024-03-13 fix.
- **platform-list check:** this name was not among the 26 seen on the live Steam page (2026-11-07 recount); unverified against live platform list.
_source: https://www.wemod.com/cheats/dune-spice-wars-trainers/achievements , https://truesteamachievements.com/game/Dune-Spice-Wars/achievements , https://steamstore-a.akamaihd.net/news/externalpost/steam_community_announcements/5686429670868239976 2026-11-07 · capture: web_fetch · confidence: medium · enemy-tier: 1 · puzzle-tier: 1 · category: mainline · spoiler: dlc:vernius · achievement: PatentTroll · achievement-hidden: no · trigger_type: threshold · genre: class · entity: vernius_ [Single source -- verify · class:editorial-en]

### Total Infiltration
- **id:** `MaximumInfiltration` · **hidden:** no · **trigger_type:** threshold · **genre:** class · **missable:** no · **ponr-window:** n/a · **vector-binding:** `factions/smugglers.md`
- **trigger:** as Smugglers, hold 21 infiltration levels in total (7 fields x 3 levels).
- **platform-list check:** this name was not among the 26 seen on the live Steam page (2026-11-07 recount); unverified against live platform list.
_source: https://vandal.elespanol.com/logros/pc/dune-spice-wars/111674 , https://www.wemod.com/cheats/dune-spice-wars-trainers/achievements 2026-11-07 · capture: web_fetch · confidence: medium · enemy-tier: 1 · puzzle-tier: 1 · category: mainline · spoiler: progression · achievement: MaximumInfiltration · achievement-hidden: no · trigger_type: threshold · genre: class · entity: smugglers_ [Confirmed: 2 sources, 1 language]

### World Museum
- **id:** `WorldMuseum` · **hidden:** no · **trigger_type:** threshold · **genre:** class · **missable:** no · **ponr-window:** n/a · **vector-binding:** `factions/ecaz.md`
- **trigger:** as Ecaz, build 50 Masterpieces in a single game. **prereqs:** Masterpieces cost 100 Plascrete each.
- **platform-list check:** this name was not among the 26 seen on the live Steam page (2026-11-07 recount); unverified against live platform list.
_source: https://dune-spice-wars.github.io/duneopedia/ecaz , https://vandal.elespanol.com/logros/pc/dune-spice-wars/111674 , https://www.wemod.com/cheats/dune-spice-wars-trainers/achievements 2026-11-07 · capture: web_fetch · confidence: medium · enemy-tier: 1 · puzzle-tier: 1 · category: mainline · spoiler: progression · achievement: WorldMuseum · achievement-hidden: no · trigger_type: threshold · genre: class · entity: ecaz_ [Confirmed: 2 sources, 1 language]

## Discovery

The trigger is a non-obvious interaction or a hidden route.

### Ghola Hero
- **id:** `GholaHero` · **hidden:** no · **trigger_type:** discovery · **missable:** no · **ponr-window:** n/a · **vector-binding:** `items/abilities.md`
- **trigger:** recruit the Ghola of a dead hero. **prereqs:** the hero must die first; recruiting costs -30 Standing.
_source: https://dune-spice-wars.github.io/duneopedia/arrakis , https://steamcommunity.com/stats/1605220/achievements , https://www.wemod.com/cheats/dune-spice-wars-trainers/achievements 2026-11-07 · capture: web_fetch · confidence: medium · enemy-tier: 1 · puzzle-tier: 1 · category: mainline · spoiler: progression · achievement: GholaHero · achievement-hidden: no · trigger_type: discovery_ [Confirmed: 3 sources, 1 language]

### Pest Control
- **id:** `PestControl` · **hidden:** no · **trigger_type:** discovery · **missable:** no · **ponr-window:** n/a · **vector-binding:** `mechanics.md` (Military)
- **trigger:** destroy a Renegade Base. **prereqs:** Renegade Bases spawn on some maps; the Renegades Conquest mission and Defender of the Law spawn them.
_source: https://steamstore-a.akamaihd.net/news/externalpost/steam_community_announcements/1785774543521852 , https://vandal.elespanol.com/logros/pc/dune-spice-wars/111674 , https://www.wemod.com/cheats/dune-spice-wars-trainers/achievements 2026-11-07 · capture: web_fetch · confidence: medium · enemy-tier: 1 · puzzle-tier: 1 · category: mainline · spoiler: progression · achievement: PestControl · achievement-hidden: no · trigger_type: discovery_ [Confirmed: 3 sources, 1 language]

### Lawful Aggression
> **Cross-system dependency** -- see `dependencies.md` DEP-001.
- **id:** `EndTruce` · **hidden:** no · **trigger_type:** discovery · **genre:** social · **missable:** no · **ponr-window:** n/a · **vector-binding:** `mechanics.md` (Alliances)
- **trigger:** end a Truce legally by spending Influence. **prereqs:** a Truce must be active; this avoids the -100 Standing betrayal cost. The exact Influence price was not found.
- **platform-list check:** this name was not among the 26 seen on the live Steam page (2026-11-07 recount); unverified against live platform list.
_source: https://dune-spice-wars.github.io/duneopedia/arrakis , https://www.wemod.com/cheats/dune-spice-wars-trainers/achievements 2026-11-07 · capture: web_fetch · confidence: medium · enemy-tier: 1 · puzzle-tier: 1 · category: mainline · spoiler: progression · achievement: EndTruce · achievement-hidden: no · trigger_type: discovery · genre: social_ [Confirmed: 2 sources, 1 language]

### A taste of their own medicine
- **id:** `ATasteOfHisOwnMedicine` · **hidden:** no · **trigger_type:** discovery · **missable:** no · **ponr-window:** n/a · **vector-binding:** `mechanics.md` (Espionage)
- **trigger:** kill an enemy assassin. **prereqs:** an assassin must be in play (Assassination or a Resolution such as War of Assassins).
- **platform-list check:** this name was not among the 26 seen on the live Steam page (2026-11-07 recount); unverified against live platform list.
_source: https://dunespicewars.fandom.com/wiki/Resolutions , https://www.wemod.com/cheats/dune-spice-wars-trainers/achievements 2026-11-07 · capture: web_fetch · confidence: medium · enemy-tier: 1 · puzzle-tier: 1 · category: mainline · spoiler: progression · achievement: ATasteOfHisOwnMedicine · achievement-hidden: no · trigger_type: discovery_ [Confirmed: 2 sources, 1 language]

### The Fortress
> **Cross-system dependency** -- see `dependencies.md` SEQ-002.
- **id:** `ConquestEliminateHarkonnen` · **hidden:** no · **trigger_type:** discovery · **genre:** mission, class · **missable:** scenario-locked · **ponr-window:** needs the quick-win chain and Pressure under 100% · **vector-binding:** `sections/conquest.md`
- **trigger:** eliminate Harkonnen in Conquest (the Harkonnen capital siege).
- **platform-list check:** this name was not among the 26 seen on the live Steam page (2026-11-07 recount); unverified against live platform list.
_source: https://en.namu.wiki/w/Dune:%20Spice%20Wars/%EC%A0%95%EB%B3%B5%20%EB%AA%A8%EB%93%9C , https://vandal.elespanol.com/logros/pc/dune-spice-wars/111674 , https://www.wemod.com/cheats/dune-spice-wars-trainers/achievements 2026-11-07 · capture: web_fetch · confidence: medium · enemy-tier: 2 · puzzle-tier: 2 · category: mainline · spoiler: late-game · achievement: ConquestEliminateHarkonnen · achievement-hidden: no · trigger_type: discovery · genre: mission, class · entity: harkonnen_ [Confirmed: 3 sources, 2 languages]

### The Red Exhibition
> **Cross-system dependency** -- see `dependencies.md` SEQ-002.
- **id:** `ConquestEliminateEcaz` · **hidden:** no · **trigger_type:** discovery · **genre:** mission, class · **missable:** scenario-locked · **ponr-window:** needs the quick-win chain and Pressure under 100% · **vector-binding:** `sections/conquest.md`
- **trigger:** eliminate Ecaz in Conquest (the Ecaz capital siege).
- **platform-list check:** this name was not among the 26 seen on the live Steam page (2026-11-07 recount); unverified against live platform list.
_source: https://en.namu.wiki/w/Dune:%20Spice%20Wars/%EC%A0%95%EB%B3%B5%20%EB%AA%A8%EB%93%9C , https://vandal.elespanol.com/logros/pc/dune-spice-wars/111674 , https://www.wemod.com/cheats/dune-spice-wars-trainers/achievements 2026-11-07 · capture: web_fetch · confidence: medium · enemy-tier: 2 · puzzle-tier: 2 · category: mainline · spoiler: late-game · achievement: ConquestEliminateEcaz · achievement-hidden: no · trigger_type: discovery · genre: mission, class · entity: ecaz_ [Confirmed: 3 sources, 2 languages]

### Downfall
> **Cross-system dependency** -- see `dependencies.md` SEQ-002.
- **id:** `ConquestEliminateCorrino` · **hidden:** no · **trigger_type:** discovery · **genre:** mission, class · **missable:** scenario-locked · **ponr-window:** needs the quick-win chain and Pressure under 100% · **vector-binding:** `sections/conquest.md`
- **trigger:** eliminate Corrino in Conquest (the Corrino capital siege).
- **platform-list check:** this name was not among the 26 seen on the live Steam page (2026-11-07 recount); unverified against live platform list.
_source: https://en.namu.wiki/w/Dune:%20Spice%20Wars/%EC%A0%95%EB%B3%B5%20%EB%AA%A8%EB%93%9C , https://vandal.elespanol.com/logros/pc/dune-spice-wars/111674 , https://www.wemod.com/cheats/dune-spice-wars-trainers/achievements 2026-11-07 · capture: web_fetch · confidence: medium · enemy-tier: 2 · puzzle-tier: 2 · category: mainline · spoiler: late-game · achievement: ConquestEliminateCorrino · achievement-hidden: no · trigger_type: discovery · genre: mission, class · entity: corrino_ [Confirmed: 3 sources, 2 languages]

### Siege of Arrakeen
> **Cross-system dependency** -- see `dependencies.md` SEQ-002.
- **id:** `ConquestEliminateAtreides` · **hidden:** no · **trigger_type:** discovery · **genre:** mission, class · **missable:** scenario-locked · **ponr-window:** needs the quick-win chain and Pressure under 100% · **vector-binding:** `sections/conquest.md`
- **trigger:** eliminate Atreides in Conquest. **prereqs:** the shield operation is needed.
- **platform-list check:** this name was not among the 26 seen on the live Steam page (2026-11-07 recount); unverified against live platform list.
_source: https://en.namu.wiki/w/Dune:%20Spice%20Wars/%EC%A0%95%EB%B3%B5%20%EB%AA%A8%EB%93%9C , https://vandal.elespanol.com/logros/pc/dune-spice-wars/111674 , https://www.wemod.com/cheats/dune-spice-wars-trainers/achievements 2026-11-07 · capture: web_fetch · confidence: medium · enemy-tier: 2 · puzzle-tier: 2 · category: mainline · spoiler: late-game · achievement: ConquestEliminateAtreides · achievement-hidden: no · trigger_type: discovery · genre: mission, class · entity: atreides_ [Confirmed: 3 sources, 2 languages]

### Singularity
> **Cross-system dependency** -- see `dependencies.md` SEQ-002.
> **Cross-system dependency** -- see `dependencies.md` SEQ-003.
- **id:** `ConquestEliminateVernius` · **hidden:** no · **trigger_type:** discovery · **genre:** mission, class · **missable:** scenario-locked · **ponr-window:** Vernius must be one of the two random rivals, and the siege must succeed before Pressure reaches 100% · **vector-binding:** `sections/conquest.md`, `factions/vernius.md`
- **trigger:** eliminate House Vernius in Conquest (the Singularity siege of Scholar's Refuge). **prereqs:** none beyond the random appearance; the DLC is not needed to fight Vernius as a rival.
- **platform-list check:** this name was not among the 26 seen on the live Steam page (2026-11-07 recount); unverified against live platform list.
_source: https://www.wemod.com/cheats/dune-spice-wars-trainers/achievements , https://truesteamachievements.com/game/Dune-Spice-Wars/achievements , https://en.namu.wiki/w/Dune:%20Spice%20Wars/%EC%A0%95%EB%B3%B5%20%EB%AA%A8%EB%93%9C 2026-11-07 · capture: web_fetch · confidence: medium · enemy-tier: 2 · puzzle-tier: 2 · category: mainline · spoiler: dlc:vernius · achievement: ConquestEliminateVernius · achievement-hidden: no · trigger_type: discovery · genre: mission, class · entity: vernius_ [Single source -- verify · class:editorial-en]

### Get it over with
- **id:** `AssassinateLastOpponent` · **hidden:** no · **trigger_type:** discovery · **genre:** class · **missable:** no · **ponr-window:** n/a · **vector-binding:** `factions/harkonnen.md`
- **trigger:** as Harkonnen, sacrifice an agent to assassinate your last opponent. **prereqs:** Intel level 3 and the Assassination countdown.
- **platform-list check:** this name was not among the 26 seen on the live Steam page (2026-11-07 recount); unverified against live platform list.
_source: https://vandal.elespanol.com/logros/pc/dune-spice-wars/111674 , https://www.wemod.com/cheats/dune-spice-wars-trainers/achievements 2026-11-07 · capture: web_fetch · confidence: medium · enemy-tier: 2 · puzzle-tier: 2 · category: mainline · spoiler: late-game · achievement: AssassinateLastOpponent · achievement-hidden: no · trigger_type: discovery · genre: class · entity: harkonnen_ [Confirmed: 2 sources, 1 language]

### Empire Strikes Back
- **id:** `WinMainBaseDestroyed` · **hidden:** no · **trigger_type:** discovery · **genre:** class · **missable:** no · **ponr-window:** n/a · **vector-binding:** `factions/corrino.md`
- **trigger:** as Corrino, win after one of your Imperial Bases was destroyed. **prereqs:** needs 2 or more Imperial Bases (Spare Freighter).
- **platform-list check:** this name was not among the 26 seen on the live Steam page (2026-11-07 recount); unverified against live platform list.
_source: https://dune-spice-wars.github.io/duneopedia/corrino , https://vandal.elespanol.com/logros/pc/dune-spice-wars/111674 , https://en.namu.wiki/w/Dune:%20Spice%20Wars/%EC%A0%95%EB%B3%B5%20%EB%AA%A8%EB%93%9C 2026-11-07 · capture: web_fetch · confidence: medium · enemy-tier: 1 · puzzle-tier: 1 · category: mainline · spoiler: progression · achievement: WinMainBaseDestroyed · achievement-hidden: no · trigger_type: discovery · genre: class · entity: corrino_ [Confirmed: 3 sources, 1 language]

### You Shall Not Pass
- **id:** `YouShallNotPass` · **hidden:** no · **trigger_type:** discovery · **missable:** no · **ponr-window:** n/a · **vector-binding:** `mechanics.md` (Military)
- **trigger:** own a village with 8 Heavy Militia and 2 Missile Batteries. **prereqs:** Harkonnen: Rabban gives free Heavy Militia; Border Defense gives +1 Missile Battery limit per village.
- **platform-list check:** this name was not among the 26 seen on the live Steam page (2026-11-07 recount); unverified against live platform list.
_source: https://dune-spice-wars.github.io/duneopedia/harkonnen , https://vandal.elespanol.com/logros/pc/dune-spice-wars/111674 , https://www.wemod.com/cheats/dune-spice-wars-trainers/achievements 2026-11-07 · capture: web_fetch · confidence: medium · enemy-tier: 1 · puzzle-tier: 1 · category: mainline · spoiler: progression · achievement: YouShallNotPass · achievement-hidden: no · trigger_type: discovery_ [Confirmed: 3 sources, 1 language]

## Notes

"True Friendship" (reach 100 relation with another faction) appears in the 2022 GamePressure, GRYOnline and gameplay.tips lists and in Vandal's list, but it is not among the 102 Steam names and not on WeMod's 95. It is likely retired or renamed; no entry is made for it. WeMod lists 95 achievements against Steam's 102; the seven absent from WeMod are the Conquest ones. The Xbox/Windows 10 list is a different count (26).

_source: https://steamcommunity.com/stats/1605220/achievements , https://www.wemod.com/cheats/dune-spice-wars-trainers/achievements , https://vandal.elespanol.com/logros/pc/dune-spice-wars/111674 2026-11-07 · capture: web_fetch · confidence: medium · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_ [Confirmed: 3 sources, 3 languages]

## Sources

- https://steamcommunity.com/stats/1605220/achievements (canonical list; 102 achievements, 60 rare, fetched 2026-11-07)
- https://api.steampowered.com/ISteamUserStats/GetGlobalAchievementPercentagesForApp/v0002/?gameid=1605220&format=json (ids and global completion percentages, fetched 2026-11-07)
