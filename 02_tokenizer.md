Judul: Tokenizer — Mengubah Teks menjadi Angka
📖 Definisi

Tokenizer adalah komponen pertama dalam LLM yang berfungsi untuk memecah teks menjadi token dan mengubah token menjadi ID numerik berdasarkan kamus (vocabulary) model.

Contohnya:

"Izin ditolak karena berkas tidak lengkap"
↓
['I', 'zin', 'Ġdit', 'olak', 'Ġkarena', 'Ġberkas', 'Ġtidak', 'Ġlengkap']
↓
[40, 42140, 288, 11650, 1289, 476, 320, 705]

💡 Catatan Penting

Simbol Ġ menandakan adanya spasi di depan token (fitur khas Byte Pair Encoding / BPE).

Token bisa berupa:

Kata utuh (izin)

Potongan kata (zin)

Tanda baca (.)

Spasi (Ġ)
 Contoh Kode
from transformers import AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained("distilgpt2")
text = "Izin ditolak karena berkas tidak lengkap"

tokens = tokenizer.tokenize(text)
token_ids = tokenizer.encode(text)

print("Tokens:", tokens)
print("Token IDs:", token_ids)

Output
Tokens: ['I', 'zin', 'Ġdit', 'olak', 'Ġkarena', 'Ġberkas', 'Ġtidak', 'Ġlengkap']
Token IDs: [40, 42140, 288, 11650, 1289, 476, 320, 705]

 Kesimpulan

Tokenizer adalah jembatan antara teks dan matematika — ia menerjemahkan bahasa manusia ke angka agar bisa dipahami oleh model.
