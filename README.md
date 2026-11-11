# R56: Sun Li-jen Path (v0.1.3)

An alt-history branch for Nationalist China in Road to 56. If Chiang takes the secret-police route, the player can back Colonel Sun Li-jen's reformist officers instead. The branch ends in either a peaceful handover or the Nanking Coup and a civil war.

## Install
1. Copy this folder to `Documents\Paradox Interactive\Hearts of Iron IV\mod\R56_sun_lijen\`.
2. Copy `R56_sun_lijen.mod` into `...\mod\` and fix the `path=` line to match your username.
3. In both .mod files, make `dependencies` match R56's exact `name=` and copy its `supported_version`. Both are in R56's `descriptor.mod`.
4. Enable the mod in the launcher **below** Road to 56.

## Where it sits in the tree
Unlocked by `KMT_empower_the_secret_police`, and mutually exclusive with Chiang's `KMT_gut_the_deep_state_new`.

| Focus | Effect |
|---|---|
| The Officers' Memorandum | Adds the *Disquiet* spirit (-10% PP), unlocks decisions |
| Court the Moderates → A Hero of the Nation | +5% democratic, unlocks *Reach Out to the Liberals*; Sun +1 skill, unlocks *Promote the War Hero* |
| Tax Police Model → American Methods | *Professional Training* spirit; asks the USA for advisors (tech bonus) |
| **Generalissimo Steps Aside** (needs democratic >15%, stability >50%, war-hero status) | Sun takes over peacefully |
| **Nanking Coup** (always available) | Civil war: loyalists take ~65%, Sun keeps the capital and 5 elite divisions |
| The New Army | Lower manpower, higher quality. The coup version is stronger |
| Special Service Units / Discipline over Chaos | Special forces cap; stability, plus extra PP and command power after a coup |

## Updating when R56 changes
`common/national_focus/china_nationalist.txt` is R56's file with the Sun focuses pasted in (source: `tools/SLJ_focuses.txt`, edit them there) plus one mutual-exclusion line. When R56 updates, or after editing the focuses, regenerate it:

    python tools/patch_r56_tree.py "<R56 folder>/common/national_focus/china_nationalist.txt"

## Check on first run (launch with -debug, then read logs/error.log)
- Uses R56's own `CHI_sun_li_jen` (general and high-command advisor, recruited at start).
- [ ] `CHI_sun_li_jen = { skill > 3 }` in `SLJ_triggers.txt` (delete the line if it errors).
- [ ] Coup split: test `start_civil_war`, and optionally pin `capital`/`states` with R56 state IDs.
- [ ] Spirits and the decision category have no icons yet.

## Not in v0.1
- The NCNS-based tree (`china_nationalist_sea.txt`). Hook it the same way.
- A "military hardliners" option as a third choice.
- Chiang-specific focuses later in the tree aren't blocked after Sun takes over.
