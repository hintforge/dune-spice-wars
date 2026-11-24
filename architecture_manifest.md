# Dune: Spice Wars -- Architecture manifest

**status:** research-integrated <!-- scaffold | research-integrated | live-observed | reconciled -->
**last_reconciled:** 2026-11-07
**research_run:** P1, P2 and P3 (each a single deep-research run, ingested 2026-11-07)

This game has no `nav/` folder (generated maps, no zone graph), so the manifest lives here at the corpus root. The reader's session-start discovery reads this file.

## Hintforge manifest

<!-- Read by the reader at session start (see docs/corpus-format.md §3). Bump corpus-core-version only when a change to docs/corpus-format.md would break an older reader; see the Versioning subsection in that doc. game-version-* fields describe the game build the corpus was authored against (player-supplied at setup; required as of v3); they are orthogonal to corpus-core-version (which is the schema axis). -->

```
corpus-core-version: 6
game-version: "current Steam build 26405381"
game-version-platform: "PC / Steam"
game-version-as-of: 2026-11-07
vector-extensions: factions
```

## Vector extensions

<!-- Wizard populates from Step 7 conditional-creation decisions. One entry per extension created. Reader uses this list to route topical questions to the right folder. Semantics are one line each; folders may be absent if the game does not need them. -->

- `factions/` -- group entities the player has a relationship with (here: the playable houses and factions, plus minor factions as research finds them), indexed by `factions/index.md`

## Notes

- **Game-type label:** procedural (confirmed by P1: three sources in three languages; skirmish and multiplayer maps are generated per game, and Conquest builds a map of a fixed set of named regions with randomised layout and resources).
- **Localization-mechanism class:** none (confirmed by P1; single community-wiki source for the "no fixed site" half).
- **Zone graph:** not applicable for generated maps. The 26 named Conquest regions are listed in `sections/conquest.md`; their adjacency is unpublished [location inventory incomplete].
- **Source-language set:** the developer language French plus Russian, Simplified Chinese and German; Steam lists nine supported languages (English, French, German, Spanish - Spain, Polish, Portuguese - Brazil, Russian, Simplified Chinese, Italian).
- **Patch the corpus targets:** the current patch wins. Stage 0 found v2.2.8.33026 (2026-11-06) as the latest update; the manifest's `game-version` above is the Steam build the player reported.
