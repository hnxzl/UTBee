"""
Script testing untuk UTBee Chatbot
Menguji berbagai pertanyaan untuk memastikan keyword matching bekerja dengan baik
"""

import json
import re


def load_data():
    """Membaca file JSON"""
    try:
        with open('data.json', 'r', encoding='utf-8') as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        print("❌ Error: File data.json tidak ditemukan!")
        return None


def get_response(user_input, data):
    """Fungsi matching dengan scoring system"""
    if not data or 'pertanyaan' not in data:
        return "⚠️ Maaf, sistem sedang bermasalah."
    
    normalized_input = user_input.lower().strip()
    
    best_match = None
    best_score = 0
    best_keyword_count = 0
    
    for item in data['pertanyaan']:
        keywords = item.get('keyword', [])
        jawaban = item.get('jawaban', '')
        
        match_score = 0
        keyword_count = 0
        
        for keyword in keywords:
            normalized_keyword = keyword.lower().strip()
            pattern = r'\b' + re.escape(normalized_keyword) + r'\b'
            if re.search(pattern, normalized_input):
                word_count = len(normalized_keyword.split())
                match_score += word_count * 10
                keyword_count += 1
        
        if match_score > best_score or (match_score == best_score and keyword_count > best_keyword_count):
            best_score = match_score
            best_keyword_count = keyword_count
            best_match = jawaban
    
    if best_match:
        return best_match
    
    return "🤔 Maaf, saya belum punya jawaban untuk pertanyaan itu."


def test_chatbot():
    """Testing berbagai pertanyaan"""
    print("="*70)
    print("TEST UTBEE CHATBOT - Keyword Matching dengan Scoring System")
    print("="*70)
    print()
    
    data = load_data()
    if not data:
        return
    
    # Daftar pertanyaan test
    test_questions = [
        "apa itu matematika diskrit",
        "biaya kuliah berapa",
        "kenapa aku males kuliah",
        "jadwal kuliah kapan",
        "siapa dosen AI",
        "tugas UTS apa",
        "dimana perpustakaan",
        "cara login portal akademik",
        "beasiswa apa saja",
        "machine learning itu apa"
    ]
    
    for i, question in enumerate(test_questions, 1):
        print(f"{i}. Pertanyaan: {question}")
        response = get_response(question, data)
        print(f"   Jawaban: {response[:100]}..." if len(response) > 100 else f"   Jawaban: {response}")
        print()
    
    print("="*70)
    print("Testing selesai!")
    print("="*70)


if __name__ == "__main__":
    test_chatbot()
