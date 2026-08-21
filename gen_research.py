# -*- coding: utf-8 -*-
"""Generate the Research (thematic) section for Dr. Qi Zhu's homepage.

Three directions, each with 3-5 representative-work cards (figure + brief text +
[PDF][Code]) followed by the full paper list of that direction (every paper gets
[PDF][Code]). Inserted before the existing Selected Publications section.

Data is transcribed from the classification the advisor finalized (2023-2026 only;
2022 & earlier excluded, plus the two segmentation papers removed).
"""
import re

PATH = r'D:\360MoveData\Users\86132\Desktop\WorkBuddy\index.html'


def hl(authors):
    # highlight both "Qi Zhu*" and "Qi Zhu" as the professor
    return re.sub(r'Qi Zhu(\*)?', r'<span class="me">Qi Zhu\1</span>', authors)


def links(doi, code=None):
    code_href = code if code else "#"
    s = '[<a href="#" target="_blank" rel="noopener">PDF</a>] [<a href="%s" target="_blank" rel="noopener">Code</a>]' % code_href
    if doi:
        s += ' [<a href="https://doi.org/%s" target="_blank" rel="noopener">DOI</a>]' % doi
    return s


def list_item(n, p):
    return ('    <div class="pub-item"><span class="pub-no">[%d]</span><div class="pub-detail">\n'
            '      <p class="pub-title">%s</p>\n'
            '      <p class="pub-authors">%s</p>\n'
            '      <p class="pub-meta"><i>%s</i>, %d.</p>\n'
            '      <p class="pub-links">%s</p>\n'
            '    </div></div>') % (n, p['t'], hl(p['a']), p['v'], p['y'], links(p['doi'], p.get('code')))


def work_card(cat, k, p):
    fig = p.get('fig') or 'images/works/cat%d-r%d.png' % (cat, k)
    desc = p.get('desc') or '[Brief description of this work &mdash; to be provided by Dr. Zhu.]'
    return ('    <div class="work-card">\n'
            '      <img class="work-fig" src="%s" alt="Framework figure" onerror="this.onerror=null;this.src=\'images/work-fig-placeholder.svg\'">\n'
            '      <div class="work-body">\n'
            '        <p class="work-title">%s</p>\n'
            '        <p class="work-authors">%s</p>\n'
            '        <p class="work-desc"><em>%s</em></p>\n'
            '        <p class="work-meta"><i>%s</i>, %d.</p>\n'
            '        <p class="work-links">%s</p>\n'
            '      </div>\n'
            '    </div>') % (fig, p['t'], hl(p['a']), desc, p['v'], p['y'], links(p['doi'], p.get('code')))


