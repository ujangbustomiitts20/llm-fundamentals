# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

vocab = {
    "saya": 0, "mau": 1, "izin": 2,
    "permohonan": 3, "makan": 4, "nasi": 5
}

np.random.seed(42)
embedding_dim = 4
embedding_matrix = np.random.randn(len(vocab), embedding_dim)

def cosine_similarity(a, b):
    return float(np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b)))

pairs = [("izin", "permohonan"), ("izin", "makan"), ("saya", "mau")]
print("Cosine similarity (-1..1, makin dekat 1 makin mirip):")
for w1, w2 in pairs:
    v1 = embedding_matrix[vocab[w1]]
    v2 = embedding_matrix[vocab[w2]]
    print(f"{w1:12s} ↔ {w2:12s} : {cosine_similarity(v1, v2):.4f}")

# Visualisasi 2 dimensi pertama
x = embedding_matrix[:, 0]
y = embedding_matrix[:, 1]
plt.figure(figsize=(7, 6))
plt.scatter(x, y, s=200, alpha=0.6)
for word, idx in vocab.items():
    plt.annotate(word, (x[idx], y[idx]),
                 ha='center',
                 bbox=dict(boxstyle='round,pad=0.3', facecolor='yellow', alpha=0.5))
plt.title("Visualisasi Embedding (2 dimensi pertama)")
plt.xlabel("Dimensi 1")
plt.ylabel("Dimensi 2")
plt.grid(True, alpha=0.3)
plt.axhline(0, linewidth=0.5)
plt.axvline(0, linewidth=0.5)
plt.tight_layout()
plt.show()
