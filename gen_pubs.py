# -*- coding: utf-8 -*-
# Rebuild the Selected Publications block for index.html.
# The official homepage lists 44 papers; the source's "[24]" appears
# twice (a duplicate label), so the last paper is labelled [43].
# We re-number 1..44 in source order. Numbering is auto-assigned.

DATA = [
 # 2026 (5)
 (r'Chaojun Li, Peiliang Gong, Shengrong Li, Chunwei Tian, Yinbo Yu, Ran Wang, Daoqiang Zhang, <span class="me">Qi Zhu*</span>',
  'Spatio-Temporal Hypergraph Attention Networks for Brain Disease Analysis',
  'IEEE Transactions on Image Processing', 2026, 'CCF-A, CAS Tier-1', '10.1109/TIP.2026.3671657'),
 (r'Jinrong Cui, Weihao Ye, Shengrong Li, Jie Wen, <span class="me">Qi Zhu*</span>',
  'Adjacent-aware Modality Recovery based on Incomplete Multi-Modal Brain Disease Diagnosis',
  'IEEE Transactions on Medical Imaging', 2026, 'CAS Tier-1', '10.1109/TMI.2026.3654000'),
 (r'Lunke Fei, Kaiting Huang, Shuping Zhao, <span class="me">Qi Zhu</span>, Bob Zhang, Wei Jia',
  'Learning Multilayer Feature Projection for Homogeneous and Heterogeneous Palmprint Recognition',
  'IEEE Transactions on Systems, Man, and Cybernetics: Systems', 2026, 'CAS Tier-1', '10.1109/TSMC.2025.3647704'),
 (r'Yixin Ji, Vince D. Calhoun, Jin Zhang, <span class="me">Qi Zhu</span>, Shengrong Li, Daniel H. Mathalon, Si Yong Yeo, Daoqiang Zhang, Shile Qi',
  'Prototypical Representation Learning for Multi-Site Domain Generalization in Schizophrenia Diagnosis',
  'IEEE Transactions on Biomedical Engineering', 2026, '', '10.1109/TBME.2026.3658874'),
 (r'Kun Wang, <span class="me">Qi Zhu*</span>, Junyong Zhao, Chuhang Zheng, Wei Shao, Daoqiang Zhang*',
  'Heterogeneous Modality Dynamic Trustworthy Fusion Network for Cross-Subject Sleep Stage Classification',
  'IEEE Transactions on Emerging Topics in Computational Intelligence', 2026, '', '10.1109/TETCI.2025.3647679'),
 # 2025 (15)
 (r'Shengrong Li, <span class="me">Qi Zhu*</span>, Chunwei Tian, Li Zhang, Bo Shen, Chuhang Zheng, Daoqiang Zhang, Wei Shao',
  'Spatio-Temporal Evolutionary Graph Learning for Brain Network Analysis using Medical Imaging',
  'IEEE Transactions on Image Processing', 2025, '34, 5860-5872; CCF-A, CAS Tier-1', '10.1109/tip.2025.3607633'),
 (r'Chuhang Zheng, <span class="me">Qi Zhu*</span>, Lunke Fei, Shengrong Li, Xiangping Bryce Zhai, David Zhang, Daoqiang Zhang',
  'Disentangled Representation Learning for Robust Brainprint Recognition',
  'IEEE Transactions on Information Forensics and Security', 2025, 'CCF-A, CAS Tier-1', '10.1109/TIFS.2025.3602266'),
 (r'Shengrong Li, <span class="me">Qi Zhu*</span>, Chunwei Tian, Wei Shao, Daoqiang Zhang',
  'Interpretable Dynamic Brain Network Analysis with Functional and Structural Priors',
  'IEEE Transactions on Medical Imaging', 2025, 'CAS Tier-1', '10.1109/TMI.2025.3584231'),
 (r'Chuhang Zheng, Chunwei Tian, Wen Jie, Daoqiang Zhang, <span class="me">Qi Zhu*</span>',
  'HeLo: Heterogeneous Multi-Modal Fusion with Label correlation for Emotion Distribution Learning',
  'ACM International Conference on Multimedia (ACM MM)', 2025, 'Accepted, CCF-A Conference', ''),
 (r'Zirui Zhang, Donghai Guan, Cetin Kaya Koc, <span class="me">Qi Zhu*</span>',
  'AdaptPFL: Unlocking Cross-Device Palmprint Recognition via Adaptive Personalized Federated Learning with Feature Decoupling',
  'IJCAI', 2025, 'Accepted, CCF-A Conference', '10.24963/ijcai.2024/787'),
 (r'Lunke Fei, Junlin He, <span class="me">Qi Zhu</span>, Shuping Zhao, Jie Wen, Yong Xu',
  'Deep Multi-View Contrastive Clustering via Graph Structure Awareness',
  'IEEE Transactions on Image Processing', 2025, 'CCF-A, CAS Tier-1', '10.1109/TIP.2025.3573501'),
 (r'Ning Yuan, Donghai Guan, Shengrong Li, Li Zhang, <span class="me">Qi Zhu*</span>',
  'Enhancing Neurodegenerative Disease Diagnosis through Confidence-Driven Dynamic Spatio-Temporal Convolutional Network',
  'IEEE Transactions on Neural Systems and Rehabilitation Engineering', 2025, '33, 1715-1728', '10.1109/tnsre.2025.3564983'),
 (r'Shengrong Li, <span class="me">Qi Zhu*</span>, Liang Sun, Kai Ma, Yixin Ji, Shile Qi, Daoqiang Zhang',
  'Multi-Modal Brain Network Fusion for Intelligent Diagnostic Devices',
  'IEEE Transactions on Consumer Electronics', 2025, '', '10.1109/TCE.2025.3563691'),
 (r'Shengrong Li, <span class="me">Qi Zhu*</span>, Donghai Guan, Bo Shen, Li Zhang, Yixin Ji, Shile Qi, Daoqiang Zhang',
  'Long-Interval Spatio-Temporal Graph Convolution for Brain Disease Diagnosis',
  'IEEE Transactions on Instrumentation and Measurement', 2025, '74, 4004511', '10.1109/tim.2025.3551032'),
 (r'<span class="me">Qi Zhu</span>, Ting Zhu, Lunke Fei, Chuhang Zheng, Wei Shao, David Zhang, Daoqiang Zhang',
 'Multi-Modal Cross-Subject Emotion Feature Alignment and Recognition with EEG and Eye Movements',
 'IEEE Transactions on Affective Computing', 2025, 'CAS Tier-1', '10.1109/taffc.2025.3554399'),
 (r'Minxu Liu, Donghai Guan, Chuhang Zheng, <span class="me">Qi Zhu*</span>',
  'Multi-Modal Discriminative Network for Emotion Recognition across Individuals',
  'IEEE Transactions on Cognitive and Developmental Systems', 2025, '', '10.1109/TCDS.2025.3552124'),
 (r'Zhu Wang, Lunke Fei, Shuping Zhao, Bob Zhang, <span class="me">Qi Zhu</span>, Imad Rida',
  'PalmMamba: Palm Intrinsic Features Learning Selective State Space Model for Palmprint Image Denoising',
  'IEEE Transactions on Multimedia', 2025, 'CAS Tier-1', '10.1109/TMM.2025.3599093'),
 (r'Qi Zhang, Weiqiang Xin, Shuai Wu, <span class="me">Qi Zhu</span>, Qiya Song, Shichao Zhang',
  'A Cluster Tree Network for Image Super-Resolution',
  'IEEE Transactions on Consumer Electronics', 2025, '', '10.1109/TCE.2025.3591767'),
 (r'Chaojun Li, Kai Ma, Shengrong Li, Xiangshui Meng, Ran Wang, Daoqiang Zhang, <span class="me">Qi Zhu*</span>',
  'Multi-channel spatio-temporal graph attention contrastive network for brain disease diagnosis',
  'NeuroImage', 2025, '307, 121013', '10.1016/j.neuroimage.2025.121013'),
 (r'Lunke Fei, Zhihao He, Wai Keung Wong, <span class="me">Qi Zhu</span>, Shuping Zhao, Jie Wen',
  'Semantic decomposition and enhancement hashing for deep cross-modal retrieval',
  'Pattern Recognition', 2025, '160, 111225; CAS Tier-1', '10.1016/j.patcog.2024.111225'),
 # 2024 (6)
 (r'<span class="me">Qi Zhu</span>, Shengrong Li, Xiangshui Meng, Qiang Xu, Zhiqiang Zhang, Wei Shao, Daoqiang Zhang',
  'Spatio-Temporal Graph Hubness Propagation Model for Dynamic Brain Network Classification',
  'IEEE Transactions on Medical Imaging', 2024, '43(6), 2381-2394; CAS Tier-1', '10.1109/tmi.2024.3363014'),
 (r'<span class="me">Qi Zhu</span>, Chuhang Zheng, Zheng Zhang, Wei Shao, Daoqiang Zhang',
 'Dynamic Confidence-Aware Multi-Modal Emotion Recognition',
 'IEEE Transactions on Affective Computing', 2024, '15(3), 1358-1370; CAS Tier-1', '10.1109/TAFFC.2023.3340924'),
 (r'Kai Ma, Xuyun Wen, <span class="me">Qi Zhu</span>, Daoqiang Zhang',
  'Ordinal Pattern Tree: A New Representation Method for Brain Network Analysis',
  'IEEE Transactions on Medical Imaging', 2024, 'CAS Tier-1', '10.1109/TMI.2023.3342047'),
 (r'Liang Sun, Yanling Fu, Junyong Zhao, Wei Shao, <span class="me">Qi Zhu</span>, Daoqiang Zhang',
  'MAS-CL: An End-to-end Multi-atlas Supervised Contrastive Learning Framework for Brain ROI Segmentation',
  'IEEE Transactions on Image Processing', 2024, 'CCF-A, CAS Tier-1', '10.1109/TIP.2024.3431451'),
 (r'Wei Shao, Hang Shi, Jianxin Liu, Yingli Zuo, Liang Sun, TianSong Xia, Wanyuan Chen, Peng Wan, Jianpeng Sheng, <span class="me">Qi Zhu</span>, Daoqiang Zhang',
  'Multi-instance Multi-task Learning for Joint Clinical Outcome and Genomic Profile Predictions from the Histopathological Images',
  'IEEE Transactions on Medical Imaging', 2024, 'CAS Tier-1', '10.1109/TMI.2024.3362852'),
 (r'Yao Wang, Lunke Fei, Shuping Zhao, <span class="me">Qi Zhu</span>, Jie Wen, Wei Jia, Imad Rida',
  'Dense Hybrid Attention Network for Palmprint Image Super-Resolution',
  'IEEE Transactions on Systems, Man, and Cybernetics: Systems', 2024, 'CAS Tier-1', '10.1109/TSMC.2023.3344607'),
 # 2023 (11)
 (r'Ruting Xu, <span class="me">Qi Zhu*</span>, Shengrong Li, Zhenghua Hou, Wei Shao, Daoqiang Zhang',
  'MSTGC: Multi-Channel Spatio-Temporal Graph Convolution Network for Multi-Modal Brain Networks Fusion',
  'IEEE Transactions on Neural Systems and Rehabilitation Engineering', 2023, '', '10.1109/TNSRE.2023.3275608'),
 (r'<span class="me">Qi Zhu</span>, Bingliang Xu, Jiashuang Huang, Heyang Wang, Ruting Xu, Wei Shao, Daoqiang Zhang',
  'Deep Multi-Modal Discriminative and Interpretability Network for Alzheimer\'s Disease Diagnosis',
  'IEEE Transactions on Medical Imaging', 2023, '42(5), 1472-1483; CAS Tier-1', '10.1109/tmi.2022.3230750'),
 (r'Wei Shao, Yingli Zuo, YangYang Shi, Yawen Wu, Jiao Tang, Junyong Zhao, Liang Sun, Zixiao Lu, Jianpeng Sheng*, <span class="me">Qi Zhu*</span>, Daoqiang Zhang*',
  'Characterizing the Survival-Associated Interactions between Tumor-infiltrating Lymphocytes and Tumors from Pathological Images and Multi-omics Data',
  'IEEE Transactions on Medical Imaging', 2023, 'CAS Tier-1', '10.1109/TMI.2023.3274652'),
 (r'<span class="me">Qi Zhu</span>, Yuze Zhou, Lunke Fei, Daoqiang Zhang, David Zhang',
  'Multi-Spectral Palmprints Joint Attack and Defense with Adversarial Examples Learning',
  'IEEE Transactions on Information Forensics and Security', 2023, '18, 1789-1799; CCF-A, CAS Tier-1', '10.1109/tifs.2023.3254432'),
 (r'Qiming Yang, <span class="me">Qi Zhu*</span>, Mingming Wang, Wei Shao*, Zheng Zhang, Daoqiang Zhang',
  'Self-Supervised Federated Adaptation for Multi-Site Brain Disease Diagnosis',
  'IEEE Transactions on Big Data', 2023, '', '10.1109/TBDATA.2023.3264109'),
 (r'<span class="me">Qi Zhu</span>, Guangnan Xin, Lunke Fei, Dong Liang, Zheng Zhang, Daoqiang Zhang, David Zhang',
  'Contactless Palmprint Image Recognition across Smartphones with Self-paced CycleGAN',
  'IEEE Transactions on Information Forensics and Security', 2023, '18, 4944-4954; CCF-A, CAS Tier-1', '10.1109/tifs.2023.3301729'),
 (r'Wei Shao, Jianxin Liu, Yingli Zuo, Shile Qi, Honghai Hong, Jianpeng Sheng*, <span class="me">Qi Zhu*</span>, Daoqiang Zhang*',
  'FAM3L: Feature-Aware Multi-modal Metric Learning for Integrative Survival Analysis of Human Cancers',
  'IEEE Transactions on Medical Imaging', 2023, 'CAS Tier-1', '10.1109/TMI.2023.3262024'),
 (r'<span class="me">Qi Zhu</span>, Qiming Yang, Mingming Wang, Xiangyu Xu, Yuwu Lu, Wei Shao, Daoqiang Zhang',
  'Multi-Discriminator Active Adversarial Network for Multi-Center Brain Disease Diagnosis',
  'IEEE Transactions on Big Data', 2023, '', '10.1109/TBDATA.2023.3294000'),
 (r'<span class="me">Qi Zhu</span>, Jing Yang, Shuihua Wang, Daoqiang Zhang, Zheng Zhang',
  'Multi-Modal Non-Euclidean Brain Network Analysis with Community Detection and Convolutional Autoencoder',
  'IEEE Transactions on Emerging Topics in Computational Intelligence', 2023, '7(2), 436-446', '10.1109/tetci.2022.3171855'),
 (r'<span class="me">Qi Zhu</span>, Yuze Zhou, Yuan Yao, Liang Sun, Feng Shi, Wei Shao, Daoqiang Zhang, Dinggang Shen',
  'Semi-Supervised Multi-View Fusion for Identifying CAP and COVID-19 with Unlabeled CT Images',
  'IEEE Transactions on Emerging Topics in Computational Intelligence', 2023, '7(3), 887-899', '10.1109/tetci.2022.3224937'),
 (r'Liang Sun, Wei Shao, <span class="me">Qi Zhu</span>, Meiling Wang, Gang Li, Daoqiang Zhang',
  'Multi-scale multi-hierarchy attention convolutional neural network for fetal brain extraction',
  'Pattern Recognition', 2023, '133; CAS Tier-1', ''),
 (r'Jianpeng Sheng, Juan Du, Junlei Zhang, Lin Wang, Xun Wang, Yaxing Zhao, Jiaoying Lu, Tingmin Fan, Meng Niu, Jie Zhang, Fei Cheng, Jun Li, <span class="me">Qi Zhu</span>, Daoqiang Zhang, Hao Pei, Jing Zhang, He Huang, Xiaocang Cao, Xinjuan Liu, Wei Shao',
  'Selective oxidative protection leads to tissue topological changes orchestrated by macrophage during ulcerative colitis',
  'Nature Communications', 2023, '14, 3675; CAS Tier-1', '10.1038/s41467-023-39173-2'),
 # 2022 (5)
 (r'<span class="me">Qi Zhu</span>, Ruting Xu, Ran Wang, Xijia Xu, Zhiqiang Zhang, Daoqiang Zhang',
  'Stacked Topological Preserving Dynamic Brain Networks Representation and Classification',
  'IEEE Transactions on Medical Imaging', 2022, '41(11), 3473-3484; CAS Tier-1', ''),
 (r'<span class="me">Qi Zhu</span>, Heyang Wang, Bingliang Xu, Zhiqiang Zhang, Wei Shao, Daoqiang Zhang',
  'Multi-Modal Triplet Attention Network for Brain Disease Diagnosis',
  'IEEE Transactions on Medical Imaging', 2022, '41(12), 3884-3894; CAS Tier-1', ''),
 (r'Yuwu Lu, <span class="me">Qi Zhu</span>, Bob Zhang, Zhihui Lai, Xuelong Li',
  'Weighted Correlation Embedding Learning for Domain Adaptation',
  'IEEE Transactions on Image Processing', 2022, '31, 5303-5316; CCF-A, CAS Tier-1', ''),
 (r'<span class="me">Qi Zhu</span>, Ting Zhu, Rui Zhang, Haizhou Ye, Kai Sun, Yong Xu, Daoqiang Zhang',
  'A Cognitive Driven Ordinal Preservation for Multi-Modal Imbalanced Brain Disease Diagnosis',
  'IEEE Transactions on Cognitive and Developmental Systems', 2022, '', '10.1109/TCDS.2022.3175360'),
 (r'<span class="me">Qi Zhu</span>, Huijie Li, Haizhou Ye, Zhiqiang Zhang, Ran Wang, Zizhu Fan, Daoqiang Zhang',
  'Incomplete multi-modal brain image fusion for epilepsy classification',
  'Information Sciences', 2022, '582, 316-333', ''),
 # 2021 (1)
 (r'Rui Zhang, <span class="me">Qi Zhu*</span>, Xiangyu Xu, Daoqiang Zhang, Sheng-Jun Huang',
  'Visual-guided attentive attributes embedding for zero-shot learning',
  'Neural Networks', 2021, '143, 709-718; CAS Tier-1', ''),
 # 2020 (1)
 (r'<span class="me">Qi Zhu</span>, Rui Zhang, Sheng-Jun Huang, Zheng Zhang, Daoqiang Zhang',
  'LGSLRR: Towards fusing discriminative ordinal local and global structured low-rank representation for image recognition',
  'Information Sciences', 2020, '539, 522-535', ''),
]

