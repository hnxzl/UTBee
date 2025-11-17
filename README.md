# 🐝 UTBee - Chatbot Asisten Akademik Universitas Teknologi Bandung

## Informasi Project

**Nama Project:** UTBee – Chatbot Asisten Akademik Universitas Teknologi Bandung

**Mata Kuliah:** Artificial Intelligence (3 SKS)

**Dosen Pengampu:** Dedi Rosadi, S.Kom.

**Mahasiswa:** Ezra Ben Hanschel

**NIM:** 22552011038

**Kelas:** TIF RM 22B

**Universitas:** Universitas Teknologi Bandung

---

## Deskripsi

UTBee adalah chatbot asisten virtual yang dirancang untuk membantu mahasiswa Universitas Teknologi Bandung dalam mendapatkan informasi akademik dengan cepat dan mudah. Chatbot ini menggunakan pendekatan **Rule-Based System** dengan metode **Keyword Matching** untuk memberikan respons yang relevan berdasarkan pertanyaan pengguna.

### Tujuan Project

Project ini dibuat sebagai bagian dari Ujian Tengah Semester (UTS) mata kuliah Artificial Intelligence dengan tujuan:

1. Mendemonstrasikan pemahaman konsep AI sederhana berbasis rule-based
2. Mengimplementasikan sistem keyword matching untuk chatbot
3. Menyediakan solusi praktis untuk kebutuhan informasi akademik kampus

---

## Fitur Utama

- ✅ **Keyword Matching Cerdas**: Mencocokkan pertanyaan pengguna dengan database menggunakan regex
- ✅ **Database JSON Fleksibel**: Mudah menambah atau mengubah pertanyaan-jawaban
- ✅ **Interface Terminal**: Chatbot dapat dijalankan langsung di command line
- ✅ **Interface GUI (Opsional)**: Tersedia versi GUI menggunakan Tkinter
- ✅ **Respons Ramah**: Gaya percakapan yang friendly dan khas asisten kampus
- ✅ **Offline**: Tidak memerlukan koneksi internet atau API eksternal
- ✅ **Ringan**: Tidak menggunakan library berat seperti transformers atau NLTK

---

## Konsep AI yang Digunakan

### Rule-Based System dengan Keyword Matching

UTBee menggunakan **Rule-Based System**, yaitu sistem AI yang bekerja berdasarkan aturan-aturan (rules) yang telah ditentukan sebelumnya. Sistem ini tidak menggunakan machine learning atau AI generatif, melainkan logika matching sederhana:

**Cara Kerja:**

1. **Input Processing**: Sistem menerima input dari pengguna
2. **Normalisasi**: Input diubah ke lowercase dan dibersihkan dari spasi berlebih
3. **Keyword Matching**: Sistem mencari kecocokan antara kata kunci (keyword) dalam database dengan input pengguna menggunakan regular expression
4. **Response Generation**: Jika keyword cocok, sistem mengembalikan jawaban yang sesuai
5. **Default Response**: Jika tidak ada keyword yang cocok, sistem memberikan respons default

**Keunggulan Pendekatan Ini:**

- Cepat dan efisien
- Akurat untuk domain spesifik (akademik kampus)
- Mudah di-maintain dan dikembangkan
- Tidak memerlukan training data atau model ML

---

## Struktur Project

```
UTBee_Chatbot/
├── chatbot.py              # File utama chatbot (versi terminal)
├── chatbot_gui.py          # File chatbot dengan GUI Tkinter
├── data.json               # Database pertanyaan-jawaban
├── requirements.txt        # File dependensi project
└──  README.md               # Dokumentasi project
```

---

## Cara Menjalankan Program

### Prasyarat

- Python 3.10 atau versi lebih baru
- File `data.json` harus berada di folder yang sama dengan script

### Menjalankan Versi Terminal

1. Buka terminal/command prompt
2. Navigasi ke folder project:
   ```bash
   cd path/to/UTBee_Chatbot
   ```
3. Jalankan chatbot:
   ```bash
   python chatbot.py
   ```

### Menjalankan Versi GUI

1. Pastikan Tkinter sudah terinstall (biasanya sudah built-in di Python)
2. Jalankan chatbot GUI:
   ```bash
   python chatbot_gui.py
   ```

### Mengakhiri Percakapan

- **Versi Terminal**: Ketik `exit`, `keluar`, `quit`, atau `bye`
- **Versi GUI**: Ketik salah satu kata di atas atau tutup window

---

## Cara Menambahkan Data Baru

Untuk menambahkan pertanyaan dan jawaban baru ke dalam chatbot:

1. Buka file `data.json`
2. Tambahkan entri baru dalam array `pertanyaan` dengan format:

```json
{
  "keyword": ["kata_kunci_1", "kata_kunci_2", "kata_kunci_3"],
  "jawaban": "Jawaban yang akan diberikan chatbot ketika keyword cocok"
}
```

**Contoh Penambahan:**

