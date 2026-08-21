#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Map local PDF files in ./papers to publication entries in index.html by title.
   For each matched block:
     - if it already has a bare href="#" PDF slot, fill it;
     - otherwise (e.g. Selected Publications entries that only had [DOI]) insert a [PDF] link.
   Idempotent: never duplicates a link for the same paper."""
import re
from urllib.parse import quote

PATH = r"D:\360MoveData\Users\86132\Desktop\WorkBuddy\index.html"

def norm(s):
    s = re.sub(r"<.*?>", "", s)
    s = s.lower().strip().replace("_", " ")
    return re.sub(r"\s+", " ", s)

MAPPING = {
    norm("Spatio-Temporal Hypergraph Attention Networks for Brain Disease Analysis"):
        "Spatio-Temporal_Hypergraph_Attention_Networks_for_Brain_Disease_Analysis.pdf",
    norm("Spatio-Temporal Evolutionary Graph Learning for Brain Network Analysis using Medical Imaging"):
        "Spatio-Temporal_Evolutionary_Graph_Learning_for_Brain_Network_Analysis_Using_Medical_Imaging.pdf",
    norm("Interpretable Dynamic Brain Network Analysis with Functional and Structural Priors"):
        "Interpretable_Dynamic_Brain_Network_Analysis_With_Functional_and_Structural_Priors.pdf",
    norm("Spatio-Temporal Graph Hubness Propagation Model for Dynamic Brain Network Classification"):
        "Spatio-Temporal Graph Hubness Propagation Model for Dynamic Brain Network Classification.pdf",
    norm("Enhancing Neurodegenerative Disease Diagnosis through Confidence-Driven Dynamic Spatio-Temporal Convolutional Network"):
        "Enhancing Neurodegenerative Disease Diagnosis Through Confidence-Driven Dynamic Spatio-Temporal Convolutional Network.pdf",
    norm("Multi-Modal Brain Network Fusion for Intelligent Diagnostic Devices"):
        "Multi-Modal Brain Network Fusion for Intelligent Diagnostic Devices.pdf",
    norm("Long-Interval Spatio-Temporal Graph Convolution for Brain Disease Diagnosis"):
        "Long-Interval_Spatio-Temporal_Graph_Convolution_for_Brain_Disease_Diagnosis.pdf",
    norm("Multi-channel spatio-temporal graph attention contrastive network for brain disease diagnosis"):
        "Multi-channel spatio-temporal graph attention contrastive network for brain disease diagnosis.pdf",
    norm("Disentangled Representation Learning for Robust Brainprint Recognition"):
        "Disentangled_Representation_Learning_for_Robust_Brainprint_Recognition.pdf",
    norm("AdaptPFL: Unlocking Cross-Device Palmprint Recognition via Adaptive Personalized Federated Learning with Feature Decoupling"):
        "AdaptPFL_ Unlocking Cross-Device Palmprint Recognition via Adaptive Personalized Federated Learning with Feature Decoupling.pdf",
    norm("Multi-Modal Cross-Subject Emotion Feature Alignment and Recognition with EEG and Eye Movements"):
        "Multi-Modal Cross-Subject Emotion Feature Alignment and Recognition With EEG and Eye Movements.pdf",
    norm("Dynamic Confidence-Aware Multi-Modal Emotion Recognition"):
        "Dynamic Confidence-Aware Multi-Modal Emotion Recognition.pdf",
    norm("Semantic decomposition and enhancement hashing for deep cross-modal retrieval"):
        "Semantic decomposition and enhancement hashing for deep cross-modal retrieval.pdf",
    norm("HeLo: Heterogeneous Multi-Modal Fusion with Label correlation for Emotion Distribution Learning"):
        "Heterogeneous Multi-Modal Fusion with Label Correlation for Emotion Distribution Learning.pdf",
    norm("Selective oxidative protection leads to tissue topological changes orchestrated by macrophage during ulcerative colitis"):
        "Selective oxidative protection leads to tissue topological changes orchestrated by macrophage during ulcerative colitis.pdf",
    norm("Heterogeneous Modality Dynamic Trustworthy Fusion Network for Cross-Subject Sleep Stage Classification"):
        "Heterogeneous Modality Dynamic Trustworthy Fusion Network for Cross-Subject Sleep Stage Classification.pdf",
    norm("Contactless Palmprint Image Recognition across Smartphones with Self-paced CycleGAN"):
        "Contactless Palmprint Image Recognition Across Smartphones With Self-Paced CycleGAN.pdf",
    norm("Semi-Supervised Multi-View Fusion for Identifying CAP and COVID-19 with Unlabeled CT Images"):
        "Semi-Supervised_Multi-View_Fusion_for_Identifying_CAP_and_COVID-19_With_Unlabeled_CT_Images.pdf",
    norm("Multi-Modal Discriminative Network for Emotion Recognition across Individuals"):
        "Multimodal_Discriminative_Network_for_Emotion_Recognition_Across_Individuals.pdf",
    norm("Adjacent-aware Modality Recovery based on Incomplete Multi-Modal Brain Disease Diagnosis"):
        "Adjacent-Aware_Modality_Recovery_Based_on_Incomplete_Multi-Modal_Brain_Disease_Diagnosis.pdf",
    norm("Prototypical Representation Learning for Multi-Site Domain Generalization in Schizophrenia Diagnosis"):
        "Prototypical_Representation_Learning_for_Multi-Site_Domain_Generalization_in_Schizophrenia_Diagnosis.pdf",
    norm("Ordinal Pattern Tree: A New Representation Method for Brain Network Analysis"):
        "Ordinal_Pattern_Tree_A_New_Representation_Method_for_Brain_Network_Analysis.pdf",
    norm("MSTGC: Multi-Channel Spatio-Temporal Graph Convolution Network for Multi-Modal Brain Networks Fusion"):
        "MSTGC_Multi-Channel_Spatio-Temporal_Graph_Convolution_Network_for_Multi-Modal_Brain_Networks_Fusion.pdf",
    norm("Self-Supervised Federated Adaptation for Multi-Site Brain Disease Diagnosis"):
        "Self-Supervised_Federated_Adaptation_for_Multi-Site_Brain_Disease_Diagnosis.pdf",
    norm("Deep Multi-Modal Discriminative and Interpretability Network for Alzheimer's Disease Diagnosis"):
        "Deep_Multi-Modal_Discriminative_and_Interpretability_Network_for_Alzheimers_Disease_Diagnosis.pdf",
    norm("Multi-Discriminator Active Adversarial Network for Multi-Center Brain Disease Diagnosis"):
        "Multi-Discriminator_Active_Adversarial_Network_for_Multi-Center_Brain_Disease_Diagnosis.pdf",
    norm("Multi-Modal Non-Euclidean Brain Network Analysis with Community Detection and Convolutional Autoencoder"):
        "Multi-Modal_Non-Euclidean_Brain_Network_Analysis_With_Community_Detection_and_Convolutional_Autoencoder.pdf",
    norm("PalmMamba: Palm Intrinsic Features Learning Selective State Space Model for Palmprint Image Denoising"):
        "PalmMamba_Palm_Intrinsic_Features_Learning_Selective_State_Space_Model_for_Palmprint_Image_Denoising.pdf",
    norm("Deep Multi-View Contrastive Clustering via Graph Structure Awareness"):
        "Deep_Multi-View_Contrastive_Clustering_via_Graph_Structure_Awareness.pdf",
    norm("Learning Multilayer Feature Projection for Homogeneous and Heterogeneous Palmprint Recognition"):
        "Learning_Multilayer_Feature_Projection_for_Homogeneous_and_Heterogeneous_Palmprint_Recognition.pdf",
    norm("A Cluster Tree Network for Image Super-Resolution"):
        "A_Cluster_Tree_Network_for_Image_Super-Resolution.pdf",
    norm("Multi-instance Multi-task Learning for Joint Clinical Outcome and Genomic Profile Predictions from the Histopathological Images"):
        "Multi-Instance_Multi-Task_Learning_for_Joint_Clinical_Outcome_and_Genomic_Profile_Predictions_From_the_Histopathological_Images.pdf",
    norm("Multi-Spectral Palmprints Joint Attack and Defense with Adversarial Examples Learning"):
        "Multi-Spectral_Palmprints_Joint_Attack_and_Defense_With_Adversarial_Examples_Learning.pdf",
    norm("Characterizing the Survival-Associated Interactions between Tumor-infiltrating Lymphocytes and Tumors from Pathological Images and Multi-omics Data"):
        "Characterizing_the_Survival-Associated_Interactions_Between_Tumor-Infiltrating_Lymphocytes_and_Tumors_From_Pathological_Images_and_Multi-Omics_Data.pdf",
    norm("Dense Hybrid Attention Network for Palmprint Image Super-Resolution"):
        "Dense_Hybrid_Attention_Network_for_Palmprint_Image_Super-Resolution.pdf",
    norm("FAM3L: Feature-Aware Multi-modal Metric Learning for Integrative Survival Analysis of Human Cancers"):
        "FAM3L_Feature-Aware_Multi-Modal_Metric_Learning_for_Integrative_Survival_Analysis_of_Human_Cancers.pdf",
}

html = open(PATH, encoding="utf-8").read()
parts = re.split(r'(<div class="(?:pub-item|work-card)">)', html)
out, inserted, filled, matched = [], 0, 0, set()

i, n = 0, len(parts)
while i < n:
    seg = parts[i]
    if re.match(r'<div class="(?:pub-item|work-card)">', seg):
        out.append(seg)
        i += 1
        content = parts[i] if i < n else ""
        m = re.search(r'<p class="(?:work-title|pub-title)">(.*?)</p>', content, re.S)
        if m:
            key = norm(m.group(1))
            if key in MAPPING:
                fn = MAPPING[key]
                href = "papers/" + quote(fn)
                matched.add(key)
                if href not in content:
                    if 'href="#"' in content:
                        content = re.sub(r'href="#"', 'href="%s"' % href, content, count=1)
                        filled += 1
                    elif 'class="pub-links"' in content or 'class="work-links"' in content:
                        content = re.sub(r'(<p class="(?:pub-links|work-links)">)',
                                          r'\1[<a href="%s" target="_blank" rel="noopener">PDF</a>] ' % href,
                                          content, count=1)
                        inserted += 1
                    else:
                        # entry has no links paragraph at all (e.g. no-DOI Selected Publications
                        # entries generated without one) -> add a complete PDF line after the meta
                        content = re.sub(r'(<p class="(?:pub-meta|work-meta)">.*?</p>)',
                                          r'\1\n      <p class="pub-links">[<a href="%s" target="_blank" rel="noopener">PDF</a>]</p>' % href,
                                          content, count=1)
                        inserted += 1
        out.append(content)
        i += 1
    else:
        out.append(seg)
        i += 1

open(PATH, "w", encoding="utf-8").write("".join(out))
print("papers matched:", len(matched), "| PDF slots filled:", filled, "| PDF links inserted:", inserted)
