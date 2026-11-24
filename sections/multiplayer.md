# Dune: Spice Wars -- Multiplayer and co-op

**status:** research-integrated
**last_reconciled:** 2026-11-24
**patch note:** current patch v2.2.8.33026 wins. Multiplayer-specific changes come from the official notes through v2.2.8.33019.

## Modes and lobby

Official support: free-for-all up to 4 players, 1v1 (Kanly) and 2v2, on dedicated servers plus peer-to-peer (P2P). AI can fill slots. Map size, sandworm, storm and Sietch activity and victory conditions are configurable. Steam lists the categories PvP, Online PvP, Co-op and Online Co-op. Lobbies allow up to 8 spectators (Community Update #3, 2024-08-01). P2P hosts can spectate, and spectating defaults on for public non-P2P games since v2.2.8.33019. The lobby shows an icon for players who left more than three games early within 12 hours (v2.2.8.33019).

_source: https://steamstore-a.akamaihd.net/news/externalpost/steam_community_announcements/1847286114027994 , https://steamstore-a.akamaihd.net/news/externalpost/steam_community_announcements/5963413728335113504 , https://steamstore-a.akamaihd.net/news/externalpost/steam_community_announcements/6214419350719070750 2026-11-07 · capture: web_fetch · confidence: medium · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_ [Single source -- verify · class:official-pr]

In multiplayer "Slow" has been the default Landsraad timer since v2.2.3 (2024-12-04): preliminary phases of up to 1 min 30 s each and a vote of up to 5 min. "Fast" gives 30 s and 45 s. [patch: 2024-12-04; unchanged in the later notes read]

_source: https://steamstore-a.akamaihd.net/news/externalpost/steam_community_announcements/1784506359205976 2026-11-07 · capture: web_fetch · confidence: medium · enemy-tier: 1 · puzzle-tier: 1 · category: mainline · spoiler: progression_ [Single source -- verify · class:official-pr]

## Lobby flow

Match modes are Battle of Arrakis (free-for-all or 2v2 on dedicated maps) and Kanly Duel (1v1). The Random map type was added in v2.2.2. Disconnected players can stay paused and rejoin from the multiplayer screen (2024-08-13). A dead P2P host's AIs keep voting (fixed in v2.2.8.33019).

_source: https://steamstore-a.akamaihd.net/news/externalpost/steam_community_announcements/1783872412139437 , https://steamstore-a.akamaihd.net/news/externalpost/steam_community_announcements/5963414363408049434 , https://steamstore-a.akamaihd.net/news/externalpost/steam_community_announcements/1847286114027994 , https://truesteamachievements.com/game/Dune-Spice-Wars/achievements 2026-11-07 · capture: web_fetch · confidence: medium · enemy-tier: 1 · puzzle-tier: 1 · category: mainline · spoiler: progression_ [Single source -- verify · class:official-pr]

The host can switch the four victory types on or off: Political, Economic, Hegemony and Domination; the achievement Insanity needs all four on.

_source: https://steamstore-a.akamaihd.net/news/externalpost/steam_community_announcements/1783872412139437 , https://steamstore-a.akamaihd.net/news/externalpost/steam_community_announcements/5963414363408049434 , https://steamstore-a.akamaihd.net/news/externalpost/steam_community_announcements/1847286114027994 , https://truesteamachievements.com/game/Dune-Spice-Wars/achievements 2026-11-07 · capture: web_fetch · confidence: medium · enemy-tier: 2 · puzzle-tier: 2 · category: mainline · spoiler: late-game_ [Single source -- verify · class:official-pr]

A 2025-11 co-op skirmish report: a non-host's client displayed Economic instead of Political, so the Governorship Charter showed as Council Representative (one player's report).

_source: https://www.reddit.com/r/Dunespicewars/comments/1orxpub/dune_governorship_charter_missing_with_political/ 2026-11-07 · capture: web_fetch · confidence: low · enemy-tier: 2 · puzzle-tier: 2 · category: mainline · spoiler: late-game_ [Single source -- verify · class:forum]

