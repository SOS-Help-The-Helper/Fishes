# Fish Highlight — Production Review & Remaster Notes

Source: `Fishhighlight v4.mp4` · 4:01 · 1080p23.976 · analyzed 2026-07-24

## What was measured

| Metric | v4 (original) | Remaster |
|---|---|---|
| Integrated loudness | −12.9 LUFS | −13.9 LUFS (streaming standard) |
| Peak level | 0.0 dBFS (clipping) | −1.5 dBTP |
| Hard cuts | 79 (median shot 1.9 s, shortest 0.17 s) | — |
| Cut-to-beat alignment | 51% within 83 ms of a beat (chance = 48%) | — |
| Felt tempo | ~86 BPM · bar ≈ 2.8 s · 8-bar phrase ≈ 22.3 s | — |

The edit currently has no rhythmic relationship to the music — which means full freedom
to add one deliberately (see playbook below).

## Audio remaster (already done — files in `audio/`)

The soundtrack was split with Demucs (htdemucs) into a **voice** stem (song vocals +
vows/toasts/crowd speech) and a **music** stem, then rebuilt:

- Music ducks up to **−7 dB under every speech region**, following the voice envelope,
  with 0.75 s ramps: opening toasts 0:04–0:18, vows 1:01–1:22, 1:34–1:41, 1:48–1:52,
  closing vow audio 3:35–3:57.
- Dialogue lifted **+2.5 dB** in those regions.
- Master chain: 30 Hz high-pass → two-pass loudnorm to −14 LUFS / −1.5 dBTP (linear mode).

### Files

| File | Use |
|---|---|
| `audio/remastered_audio.flac` | Full new soundtrack — drop under your timeline, mute the old mix |
| `audio/remastered_audio.m4a` | Same, small AAC copy |
| `audio/stem_vocals_speech.flac` | Voices only (song vocals + speech) |
| `audio/stem_music.flac` | Music only — rebalance against the voice stem freely |

If you still have the editing project, exporting the real music file and the clip-audio
track separately beats AI separation — use these numbers as the recipe either way.

## Musicality playbook (the "intertwined" feel)

Three layers, none of which is cut-on-every-beat:

**1. Cut scenes on phrases, cut shots freely.** The song's structural seams are at
1:36, 2:04, 2:28, 2:42, 3:19, 3:38. Slide each *scene* change (ceremony → formals →
party → pool dance floor → ceremony callback) onto a seam; inside a phrase, cut on the
footage, not the grid.

**2. Pick ~5 hit points, ignore the rest.** Ring reveal, first kiss, dance-floor jump,
sparkler/pool moment, final wide. Nudge just those so the impact frame lands on a
downbeat (beats are 0.35 s apart — moves are never more than ~0.2 s). Sparse sync reads
as magic; global sync reads as a metronome.

**3. Let the song's dynamics set shot length.** Currently ~1.9 s median throughout.
Instead: verses 3–5 s, chorus 1–2 s, the hottest section (2:04–3:00) the fastest
montage, then long again for the callback. Speed-ramps: start 3× slow, land real time on
a phrase seam; or hold slow-mo through a vocal line, snap to real time on the chorus.

## Visual fixes, ranked by impact

1. **Unify vertical-clip treatment** (biggest "phone edit" tell — currently a mix of
   black pillars and blur-fill). Pick one: consistent graded blur-fill, push-in to fill
   frame, or two verticals side-by-side during the party montage.
2. **Replace the Instagram screen recording at 2:09–2:21** — IG logo + username overlay
   baked in, double compression. Get the original file, or crop past the overlay and
   halve its length.
3. **One unifying grade** over all clips (warm highlights, lifted blacks, teal ocean),
   with per-clip WB/exposure matching underneath. Denoise + tame the red LED wash in
   night reception clips.
4. **Intercut the 19 s ceremony wide (1:01–1:21)** — keep vow audio running, cut away
   twice to faces/hands/rings (guests were filming; footage exists).
5. **Stabilize handheld clips; conform frame rates** — retime 60 fps clips to slow-mo
   rather than dropping frames into the 23.976 timeline.

## Keep — these already work

- **The ceremony-callback ending (3:35–4:01).** Strongest structural idea in the cut.
  Sharpen: music falls to just voice + waves, one final musical button under the last
  frame; trim the closing wide a few seconds.
- **The pool dance-floor overhead (3:19–3:27).** Genuinely cinematic — give it the full
  phrase starting at 3:19.

---

## v6 changelog (2026-07-24)

Full re-edit delivered as `v6/Fishhighlight_v6.mp4.part00..02` — rejoin with:
`cat v6/Fishhighlight_v6.mp4.part* > Fishhighlight_v6.mp4`

- **Runtime 4:01.5 → 3:31.2.** Act II distilled; all splices on lyric-line boundaries.
  Cut: blurry dance verticals (1:42.1–1:48.5), dark walking shot (2:05.9–2:08.8),
  instrumental dance block (2:21.3–2:33.9, pool-floor visual relocated over the old
  food-plate shot), table-setting/car-selfie block (3:04.5–3:09.0), 4 s tail trim.
  Kept: Instagram dance clip (full), bachelor-party lifts, "Day 3" story clip.
- **Hinge sharpened:** deeper music duck under "I now pronounce you husband and wife"
  plus a quick dip before the crowd "Woo!", which now cuts straight to the first dance
  on "'cause that's all that really matters in the end."
- **Vow wide intercut:** digital punch-in (1:07–1:10.5) and hands close-up cutaway
  (1:15.5–1:17.3) break up the 19 s locked wide; vow audio continuous.
