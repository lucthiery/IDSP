# Botnet detection in the age of GenAI
**Problem Statement:** The rise of large language models (LLMs) has enabled a new generation of autonomous, human-like social media bots that produce convincing text, images, and interactions at scale. Traditional bot-detection systems—designed for rule-based or spam-style automation—can no longer reliably identify these GenAI-powered influence networks, which increasingly distort public discourse and amplify misinformation on platforms such as X (formerly Twitter).

This thesis addresses the absence of a comprehensive, multimodal, and empirically validated framework capable of detecting and understanding LLM-driven botnets. The goal is to develop either:
1. (Dataset) Build a robust detection pipeline that combines metadata, text, behavioral, and visual cues to recognize synthetic agents and coordinated activity.
2. (Study) Analyse empirical evidence of their current influence and structure by studying human inability to question output.

**KPIS:** 
1. Size and quality of dataset and the built models
2. Empirical Study 

## Overview of Chapters and Papers
1. Questions
2. Papers
3. Past
4. .....

## Research Questions 

* To what extent have LLM-powered botnets already influenced opinions on X/Twitter in the past and how successful were they?

### 1. Dataset and Model Focus

* Empirical influence analysis: How much reach and topical influence do identified LLM-powered accounts exert compared to human accounts and traditional bots? (metrics: impressions/retweets, centrality, cascade size)
* Dataset composition question: What is the optimal size and mix of real, weakly-labeled, human-verified, synthetic and simulated examples (text, metadata, images, graph traces) required to train models that generalize across time and events?
* Generalization & temporal robustness: How well do models trained on past events (e.g., 2022–2023 data) transfer to new topics and post-LLM waves (2024–2025)? Which domain-adaptation techniques (fine-tuning, adversarial augmentation, continual learning) improve transfer?

### 2. Societal Aspects Focus
* Empirical influence analysis: In realistic social contexts, how effectively do LLM-powered accounts shift participant opinions compared to human or traditional bot messages? (metrics: pre/post attitude change, message adoption rate)
* Persuasion mechanism: Which conversational strategies produced by LLMs (personalization, emotional framing, repetition, authority cues) yield the largest opinion shifts, and do they differ from human persuasive strategies?
* Interventions & resilience: Which low-cost interventions (explicit provenance tags, critical-thinking prompts, source warnings, brief training) reduce persuasion success of LLM-generated messages, and what is their effect size and persistence?
* Confirmation bias interaction: How does prior belief alignment (confirmatory vs disconfirmatory messages) mediate susceptibility to LLM-generated misinformation? Are people more likely to accept LLM content that confirms their preexisting beliefs?

## Past Research

### Proof of Botnets with Agenda
1. 2024 – OpenAI “Influence and Cyber Operations: An Update” – OpenAI – Report documents how OpenAI disrupted more than 20 covert influence operations during 2024 using its models; these operations included fake social-media personas, content generation, multilingual campaigns.
2. 2024 – Meta Platforms “Quarterly Adversarial Threat Report Q1 2024” – Meta Platforms – Describes how the largest covert online influence operation ever disrupted by Meta (the “Spamouflage” network tied to Chinese law-enforcement) has evolved and begun to use GenAI tools in its campaigns. 
3. 2024 – Centre for Emerging Technology & Security (CETaS) “AI-Enabled Influence Operations: Safeguarding Future Elections” – CETaS UK – Research report analyzing how AI/GenAI tools (text, image, video) alter the threat landscape for election-related influence operations, and what protective factors might mitigate those threats.
4. 2023/2024 – "Synthetic Image Generation in Cyber Influence Operations: An Emergent Threat?" (Mathys, Willi, Graber, Meier) – Swiss research – Explores how generative image-models are beginning to be exploited in cyber influence operations, assessing the accessibility, realism, and threat potential of synthetic visuals in such campaigns.
5. 2024 - "Analyzing Russia’s Propaganda Tactics on Twitter Using Mixed Methods Network Analysis and NLP" (Carnegie Mellon University, EPJ Data Science) – This study investigates Russian propaganda on Twitter during the 2022 invasion of Ukraine, focusing on the “fascism/Nazism” narrative used to justify the war. Using over 6 million tweets in English and Russian, it combines network analysis, BERTopic modeling, and qualitative review to identify the main actors, communities, and narratives spreading this discourse. The authors find that Russian state accounts (e.g., MFA, embassies, RT) and coordinated alt-right networks were central to disseminating anti-Ukraine and anti-West content, while pro-Ukraine users actively countered these narratives. The analysis confirms a hybrid disinformation ecosystem—a mix of bots, trolls, and state-linked influencers—strategically reinforcing propaganda across language communities to erode Western support for Ukraine and legitimize the invasion.


