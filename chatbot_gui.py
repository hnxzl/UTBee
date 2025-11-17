"""
UTBee GUI - Interface Grafis untuk Chatbot UTBee
Menggunakan Tkinter untuk membuat antarmuka chat sederhana

Fitur:
- Area tampilan percakapan (chat history)
- Input box untuk mengetik pertanyaan
- Tombol kirim untuk mengirim pertanyaan
- Scrollbar untuk navigasi chat
"""

import tkinter as tk
from tkinter import scrolledtext, messagebox
import json
import re


class UTBeeChatbotGUI:
    """
    Class untuk membuat GUI chatbot menggunakan Tkinter
    """
    
    def __init__(self, root):
        """
        Inisialisasi GUI dan komponen-komponennya
        """
        self.root = root
        self.root.title("🐝 UTBee - Asisten Akademik UTB")
        self.root.geometry("600x700")
        self.root.resizable(False, False)
        
        # Set warna tema
        self.bg_color = "#f0f0f0"
        self.user_color = "#DCF8C6"
        self.bot_color = "#FFFFFF"
        self.primary_color = "#FFA500"  # Orange untuk tema UTBee
        
        self.root.configure(bg=self.bg_color)
        
        # Load data dari JSON
        self.data = self.load_data()
        
        # Setup GUI components
        self.setup_gui()
        
        # Tampilkan pesan selamat datang
        self.display_welcome_message()
    
    def load_data(self):
        """
        Memuat data dari file data.json
        """
        try:
            with open('data.json', 'r', encoding='utf-8') as file:
                data = json.load(file)
                return data
        except FileNotFoundError:
            messagebox.showerror("Error", "File data.json tidak ditemukan!")
            return None
        except json.JSONDecodeError:
            messagebox.showerror("Error", "Format JSON tidak valid!")
            return None
    
    def setup_gui(self):
        """
        Membuat dan mengatur komponen GUI
        """
        # Header
        header_frame = tk.Frame(self.root, bg=self.primary_color, height=80)
        header_frame.pack(fill=tk.X, side=tk.TOP)
        
        title_label = tk.Label(
            header_frame,
            text="🐝 UTBee Chatbot",
            font=("Arial", 20, "bold"),
            bg=self.primary_color,
            fg="white"
        )
        title_label.pack(pady=10)
        
        subtitle_label = tk.Label(
            header_frame,
            text="Asisten Akademik Universitas Teknologi Bandung",
            font=("Arial", 10),
            bg=self.primary_color,
            fg="white"
        )
        subtitle_label.pack()
        
        # Chat display area dengan scrollbar
        chat_frame = tk.Frame(self.root, bg=self.bg_color)
        chat_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        self.chat_display = scrolledtext.ScrolledText(
            chat_frame,
            wrap=tk.WORD,
            font=("Arial", 11),
            bg="#FFFFFF",
            state=tk.DISABLED,
            height=20
        )
        self.chat_display.pack(fill=tk.BOTH, expand=True)
        
        # Tag untuk styling pesan
        self.chat_display.tag_config("user", foreground="#0066CC", font=("Arial", 11, "bold"))
        self.chat_display.tag_config("bot", foreground="#FF6600", font=("Arial", 11, "bold"))
        self.chat_display.tag_config("timestamp", foreground="#888888", font=("Arial", 9))
        
        # Input area
        input_frame = tk.Frame(self.root, bg=self.bg_color)
        input_frame.pack(fill=tk.X, padx=10, pady=10)
        
        self.input_box = tk.Entry(
            input_frame,
            font=("Arial", 12),
            relief=tk.SOLID,
            borderwidth=1
        )
        self.input_box.pack(side=tk.LEFT, fill=tk.X, expand=True, ipady=8)
        self.input_box.bind("<Return>", lambda event: self.send_message())
        self.input_box.focus()
        
        send_button = tk.Button(
            input_frame,
            text="Kirim 📤",
            font=("Arial", 12, "bold"),
            bg=self.primary_color,
            fg="white",
            relief=tk.FLAT,
            cursor="hand2",
            command=self.send_message,
            width=10
        )
        send_button.pack(side=tk.RIGHT, padx=(10, 0))
        
        # Footer info
        footer_label = tk.Label(
            self.root,
            text="Ketik pesan dan tekan Enter atau klik Kirim",
            font=("Arial", 9),
            bg=self.bg_color,
            fg="#666666"
        )
        footer_label.pack(pady=(0, 5))
    
    def display_welcome_message(self):
        """
        Menampilkan pesan selamat datang saat aplikasi dibuka
        """
        welcome_text = (
            "Halo! Selamat datang di UTBee! 🐝\n\n"
            "Saya adalah asisten virtual Universitas Teknologi Bandung.\n"
            "Saya siap membantu menjawab pertanyaan seputar akademik kampus!\n\n"
            "Silakan tanyakan tentang:\n"
            "• Jadwal kuliah\n"
            "• Informasi dosen\n"
            "• Tugas dan UTS\n"
            "• Fasilitas kampus\n"
            "• Dan banyak lagi!\n\n"
            "Ketik pertanyaan Anda di bawah ini. 😊"
        )
        self.display_message("UTBee", welcome_text)
    
    def display_message(self, sender, message):
        """
        Menampilkan pesan di area chat
        """
        self.chat_display.config(state=tk.NORMAL)
        
        # Tambahkan spacing
        if self.chat_display.get("1.0", tk.END).strip():
            self.chat_display.insert(tk.END, "\n\n")
        
        # Tag untuk sender
        tag = "bot" if sender == "UTBee" else "user"
        
        # Tampilkan nama sender
        self.chat_display.insert(tk.END, f"{sender}:\n", tag)
        
        # Tampilkan pesan
        self.chat_display.insert(tk.END, message)
        
        # Auto-scroll ke bawah
        self.chat_display.see(tk.END)
        self.chat_display.config(state=tk.DISABLED)
    
    def get_response(self, user_input):
        """
        Mendapatkan respons dari sistem AI dengan scoring system
        """
        if not self.data or 'pertanyaan' not in self.data:
            return "⚠️ Maaf, sistem sedang bermasalah. Silakan coba lagi nanti."
        
        normalized_input = user_input.lower().strip()
        
        # Variabel untuk menyimpan kandidat jawaban terbaik
        best_match = None
        best_score = 0
        best_keyword_count = 0
        
        for item in self.data['pertanyaan']:
            keywords = item.get('keyword', [])
            jawaban = item.get('jawaban', '')
            
            # Hitung skor matching
            match_score = 0
            keyword_count = 0
            
            for keyword in keywords:
                normalized_keyword = keyword.lower().strip()
                pattern = r'\b' + re.escape(normalized_keyword) + r'\b'
                if re.search(pattern, normalized_input):
                    # Keyword yang lebih panjang mendapat skor lebih tinggi
                    word_count = len(normalized_keyword.split())
                    match_score += word_count * 10
                    keyword_count += 1
            
            # Update best match jika skor lebih tinggi atau jumlah keyword lebih banyak
            if match_score > best_score or (match_score == best_score and keyword_count > best_keyword_count):
                best_score = match_score
                best_keyword_count = keyword_count
                best_match = jawaban
        
        # Jika ada keyword yang cocok, kembalikan jawaban terbaik
        if best_match:
            return best_match
        
        return "🤔 Maaf, saya belum punya jawaban untuk pertanyaan itu. Coba tanyakan tentang jadwal, dosen, UTS, atau informasi kampus lainnya!"
    
    def send_message(self):
        """
        Mengirim pesan dari pengguna dan mendapatkan respons dari bot
        """
        user_input = self.input_box.get().strip()
        
        # Validasi input kosong
        if not user_input:
            return
        
        # Tampilkan pesan pengguna
        self.display_message("Anda", user_input)
        
        # Kosongkan input box
        self.input_box.delete(0, tk.END)
        
        # Cek apakah pengguna ingin keluar
        if user_input.lower() in ['exit', 'keluar', 'quit', 'bye', 'selesai']:
            response = self.get_response(user_input)
            self.display_message("UTBee", response)
            self.root.after(2000, self.root.quit)  # Tutup aplikasi setelah 2 detik
            return
        
        # Dapatkan respons dari sistem AI
        response = self.get_response(user_input)
        
        # Tampilkan respons bot
        self.display_message("UTBee", response)


def main():
    """
    Fungsi utama untuk menjalankan GUI chatbot
    """
    root = tk.Tk()
    app = UTBeeChatbotGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()
