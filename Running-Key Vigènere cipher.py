# Fungsi Enkripsi Menggunakan Running key vigenere cipher
def running_key_vigenere_encrypt(plain_text, key):
    encrypted_text = ""
    key_length = len(key)

#  Melakukan perulangan pada setiap karakter dalam inputan
    for i in range(len(plain_text)):
        char = plain_text[i]
        if char.isalpha():
            key_char = key[i % key_length].lower()
            key_shift = ord(key_char) - ord('a')
            if char.isupper():
                encrypted_char = chr(((ord(char) - ord('A') + key_shift) % 26) + ord('A'))
            else:
                encrypted_char = chr(((ord(char) - ord('a') + key_shift) % 26) + ord('a'))
            encrypted_text += encrypted_char
        else:
            encrypted_text += char

    return encrypted_text

# Fungsi Dnkripsi Menggunakan Running key vigenere cipher
def running_key_vigenere_decrypt(encrypted_text, key):
    decrypted_text = ""
    key_length = len(key)

#  Melakukan perulangan pada setiap karakter dalam inputan
    for i in range(len(encrypted_text)):
        char = encrypted_text[i]
        if char.isalpha():
            key_char = key[i % key_length].lower()
            key_shift = ord(key_char) - ord('a')
            if char.isupper():
                decrypted_char = chr(((ord(char) - ord('A') - key_shift + 26) % 26) + ord('A'))
            else:
                decrypted_char = chr(((ord(char) - ord('a') - key_shift + 26) % 26) + ord('a'))
            decrypted_text += decrypted_char
        else:
            decrypted_text += char

    return decrypted_text

def main():
    while True:
        choice = input("Pilih operasi \n 1 Enkripsi \n 2 Dekripsi  \n 3 Exit \n ")
        
        if choice == '1':
            plain_text = input("Masukkan Teks : ")
            key = input("Masukkan Kunci: ")
            encrypted_text = running_key_vigenere_encrypt(plain_text, key)
            print("Teks terenkripsi:", encrypted_text)
        elif choice == '2':
            encrypted_text = input("Masukkan Teks : ")
            key = input("Masukkan Kunci: ")
            decrypted_text = running_key_vigenere_decrypt(encrypted_text, key)
            print("Teks terdekripsi:", decrypted_text)
        elif choice == '3':
            print("Terima kasih :).")
            break
        else:
            print("ERROR 404")

if __name__ == "__main__":
    main()
