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

---

## v9 — no more mirrored-blur (2026-07-24)

Same cut/audio as v8 (2:59.6). Every blurred-clone background replaced:
- Near-wide clips (active ≥1400 px): full-bleed 16:9 crop, top-biased, light sharpening.
- True verticals: "album card" — dark warm gradient + vignette, thin frame line.
- Old photos: borderless cards (their own matting merges into the gradient).
- IG clip: cropped to content column (full height, no quality loss), carded.
- 9:16 Reel: gradient canvas instead of blurred clone. Files: `v9/`.

---

## v10/v11 — couple-focused Act I + gentler ducking (2026-07-24)

Runtime 2:59.6 unchanged. Files: `v11/` (16:9 parts + 9:16 Reel), `audio/audio_v11_master.flac`.

**Act I re-arrangement (video-only):** cocktail crowd trimmed to a 2.5 s glimpse — family
photo now holds through "I gained a daughter" (freeze + Ken Burns) and returns as a
zoom-out callback on "Mama, she's the one"; coastline vista → couple slow-dance card;
venue tent → sweetheart-table laughs; car selfie → couple dance; string-lights
atmosphere → slow-mo couple slow dance; cove vista → altar close-up punch; group formal →
family-photo callback; cocktail deck + champagne → intimate night-couple builds.
Displaced fun moved into Act II: champagne toast into the friends chorus, selfie beat
into the sunset block. Bride/groom prep and all dad moments kept.

**Audio (v11):** speech ducking eased −7 → −4 dB, dialogue lift +2.5 → +1.5 dB, ramps
0.75 → 1.2 s — music stays present under toasts/vows/blessing instead of dropping away.

---

## v12 — the transitions cut (2026-07-24)

Runtime 2:59.5. Files: `v12/` (16:9 parts + 9:16 Reel). Same v11 audio.

- **27 dissolves** through the Act I love story and the blessing coda, each side
  micro-speed-stretched so runtime and music sync are preserved to the frame.
- **White-flash hits (0.2 s)**: school portrait → young-couple photo (childhood quick-hit
  pair), pronouncement → pool-floor drop, IG clip → chorus 2 (visually masks the music splice).
- **Fade-through-black** into the final wide; existing fade-out retained.
- **Hard cuts kept deliberately** in the party montage, burst, and vows angle-changes.
- Built as 71 per-piece renders assembled into 39 chapter graphs (xfade) joined
  losslessly at hard cuts.

---

## v14 — no splice, title card, restructured Act II (2026-07-24)

**Runtime 2:59.5 -> 2:27.5.** Files: `v14/` (16:9 parts + 9:16 Reel),
`audio/audio_v14_master.flac`.

- **Splice eliminated.** Act II no longer replays material heard earlier. The film now
  exits Act I right after the pronouncement (source 1:42.3) and enters song 2 at its
  later section (source 3:05.9), then runs continuously to the end of the song. Exactly
  one music junction in the whole film, and the two cut points are 60 bars apart, both
  landing on beats with 0 ms error, joined by a 150 ms equal-power crossfade.
- **The song's own climax now carries the party.** Energy analysis found a break
  (near-silence) followed by the song's loudest section 13 s after the new entry point.
  The friend-burst montage was moved to land on it, masked by a white flash.
- **Act II order:** pool-floor overhead (entry) -> IG dance clip -> couple under purple
  lights (across the break) -> FLASH -> friend burst (climax) -> bachelor lifts ->
  night dancing -> pool floor. Coda unchanged.
- **Title card** ("Tim & Allison / The Wedding Film") over the opening water shot,
  fading in at 0:00.7 and out by 0:04. No added runtime.
- **Bug fix:** one punch-in piece was not receiving its transition extension in v12/v13,
  leaving its dissolve slightly short. Corrected.

---

## v16 — final (2026-07-24)

**2:24.6.** Files: `v16/` (16:9 parts + 9:16 Reel + captions.ass), `audio/audio_v16_master.flac`.

Built from a full labelled catalog of all 80 source shots, so every clip sits in its
correct chapter. The only deliberate out-of-order moment is the opening toast.

- **Act I — chronological**: island vista + title (Est. 7.24.2023) / welcome party under
  the parents' toast / family photo / FILM STRIP carrying childhood + four new
  pre-wedding photos / those photos held individually / arrival + venue / RING REVEAL on
  the chorus hit at 0:37.7 / getting ready / first look with dad (incl. #55, corrected
  from "couple" to bride-and-dad) / processional / vows at 1:01.6 (audio and picture
  aligned) / ceremony / pronouncement at 1:35.6.
