# Dune: Spice Wars -- Open conflicts between sources

**status:** research-integrated
**last_reconciled:** 2026-11-24
**patch note:** current patch v2.2.8.33026 (2026-11-06) wins. Every row keeps all values and their sources; none is settled by guessing. Where an official dated note is the latest rule change found, the "current-patch reading" column says so and the reader must still present the other value as disputed. Each row carries its own tier so it is hidden like the claim it disputes. The claim files that hold the same facts carry the "Contradicted" label.

## Open conflicts

| Topic | Values and sources | Current-patch reading | tier |
|---|---|---|---|
| Days the Governor must hold the title (Political victory) | 60 days in three 2022 early-access pages (GameRant, gamewave.fr, GamePressure); the official 2022-07-29 note says the time was "slightly increased to allow for 2 Landsraad voting phases" and gives no number; 30 days per the Fandom Charter page, a Steam beginner guide and a 2023 Reddit title; 45 days per Duneopedia (undated, after 2024-08) | not determined; no source states the value on v2.2.8.33026 (table in `sections/landsraad.md`) | late-game |
| Great House Conquest territory goal | official Community Update #4 (2024-11-18): "8 -> 10 controlled territory to validate the conquest objective, in great houses conquests"; NamuWiki (page modified 2026-08-07) still prints "8 or more"; the P2 research read the same official change as raising the Water Gift secondary objective from 8 to 10 territories; a 2025-07 player run ended on 9 territories with a Fremen-alliance goal | the dated official note says 10 and no later change was found, so 10 is the working value; NamuWiki's 8 may be stale; whether the note means the win goal, the Water Gift objective or both is not confirmed | late-game |
| Demolition armor destruction | official Heroes of Dune notes (2024-03-07): "Armor can no longer be shredded, but every faction has a unit that reduces armor value by a flat amount, as well as a unit made to kill high-armored opponents"; Duneopedia (undated, at least as new as 2024-08-22) still prints "Demolition: Area damage; 30% chance to destroy Armor" for several units and "50% Armor destroy chance" for the Altar's siege weapons | no patch note after 2024-03-07 mentions Demolition; whether the 30% is live is unverified, so do not state it as a current rule | progression |
| Smugglers' Main Base Hidden Explosives | Duneopedia: destroys 20 Armor from the Main Base; Community Update #4 (2024-11-18): no longer reduces armor, disables the Main Base's attack for a day | the official note is later; a later change is not ruled out | progression |
| Ecaz breaking a Truce | Duneopedia: cannot; Community Update #4 (2024-11-18): can, with +100% Standing loss and no damage bonus (Ecaz could not at 1.0); the "Reverend Mother" quest was removed for Ecaz in 2024-03 for clashing with the no-break rule | the official note is dated and no later change was found; Duneopedia is undated | progression |
| Standing gained per active Truce each council | 5 in the 2023-06-22 changelist; 4 on the Fandom Landsraad Standing page | Fandom is the later page but undated | progression |
| Border Defense militia armor and Energy Efficiency | Border Defense: +4 per Duneopedia, +2 per the 2024-03-07 changelist; Energy Efficiency (a shared Military development, also in the Vernius tree): +50% per Duneopedia, +30% per the changelist and per a French video (2024-03-30) | not determined; no patch note after 2024-03-07 names Border Defense or Energy Efficiency, so the later value is not found | none |
| Which factions have the Army Logistics second-slot development | Duneopedia lists it among the 36 shared nodes but only in the Atreides and Ecaz Military trees | whether it is shared or faction-only is unclear (`items/developments.md`) | progression |
| Game speed steps | 2023-24 guide against a 2022 blog (values in `controls.md`) | not closed | none |
| First hero pick cost (every faction) | Duneopedia prints that a hero costs 1,000 Solari to recruit; the 2024-03-07 Heroes of Dune changelist says heroes "become available for free at 10k hegemony" and a re-buy after death costs 1,000 Solari plus 30 Standing (Fremen: 150 Authority) | probably free for the first pick, not confirmed; no source newer than 2024-03-07 was found | progression |

