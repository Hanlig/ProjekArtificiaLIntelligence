# chatbot_test.py

import joblib

# Load model intent yang sudah dilatih
model = joblib.load("intent_model.pkl")

print("Chatbot: Halo! Saya admin toko kue. Ketik 'keluar' untuk mengakhiri.")

while True:
    user_input = input("Anda: ")
    if user_input.lower() in ["keluar", "exit", "quit"]:
        print("Chatbot: Terima kasih, sampai jumpa!")
        break

    # Prediksi intent dari input pengguna
    intent = model.predict([user_input])[0]

    # Respons berdasarkan intent
    if intent == "greeting":
        print("Chatbot: Hai juga! Ada yang bisa saya bantu?")
    elif intent == "order":
        print("Chatbot: Baik, kak! Ingin pesan kue apa?")
    elif intent == "price":
        print("Chatbot: Untuk jenis kue apa dulu ya, kak?")
    elif intent == "location":
        print("Chatbot: Toko kami ada di Jl. Mawar No. 123, Bandung.")
    elif intent == "hours":
        print("Chatbot: Kami buka setiap hari dari jam 08.00 sampai 20.00.")
    elif intent == "thanks":
        print("Chatbot: Sama-sama, kak 😊")
    elif intent == "goodbye":
        print("Chatbot: Sampai jumpa, kak!")
    else:
        print("Chatbot: Maaf, saya belum mengerti maksudnya 😅")
