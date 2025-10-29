# Multimodal Bot Detection Project

## Overview
This project explores **fake account and bot detection on social media** with a focus on **modern LLM-powered bots** (post-2023).  
The goal is to combine **large-scale weakly labeled datasets**, **small gold-labeled datasets**, **synthetic simulations**, and **visual profile datasets** into one **multimodal detection pipeline**.

The project is part of my **Interdisciplinary Data Science Project (IDSP)** at TU Wien.

---

## Datasets
This repository integrates **four complementary datasets**:

1. **BotArtist (2022–23)**  
   - **Scale:** 10.9M Twitter profiles (weak labels).  
   - **Type:** Real, large-scale, war-related.  
   - **Link:** [Zenodo](https://zenodo.org/records/11203900)  

2. **Fox8-23 (2023)**  
   - **Scale:** 2,280 accounts (balanced bots vs humans).  
   - **Type:** Real, small, gold labels (verified LLM bots).  
   - **Links:** [Zenodo](https://zenodo.org/record/10066202), [GitHub](https://github.com/osome-iu/AIBot_fox8)  

3. **BotSim-24 (2024)**  
   - **Scale:** Synthetic simulation dataset.  
   - **Type:** Synthetic, flexible, ground-truth labels.  
   - **Links:** [Arxiv](https://arxiv.org/abs/2412.13420), [GitHub](https://github.com/QQQQQQBY/BotSim/tree/main)  

4. **X Fake Profile Detection (Dracewicz & Sepczuk, 2024)**  
   - **Scale:** 15,000 synthetic profile screenshots.  
   - **Type:** Synthetic, image-based, gold labels.  
   - **Link:** [Hugging Face](https://huggingface.co/datasets/drveronika/x_fake_profile_detection)  

---

## Methodology
The project follows **CRISP-DM** and integrates multiple methods:

- **Pretraining:** on large-scale weak labels (BotArtist).  
- **Fine-tuning:** on gold-labeled small datasets (Fox8-23).  
- **Robustness Testing:** with simulated botnets (BotSim-24).  
- **Multimodal Fusion:** integrating text (tweets), metadata, graph features, and images (Dracewicz dataset).  
- **Explainability:** SHAP (tabular/text) + Grad-CAM (images).  

---

## Goals
- Develop a **multimodal detection pipeline** that scales across domains.  
- Evaluate detection on **modern LLM-powered bots**.  
- Provide **transparent, reproducible experiments** with bias-awareness.  

---

## Getting Started
Clone the repo:

```bash
git clone https://github.com/lucthiery/IDSP.git
cd IDSP