- **Unified verticals:** 25 pillarboxed/letterboxed shots converted to blurred-fill.
- **Night cleanup:** mild denoise on 14 low-light shots.
- **Unified grade:** gentle warm highlights, +5% saturation, slight contrast across all.
- **Audio master:** `audio/audio_v6_master.flac` — −13.9 LUFS, −1.5 dBTP.

---

## v7 — lyric ↔ visual map and re-arrangement (2026-07-24)

Songs identified: **Act I — Spencer Crandall, "My Person"** · **Act II — ILLENIUM feat.
Teddy Swims, "All That Really Matters"**. Runtime 3:24.

| v7 time | Audio (lyric cue / speech) | On screen |
|---|---|---|
| 0:00 | waves, terrace reveal | empty ceremony arch over the sea |
| 0:04 | parents' toast — "I didn't lose a son…" | sunset cocktail party |
| 0:12 | "I was lookin' for a long time…" | childhood photos (blur-filled) |
| 0:16 | "…never found nobody like you" | engagement ring reveal |
| 0:18 | Mai Tai meet-cute verse | coastline, hair & prep, venue |
| 0:33 | "…that night I'd find my person" | bridal party, groomsmen |
| 0:37 | chorus: "my heartbeat, my slow dance" | **dad first-look trio (kept)** |
| 0:40 | "Sunday mornin' sippin' coffee in bed" | **couple vertical + couple arch portraits (new)** |
| 0:45 | "my best friend…" | groom spins bride; couple at arch |
| 0:49 | "reason for speedin' home from work" | night string-lights flash-forward |
| 0:54 | "my savin' grace, my everything" | dad walks bride down the steps |
| 0:57 | "never been more sure" | hands close-up at the altar |
| 0:59 | "…that you're my person" | **carry-kiss + night embrace (new)** |
| 1:02–1:21 | THE VOWS (music ducked) | ceremony wide + two punch-ins |
| 1:22 | bridge: "Mama, she's the one" | **dad + bride portrait (relocated here)** |
| 1:30 | "yeah, you're my person" outro | reception-entrance build (brightened) |
| 1:36 | "I now pronounce you husband and wife" → "Woo!" | ceremony wide, on the musical seam |
| 1:42 | **restored full chorus entry** "…hold on to / find someone who'll be there for you" | **pool dance floor overhead + couple (new)** |
| 1:49 | "that's all that really matters in the end" | first dance under the lights |
| 2:02 | chorus climax | friend-burst montage (8 cuts) |
| 2:09 | instrumental drop | IG dance clip (brightened, full length) |
| 2:21 | **single beat-snapped splice** → chorus 2: "Find something you can hold on to" | golden-hour friends block |
| 2:31 | "find somewhere you can come home to" | couple under purple lights (new) |
| 2:36 | "find someone that'll die for you" | bachelor-party lifts |
| 2:39 | "that's all that really matters…" | slow dance, sweetheart table |
| 2:46 | instrumental outro | pool dance floor, full phrase |
| 2:57 | night dance wind-down | couple in the dark (new fill) |
| 2:59 | officiant: "…bless these two… their love is real" | ceremony callback |
| 3:08 | "you're a force when you're together. I love you guys." | final wide, 1.2 s fade |

### v7 changes from feedback
- **Chorus visuals re-arranged**: "my person" now belongs to the couple; dad shots kept
  on "my slow dance" and moved onto "Mama, she's the one."
- **Cut entirely**: roaming-guests pre-ceremony wide, posed dad portrait (relocated as a
  1.5 s slice), the full "hard to tell the truth" verse (~21 s — lyrics not wedding-apt),
  second-half landscape/beach shots (harbor, night vista, Day 3 beach, drone swim),
  table-setting + car-selfie block visuals.
- **Song-2 audio smoothed**: ONE beat-snapped splice (141.39 → 174.54 source) with 150 ms
  fades instead of three butt cuts; full chorus entry line restored so the transition hits.
- **Mix fix**: ducking now applies only to real speech (toasts/vows/officiant) — v6 was
  ducking under Teddy Swims' own chorus vocal, thinning the drop.
- **Night shots brightened**: two-tier gamma/denoise lift (strong <35 luma, medium <45),
  including the IG clip.
- **More video, fewer stills** in Act II fills: replaced with first-dance, pool-floor,
  couple-dance footage freed by the cuts.

---

## v8 — the Reel cut (2026-07-24)

**2:59.6 — Instagram Reel legal.** Files: `v8/Fishhighlight_v8_reel.mp4.part00..02`
(16:9, rejoin with `cat`), `v8/Fishhighlight_v8_reel_9x16.mp4` (1080×1920, post-ready),
`audio/audio_v8_master.flac`.

- **Splice rebuilt**: single music cut, out at 2:14.3 on a downbeat, in at "Find
  somewhere you can come home to" — exactly 37 bars apart so the bar clock never skips.
  True 150 ms equal-power overlap crossfade + one-beat 2.5 dB pre-dip.
- **To 3:00 with no new music seams**: IG clip trimmed to 5.4 s inside the instrumental
  (same single splice, widened), chorus 2's repeated first half dropped, two officiant
  sentences lifted at speech pauses.
- **Motion pass**: 4–6% Ken Burns push-ins on stills and static holds; slow pull-out on
  the final wide; optical-flow slow motion on dad hug ("my slow dance"), bride spin
  ("my best friend"), carry-kiss ("…that you're my person").
- **More voice-over-b-roll**: "you make me laugh" → groom pool candid during vows;
  officiant blessing plays over sunset friends / arch group / night dance.