Teams and co-op: online co-op skirmish against the AI exists, and 2v2 and team play; Alt+click pings (2023-06-22). How allied victory is decided is not documented in anything read. [location inventory incomplete]

_source: https://docs.google.com/document/d/1LOwlJxOl1-0WhCfDtR5rmxcoiG30G8nzNREUZxs6Ch4 , https://www.reddit.com/r/Dunespicewars/comments/1orxpub/dune_governorship_charter_missing_with_political/ 2026-11-07 · capture: web_fetch · confidence: medium · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_ [Single source -- verify · class:official-pr]

Vernius in multiplayer: the DLC owner can pick House Vernius in free-for-all, team and online co-op lobbies, and an AI Vernius may appear in any lobby; whether a player without the DLC can join, host or team with a lobby where another player chose Vernius is not stated by any source read. The 2024-04-02 notes list "Vernius gives unlocked developments to teammates in 2v2" among the fixes (the result does not say whether the fix added or removed that sharing, so the current 2v2 behaviour is unverified), and obfuscating a development affects every faction in the lobby, Vernius included. Details: `factions/vernius.md`.

_source: https://steamstore-a.akamaihd.net/news/externalpost/steam_community_announcements/5679673637652411370 , https://steamstore-a.akamaihd.net/news/externalpost/steam_community_announcements/5749481331455200622 , https://store.steampowered.com/api/appdetails?appids=2807090&cc=us&l=english 2026-11-07 · capture: web_fetch · confidence: medium · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: dlc:vernius · entity: vernius_ [Single source -- verify · class:official-pr]

> see factions/vernius.md for full summary

## Co-op

Steam lists "Co-op" and "Online Co-op", which the game realises as 2v2 teams against other humans or AI. True co-op Conquest exists only as the unofficial CoopQuest mod (2026-11-02 listing).

_source: https://store.steampowered.com/api/appdetails?appids=1605220 , https://www.nexusmods.com/games/dunespicewars/mods 2026-11-07 · capture: web_fetch · confidence: medium · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_ [Confirmed: 2 sources, 1 language]

## Mods

The "Community Multiplayer Rebalance" and Community Patch mods only work in P2P games with the host running them ("ACTIVE MOD = NO REGULAR PUBLIC GAMES"). The in-game /enableCheats command (v2.2.8.33019) disables achievements for that save.

_source: https://www.nexusmods.com/games/dunespicewars/mods , https://steamstore-a.akamaihd.net/news/externalpost/steam_community_announcements/1847286114027994 2026-11-07 · capture: web_fetch · confidence: medium · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_ [Single source -- verify · class:datamining]

## Voting, AI and play advice

Voting phase rules (v2.2.4) are in `mechanics.md`. v2.2.8.33019 fixed AIs not voting after a P2P host dies. Player advice: a passive mid-to-late game lets a winner run away, and reaching 20,000 Hegemony early means being teamed against. [patch: 2024-01 to 2024-03 for the advice]

_source: https://steamstore-a.akamaihd.net/news/externalpost/steam_community_announcements/1847286114027994 , https://www.reddit.com/r/Dunespicewars/comments/197fpur/what_is_your_favourite_build_orders/ , https://steamcommunity.com/sharedfiles/filedetails/?id=3058990585 2026-11-07 · capture: web_fetch · confidence: medium · enemy-tier: 1 · puzzle-tier: 1 · category: mainline · spoiler: progression_ [Confirmed: 3 sources, 1 language]

## Multiplayer-only achievements

Playing with Others (finish a multiplayer game without forfeiting), Thrill of Victory (win a standard multiplayer game with at least one other player), Peaceful Dune and One Against All (need a full 4-player lobby). See `achievements.md`.

_source: https://vandal.elespanol.com/logros/pc/dune-spice-wars/111674 , https://www.wemod.com/cheats/dune-spice-wars-trainers/achievements 2026-11-07 · capture: web_fetch · confidence: medium · enemy-tier: 1 · puzzle-tier: 1 · category: mainline · spoiler: progression_ [Confirmed: 2 sources, 1 language]
