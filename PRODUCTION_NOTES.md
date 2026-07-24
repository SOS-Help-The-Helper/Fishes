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
