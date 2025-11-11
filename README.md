# LLM Fundamentals: Dari Teks → Token → Embedding → Transformer

Repo ini berisi dokumentasi dan kode praktik untuk memahami alur dasar LLM:
1) **Teks (Input)**
2) **Tokenizer**
3) **Embedding**
4) **Transformer** (gambaran & eksplorasi)

##  Cara Pakai
```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt

 Menjalankan Demo
# 1. Teks input
python src/01_text_input.py

# 2. Tokenizer (HuggingFace)
python src/02_tokenizer.py

# 3a. Embedding dasar (random init)
python src/03_embedding_basics.py

# 3b. Cosine similarity antar kata
python src/03_embedding_similarity.py


Notebook opsional (jelajah transformer/attention):
notebooks/04_transformer_explore.ipynb

 Dokumentasi Teori


:

01_text_input.md

02_tokenizer.md

03_embedding.md

04_transformer.md



🔑 Lisensi

MIT – silakan gunakan dan sebarkan.


## 2) `requirements.txt`
```txt
numpy==1.26.4
pandas==2.2.2
matplotlib==3.8.4
transformers==4.45.2
torch>=2.2.0
tqdm==4.66.4

3) .gitignore
venv/
__pycache__/
.ipynb_checkpoints/
*.pyc
.DS_Store

4) LICENSE

Pilih MIT agar bebas dipakai:

MIT License
Copyright (c) 2025 ...

Permission is hereby granted, free of charge, to any person obtaining a copy...
