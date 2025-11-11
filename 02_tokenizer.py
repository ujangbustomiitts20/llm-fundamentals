# -*- coding: utf-8 -*-
from transformers import AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained("distilgpt2")
text = "Izin ditolak karena berkas tidak lengkap"

tokens = tokenizer.tokenize(text)
token_ids = tokenizer.encode(text)

print("Teks:", text)
print("Tokens:", tokens)
print("Token IDs:", token_ids)
