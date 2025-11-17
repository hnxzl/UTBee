"""
UTBee - Chatbot Asisten Akademik Universitas Teknologi Bandung
Mata Kuliah: Artificial Intelligence (3 SKS)
Dosen: Dedi Rosadi, S.Kom.
Mahasiswa: Ezra Ben Hanschel (NIM: 22552011038)
Kelas: TIF RM 22B

Konsep AI yang digunakan: Rule-Based System dengan Keyword Matching
Chatbot ini menggunakan pendekatan rule-based sederhana dengan mencocokkan
keyword dari input pengguna dengan database pertanyaan-jawaban di file JSON.
"""

import json
import os
import re


def load_data():
    """
    Fungsi untuk membaca dan memuat data dari file data.json
    
    Returns:
        dict: Data pertanyaan dan jawaban dalam format dictionary
              Mengembalikan None jika file tidak ditemukan atau error
    """
    try:
        # Membaca file JSON yang berisi database pertanyaan-jawaban
        with open('data.json', 'r', encoding='utf-8') as file:
            data = json.load(file)
            print("✅ Data berhasil dimuat dari data.json")
            return data
    except FileNotFoundError:
        print("❌ Error: File data.json tidak ditemukan!")
        return None
    except json.JSONDecodeError:
        print("❌ Error: Format JSON tidak valid!")
        return None


def get_response(user_input, data):
    """
    Fungsi utama untuk memproses input pengguna dan memberikan respons
    
    Logika AI (Rule-Based Keyword Matching dengan Scoring):
    1. Normalisasi input pengguna (lowercase, hapus spasi berlebih)
    2. Loop melalui setiap entri pertanyaan dalam database
    3. Hitung skor berdasarkan jumlah dan spesifisitas keyword yang cocok
    4. Prioritaskan jawaban dengan skor tertinggi
    5. Jika skor sama, pilih yang paling banyak keyword cocok
    6. Jika tidak ada keyword yang cocok, kembalikan respons default
    
    Args:
        user_input (str): Teks input dari pengguna
        data (dict): Data pertanyaan-jawaban dari JSON
    
    Returns:
        str: Jawaban/respons yang sesuai dengan input pengguna
    """
    # Validasi data
    if not data or 'pertanyaan' not in data:
        return "⚠️ Maaf, sistem sedang bermasalah. Silakan coba lagi nanti."
    
    # Normalisasi input: ubah ke lowercase dan hapus spasi berlebih
    normalized_input = user_input.lower().strip()
    
    # Variabel untuk menyimpan kandidat jawaban terbaik
    best_match = None
    best_score = 0
    best_keyword_count = 0
    
    # Loop melalui setiap entri pertanyaan dalam database
    for item in data['pertanyaan']:
        keywords = item.get('keyword', [])
        jawaban = item.get('jawaban', '')
        
        # Hitung skor matching untuk entri ini
        match_score = 0
        keyword_count = 0
        
        # Cek setiap keyword dalam list
        for keyword in keywords:
            # Normalisasi keyword
            normalized_keyword = keyword.lower().strip()
            
            # Matching: cek apakah keyword ada dalam input pengguna
            # Gunakan regex untuk matching word boundary agar lebih akurat
            pattern = r'\b' + re.escape(normalized_keyword) + r'\b'
            if re.search(pattern, normalized_input):
                # Keyword ditemukan! Tambahkan skor
                # Keyword yang lebih panjang mendapat skor lebih tinggi
                word_count = len(normalized_keyword.split())
                match_score += word_count * 10  # Bobot untuk panjang keyword
                keyword_count += 1  # Hitung jumlah keyword yang cocok
        
        # Update best match jika:
        # 1. Skor lebih tinggi, ATAU
        # 2. Skor sama tapi jumlah keyword cocok lebih banyak
        if match_score > best_score or (match_score == best_score and keyword_count > best_keyword_count):
            best_score = match_score
            best_keyword_count = keyword_count
            best_match = jawaban
    
    # Jika ada keyword yang cocok, kembalikan jawaban terbaik
    if best_match:
        return best_match
    
    # Jika tidak ada keyword yang cocok, kembalikan respons default
    return "🤔 Maaf, saya belum punya jawaban untuk pertanyaan itu. Coba tanyakan tentang jadwal, dosen, UTS, atau informasi kampus lainnya!"


def print_welcome():
    """
    Fungsi untuk menampilkan pesan pembuka chatbot
    """
    print("\n" + "="*60)
    print("🐝 Selamat datang di UTBee! 🐝")
    print("Asisten Akademik Universitas Teknologi Bandung")
    print("="*60)
    print("Halo! Saya UTBee, asisten virtual kampus. 😊")
    print("Saya siap membantu menjawab pertanyaan seputar akademik UTB!")
    print("\nKetik 'exit' atau 'keluar' untuk mengakhiri percakapan.")
    print("="*60 + "\n")


def main():
    """
    Fungsi utama untuk menjalankan chatbot di terminal
    
    Alur kerja:
    1. Tampilkan pesan selamat datang
    2. Load data dari JSON
    3. Jalankan loop percakapan
    4. Terima input pengguna
    5. Proses input dan berikan respons
    6. Ulangi sampai pengguna mengetik 'exit' atau 'keluar'
    """
    # Tampilkan pesan pembuka
    print_welcome()
    
    # Muat data dari file JSON
    data = load_data()
    
    # Jika data gagal dimuat, hentikan program
    if not data:
        print("Program dihentikan karena data tidak dapat dimuat.")
        return
    
    print("UTBee siap melayani! 🚀\n")
    
    # Loop percakapan utama
    while True:
        # Terima input dari pengguna
        user_input = input("Anda: ").strip()
        
        # Validasi input kosong
        if not user_input:
            print("UTBee: Silakan ketik pertanyaan Anda! 😊\n")
            continue
        
        # Cek apakah pengguna ingin keluar
        if user_input.lower() in ['exit', 'keluar', 'quit', 'bye']:
            # Ambil respons khusus untuk exit dari data
            farewell_response = get_response(user_input, data)
            print(f"UTBee: {farewell_response}")
            print("\n" + "="*60)
            print("Terima kasih telah menggunakan UTBee! 🐝")
            print("Semoga informasinya bermanfaat. Sampai jumpa! 👋")
            print("="*60 + "\n")
            break
        
        # Proses input dan dapatkan respons dari sistem AI
        response = get_response(user_input, data)
        
        # Tampilkan respons
        print(f"UTBee: {response}\n")


# Entry point program
if __name__ == "__main__":
    main()