```json
{
  "pertanyaan": [
    {
      "keyword": ["kantin", "makan", "cafe"],
      "jawaban": "🍽️ Kantin kampus UTB buka dari pukul 07.00-17.00 dengan berbagai pilihan menu!"
    }
  ]
}
```

**Tips:**

- Gunakan keyword yang beragam untuk meningkatkan akurasi matching
- Keyword tidak case-sensitive (otomatis diubah ke lowercase)
- Gunakan emoji untuk membuat jawaban lebih menarik

---

## Contoh Percakapan

### Percakapan 1: Tentang Dosen

```
Anda: Siapa dosen pengampu AI?
UTBee:  Dosen pengampu mata kuliah Artificial Intelligence adalah Bapak Dedi Rosadi, S.Kom. Beliau mengajar di kelas TIF RM 22B dengan beban 3 SKS.
```

### Percakapan 2: Tentang Jadwal

```
Anda: Dimana saya bisa lihat jadwal kuliah?
UTBee:  Jadwal kuliah semester ini dapat dilihat di portal akademik Universitas Teknologi Bandung. Anda juga bisa menghubungi bagian akademik untuk informasi lebih detail!
```

### Percakapan 3: Tentang Tugas UTS

```
Anda: Apa tugas UTS kita?
UTBee:  UTS kali ini berupa proyek chatbot berbasis JSON bernama UTBee. Pastikan file data.json berfungsi dengan baik dan chatbot dapat menjawab pertanyaan seputar akademik kampus!
```

### Percakapan 4: Pertanyaan Tidak Dikenali

```
Anda: Apa cuaca hari ini?
UTBee:  Maaf, saya belum punya jawaban untuk pertanyaan itu. Coba tanyakan tentang jadwal, dosen, UTS, atau informasi kampus lainnya!
```

---

##  Teknologi yang Digunakan

- **Bahasa Pemrograman**: Python 3.10+
- **Library Standar**:
  - `json` - untuk membaca dan parsing file JSON
  - `re` - untuk regular expression matching
  - `tkinter` - untuk membuat GUI (opsional)
  - `os` - untuk operasi file system

**Catatan Penting**: Project ini sengaja tidak menggunakan library AI/ML yang berat seperti:

- ❌ transformers
- ❌ openai
- ❌ nltk
- ❌ tensorflow/pytorch

Hal ini sesuai dengan tujuan pembelajaran konsep AI rule-based yang sederhana.

---

##  Alur Kerja Sistem

```
┌─────────────────┐
│  User Input     │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  Normalisasi    │ (lowercase, trim)
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  Load JSON Data │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Loop Pertanyaan │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Keyword Match?  │
└────┬───────┬────┘
     │ Ya    │ Tidak
     ▼       ▼
┌─────────┐ ┌─────────────┐
│ Respons │ │   Default   │
│ Sesuai  │ │   Respons   │
└─────────┘ └─────────────┘
```

---

##  Testing & Validasi

Chatbot telah diuji dengan berbagai skenario:

✅ Input dengan huruf kapital  
✅ Input dengan spasi berlebih  
✅ Input dengan multiple keywords  
✅ Input yang tidak ada dalam database  
✅ Input untuk keluar (exit, keluar)  
✅ File JSON tidak ditemukan (error handling)  
✅ Format JSON rusak (error handling)

---

##  Pengembangan Lebih Lanjut

Potensi pengembangan UTBee di masa depan:

1. **Natural Language Processing**: Integrasi dengan NLTK untuk pemrosesan bahasa yang lebih canggih
2. **Machine Learning**: Implementasi model ML untuk learning dari interaksi user
3. **Database Integration**: Koneksi ke database real-time kampus
4. **Multi-language Support**: Dukungan bahasa Inggris
5. **Voice Interface**: Integrasi dengan speech recognition
6. **Web Interface**: Deployment sebagai web app dengan Flask/Django
7. **Analytics Dashboard**: Tracking pertanyaan yang sering ditanyakan

---

## Informasi Mahasiswa

**Nama:** Ezra Ben Hanschel  
**NIM:** 22552011038  
**Kelas:** TIF RM 22B  
**Program Studi:** Teknik Informatika  
**Universitas:** Universitas Teknologi Bandung

---


---

## 📄 Lisensi

Project ini dibuat untuk keperluan akademik (UTS Artificial Intelligence) di Universitas Teknologi Bandung.

---

## Acknowledgments

Terima kasih kepada:

- **Bapak Dedi Rosadi, S.Kom.** - Dosen Pengampu mata kuliah Artificial Intelligence
- **Universitas Teknologi Bandung** - Institusi pendidikan
- Seluruh rekan mahasiswa kelas TIF RM 22B

---

**🐝 UTBee - Your Academic Companion at Universitas Teknologi Bandung**

_"Membantu mahasiswa mendapatkan informasi kampus dengan cepat, mudah, dan menyenangkan!"_

---

**Tanggal Pembuatan:** November 2025  
**Versi:** 1.0.0  
**Status:** ✅ Production Ready