Links:
    1. https://cdn.openai.com/threat-intelligence-reports/influence-and-cyber-operations-an-update_October-2024.pdf?utm_source=chatgpt.com
    2. https://md.teyit.org/file/meta-threat-report.pdf 
    3. https://cetas.turing.ac.uk/publications/ai-enabled-influence-operations-safeguarding-future-elections
    4. https://arxiv.org/pdf/2403.12207 
    5. https://epjdatascience.springeropen.com/articles/10.1140/epjds/s13688-024-00479-w 

### Proof of Concept for Botnets
1. 2024 – “On the Conversational Persuasiveness of Large Language Models” (EPFL & FBK) – A randomized controlled trial with 820 participants demonstrated that GPT-4 can outperform humans in direct debates, increasing persuasion success by 81.7% when given access to personal data. The study proves LLMs can effectively microtarget and adapt arguments in real time, validating their potential use for manipulative chatbot campaigns.
2. 2024 – “Large Language Models Can Consistently Generate High-Quality Content for Election Disinformation Operations” (Alan Turing Institute) – Introduces the DisElect dataset (2,200 disinformation prompts) to test 13 LLMs. Most models generated realistic political misinformation on command; human judges failed to distinguish AI-written election content more than half the time. Confirms that GenAI can automate disinformation operations with human-level realism.
3. 2023 – “Preparing for Generative AI in the 2024 Election: Recommendations and Best Practices” (University of Chicago & Stanford) – A policy white paper summarizing expert consensus that generative AI poses major election risks through deepfakes, microtargeting, and AI-powered manipulation. Cites early cases of AI use in political media and calls for watermarking, transparency, and coordinated “October surprise” response plans.
4. 2023 – “How Social Bots Can Influence Public Opinion More Effectively: Right Connection Strategy” (Physica A, Nanjing University of Aeronautics & Astronautics) – Using agent-based simulations, the study shows bot influence depends more on network positioning and interaction strategy than on bot quantity. Demonstrates how adaptive, human-like connection behavior can significantly amplify persuasion in online social networks.

Links:
    1. https://arxiv.org/abs/2403.14380
    2. https://arxiv.org/abs/2408.06731
    3. https://www.gsb.stanford.edu/faculty-research/publications/preparing-generative-ai-2024-election-recommendations-best-practices
    4. https://www.sciencedirect.com/science/article/pii/S037843712300941X 

### Problems of Mitigation by Social media Platforms

### Turing Test: GenAI content vs Human ability to question (system 2)

## Botdetection before GenAi (pre 2023)

## Building a Dataset

| ID | Dataset                                          | What it contains                                     | Trains which base model                                | Input features (examples)                                                                       | Labels used                      | Output to meta-model                                              |
| -- | ------------------------------------------------ | ---------------------------------------------------- | ------------------------------------------------------ | ----------------------------------------------------------------------------------------------- | -------------------------------- |------------------------------------------------------------------- 
| A  | **BotArtist** (2022–23, \~10.9M users)           | Tabular account metadata & ratios (no tweets/images) | **Metadata model** (e.g., XGBoost / TabTransformer)    | followers, following, statuses, `*_by_age`, `foll_friends`, entropy, verified/protected         | **Weak** (BotArtist predictions) | \`P(bot, metadata)`                                               |
| B  | **Fox8-23** (2023, 2,280 users)                  | Tweets + some profile info (gold labels)             | **Text/content model** (e.g., BERTweet/SBERT + LR/MLP) | tweet embeddings (mean/attention pooled per user), simple metadata                              | **Gold** (human-verified)        | \`P(bot, tweets)`                                                 |
| C  | **BotSim-24** (synthetic, 2024)                  | Simulated interactions & behaviors                   | **Behavior model** (e.g., XGBoost or GNN on cascades)  | inter-tweet times, diurnal patterns, reply/retweet ratios, cascade stats, coordination features | **Gold** (by design)             | \`P(bot, behavior)`                                               |
| D  | **Dracewicz & Sepczuk** (synthetic images, 2024) | Profile screenshots (Bot/Cyborg/Real/Verified)       | **Visual model** (e.g., CLIP/ViT fine-tune)            | image embeddings of avatar/banner/UI                                                            | **Gold** (by design)             | \`P(bot, visual)`(map Cyborg/Verified to human vs bot for binary) |


## Modelling

## Evaluation

## Findings