def build():
    N = len(DATA)
    out = []
    cur = None
    n = 0
    for authors, title, venue, year, tags, doi in DATA:
        n += 1
        if year != cur:
            cur = year
            out.append('    <!-- ===== %d ===== -->' % year)
            out.append('    <div class="pub-year"><a name="pub%d"></a>%d</div>' % (year, year))
            out.append('')
        meta = '<i>%s</i>, %d.' % (venue, year)
        if tags:
            meta += ' (%s)' % tags
        doi_link = '      <p class="pub-links">[<a href="https://doi.org/%s" target="_blank" rel="noopener">DOI</a>]</p>' % doi if doi else ''
        block = ('    <div class="pub-item"><span class="pub-no">[%d]</span><div class="pub-detail">\n'
                 '      <p class="pub-title">%s</p>\n'
                 '      <p class="pub-authors">%s</p>\n'
                 '      <p class="pub-meta">%s</p>\n'
                 '%s'
                 '    </div></div>') % (n, title, authors, meta, (doi_link + '\n') if doi_link else '')
        out.append(block)
        out.append('')
    return N, '\n'.join(out)

if __name__ == '__main__':
    import re
    from collections import Counter
    N, generated = build()

    # 1) numbering must be 1..N, unique, no gaps
    nums = [int(x) for x in re.findall(r'pub-no">\[(\d+)\]', generated)]
    assert nums == list(range(1, N + 1)), 'numbering mismatch: %s' % nums

    # 2) warn on any duplicate paper title (case-insensitive)
    titles = [t.strip().lower() for _, t, _, _, _, _ in DATA]
    dupes = [t for t, c in Counter(titles).items() if c > 1]
    if dupes:
        print('WARNING: duplicate titles detected ->', dupes)
    else:
        print('OK: %d entries, numbers 1..%d unique, no duplicate titles' % (N, N))

    # 3) replace the publications block in index.html cleanly.
    #    anchor on the FIRST year marker (start of old block) and the Honors marker.
    path = r'D:\360MoveData\Users\86132\Desktop\WorkBuddy\index.html'
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    start_marker = '<!-- ===== 2026'
    end_marker = '<!-- ===== Honors'
    s = content.find(start_marker)
    e = content.find(end_marker)
    assert s != -1 and e != -1 and s < e, 'anchor markers not found / out of order'
    head = content[:s]
    tail = content[e:]
    new_content = head + '\n' + generated + '\n\n  ' + tail
    with open(path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print('WROTE index.html (replaced publications block cleanly)')
