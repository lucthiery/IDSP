# Multimodal Bot Detection Project (IDSP)

## Overview
This project investigates the detection of **GenAI-powered botnets** on X (formerly Twitter) using a **multimodal ensemble approach**.  
Modern Generative AI (GenAI) systems can generate convincing text, realistic images, and even video content, making automated accounts almost indistinguishable from real users.  

The goal of this project is to develop and evaluate a **stacked ensemble detection framework** that combines the predictions of multiple models — each trained on a different feature modality — into a unified classification signal.  
The project is conducted as part of the **Interdisciplinary Data Science Project (IDSP)** at **TU Wien**.

---

## Research
All research papers and references used in the project are documented in the `/Research` folder.  
The project is informed by current reports and academic work, including:

- **OpenAI (2024)** – *Influence and Cyber Operations: An Update*  
- **Meta Platforms (2024)** – *Quarterly Adversarial Threat Report Q1 2024*  
- **CETaS / Alan Turing Institute (2024)** – *AI-Enabled Influence Operations: Safeguarding Future Elections*  
- **Choi et al. (2024)** – *Analyzing Russia’s Propaganda Tactics on Twitter using Mixed-Methods Network Analysis and NLP*  

These works provide empirical proof that GenAI-powered influence networks already exist and actively shape online discourse.

---

## Datasets
The detection pipeline integrates **four complementary datasets** plus one **self-created gold validation dataset**:

| ID | Dataset | Year | Type | Description |
|----|----------|------|------|-------------|
| 0 | **Gold.csv** | 2025 | Manual | Manually labeled, small validation dataset (≈400 accounts) for cross-model calibration. |
| A | **BotArtist** | 2022–23 | Real / Weak Labels | ~10.9M Twitter profiles with account-level metadata and ratios; large-scale war-related collection. |
| B | **Fox8-23** | 2023 | Real / Gold Labels | 2,280 manually verified human vs GenAI bot accounts with tweet text and basic metadata. |
| C | **BotSim-24** | 2024 | Synthetic / Simulated | Synthetic simulation of coordinated botnet behaviors and interaction networks. |
| D | **X Fake Profile Detection (Dracewicz & Sepczuk)** | 2024 | Synthetic / Visual | 15,000 profile screenshots labeled as Bot, Cyborg, or Human for image-based modeling. |

---

## Methodology
The project follows the **CRISP-DM framework** with emphasis on **reproducibility**, **multimodal modeling**, and **ensemble learning**.

### Pipeline Overview
1. **Data Preparation:**  
   Feature extraction, normalization, embedding generation, and outlier detection.
2. **Model Training per Modality:**  
   - **Metadata:** models trained on profile-level and activity-based features.  
   - **Text:** models leveraging tweet content and linguistic representations.  
   - **Behavior:** models analyzing temporal, coordination, and interaction patterns.  
   - **Visual:** models based on profile and image features.
3. **Prediction Aggregation:**  
   Collect each model’s probability output `P(bot | modality)` across all datasets.
4. **Meta-Ensemble / Majority Voting:**  
   - Level 1: Majority vote of individual modality models.  
   - Level 2: Stacked meta-classifier (meta-learner) combining base model outputs.
5. **(Optional) Human-Labeled Validation:**  
   Small gold dataset (`Gold.csv`) used for ensemble calibration and robustness testing.
6. **Evaluation & Explainability:**  
   ROC-AUC, PR-AUC, F1, and Brier Score; SHAP and Grad-CAM for interpretability.

---

## Goals
- Build a **reproducible multimodal detection pipeline** for modern GenAI-powered bots.  
- Evaluate **ensemble-based classification** on real, weakly labeled, and synthetic datasets.  
- Integrate a **human-labeled gold validation set** to test ensemble calibration and interpretability.  
- Produce **transparent, bias-aware, and well-documented** results.  

---

## Expected Results
| Model | Baseline (AUC / F1) | Target (AUC / F1) |
|--------|----------------------|--------------------|
| Metadata Model | 0.90 / 0.88 | ≥ 0.92 / 0.90 |
| Text Model | 0.93 / 0.90 | ≥ 0.95 / 0.92 |
| Behavior Model | 0.88 / 0.86 | ≥ 0.91 / 0.89 |
| Visual Model | 0.85 / 0.80 | ≥ 0.88 / 0.83 |
| Meta-Ensemble | — | ≥ 0.96 / 0.94 |

---

## Getting Started

Clone this repository and navigate into the project directory:
```bash
git clone https://github.com/lucthiery/IDSP.git
cd IDSP
