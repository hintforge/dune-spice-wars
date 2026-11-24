# Dependencies -- Dune: Spice Wars
<!-- hintforge · stitch pass · last run: 2026-11-24 (re-run after doctor) -->
<!-- Every stitch run re-audits ALL existing edges + adds new ones. The per-edge convergence audit (open each cited source, verify the specific value) applies to every row in this file on every run, not just new candidates. A game patch, DLC, or new ingestion phase can change facts that existing edges cite -- only a full re-audit catches that. See `stitch_and_zipper.md` Phase B "Re-run scope: always full." Inconsistencies (cited source contradicts edge text) land in the `## Corpus inconsistencies` section; the edge row stays in place. -->

## Cross-system edges

| Edge ID | System A | System B | Dependency description | Confidence | tier | Source files |
|---------|----------|----------|------------------------|------------|------|--------------|
| DEP-001 | Truces | Landsraad Standing | Betraying a Truce costs -100 Standing (Ecaz break one with +100% Standing loss under the 2024-11-18 official note); ending a Truce by spending Influence (the Lawful Aggression achievement) avoids that cost; Successful Betrayal needs the betrayed faction eliminated within 20 days of the betrayal | high | progression | mechanics.md, sections/landsraad.md, sections/solo_skirmish.md, sections/progression.md, achievements.md, factions/ecaz.md |
| DEP-002 | Vernius Neural Nodes | Landsraad Standing tiers | A Neural Node costs Landsraad Standing as well as 50 Plascrete (four publishers say so; the amount 3 rests on one video), so a wide node network pulls Standing toward the Low tier (under 200: -2 Influence production; under 100: no vote, -3 Influence production and a Landsraad Guard raid every 20 days) | medium | dlc:vernius | factions/vernius.md, sections/progression.md, mechanics.md |
| DEP-003 | Vernius obfuscation | Landsraad Standing | Obfuscation (unlocked at 10,000 Hegemony) costs 20 Standing, so it cannot be done below 20 Standing | medium | dlc:vernius | factions/vernius.md, sections/progression.md, mechanics.md |
| DEP-004 | Vernius Harmless Gadget treaty | Landsraad Standing and Vernius Information | Heretical Computing unlocks the treaty (100 Solari); the faction that accepts it loses 10 Standing (one forum thread) and gets an Analytical Machine, and with Holistic Thinking Vernius gains +1 Information level in factions that accepted it; since 2025-07-09 the treaty no longer breaks when entering Conflict with Vernius | medium | dlc:vernius | factions/vernius.md, sections/landsraad.md, sections/progression.md |
| DEP-005 | Heroes | Landsraad Standing | Bringing a dead hero back (a Ghola re-buy) costs -30 Standing as well as Solari (1,000; Fremen 150 Authority); heroes unlock at 10,000 Hegemony; whether the first pick is free or costs 1,000 Solari is an open conflict (`sections/conflicts.md`) | medium | progression | mechanics.md, sections/landsraad.md, sections/progression.md, factions/vernius.md |
| DEP-006 | Spice Tax | Landsraad Standing and Hegemony | Spice Tax is due every 25 days; missing it costs -20 Standing and each payment gives +1,000 Hegemony | medium | progression | mechanics.md, sections/landsraad.md, sections/progression.md |
| DEP-007 | Atreides 10,000 Hegemony perk | Landsraad Charters | At 10,000 Hegemony the Atreides ignore Charter prerequisites except Standing, so holding every Charter (Landsraad's Favorite) needs only the Standing level (250 for the common Charters, 450 for the Governorship) | medium | late-game | factions/atreides.md, mechanics.md, achievements.md, sections/landsraad.md |
| DEP-008 | Smugglers | Landsraad | The Smugglers join the Landsraad only at 5,000 Hegemony (with 50 votes and 200 Standing); the Fremen never join | medium | progression | factions/smugglers.md, sections/landsraad.md, sections/solo_skirmish.md |
| DEP-009 | Sietch pillaging | Sietch alliances and the Fremen Governorship | Pillaging a Sietch loses its alliance and leaves it devastated; devastated Sietches cannot be built on by the Fremen except at large cost, and the Fremen Governorship needs every non-devastated Sietch allied and at least 3/4 of Sietches non-devastated | high | late-game | mechanics.md, sections/landsraad.md, sections/missables.md |
| DEP-010 | Conquest Ancient Sietch choice | Fremen friendship (Alliance goal, Friendly Native) | Protecting the Ancient Sietch gives +30 Fremen friendship (+20 if the protection fails); plundering it gives -30 friendship and +5 development assets; the choice cannot be undone; 100% friendship is a win-condition goal and the achievement Friendly Native | medium | late-game | sections/conquest.md, sections/missables.md, achievements.md, factions/fremen.md |
| DEP-011 | Vernius patents | Patent Troll achievement | Patents unlock at 5,000 Hegemony, cost 600 Solari to file and rivals pay 500 each; Patent Troll needs 5,000 Solari from patents in one game (at least 10 sales) | medium | dlc:vernius | factions/vernius.md, sections/progression.md, achievements.md |
| DEP-012 | Armory gear slots | Military developments | Slot 1 comes from Survival Training (Military tier 1); slot 2 needs one specific Military development per faction (Army Logistics for Atreides and Ecaz, Adrenaline Addiction for Harkonnen, Industrial Scavenging for the Smugglers, Imperial Command for Corrino, Stalwart Alliance for the Fremen); gear is free to install and 500 Solari to swap | medium | progression | items/gear.md, items/developments.md, items/upgrades.md, factions/atreides.md, sections/progression.md |
| DEP-013 | Vernius Armory gear slot | Vernius Military development | Vernius's second Armory slot comes from the Water Batteries development (Military), which also lets Water stand in for missing Fuel Cells; gear is free to install and 500 Solari to swap | medium | dlc:vernius | factions/vernius.md, items/gear.md |

### Optional cluster links

Each independently testable relationship gets its own DEP row and audit. A genuinely indivisible relationship stays one row. When several rows describe facets of one cluster, the Cross-system edges table may add `Related DEP(s)` after Source files; list only DEP IDs that exist in this file. The default six-column table remains valid, and existing guides require no migration. A shared name alone does not justify a relationship.

## PoNR / lockout edges

| Edge ID | Trigger | Locked out | Notes | tier | Source files |
|---------|---------|------------|-------|------|--------------|
| PON-001 | Using Nuclear Warheads (needs a Nuclear Silo: 2,000 Solari, 1,000 Plascrete, 10 Fuel Cells) | The Dune Governorship (Political victory) in that game | -500 Standing; the Governorship needs 450 Standing and 1 Charter (an Atreides at 10,000 Hegemony needs only the Standing, DEP-007) | late-game | mechanics.md, sections/landsraad.md, sections/missables.md, achievements.md |
| PON-002 | Conquest Pressure reaching 100% after the post-mission bonus pick | The run, even when the victory goals are met | Pressure rises +3% per owned territory each time a zone is occupied; the latest safe point is under 50%; cuts: Agony defence 15%, capital-siege secondary objective 20%, first Ancient Sietch goal 5% | late-game | sections/conquest.md, sections/missables.md, achievements.md |
| PON-003 | A Loss of Rights resolution passing at the council after the Dune Governorship was won | Every active Charter except one awarded in the same council | the first Governorship election guarantees the vote at the next council, but it can be defeated: out-vote it, hold the Speaker of the Council Charter to re-roll it, or remove rivals who can no longer vote (a 2023-09 thread; current status unverified) | late-game | mechanics.md, sections/landsraad.md, sections/missables.md |

## Missable / sequencing dependencies

| Edge ID | Action | Window | Consequence | tier | Source files |
|---------|--------|--------|-------------|------|--------------|
| SEQ-001 | Win a Conquest | under 4 years (whether in-game is not confirmed) and before Pressure reaches 100% | the Kwisatz Haderach achievement is forfeited by a slow run | late-game | achievements.md, sections/missables.md, sections/conquest.md |
| SEQ-002 | Conquest capital sieges (the Eliminate achievements) | after quick successive wins (an adjacent capital; 2 or more of the named mission types; the defender failing twice) and with Pressure under 100% | otherwise the sieges stay closed (the activation rule is a community guess) | late-game | sections/conquest.md, sections/missables.md, achievements.md |
| SEQ-003 | Singularity siege of Vernius in Conquest | Vernius must appear as one of the two random rivals | no DLC is needed to fight Vernius; success removes Vernius permanently; the S-Bolt secondary objective (destroy it before the defender's Knowledge reaches 100) is optional and gives +5 development assets and -20% Pressure | dlc:vernius | sections/conquest.md, factions/vernius.md, achievements.md |

## Stitch run log

| Date | Scope | Edges written | Edges proposed (pending) | Inconsistencies surfaced | Model |
|------|-------|---------------|--------------------------|--------------------------|-------|
| 2026-11-24 | full | 18 | 0 | 4 (3 resolved in 5b; 1 open) | sonnet-class |
| 2026-11-24 (re-run after doctor) | full (19 edges re-audited) | 0 | 0 | 2 (1 resolved in 5b; 1 open) | sonnet-class |

<!-- Inconsistencies surfaced: count from the per-edge convergence audit (stitch_and_zipper.md Phase B). Counts must be derived by reading this file, not recalled. A non-zero count requires an explicit chat call-out and, in the Corpus inconsistencies section below, either at least one populated row (inconsistencies still open) or, when every one was resolved in stitch step 5b and its row removed, the cell written as `N (resolved in 5b)`. -->

## Corpus inconsistencies

Stitch's per-edge convergence audit (see [`stitch_and_zipper.md`](https://github.com/hintforge/builder/blob/main/stitch_and_zipper.md) Phase B) populates this section when a candidate edge's cited sources contradict each other. Each row records the contradiction; resolving it is the user's call (or a follow-up doctor / ingestion run). Edges blocked on an unresolved entry are NOT written to the tables above until the inconsistency is closed.

| Detected | Files | Conflicting values | Suspected authoritative source | Status | tier |
|----------|-------|--------------------|--------------------------------|--------|------|
| 2026-11-24 | mechanics.md, sections/progression.md, factions/vernius.md, sections/conflicts.md | mechanics.md says heroes cost 1,000 Solari to recruit; sections/progression.md and factions/vernius.md say the first hero pick is free (changelist: "available for free at 10k hegemony") and only a re-buy costs 1,000 Solari plus 30 Standing. The same disagreement is now registered as a general row in sections/conflicts.md (and still as a Vernius row) | blank for the user to resolve: no source newer than the 2024-03-07 changelist was found | open | progression |

<!-- Status vocabulary: open (just surfaced) | resolved (user picked authoritative value + corrected the other file) | accepted (user accepted both -- rare; usually means the claim is genuinely ambiguous in-game). When status flips to resolved, the next stitch run can re-evaluate the edge. -->
