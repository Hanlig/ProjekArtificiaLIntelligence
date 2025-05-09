import joblib
from entity_extraction import ekstrak_entitas
from menu_kue import menu_kue

# Memuat model intent yang sudah dilatih
model = joblib.load("intent_model.pkl")

print("Chatbot: Halo! Saya admin toko kue. Ketik 'keluar' untuk mengakhiri.")

while True:
    user_input = input("Anda: ")
    if user_input.lower() in ["keluar", "exit", "quit", "bay"]:
        print("Chatbot: Terima kasih, sampai jumpa!")
        break

    intent = model.predict([user_input])[0]

    if intent == "greeting":
        salam = "Hai"
        if "halo" in user_input.lower():
            salam = "Halo"
        elif "hai" in user_input.lower():
            salam = "Hai"
        elif "selamat pagi" in user_input.lower():
            salam = "Selamat pagi"

        print(f"Chatbot: {salam} kak! Selamat datang di *Dapur Rasa Manis*, kami jual aneka kue premium handmade. Ada yang bisa dibantu?")

    elif intent == "order":
        entities = ekstrak_entitas(user_input)
        kue = entities["kue"]
        jumlah = entities["jumlah"]

        if not kue:
            print("Chatbot: Ingin pesan kue apa, kak?")
        else:
            respon = "Chatbot: Baik kak, pesanan kamu:\n"
            total = 0
            for i, k in enumerate(kue):
                jml = int(jumlah[i]) if i < len(jumlah) else 1
                harga = menu_kue[k]
                total += harga * jml
                respon += f"- {jml} {k} (Rp{harga:,} x {jml}) = Rp{harga * jml:,}\n"
            respon += f"Total: Rp{total:,}"
            print(respon)

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

    elif intent == "menu":
        print("Chatbot: Ini daftar kue yang tersedia:")
        for kue, harga in menu_kue.items():
            print(f"- {kue.title()} (Rp{harga:,})")

    # Untuk pertanyaan yang tidak dikenali
    elif intent == "unknown":
        # Menyimpan pertanyaan yang tidak dikenali ke dalam file
        with open("unhandled_questions.txt", "a", encoding="utf-8") as file:
            file.write(user_input + "\n")
        print("Chatbot: Maaf kak, saya belum paham maksudnya. Boleh dijelaskan dengan kata lain?")

    else:
        print("Chatbot: Maaf, saya belum mengerti maksudnya 😅")
