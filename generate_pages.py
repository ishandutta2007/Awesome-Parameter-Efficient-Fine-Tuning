import os

pages = {
    'bottleneck_adapter_era.md': ('The Bottleneck Adapter Era', 'Detailed information about Bottleneck Adapters.\n\n```mermaid\ngraph TD;\n    A[Input] --> B[Self Attention];\n    B --> C[Adapter Layer];\n    C --> D[Feed Forward];\n    D --> E[Adapter Layer];\n    E --> F[Output];\n```'),
    'soft_prompting_era.md': ('The Soft Prompting Era', 'Detailed information about Soft Prompting, Prefix-Tuning, and Prompt Tuning.\n\n```mermaid\ngraph TD;\n    A[Virtual Tokens] --> B[Self Attention];\n    C[Real Tokens] --> B;\n    B --> D[Output];\n```'),
    'low_rank_adaptation_era.md': ('The Low-Rank Adaptation Era (LoRA)', 'Detailed information about LoRA.\n\n```mermaid\ngraph TD;\n    A[Input] --> B[Pre-trained Weight W];\n    A --> C[Low Rank A];\n    C --> D[Low Rank B];\n    B --> E[Add];\n    D --> E;\n```'),
    'additive_methods.md': ('Additive Methods', 'Detailed information about Additive Methods.\n\n```mermaid\ngraph TD;\n    A[Base Architecture] --> B[+ New Modules];\n    B --> C[Modified Architecture];\n```'),
    'selective_methods.md': ('Selective Methods', 'Detailed information about Selective Methods like BitFit.\n\n```mermaid\ngraph TD;\n    A[Full Parameters] --> B[Select Subset];\n    B --> C[Fine-tune Subset Only];\n```'),
    'reparameterization_methods.md': ('Reparameterization Methods', 'Detailed information about Reparameterization Methods.\n\n```mermaid\ngraph TD;\n    A[Weight Update] --> B[Low-Rank Approximation];\n    B --> C[Efficient Training];\n```'),
    'qlora.md': ('QLoRA (Quantized Low-Rank Adaptation)', 'Detailed information about QLoRA.\n\n```mermaid\ngraph TD;\n    A[4-bit Base Model] --> B[LoRA Adapters];\n    B --> C[Memory Efficient Training];\n```'),
    'dora.md': ('DoRA (Weight-Decomposed Low-Rank Adaptation)', 'Detailed information about DoRA.\n\n```mermaid\ngraph TD;\n    A[Weight Matrix] --> B[Magnitude Component];\n    A --> C[Directional Component];\n    C --> D[LoRA Update];\n```'),
    'adalora.md': ('AdaLoRA (Adaptive Low-Rank Adaptation)', 'Detailed information about AdaLoRA.\n\n```mermaid\ngraph TD;\n    A[All Layers] --> B[SVD Importance Metric];\n    B --> C[Dynamic Rank Allocation];\n```'),
    'multi_tenant_saas.md': ('Multi-Tenant Saas API Environments', 'Detailed information about Multi-Tenant SaaS with LoRA.\n\n```mermaid\ngraph TD;\n    A[Base Model in VRAM] --> B[User 1 LoRA];\n    A --> C[User 2 LoRA];\n    A --> D[User 3 LoRA];\n```'),
    'edge_tinyml.md': ('Edge & TinyML Device Personalization', 'Detailed information about Edge Device Personalization.\n\n```mermaid\ngraph TD;\n    A[Local Sensor Data] --> B[On-Device QLoRA];\n    B --> C[Personalized Model];\n```'),
    'cross_domain_modality.md': ('Cross-Domain Modality Expansion', 'Detailed information about Cross-Domain Modality Expansion.\n\n```mermaid\ngraph TD;\n    A[Image Input] --> B[Visual Adapter];\n    B --> C[Frozen LLM];\n```')
}

os.makedirs('pages', exist_ok=True)
for filename, (title, content) in pages.items():
    with open(f'pages/{filename}', 'w', encoding='utf-8') as f:
        f.write(f'# {title}\n\n{content}\n\n[Back to README](../README.md)')
