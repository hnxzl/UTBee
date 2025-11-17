import tkinter as tk
from tkinter import scrolledtext, messagebox
import json
import re


class UTBeeChatbotGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("UTBee - Asisten Akademik UTB")
        self.root.geometry("600x700")
        self.root.resizable(False, False)
        self.bg_color = "#f0f0f0"
        self.user_color = "#DCF8C6"
        self.bot_color = "#FFFFFF"
        self.primary_color = "#FFA500"
        self.root.configure(bg=self.bg_color)
        self.data = self.load_data()
        self.setup_gui()
        self.display_welcome_message()

    def load_data(self):
        try:
            with open('data.json', 'r', encoding='utf-8') as file:
                return json.load(file)
        except FileNotFoundError:
            messagebox.showerror("Error", "File data.json tidak ditemukan!")
            return None
        except json.JSONDecodeError:
            messagebox.showerror("Error", "Format JSON tidak valid!")
            return None

    def setup_gui(self):
        header_frame = tk.Frame(self.root, bg=self.primary_color, height=80)
        header_frame.pack(fill=tk.X, side=tk.TOP)
        tk.Label(header_frame, text="UTBee Chatbot", font=("Arial", 20, "bold"), bg=self.primary_color, fg="white").pack(pady=10)
        tk.Label(header_frame, text="Asisten Akademik Universitas Teknologi Bandung", font=("Arial", 10), bg=self.primary_color, fg="white").pack()
        chat_frame = tk.Frame(self.root, bg=self.bg_color)
        chat_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        self.chat_display = scrolledtext.ScrolledText(chat_frame, wrap=tk.WORD, font=("Arial", 11), bg="#FFFFFF", state=tk.DISABLED, height=20)
        self.chat_display.pack(fill=tk.BOTH, expand=True)
        self.chat_display.tag_config("user", foreground="#0066CC", font=("Arial", 11, "bold"))
        self.chat_display.tag_config("bot", foreground="#FF6600", font=("Arial", 11, "bold"))
        self.chat_display.tag_config("timestamp", foreground="#888888", font=("Arial", 9))
        input_frame = tk.Frame(self.root, bg=self.bg_color)
        input_frame.pack(fill=tk.X, padx=10, pady=10)
        self.input_box = tk.Entry(input_frame, font=("Arial", 12), relief=tk.SOLID, borderwidth=1)
        self.input_box.pack(side=tk.LEFT, fill=tk.X, expand=True, ipady=8)
        self.input_box.bind("<Return>", lambda event: self.send_message())
        self.input_box.focus()
        tk.Button(input_frame, text="Kirim", font=("Arial", 12, "bold"), bg=self.primary_color, fg="white", relief=tk.FLAT, cursor="hand2", command=self.send_message, width=10).pack(side=tk.RIGHT, padx=(10, 0))
        tk.Label(self.root, text="Ketik pesan dan tekan Enter atau klik Kirim", font=("Arial", 9), bg=self.bg_color, fg="#666666").pack(pady=(0, 5))

    def display_welcome_message(self):
        welcome_text = (
            "Halo! Selamat datang di UTBee!\n\n"
            "Saya siap membantu menjawab pertanyaan seputar akademik kampus.\n\n"
            "Tanyakan tentang: jadwal kuliah, dosen, UTS, fasilitas kampus, dan lainnya.\n\n"
            "Ketik pertanyaan Anda di bawah ini."
        )
        self.display_message("UTBee", welcome_text)

    def display_message(self, sender, message):
        self.chat_display.config(state=tk.NORMAL)
        if self.chat_display.get("1.0", tk.END).strip():
            self.chat_display.insert(tk.END, "\n\n")
        tag = "bot" if sender == "UTBee" else "user"
        self.chat_display.insert(tk.END, f"{sender}:\n", tag)
        self.chat_display.insert(tk.END, message)
        self.chat_display.see(tk.END)
        self.chat_display.config(state=tk.DISABLED)

    def get_response(self, user_input):
        if not self.data or 'pertanyaan' not in self.data:
            return "Data tidak tersedia."
        normalized_input = user_input.lower().strip()
        best_match = None
        best_score = 0
        best_keyword_count = 0
        for item in self.data['pertanyaan']:
            keywords = item.get('keyword', [])
            jawaban = item.get('jawaban', '')
            match_score = 0
            keyword_count = 0
            for keyword in keywords:
                nk = keyword.lower().strip()
                pattern = r'\b' + re.escape(nk) + r'\b'
                if re.search(pattern, normalized_input):
                    match_score += len(nk.split()) * 10
                    keyword_count += 1
            if match_score > best_score or (match_score == best_score and keyword_count > best_keyword_count):
                best_score = match_score
                best_keyword_count = keyword_count
                best_match = jawaban
        if best_match:
            return best_match
        return "Maaf, belum ada jawaban untuk itu."

    def send_message(self):
        user_input = self.input_box.get().strip()
        if not user_input:
            return
        self.display_message("Anda", user_input)
        self.input_box.delete(0, tk.END)
        if user_input.lower() in ['exit', 'keluar', 'quit', 'bye', 'selesai']:
            self.display_message("UTBee", self.get_response(user_input))
            self.root.after(2000, self.root.quit)
            return
        self.display_message("UTBee", self.get_response(user_input))


def main():
        root = tk.Tk()
        UTBeeChatbotGUI(root)
        root.mainloop()

if __name__ == "__main__":
    main()
