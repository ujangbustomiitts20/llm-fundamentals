Embedding — Mengubah Token Menjadi Vektor Bermakna
📖 Definisi

Embedding adalah representasi numerik berdimensi tinggi dari setiap token.
Alih-alih hanya berupa ID (angka tunggal), embedding memetakan setiap kata ke vektor yang mengandung makna semantik.

Contoh:

Kata	ID	Vektor
izin	2	[0.12, -0.45, 0.33, ...]
permohonan	3	[-0.22, 0.09, 0.87, ...]

Kata-kata yang mirip maknanya (seperti izin dan permohonan) akan memiliki vektor yang berdekatan di ruang vektor.

 Praktik: Membuat Embedding Sederhana
Langkah 1: Membuat Vocabulary
vocab = {
    "saya": 0, "mau": 1,
    "izin": 2, "permohonan": 3,
    "makan": 4, "nasi": 5
}

Langkah 2: Membuat Embedding Matrix
import numpy as np
np.random.seed(42)
embedding_dim = 4
embedding_matrix = np.random.randn(len(vocab), embedding_dim)

Langkah 3: Ambil Embedding Per Kata
word = "izin"
print(f"'{word}' → {embedding_matrix[vocab[word]]}")

Langkah 4: Hitung Similarity
def cosine_similarity(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

Pasangan	Similarity
izin ↔ permohonan	0.89
izin ↔ makan	0.12
Langkah 5: Visualisasi 2D

Gunakan matplotlib untuk memplot dimensi 1 dan 2 dari embedding:

Titik yang berdekatan menunjukkan kata yang maknanya mirip.

Titik yang jauh menunjukkan kata yang berbeda konteks.

plt.scatter(x, y)
plt.annotate("izin", (x[2], y[2]))

Interpretasi

Embedding adalah “pemahaman matematis” model terhadap makna kata.
Model tahu bahwa izin lebih dekat dengan permohonan daripada dengan makan, walaupun semua direpresentasikan sebagai angka.
