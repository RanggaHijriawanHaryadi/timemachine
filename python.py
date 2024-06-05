import base64

# Encode pesan menggunakan Base64
encoded_message = base64.b64encode(b'cGljb0NURnt0MW0zbUAjaDFuM18xODZjZDdkN30=').decode()

def reveal_message(encoded_message):
    decoded_bytes = base64.b64decode(encoded_message.encode())
    secret_message = base64.b64decode(decoded_bytes).decode()
    return secret_message

while True:
    # Minta pengguna untuk memasukkan dua angka untuk perkalian
    num1 = int(input("Masukkan angka pertama: "))
    if num1 != 7:
        if num1 < 7:
            print("Bilangan pertama kurang besar.")
       
        else:
            print("Bilangan pertama kurang kecil.")
        continue

    num2 = int(input("Masukkan angka kedua: "))
    if num2 != 10:
        if num2 < 10:
            print("Bilangan kedua kurang besar.")
       
        else:
            print("Bilangan kedua kurang kecil.")
        continue

    # Menghitung hasil perkalian
    user_answer = num1 * num2

    # Periksa apakah hasil perkalian adalah 70
    if user_answer == 70:
        print(f"Encoded message: {reveal_message(encoded_message)}")
        break
    else:
        print("Jawaban salah atau tidak sesuai, coba lagi.")
