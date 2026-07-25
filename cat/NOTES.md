# Cat glamour cut — analysis & build notes

Source: `80664450236__F323C62298054892A4B2182B9D313133.mov` · music: `bossy.mp3`
Analyzed 2026-07-25.

## Source analysis

### Video

| Property | Value | Consequence |
|---|---|---|
| Container | QuickTime, iPhone 16 Pro Max, iOS 26.5 | — |
| Codec | HEVC, 10-bit `yuv420p10le`, 5.1 Mbps | Good bit depth to grade into |
| Stored size | 1920×1080, rotation −90 | **Displays 1080×1920 portrait** — vertical native |
| Frame rate | 30 fps, 144 frames | — |
| Duration | 4.80 s | The binding constraint on everything |
| Colour | BT.2020 primaries, HLG transfer (`arib-std-b67`) | HDR — must be tone-mapped, not just copied |
| HDR metadata | **Dolby Vision profile 8.4** (`bl_signal_compatibility_id 4` = HLG-compatible) | Most editors ignore the RPU and render flat/grey |
| Audio | AAC stereo + 4-ch spatial, **−48.1 LUFS** | Effectively silent room tone — discard it |

Extra: 4 timed-metadata streams (gyro/stabilisation/exposure telemetry).

### Image quality — measured, not eyeballed

Contrast-normalised Laplacian variance across all 144 frames:

- min **14** · median **21** · max **26** (a crisply focused shot lands 100+)
- Sharpest frames: **3.27–3.60 s** — the head-up look to camera
- Softest frames: **0.00–0.25 s** — motion blur on the grooming

Noise MAD in flat carpet ≈ **1.0** — very low. That is not a compliment: it means
the iPhone's high-ISO denoiser already ran and smeared the fine detail away. There is
no grain left to remove, and no detail left to recover from the shadows. Sharpening can
restore *acuity* (edge contrast) but cannot restore *resolution*. This is the ceiling on
"crispness" and no tool changes it — the fix is a re-shoot with more light.

Naive Hable tone-mapping produced Y range 12–156 of 255 with mean saturation 21 —
flat, dark, and desaturated. Most of the visual gain below comes from grading that
properly, not from sharpening.

### Music — `bossy.mp3`

- Suno-generated, 124.94 s, −13.6 LUFS, LRA 3.2 (heavily limited, as expected)
- **95.7 BPM** → bar = **2.508 s**, 8-bar phrase = **20.06 s**
- First beat at **0.279 s** — the grid is offset from zero
- Section boundaries: 3.69, 7.24, 8.15, 12.68, **41.77**, 93.55, 103.68, 107.58, 123.04 s
- Energy ramps from RMS 0.051 (0–10 s) to 0.110 (70–80 s), dips at 90–100 s, peaks again 110–120 s

**The mismatch to plan around: 4.8 s of footage against 125 s of music.** Even at 5×
slow motion the footage yields ~24 s. The cut below uses one 8-bar phrase (20.06 s) and
lets the music fade; it does not try to fill the track.

## The cut — `cat_glamour_v1.mp4`

20.06 s = exactly 8 bars. Four shots, each 5.466 s, joined by 0.6 s dissolves centred on
bar lines (5.016 / 10.032 / 15.048 s). Music starts at 0.279 s so its downbeat lands on
video t=0.

| Shot | Source | Slow factor | Move |
|---|---|---|---|
| A | 0.45–1.65 s | 4.55× | 1.00 → 1.14 push, centred on the body |
| B | 1.60–2.80 s | 4.55× | 1.12 → 1.26, drifting toward the head |
| C | 2.75–3.85 s | 4.97× | 1.20 → 1.38, the head lift |
| D | 3.75–4.78 s | 5.31× | 1.32 → 1.58, into the face — the hero frames |

Shots overlap in source so the dissolves cross-cut the same action rather than jumping.

### Per-shot chain (`render_shot.sh`), in order — the order is the point

1. **HDR → SDR**: `zscale` to linear light at `npl=88` → `tonemap=mobius:param=0.3:desat=0`
   → back to BT.709. Tone-mapping in linear light is what stops the grade going muddy.
2. **Denoise before anything else**: `hqdn3d=2:3:5:7`. Sharpening first would lock the
   chroma mush in permanently.
3. **Slow motion**: `minterpolate=fps=120:mi_mode=mci:mc_mode=aobmc:me_mode=bidir:vsbmc=1`
   — motion-compensated optical flow synthesising real intermediate frames, then
   `setpts` to retime. Not frame duplication; not frame blending.
4. **Supersample to 2160×3840** (lanczos) — all sharpening, grading and zooming happen
   at 4K so the push-ins crop into real pixels, then land back at 1080×1920.
5. **Acuity**: `unsharp=5:5:1.0:5:5:0.3` then `cas=0.5` (contrast-adaptive sharpening —
   adds bite without the white haloing that plain unsharp gives at this strength).
6. **Grade**: `eq` contrast 1.16 / sat 1.18 → `colorbalance` cooling the shadows and
   warming the highlights (the tungsten source was already orange; this separates the
   ends of the scale instead of adding more amber) → `curves` S-curve with a 0.02 black
   lift and a 0.96 highlight ceiling so the white wall stops clipping.
7. **Bloom / Pro-Mist**: bright-pass above 0.62 → `gblur sigma=30` → screened back at
   0.22 opacity. This is the beauty-lighting look — highlights bleed into the shadows,
   skin (fur) reads softer while edges stay sharp.
8. **`zoompan`** at 4K, output 1080×1920, focus point tracked per shot toward the head.
9. **`vignette=PI/5`** to pull the eye off the carpet.
10. **`noise=alls=5:allf=t+u`** — grain re-added last. Without it, step 2 + step 5 leave
    a plastic, waxy surface. Fine grain reads as texture and hides banding in the wall.

### Master

`libx264 crf 16 preset slow`, 1080×1920 @ 30, `+faststart`. Audio: music trimmed to
20.064 s, 0.4 s fade in, 1.46 s fade out, `loudnorm I=-14 TP=-1.5 LRA=11` →
measured **−13.8 LUFS**, streaming spec. Delivery copy at crf 20 / 12 Mbps cap = 11 MB.

## What would raise this further

- **A longer take.** Everything else is downstream of 4.8 s. 30–60 s of the same cat in
  the same spot would allow real shot variety instead of four crops of one action.
- **Light.** One bounced lamp off the white wall would move the Laplacian numbers more
  than every filter in this file combined.
- **Shoot in 4K/60 or 1080/120** — 120 fps gives genuine slow motion and makes
  `minterpolate` unnecessary, which removes the only step here that can invent artefacts.