_source: https://gamerant.com/dune-spice-wars-win-conditions-victory-how/ , https://www.gamepressure.com/dune-spice-wars/victory-conditions/z1fbde , https://steamstore-a.akamaihd.net/news/externalpost/steam_community_announcements/4587497456683917161 , https://dunespicewars.fandom.com/wiki/Charter , https://dune-spice-wars.github.io/duneopedia/gameplay.html , https://steamstore-a.akamaihd.net/news/externalpost/steam_community_announcements/1783238125343186 , https://en.namu.wiki/w/Dune:%20Spice%20Wars/%EC%A0%95%EB%B3%B5%20%EB%AA%A8%EB%93%9C , https://www.reddit.com/r/Dunespicewars/comments/1lsxdbc/am_i_ready_for_multiplayer_any_tips/ , https://steamstore-a.akamaihd.net/news/externalpost/steam_community_announcements/5679673637652411956 , https://dune-spice-wars.github.io/duneopedia/units.html , https://dune-spice-wars.github.io/duneopedia/developments.html , https://dunespicewars.fandom.com/wiki/Landsraad_Standing , https://docs.google.com/document/d/1LOwlJxOl1-0WhCfDtR5rmxcoiG30G8nzNREUZxs6Ch4 , https://www.youtube.com/watch?v=ZFNAL3cVmoM , https://dune-spice-wars.github.io/duneopedia/arrakis 2026-11-07 · capture: web_fetch · confidence: low · enemy-tier: 2 · puzzle-tier: 2 · category: mainline · spoiler: late-game_ [Contradicted across sources -- see notes]

## Resolved by P2

| Topic | What the sources showed | tier |
|---|---|---|
| Hawk (Spacing Guild air unit) HP and Power | official: 200 HP and 11 Power (2024-03-07), then 270 HP and 8 Power (2024-08-01), then 250 HP (2024-08-13); Duneopedia now prints 250 HP, 8 Power, upkeep 12, 9 Guild Favor. The sources agree on the latest values; the P1 conflict was a stale note against a newer one | progression |
| Spire (Fremen air unit) Power | official: 8 Power (2024-08-01), then 9 Power (v2.1.6.32344, 2024-08-22); Duneopedia prints 9 Power, 150 HP, armor 3, upkeep 9, +40% outside own territory. The Spire is a Fremen unit, not a Smugglers unit: the Air & Sand post (2022-11-17), the Heroes of Dune changelist and Community Update #3 list it under The Fremen, Duneopedia has it on the Fremen page built at the Fremen-only Recycling Plant, and the Smugglers' air units are the Banshee and the Wraith (P3 corrected the earlier "Smuggler" label) | progression |

_source: https://steamstore-a.akamaihd.net/news/externalpost/steam_community_announcements/5679673637652411956 , https://steamstore-a.akamaihd.net/news/externalpost/steam_community_announcements/5963413728335113504 , https://steamstore-a.akamaihd.net/news/externalpost/steam_community_announcements/5963414363408049434 , https://steamstore-a.akamaihd.net/news/externalpost/steam_community_announcements/5875595438688096662 , https://steamstore-a.akamaihd.net/news/externalpost/steam_community_announcements/4789043687474321138 , https://docs.google.com/document/d/1kgajYkMYh6QC1wzq8RQfmYiiNiTF7-svVo3t1nQmE0I , https://dune-spice-wars.github.io/duneopedia/units.html 2026-11-07 · capture: web_fetch · confidence: medium · enemy-tier: 1 · puzzle-tier: 1 · category: mainline · spoiler: progression_ [Confirmed: 2 sources, 1 language]

| Topic | What the sources showed | tier |
|---|---|---|
| Hegemony victory at 30,000 or 25,000 | the 2023-06-22 changelist states "Victory is at 30 000 Hegemony"; a late-2022 guide described a 25,000 limit, which predates it | late-game |

_source: https://docs.google.com/document/d/1LOwlJxOl1-0WhCfDtR5rmxcoiG30G8nzNREUZxs6Ch4 2026-11-07 · capture: web_fetch · confidence: medium · enemy-tier: 2 · puzzle-tier: 2 · category: mainline · spoiler: late-game_ [Single source -- verify · class:official-pr]

