# Dune: Spice Wars -- Factions

**status:** research-integrated
**last_reconciled:** 2026-11-07
**class:** factions

## Why this file exists

This file is the roster of the playable factions and where to read about each. The reader consults it for roster-shaped questions ("what factions are there", "which are free"). Per-faction detail lives in `factions/<entity-id>.md`.

## Roster

Six factions are playable in the base game; House Vernius of Ix is the one paid DLC Steam lists (released 2024-03-07); P3 wrote its file, `factions/vernius.md` (seven playable houses in all with the DLC). Free-versus-paid check: Steam lists exactly one DLC; the official 1.0 FAQ says six factions were available at release.

| entity-id | display name | entity-status | status | first-encounter zone | missable |
|---|---|---|---|---|---|
| atreides | House Atreides | unspecified | research-integrated | n/a (generated maps) | no |
| harkonnen | House Harkonnen | unspecified | research-integrated | n/a (generated maps) | no |
| smugglers | Smugglers | unspecified | research-integrated | n/a (generated maps) | no |
| fremen | Fremen | unspecified | research-integrated | n/a (generated maps) | no |
| corrino | House Corrino | unspecified | research-integrated | n/a (generated maps) | no |
| ecaz | House Ecaz | unspecified | research-integrated | n/a (generated maps) | no |
| vernius | House Vernius of Ix (paid DLC) | unspecified | research-integrated | n/a (generated maps) | no |

_source: https://store.steampowered.com/api/appdetails?appids=1605220 , https://store.steampowered.com/api/appdetails?appids=2807090 , https://steamstore-a.akamaihd.net/news/externalpost/steam_community_announcements/5141476355678693098 2026-11-07 · capture: web_fetch · confidence: medium · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_ [Single source -- verify · class:official-pr]

Each faction file carries the leader, bonuses and unit roster; councilors, heroes and operations are in `items/abilities.md`, developments and buildings in `items/upgrades.md`, builds in `items/builds.md`. The Landsraad and the neutral Sietches are systems, not factions: see `mechanics.md`. The Fremen faction is distinct from the neutral Sietch allies every faction can recruit.

## Pointer rules

- Claims about a faction route to their primary-vector destination; the faction file summarises and points back.
- No hidden entities in this class.
- Design note: the faction files and the per-category files in `items/` list the same factions along different axes (by faction here, by category there), and each faction's achievements are summarised here with the full list in `achievements.md`. This is an accepted overlap with one home per fact, not a duplicate.