# ---------------- Brain Network Analysis (16) ----------------
CAT1 = [
    {'a': 'Chaojun Li, Peiliang Gong, Shengrong Li, Chunwei Tian, Yinbo Yu, Ran Wang, Daoqiang Zhang, Qi Zhu*',
     't': 'Spatio-Temporal Hypergraph Attention Networks for Brain Disease Analysis',
     'v': 'IEEE Transactions on Image Processing', 'y': 2026, 'doi': '10.1109/TIP.2026.3671657',
     'desc': 'The article proposes a spatio-temporal hypergraph attention network framework for brain network analysis.'},
    {'a': 'Jinrong Cui, Weihao Ye, Shengrong Li, Jie Wen, Qi Zhu*',
     't': 'Adjacent-aware Modality Recovery based on Incomplete Multi-Modal Brain Disease Diagnosis',
     'v': 'IEEE Transactions on Medical Imaging', 'y': 2026, 'doi': '10.1109/TMI.2026.3654000'},
    {'a': 'Yixin Ji, Vince D Calhoun, Jin Zhang, Qi Zhu, Shengrong Li, Daniel H Mathalon, Si Yong Yeo, Daoqiang Zhang, Shile Qi',
     't': 'Prototypical Representation Learning for Multi-Site Domain Generalization in Schizophrenia Diagnosis',
     'v': 'IEEE Transactions on Biomedical Engineering', 'y': 2026, 'doi': '10.1109/TBME.2026.3658874'},
    {'a': 'Shengrong Li, Qi Zhu*, Chunwei Tian, Li Zhang, Bo Shen, Chuhang Zheng, Daoqiang Zhang, Wei Shao',
     't': 'Spatio-Temporal Evolutionary Graph Learning for Brain Network Analysis using Medical Imaging',
     'v': 'IEEE Transactions on Image Processing', 'y': 2025, 'doi': '10.1109/tip.2025.3607633',
     'desc': 'This work proposes a topological evolution graph learning model to capture disease-related spatio temporal topological features in DFBNs.'},
    {'a': 'Shengrong Li, Qi Zhu*, Chunwei Tian, Wei Shao, Daoqiang Zhang',
     't': 'Interpretable Dynamic Brain Network Analysis with Functional and Structural Priors',
     'v': 'IEEE Transactions on Medical Imaging', 'y': 2025, 'doi': '10.1109/TMI.2025.3584231',
     'desc': 'In this paper, an interpretable spatio-temporal tensor graph convolutional network is proposed for DFBN analysis.'},
    {'a': 'Ning Yuan, Donghai Guan, Shengrong Li, Li Zhang, Qi Zhu*',
     't': 'Enhancing Neurodegenerative Disease Diagnosis through Confidence-Driven Dynamic Spatio-Temporal Convolutional Network',
     'v': 'IEEE Transactions on Neural Systems and Rehabilitation Engineering', 'y': 2025, 'doi': '10.1109/tnsre.2025.3564983', 'code': 'https://github.com/YNingCode/CD-DSTCN'},
    {'a': 'Shengrong Li, Qi Zhu*, Liang Sun, Kai Ma, Yixin Ji, Shile Qi, Daoqiang Zhang',
     't': 'Multi-Modal Brain Network Fusion for Intelligent Diagnostic Devices',
     'v': 'IEEE Transactions on Consumer Electronics', 'y': 2025, 'doi': '10.1109/TCE.2025.3563691'},
    {'a': 'Shengrong Li, Qi Zhu*, Donghai Guan, Bo Shen, Li Zhang, Yixin Ji, Shile Qi, Daoqiang Zhang',
     't': 'Long-Interval Spatio-Temporal Graph Convolution for Brain Disease Diagnosis',
     'v': 'IEEE Transactions on Instrumentation and Measurement', 'y': 2025, 'doi': '10.1109/tim.2025.3551032'},
    {'a': 'Chaojun Li, Kai Ma, Shengrong Li, Xiangshui Meng, Ran Wang, Daoqiang Zhang, Qi Zhu*',
     't': 'Multi-channel spatio-temporal graph attention contrastive network for brain disease diagnosis',
     'v': 'NeuroImage', 'y': 2025, 'doi': '10.1016/j.neuroimage.2025.121013',
     'code': 'https://github.com/xbrainnet/MSTGAC'},
    {'a': 'Qi Zhu, Shengrong Li, Xiangshui Meng, Qiang Xu, Zhiqiang Zhang, Wei Shao, Daoqiang Zhang',
     't': 'Spatio-Temporal Graph Hubness Propagation Model for Dynamic Brain Network Classification',
     'v': 'IEEE Transactions on Medical Imaging', 'y': 2024, 'doi': '10.1109/tmi.2024.3363014',
     'desc': 'In this paper, optimal transport (OT) theory is introduced to capture the topology evolution of dynamic brain networks, and a multi-channel spatio-temporal graph convolutional network is developed to collaboratively extract temporal and spatial features from the evolution networks.'},
    {'a': 'Kai Ma, Xuyun Wen, Qi Zhu, Daoqiang Zhang',
     't': 'Ordinal Pattern Tree: A New Representation Method for Brain Network Analysis',
     'v': 'IEEE Transactions on Medical Imaging', 'y': 2024, 'doi': '10.1109/TMI.2023.3342047'},
    {'a': 'Ruting Xu, Qi Zhu*, Shengrong Li, Zhenghua Hou, Wei Shao, Daoqiang Zhang',
     't': 'MSTGC: Multi-Channel Spatio-Temporal Graph Convolution Network for Multi-Modal Brain Networks Fusion',
     'v': 'IEEE Transactions on Neural Systems and Rehabilitation Engineering', 'y': 2023, 'doi': '10.1109/TNSRE.2023.3275608'},
    {'a': 'Qi Zhu, Bingliang Xu, Jiashuang Huang, Heyang Wang, Ruting Xu, Wei Shao, Daoqiang Zhang',
     't': "Deep Multi-Modal Discriminative and Interpretability Network for Alzheimer's Disease Diagnosis",
     'v': 'IEEE Transactions on Medical Imaging', 'y': 2023, 'doi': '10.1109/tmi.2022.3230750'},
    {'a': 'Qiming Yang, Qi Zhu*, Mingming Wang, Wei Shao*, Zheng Zhang, Daoqiang Zhang',
     't': 'Self-Supervised Federated Adaptation for Multi-Site Brain Disease Diagnosis',
     'v': 'IEEE Transactions on Big Data', 'y': 2023, 'doi': '10.1109/TBDATA.2023.3264109',
     'code': 'https://github.com/nuaayqm/S2FA'},
    {'a': 'Qi Zhu, Qiming Yang, Mingming Wang, Xiangyu Xu, Yuwu Lu, Wei Shao, Daoqiang Zhang',
     't': 'Multi-Discriminator Active Adversarial Network for Multi-Center Brain Disease Diagnosis',
     'v': 'IEEE Transactions on Big Data', 'y': 2023, 'doi': '10.1109/TBDATA.2023.3294000'},
    {'a': 'Qi Zhu, Jing Yang, Shuihua Wang, Daoqiang Zhang, Zheng Zhang',
     't': 'Multi-Modal Non-Euclidean Brain Network Analysis with Community Detection and Convolutional Autoencoder',
     'v': 'IEEE Transactions on Emerging Topics in Computational Intelligence', 'y': 2023, 'doi': '10.1109/tetci.2022.3171855'},
]

