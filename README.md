# CONTRAST ATLAS participant dataset v1.0.4

This public release contains only participant-safe data. It contains no organizer raw source archive, held-out reference image, private answer, or source-ID map. The upstream material is the [Smartphone Image Denoising Dataset](https://abdokamel.github.io/sidd/), published under MIT. The root [LICENSE](LICENSE) applies to this derived public release. Original attribution and transformation details are in [SOURCE_LICENSE_NOTICE.md](SOURCE_LICENSE_NOTICE.md).

Download `participant_dataset.zip` (603,655,847 bytes; SHA-256 `2a0b8cc65404a69985b0d4a52769b4a2a98e181bc08792191065a1a37eb177c7`). The [member manifest](public_release_manifest.json) records the SHA-256 and byte length of each of its 2,602 members; `python verify_release.py participant_dataset.zip` checks the asset.

The ZIP includes 1,440 noisy tiles, 1,152 training reference tiles, measured training rewards, the evaluation tile index, and a nonconstant, noisy-tile-only sample submission. The identity-action gain is implicitly zero, so the training rewards CSV stores only gains 1–3. The challenge scores forecast accuracy, measured utility, and policy alignment. See [DATASET_CARD.md](DATASET_CARD.md) for the schemas and limitations.
