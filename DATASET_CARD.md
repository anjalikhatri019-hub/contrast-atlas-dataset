# CONTRAST ATLAS dataset card

## Identity and source

CONTRAST ATLAS is a derived benchmark from the Smartphone Image Denoising Dataset (SIDD), created by Abdelrahman Abdelhamed, Stephen Lin, and Michael S. Brown. The publisher's [SIDD page](https://abdokamel.github.io/sidd/) describes the paired noisy sRGB and ground-truth estimates and states the MIT License. The organizer selected 30 paired source instances from SIDD Small sRGB and retains member CRCs and curated-file SHA-256 hashes. The original images and reference estimates remain SIDD material; the tile transformations, action rewards, and split are challenge-specific derivatives.

## Prepared files and types

- `noisy/<tile_id>.png`: 1,440 noisy 384-by-384 RGB tiles, PNG encoded with 8-bit channels. OpenCV reads them as BGR arrays. Each tile is a center-grid crop with a deterministic rotation and optional reflection.
- `train_reference/<tile_id>.png`: 1,152 paired reference tiles in the same format, for training only. No evaluation reference tile is present.
- `train_rewards.csv`: 1,152 rows, ordered columns `tile_id,image_id,row,col,gain_0,gain_1,gain_2,gain_3,action`. The first two fields are categorical opaque strings; row and col are zero-based tile grid coordinates; gains are measured contrast-loss reductions relative to identity in dimensionless loss units; `action` is the per-image budget-optimal training action 0–3.
- `test_tiles.csv`: 288 rows, ordered columns `tile_id,image_id,row,col`. It identifies every evaluation tile and contains no target.
- `sample_submission.csv`: 288 rows, ordered columns `tile_id,image_id,gain_1,gain_2,gain_3,action`. Every gain forecast and action is zero; it is valid and scores zero.
- `DATASET_CARD.md`: this card.
- `SOURCE_LICENSE_NOTICE.md`: source attribution, license scope, and transformation notice.

The private prepared files are `answers.csv`, `source_map.json`, and `SOURCE_LICENSE_EVIDENCE.md`. The private answer CSV has exactly the same ordered header as the sample. Its three gain columns contain actual measured reductions and `action` contains the measured-gain budget oracle. `source_map.json` connects opaque IDs to source instances for organizer auditing. The organizer raw input contains all 30 noisy/reference source pairs and a provenance manifest; that raw input is not participant data.

## Labels, budget, and score

Actions 0/1/2/3 apply the four treatments defined in `challenge_core.py` and cost 0/1/3/2 abstract processing credits. The 32-credit budget is per 48-tile image, not a measured wall-clock time. Each gain is `loss(identity, reference) - loss(action, reference)`; it can be negative and is not a probability or normalized leaderboard score. The loss combines reference-edge gradient error, candidate gradient in reference-flat pixels, and luminance error, with weights 0.35/0.35/0.30. Participants forecast the three nonidentity gains in the same dimensionless loss units, then choose a budget-optimal action for those forecasts. Realized utility is selected measured gain divided by the measured-gain oracle, clipped to [0,1]. Forecast skill is one minus forecast MSE divided by the MSE of fixed public training-mean forecasts `(0.0056081572577770375, 0.011887248053830657, 0.010854216640897604)`, clipped to [0,1]. The image score multiplies utility by forecast skill, and the final score averages images. A budget or forecast-consistency violation invalidates the submission before scoring.

## Split and permitted use

All captures from original source scenes 003 and 008 are held out; the remaining eight scenes form training. Source instance names and scene numbers are not exposed in prepared participant filenames. Participants may use public noisy tiles, training reference tiles and labels, and published challenge code to train a policy. The challenge is intended for research on cost-constrained image processing and local contrast fidelity, not for medical or forensic interpretation, human aesthetic preference prediction, or camera-quality certification.

## Known limitations and generalization

Only ten original scenes and the cameras/lighting configurations present in the selected SIDD subset are covered. Different captures of the same scene can be highly correlated, hence the whole-scene holdout. The SIDD ground truth is an estimated reference, not a noise-free physical measurement. The abstract credit costs are a contest processing budget, not calibrated energy or latency. The chosen contrast loss is a defined operational utility, not a validated human perception score. Public source photographs may permit visual source lookup despite crops, rotations, reflections, and opaque IDs. Official novelty, difficulty, and source-lookup resistance have not been established.
