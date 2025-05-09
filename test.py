import nltk
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

# Download NLTK data
nltk.download('punkt')

# Data untuk chatbot
corpus = [
    "Halo, ada yang bisa saya bantu?",
    "Apa kabar? Saya adalah chatbot yang siap membantu Anda.",
    "Saya menggunakan NLP dan Machine Learning untuk merespons.",
    "Ceritakan lebih banyak tentang masalah Anda.",
    "Terima kasih telah menghubungi saya.",
    "Selamat tinggal, semoga harimu menyenangkan!"
]

# Preprocessing
vectorizer = CountVectorizer().fit_transform(corpus)
vectors = vectorizer.toarray()

def chatbot_response(user_input):
    user_input = user_input.lower()
    user_vector = CountVectorizer().fit(corpus).transform([user_input]).toarray()
    cosine_similarities = cosine_similarity(user_vector, vectors)
    response_index = np.argmax(cosine_similarities)
    
    if cosine_similarities[0][response_index] == 0:
        return "Maaf, saya tidak mengerti. Bisa dijelaskan lebih lanjut?"
    else:
        return corpus[response_index]

# Main loop
print("Chatbot: Halo! Saya adalah chatbot berbasis NLP dan Machine Learning. Ketik 'keluar' untuk mengakhiri percakapan.")
while True:
    user_input = input("Anda: ")
    if user_input.lower() == 'keluar':
        print("Chatbot: Selamat tinggal!")
        break
    response = chatbot_response(user_input)
    print(f"Chatbot: {response}")