- **Act II — chronological celebration** from the kiss through portraits, formals,
  cocktail hour, golden hour, the friend burst landing on the song's climax, reception,
  bachelor party, night dancing.
- **Coda** — the blessing over the ceremony, closing on their married portrait at the
  arch in slow motion, fading out.
- **Removed** per review: #56, #68, #70, #71, plus all reception footage that had been
  sitting in Act I.
- **Transitions**: film strip, 16 defocus dissolves, dissolves, whip-pans, white flashes
  on the ring and the drop. No shutter squeeze.
- **Captions**: spoken word only (toast, vows, blessing), text supplied by the couple.
  Pronouncement intentionally uncaptioned.
- **Mix**: steady −3 dB duck under speech with 1.5 s ramps (replaces envelope-following,
  which pumped). Officiant filler trimmed; closing line removed.

---

## v17 — native vertical + restored music (2026-07-25)

**2:24.6. Two native builds** — `v17/Fishhighlight_v17_vertical.mp4.part*` (1080x1920,
the primary/post file) and `v17/Fishhighlight_v17_wide.mp4.part*` (1920x1080).
Rejoin each with `cat <parts> > file.mp4`. Plus both caption files and
`audio/audio_v17_master.flac`.

- **Native 9:16 build**: vertical clips and portrait photos render full-bleed or
  near-full-width; landscape clips sit large on the gradient with captions below.
  No more card-inside-letterbox nesting.
- **Music mystery solved**: the source file itself ducks the music 14–20 dB under the
  vows and officiant (baked into the original edit). Restored +8 dB under vows, +5 dB
  under the pronouncement, +13 dB under the blessing — then mastered to −11.8 LUFS
  (≈2.5 dB louder overall).
- Caption corrected: "I lost a son, I gained a daughter."
- 0:48–1:02 dad run intercut with guests, venue detail, aerial deck, bride+dad (#55).
- Bridesmaid walk-through cutaway removed; vow cutaways now land on caption lines
  (Colorado photo on "adventure-seeking spirit", Halloween photo on "make me laugh").
- Friend burst starts at 1:52.89; groom's IG dance clip follows, then dance-floor
  and night-dancing footage.
- Final married portrait: slow-motion + hold, 2.5 s fade.

---

## v18 (2026-07-25)

**2:26.8, both formats in `v18/`** (vertical = primary). Built with piece-level reuse —
only ~25 of 126 pieces re-rendered.

- Ring reveal at exactly 0:36.42.
- Film strip cut to 2 photos (school portrait + young-couple photo); no photo appears
  twice anywhere (pumpkin/mountain held once in the open; Colorado and Halloween photos
  appear only at their matching vow lines).
- Landscape photos letterbox at full width in vertical (no more couples cropped
  off-frame); portrait photos stay full-bleed.
- Father-daughter dance (#55) moved to Act II; hands close-up extended (slow-mo) at
  0:59; officiant-visible clip removed from the song section.
- Burst at 1:51.89; IG groom clip follows with the handle/logo erased (delogo).
- Captions in Great Vibes script, placed inside the picture with outline+shadow.
- Final portrait holds 2 s longer, 3 s fade (video and audio).

---

## v19 — vertical only (2026-07-25)

**2:29.9. `v19/` (vertical parts + captions).** Wide format dropped per request —
vertical is now the sole deliverable going forward.

- Speech boost raised further: vows +11dB, pronouncement +7dB, blessing +16dB/+18dB.
- Mother's shot (#6) held 1s longer.
- Stairs descent (#20,#19, gentle slow-mo) swapped into the "setting the scene" slot;
  the ceremony/officiant wide (#22) moved to the stairs' old position.
- Aerial deck shot (#58) removed.
- The long silent-looking wide (#79) cut from 8.05s to 3.5s.
- Act II extended ~3s (natural continuation of the same song, no new splice) with two
  more after-party shots (#36 poolside toast, #62 gold-dress dancing) bridging into the
  coda instead of an abrupt cut.
- Coda: #77 swapped for #74 (couple embracing at night) — romantic replacement.
- **Ending fixed**: previously ~2s of pure digital silence played under the final hold.
  Replaced with continued (heavily boosted) real stem audio through 237.5s, fading from
  audible music rather than from nothing.
- Captions re-timed to the new (longer) Act II boundary.