| Topic | What the sources showed | tier |
|---|---|---|
| Number of Conquest passive bonuses | 16 listed as generic plus 26 named separately = 42, matching P1's "about 42"; the P2 result's "about 31" is a miscount of its own 26-name list | progression |
| Smugglers' Conquest starting traits | the P2 result prints "(8)" but lists nine names (Another Man's Treasure, Early Birds, Gigantic Water Tanks, Grocer Network, One-Armed Bandit, Rotten From the Inside, Street-Smart, Vanguard Outposts, Well-Traveled); nine is recorded | progression |

_source: https://en.namu.wiki/w/Dune:%20Spice%20Wars/%EC%A0%95%EB%B3%B5%20%EB%AA%A8%EB%93%9C 2026-11-07 · capture: web_fetch · confidence: medium · enemy-tier: 1 · puzzle-tier: 1 · category: mainline · spoiler: progression_ [Single source -- verify · class:community-wiki]

## Open conflicts added by P3 (House Vernius of Ix)

| Topic | Values and sources | Current-patch reading | tier |
|---|---|---|---|
| Neural Node Standing cost (the amount) | Duneopedia (undated) prints "Cost: 50 Plascrete", no upkeep, and says nothing about Standing; Daevohk's video (2024-06-18) says each node costs "three Landsraad standing in addition to the plascrete"; DuneBro (2024-03-12) says "a little standing", a French video (Noteau, 2024-05-11) says nodes "cost reputation", and a 2024-04-21 Steam forum post says relays cost standing | no patch note changes either reading. That a Standing cost exists has four independent mentions; the number 3 has one (Daevohk). Present both and say current value unverified | dlc:vernius |
| Sequential Thinking Knowledge per node on the longest path | +1 Knowledge (release post, 2024-03-07) against +0.5 (Duneopedia, undated); both give +2% Authority | not determined; no patch note found for a change | dlc:vernius |
| First hero pick cost | the changelist says heroes "become available for free at 10k hegemony" and a re-buy costs 1,000 Solari plus 30 Standing; Duneopedia prints 1,000 Solari to recruit | probably free for the first pick, not confirmed | dlc:vernius |
| Bolig Avati wording | release post: "+1 Knowledge per district bonus"; Duneopedia: "+1 Knowledge when a new District is established" | no patch note; the reword is unexplained | dlc:vernius |
| Tessia Vernius Knowledge to Intel | official release text: 50% of idle Knowledge becomes Intel (plus Solari since 2024-03-20); DuneBro (2024-03-12) says 100% | the official value is later and dated; the video predates the 2024-03-20 patch | dlc:vernius |
| Tether bonus per Knowledge | Daevohk: +0.5% attack speed per Knowledge (60 Knowledge = +30%); DuneBro: tethered drones "get additional damage per each knowledge"; the official text and Duneopedia list no such bonus | not determined | dlc:vernius |
| Nuwa and Fight-Engineer repair stacking | Duneopedia: Nuwa's repair "stacks with Fight-Engineer's"; a Reddit reply: healing does not stack, "kill the engineer, the droids are 30% less effective"; the 2024-11-18 note only says repair mode persists | not determined | dlc:vernius |
| Automated Defenses release attrition (removed 2024-08-01) | -4% health per day per node (release post) against -3% when it was removed (Community Update #3) | moot, the effect was removed | dlc:vernius |
| Patent price at launch | 1,000 Solari (official release post) against 1,500 (one Reddit player) | moot, the current price is 600 | dlc:vernius |
| Analytical Machine price | 900 Solari plus 30 Standing for the first and 1,000 plus 33 for the second (Daevohk, 2024-06-18) against the official 100-Solari cut of 2024-03-20, which the video date follows | unclear whether the quote includes the cut | dlc:vernius |

_source: https://dune-spice-wars.github.io/duneopedia/vernius.html , https://www.youtube.com/watch?v=fcAqG6QYj4U , https://www.youtube.com/watch?v=1L-QhvIR0zk , https://www.youtube.com/watch?v=3S7XR-VRX58 , https://www.youtube.com/watch?v=ZFNAL3cVmoM , https://steamcommunity.com/app/1605220/discussions/0/4363500868530352166 , https://docs.google.com/document/d/1kgajYkMYh6QC1wzq8RQfmYiiNiTF7-svVo3t1nQmE0I , https://steamstore-a.akamaihd.net/news/externalpost/steam_community_announcements/5679673637652411370 , https://steamstore-a.akamaihd.net/news/externalpost/steam_community_announcements/5963413728335113504 , https://steamstore-a.akamaihd.net/news/externalpost/steam_community_announcements/5686430301714804124 , https://www.reddit.com/r/Dunespicewars/comments/1iygf2x/house_vernius_is_the_best_faction_so_far/ , https://www.reddit.com/r/Dunespicewars/comments/1mbvqhz/my_thoughts_on_vernius/ 2026-11-07 · capture: web_fetch · confidence: low · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: dlc:vernius_ [Contradicted across sources -- see notes]

## Resolved or corrected by P3

| Topic | What the sources showed | tier |
|---|---|---|
| Duneopedia's Vernius "Faction Bonuses" block | it says Vernius machine units use "Machine Scraps", need an "Ixian Foundry" and unlock a "Mobile Foundry" at 10,000 Hegemony. The official Air & Sand post (2022-11-17) says Machine Scrap is for Fremen only, and the official release post lists different starting bonuses (Tethered harvesters, shared developments, split S-Vault districts, patents at 5,000 and obfuscation at 10,000 Hegemony). The block is dropped; the rest of the Duneopedia Vernius page agrees with the official notes. It was never copied into this guide | dlc:vernius |
| The Spire is a Fremen unit | the Smugglers' air units are the Banshee and the Wraith; the Spire is listed under The Fremen in the Air & Sand post, the changelist and Community Update #3, and on Duneopedia's Fremen page | progression |

_source: https://dune-spice-wars.github.io/duneopedia/vernius.html , https://steamstore-a.akamaihd.net/news/externalpost/steam_community_announcements/5679673637652411370 , https://steamstore-a.akamaihd.net/news/externalpost/steam_community_announcements/4789043687474321138 2026-11-07 · capture: web_fetch · confidence: medium · enemy-tier: 1 · puzzle-tier: 1 · category: mainline · spoiler: dlc:vernius_ [Confirmed: 2 sources, 1 language]

| Topic | What the sources showed | tier |
|---|---|---|
| Patches that touch Vernius | P2 reported no post after v2.2.5 changing Vernius. The 2025-07-09 post (v2.2.7.32974) changes it: the Harmless Gadget treaty no longer breaks when entering conflict with Vernius. v2.2.8.33019 and v2.2.8.33026 do not touch Vernius. The unpublished v2.2.6.32935 is still unknown | dlc:vernius |
| Great-House Conquest territory goal | resolved as the working value 10 from the dated official note of 2024-11-18; the Namu page's 8 is kept as the disputed older value in the open table above | late-game |

_source: https://steamstore-a.akamaihd.net/news/externalpost/steam_community_announcements/1803527891922277 , https://steamstore-a.akamaihd.net/news/externalpost/steam_community_announcements/1783238125343186 , https://en.namu.wiki/w/Dune:%20Spice%20Wars/%EC%A0%95%EB%B3%B5%20%EB%AA%A8%EB%93%9C 2026-11-07 · capture: web_fetch · confidence: medium · enemy-tier: 2 · puzzle-tier: 2 · category: mainline · spoiler: late-game_ [Single source -- verify · class:official-pr]

| Topic | What the sources showed | tier |
|---|---|---|
| Harmless Gadget "-10" Standing | P2 listed "-10" as an unparsed Vernius line. A 2025-04-16 Reddit thread says the faction that accepts the gadget loses 10 Landsraad Standing. Harmless Gadget is a treaty unlocked by Heretical Computing, not a Resolution. Single forum source | dlc:vernius |

_source: https://www.reddit.com/r/Dunespicewars/comments/1k0j6ot/you_always_benefit_more_than_vernius_from/ 2026-11-07 · capture: web_fetch · confidence: medium · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: dlc:vernius_ [Single source -- verify · class:forum]
