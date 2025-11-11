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
python3 01_text_input.py

# 2. Tokenizer (HuggingFace)
python 02_tokenizer.py

# 3a. Embedding dasar (random init)
python 03_embedding_basics.py

# 3b. Cosine similarity antar kata
python 03_embedding_similarity.py

Dokumentasi Teori:
01_text_input.md
02_tokenizer.md
03_embedding.md


Lisensi

MIT – silakan gunakan dan sebarkan.

