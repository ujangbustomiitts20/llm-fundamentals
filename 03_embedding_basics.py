# -*- coding: utf-8 -*-
import numpy as np

vocab = {
    "saya": 0, "mau": 1, "izin": 2,
    "permohonan": 3, "makan": 4, "nasi": 5
}

vocab_size = len(vocab)
embedding_dim = 4

np.random.seed(42)
embedding_matrix = np.random.randn(vocab_size, embedding_dim)

print("Embedding Matrix shape:", embedding_matrix.shape)
for word, idx in vocab.items():
    print(f"'{word}' (ID {idx}) -> {embedding_matrix[idx]}")
