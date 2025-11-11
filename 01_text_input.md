Judul:  Memahami Input Teks pada Model Bahasa
 Ringkasan

Input teks adalah kalimat mentah (raw text) yang dimasukkan ke model bahasa untuk dianalisis.
Model tidak memahami huruf atau kata secara langsung, tetapi mengubah teks menjadi bentuk numerik agar bisa dihitung secara matematis.

 Contoh
"Izin ditolak karena berkas tidak lengkap"


Model akan memproses kalimat ini untuk mengenali struktur dan konteksnya.

Contoh Kode
text = "Izin ditolak karena berkas tidak lengkap"
print("Input:", text)

 Output
Input: Izin ditolak karena berkas tidak lengkap

💡 Penjelasan

Tahap ini adalah langkah pertama sebelum teks diubah menjadi token.
Setiap kalimat yang diberikan ke model akan dipecah menjadi unit-unit kecil (token) agar bisa diolah lebih lanjut pada tahap berikutnya.