# ---------------- Brain-Computer Interfaces (4) ----------------
CAT2 = [
    {'a': 'Chuhang Zheng, Qi Zhu*, Lunke Fei, Shengrong Li, Xiangping Bryce Zhai, David Zhang, Daoqiang Zhang',
     't': 'Disentangled Representation Learning for Robust Brainprint Recognition',
     'v': 'IEEE Transactions on Information Forensics and Security', 'y': 2025, 'doi': '10.1109/TIFS.2025.3602266',
     'desc': 'This paper proposes a disentangled representation learning based identity recognition framework, which disentangles the EEG signal into intrinsic identity-related information and biased identity-invariant information, thus enhancing the performance of EEG biometrics.'},
    {'a': 'Qi Zhu, Ting Zhu, Lunke Fei, Chuhang Zheng, Wei Shao, David Zhang, Daoqiang Zhang',
     't': 'Multi-Modal Cross-Subject Emotion Feature Alignment and Recognition with EEG and Eye Movements',
     'v': 'IEEE Transactions on Affective Computing', 'y': 2025, 'doi': '10.1109/taffc.2025.3554399',
     'desc': 'In this paper, a cross-subject multi-modal emotion recognition framework is proposed. The architecture jointly learns subject-independent representations and common features shared between EEG and eye movements.'},
    {'a': 'Minxu Liu, Donghai Guan, Chuhang Zheng, Qi Zhu*',
     't': 'Multi-Modal Discriminative Network for Emotion Recognition across Individuals',
     'v': 'IEEE Transactions on Cognitive and Developmental Systems', 'y': 2025, 'doi': '10.1109/TCDS.2025.3552124'},
    {'a': 'Qi Zhu, Chuhang Zheng, Zheng Zhang, Wei Shao, Daoqiang Zhang',
     't': 'Dynamic Confidence-Aware Multi-Modal Emotion Recognition',
     'v': 'IEEE Transactions on Affective Computing', 'y': 2024, 'doi': '10.1109/TAFFC.2023.3340924', 'code': 'https://github.com/xbrainnet/CAFNet',
     'desc': 'This paper proposes a dynamic confidence-aware fusion network for robust recognition of heterogeneous emotion features, including electroencephalogram (EEG) and facial expressions.'},
]

