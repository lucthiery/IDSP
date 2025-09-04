
| ID | Dataset                                          | What it contains                                     | Trains which base model                                | Input features (examples)                                                                       | Labels used                      | Output to meta-model |                                                            |
| -- | ------------------------------------------------ | ---------------------------------------------------- | ------------------------------------------------------ | ----------------------------------------------------------------------------------------------- | -------------------------------- | -------------------- | ---------------------------------------------------------- |
| A  | **BotArtist** (2022–23, \~10.9M users)           | Tabular account metadata & ratios (no tweets/images) | **Metadata model** (e.g., XGBoost / TabTransformer)    | followers, following, statuses, `*_by_age`, `foll_friends`, entropy, verified/protected         | **Weak** (BotArtist predictions) | \`P(bot              | metadata)\`                                                |
| B  | **Fox8-23** (2023, 2,280 users)                  | Tweets + some profile info (gold labels)             | **Text/content model** (e.g., BERTweet/SBERT + LR/MLP) | tweet embeddings (mean/attention pooled per user), simple metadata                              | **Gold** (human-verified)        | \`P(bot              | tweets)\`                                                  |
| C  | **BotSim-24** (synthetic, 2024)                  | Simulated interactions & behaviors                   | **Behavior model** (e.g., XGBoost or GNN on cascades)  | inter-tweet times, diurnal patterns, reply/retweet ratios, cascade stats, coordination features | **Gold** (by design)             | \`P(bot              | behavior)\`                                                |
| D  | **Dracewicz & Sepczuk** (synthetic images, 2024) | Profile screenshots (Bot/Cyborg/Real/Verified)       | **Visual model** (e.g., CLIP/ViT fine-tune)            | image embeddings of avatar/banner/UI                                                            | **Gold** (by design)             | \`P(bot              | visual)\` (map Cyborg/Verified to human vs bot for binary) |

# Step-by-Step Plan (Ensemble → Fusion)

## Phase 0 — Setup 
### (Day 0–2)
Repo hygiene: requirements.txt, .gitignore, src/ layout.
Repro: lock seeds, save config YAMLs, write DMP notes (licenses; no redistribution of datasets).

## Phase 1 — Data Understanding & Prep 
### (Days 3–6)
BotArtist: EDA (done), standardize/clip heavy-tailed features (log1p for counts), train/val split (stratified).
Fox8-23: Load NDJSON, embed tweets (e.g., sentence-transformers/all-MiniLM-L6-v2 or BERTweet). Aggregate per user (mean or attention pooling). Train/val split.
BotSim-24: Extract behavior features (inter-event times, burstiness, circadian entropy, cascade depth/width, shared-URL overlap). Train/val split.
Dracewicz: Generate image embeddings (e.g., CLIP ViT-B/32 or ViT-Base). If you stick to binary, map labels: Bot/Cyborg → bot, Real/Verified → human.

## Phase 2 — Train Base Models 
### (Days 7–12)
A: Metadata model (BotArtist): XGBoost (with class weights), evaluate on held-out BotArtist; calibrate probs (isotonic/Platt).
B: Text model (Fox8-23): freeze encoder → pooled embeddings → Logistic Regression / small MLP; calibrate.
C: Behavior model (BotSim-24): start with XGBoost on engineered behavior features; (optional) GNN if you have synthetic graphs.
D: Visual model (Dracewicz): fine-tune CLIP head or small CNN on embeddings; calibrate.
Save each model and a small inference wrapper that returns a single scalar: P(bot | modality).

## Phase 3 — Build the Alignment Set 
### (Days 13–15)
Collect N = 500–2,000 recent public X accounts (2023+). For each account:
Metadata via API, tweets (last 200–1,000), profile image (URL or screenshot).
Labeling: human annotation protocol (2–3 raters; adjudication rule). This is your gold for meta-training (and later, for fusion).

## Phase 4 — Meta-Classifier 
### (Days 16–18)
For each aligned account, compute four base scores:
[p_meta, p_text, p_behav, p_visual].
Train meta-classifier (Logistic Regression or XGBoost) on your alignment set labels.
Evaluate (stratified 5-fold CV). Compare to the best single modality. Plot ROC, PR, and calibration curves.

## Phase 5 — Robustness & Ablations 
### (Days 19–21)
Drop one modality at a time → measure ΔF1/ΔAUC.
Temporal robustness: split aligned set by collection week.
Sensitivity to missing modalities (e.g., no tweets or no image): fallbacks that average available probabilities or use a conditional meta-model.

## Phase 6 — Multimodal Fusion Model 
### (Days 22–28)
Move from an ensemble to a single end-to-end model:
Architecture (late fusion):
Tabular branch: MLP on BotArtist-style features (normalized).
Text branch: frozen BERTweet encoder → mean/attention pooling → projection MLP.
Image branch: frozen CLIP → projection MLP.
(Optional) Behavior branch: MLP on behavior features or a tiny temporal CNN over inter-event times.
Fusion: concatenate branch embeddings → dropout → 2–3 dense layers → sigmoid.
Training recipe:
Initialize branches from base models (or freeze encoders, train only small heads + fusion).
Curriculum: start on large weak data (tabular branch with BotArtist), then unfreeze fusion and fine-tune on Fox8-23 + your alignment set.
Regularization: mix in BotSim-24 mini-batches (behavior/text) for robustness.
Loss: binary cross-entropy; consider focal loss if imbalance remains.
Evaluation: same metrics as the ensemble; compare head-to-head. Report calibration and explainability:
SHAP for tabular branch,
attention weights or integrated gradients for text,
Grad-CAM (if using CNN) or CLIP similarity exemplars for image.

## Phase 7 — Packaging & Reporting 
### (Days 29–32)
CLI or notebook: predict_account(username) that fetches data, runs either ensemble or fusion.
Documentation: model cards, limitations (weak labels in BotArtist; synthetic bias in Dracewicz/BotSim), ethical notes.
Repro bundle: fixed seeds, environment file, experiment configs, data paths (no dataset redistribution).

## Minimal Baselines (fast to implement)
- Tabular-only model on BotArtist (strong baseline).
- Text-only model on Fox8-23 (modern LLM-bot signal).
- Ensemble (A+B) without behavior/image first; then add (C/D) once ready.


## Metrics & Checks
- Primary: 
  - F1 (macro), 
  - ROC-AUC, 
  - PR-AUC, 
  - class-weighted accuracy.
- Calibration: 
  - Brier score, 
  - reliability plots.
- Bias/robustness: 
  - topic slices, 
  - account age bins, 
  - follower count bins.