# ---------------- AI Interdisciplinary Applications (16) ----------------
CAT3 = [
    {'a': 'Lunke Fei, Kaiting Huang, Shuping Zhao, Qi Zhu, Bob Zhang, Wei Jia',
     't': 'Learning Multilayer Feature Projection for Homogeneous and Heterogeneous Palmprint Recognition',
     'v': 'IEEE Transactions on Systems, Man, and Cybernetics: Systems', 'y': 2026, 'doi': '10.1109/TSMC.2025.3647704'},
    {'a': 'Kun Wang, Qi Zhu*, Junyong Zhao, Chuhang Zheng, Wei Shao, Daoqiang Zhang*',
     't': 'Heterogeneous Modality Dynamic Trustworthy Fusion Network for Cross-Subject Sleep Stage Classification',
     'v': 'IEEE Transactions on Emerging Topics in Computational Intelligence', 'y': 2026, 'doi': '10.1109/TETCI.2025.3647679', 'fig': 'images/works/cat3-r1.png',
     'desc': 'The paper proposes a Heterogeneous Modality Dynamic Trustworthy Fusion Network (HMDT-Net) for cross-subject sleep stage classification.'},
    {'a': 'Chuhang Zheng, Chunwei Tian, Wen Jie, Daoqiang Zhang, Qi Zhu*',
     't': 'HeLo: Heterogeneous Multi-Modal Fusion with Label correlation for Emotion Distribution Learning',
     'v': 'ACM International Conference on Multimedia (ACM MM)', 'y': 2025, 'doi': '10.1145/3746027.3754852', 'fig': 'images/works/cat3-r4.png',
     'desc': 'In this paper, a multi-modal emotion distribution learning framework is proposed, aiming to fully explore the heterogeneity and complementary information in multi-modal emotional data, as well as the label correlation within mixed basic emotions.'},
    {'a': 'Zirui Zhang, Donghai Guan, Cetin Kaya Koc, Qi Zhu*',
     't': 'AdaptPFL: Unlocking Cross-Device Palmprint Recognition via Adaptive Personalized Federated Learning with Feature Decoupling',
     'v': 'IJCAI', 'y': 2025, 'doi': '10.24963/ijcai.2024/787',
     'code': 'https://gitlab.com/margother/OPL'},
    {'a': 'Lunke Fei, Junlin He, Qi Zhu, Shuping Zhao, Jie Wen, Yong Xu',
     't': 'Deep Multi-View Contrastive Clustering via Graph Structure Awareness',
     'v': 'IEEE Transactions on Image Processing', 'y': 2025, 'doi': '10.1109/TIP.2025.3573501'},
    {'a': 'Zhu Wang, Lunke Fei, Shuping Zhao, Bob Zhang, Qi Zhu, Imad Rida',
     't': 'PalmMamba: Palm Intrinsic Features Learning Selective State Space Model for Palmprint Image Denoising',
     'v': 'IEEE Transactions on Multimedia', 'y': 2025, 'doi': '10.1109/TMM.2025.3599093'},
    {'a': 'Qi Zhang, Weiqiang Xin, Shuai Wu, Qi Zhu, Qiya Song, Shichao Zhang',
     't': 'A Cluster Tree Network for Image Super-Resolution',
     'v': 'IEEE Transactions on Consumer Electronics', 'y': 2025, 'doi': '10.1109/TCE.2025.3591767',
     'code': 'https://github.com/xwq325/CTSRNet'},
    {'a': 'Lunke Fei, Zhihao He, Wai Keung Wong, Qi Zhu, Shuping Zhao, Jie Wen',
     't': 'Semantic decomposition and enhancement hashing for deep cross-modal retrieval',
     'v': 'Pattern Recognition', 'y': 2025, 'doi': '10.1016/j.patcog.2024.111225'},
    {'a': 'Wei Shao, Hang Shi, Jianxin Liu, Yingli Zuo, Liang Sun, TianSong Xia, Wanyuan Chen, Peng Wan, JianPeng Sheng, Qi Zhu, Daoqiang Zhang',
     't': 'Multi-instance Multi-task Learning for Joint Clinical Outcome and Genomic Profile Predictions from the Histopathological Images',
     'v': 'IEEE Transactions on Medical Imaging', 'y': 2024, 'doi': '10.1109/TMI.2024.3362852'},
    {'a': 'Yao Wang, Lunke Fei, Shuping Zhao, Qi Zhu, Jie Wen, Wei Jia, Imad Rida',
     't': 'Dense Hybrid Attention Network for Palmprint Image Super-Resolution',
     'v': 'IEEE Transactions on Systems, Man, and Cybernetics: Systems', 'y': 2024, 'doi': '10.1109/TSMC.2023.3344607'},
    {'a': 'Qi Zhu, Yuze Zhou, Lunke Fei, Daoqiang Zhang, David Zhang',
     't': 'Multi-Spectral Palmprints Joint Attack and Defense with Adversarial Examples Learning',
     'v': 'IEEE Transactions on Information Forensics and Security', 'y': 2023, 'doi': '10.1109/tifs.2023.3254432'},
    {'a': 'Wei Shao, Yingli Zuo, YangYang Shi, Yawen Wu, Jiao Tang, Junyong Zhao, Liang Sun, Zixiao Lu, Jianpeng Sheng*, Qi Zhu*, Daoqiang Zhang*',
     't': 'Characterizing the Survival-Associated Interactions between Tumor-infiltrating Lymphocytes and Tumors from Pathological Images and Multi-omics Data',
     'v': 'IEEE Transactions on Medical Imaging', 'y': 2023, 'doi': '10.1109/TMI.2023.3274652'},
    {'a': 'Qi Zhu, Guangnan Xin, Lunke Fei, Dong Liang, Zheng Zhang, Daoqiang Zhang, David Zhang',
     't': 'Contactless Palmprint Image Recognition across Smartphones with Self-paced CycleGAN',
     'v': 'IEEE Transactions on Information Forensics and Security', 'y': 2023, 'doi': '10.1109/tifs.2023.3301729', 'fig': 'images/works/cat3-r2.png',
     'desc': 'This work proposes a self-paced CycleGAN with self-attention modules, which simultaneously synthesizes missing data and mitigates the impact of different imaging devices.'},
    {'a': 'Wei Shao, Jianxin Liu, Yingli Zuo, Shile Qi, Honghai Hong, Jianpeng Sheng*, Qi Zhu*, Daoqiang Zhang*',
     't': 'FAM3L: Feature-Aware Multi-modal Metric Learning for Integrative Survival Analysis of Human Cancers',
     'v': 'IEEE Transactions on Medical Imaging', 'y': 2023, 'doi': '10.1109/TMI.2023.3262024'},
    {'a': 'Qi Zhu, Yuze Zhou, Yuan Yao, Liang Sun, Feng Shi, Wei Shao, Daoqiang Zhang, Dinggang Shen',
     't': 'Semi-Supervised Multi-View Fusion for Identifying CAP and COVID-19 with Unlabeled CT Images',
     'v': 'IEEE Transactions on Emerging Topics in Computational Intelligence', 'y': 2023, 'doi': '10.1109/tetci.2022.3224937'},
    {'a': 'Jianpeng Sheng, Juan Du, Junlei Zhang, Lin Wang, Xun Wang, Yaxing Zhao, Jiaoying Lu, Tingmin Fan, Meng Niu, Jie Zhang, Fei Cheng, Jun Li, Qi Zhu, Daoqiang Zhang, Hao Pei, Jing Zhang, He Huang, Xiaocang Cao, Xinjuan Liu, Wei Shao',
     't': 'Selective oxidative protection leads to tissue topological changes orchestrated by macrophage during ulcerative colitis',
     'v': 'Nature Communications', 'y': 2023, 'doi': '10.1038/s41467-023-39173-2'},
]

CATS = [
    ('Brain Network Analysis', '脑网络分析', CAT1, [1, 4, 5, 10]),
    ('Brain-Computer Interfaces', '脑机接口', CAT2, [1, 2, 4]),
    ('AI Interdisciplinary Applications', '人工智能交叉应用', CAT3, [2, 3, 13]),
]


def build():
    out = []
    out.append('<!-- ===== Research ===== -->')
    out.append('<div class="inner">')
    out.append('  <div class="section-header">')
    out.append('    <span class="title"><a name="Research"></a>Research</span>')
    out.append('    <span class="top-link">[<a href="#Top">Top</a>]</span>')
    out.append('  </div>')
    out.append('  <p class="research-intro">My research spans three interconnected directions. Representative works are highlighted with their framework figures; full paper lists (with PDF/Code links) follow each direction. <em>PDF/Code links are placeholders to be filled.</em></p>')
    for ci, (en, cn, papers, reps) in enumerate(CATS, start=1):
        out.append('  <div class="research-direction">')
        out.append('    <span class="research-dir-title">%d. %s<span class="cn">（%s）</span></span>' % (ci, en, cn))
        out.append('')
        for k, idx in enumerate(reps, start=1):
            out.append(work_card(ci, k, papers[idx - 1]))
            out.append('')
        out.append('    <p class="sub-head">Publications in this direction</p>')
        out.append('    <div class="research-list">')
        for n, p in enumerate(papers, start=1):
            out.append(list_item(n, p))
            out.append('')
        out.append('    </div>')
        out.append('  </div>')
        out.append('')
    out.append('</div>')
    out.append('')
    out.append('<div class="inner"><hr style="margin:5px 0;"></div>')
    return '\n'.join(out)


if __name__ == '__main__':
    html = build()
    with open(PATH, 'r', encoding='utf-8') as f:
        content = f.read()
    assert '<!-- ===== Selected Publications ===== -->' in content, 'marker missing'
    idx = content.index('<!-- ===== Selected Publications ===== -->')
    new = content[:idx] + html + '\n\n' + content[idx:]
    new = new.replace(
        '<td><a href="#Publications">Selected Publications</a></td>',
        '<td><a href="#Research">Research</a></td>\n        <td><a href="#Publications">Selected Publications</a></td>')
    with open(PATH, 'w', encoding='utf-8') as f:
        f.write(new)
    print('OK inserted Research section; nav updated.')
    print('directions:', len(CATS))
    print('representative cards:', sum(len(c[3]) for c in CATS))
    print('papers listed:', sum(len(c[2]) for c in CATS))
