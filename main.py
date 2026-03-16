import random 
import banner

banner.main()

angka = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
Huruf = ["A", "B", "C", "D", "E", "F", "G",
         "H", "I", "J", "K", "L", "M",
         "N", "O", "P", "Q", "R", "S", "T",
         "U", "V", "W", "X", "Y", "Z"]
huruf = ["a", "b", "c", "d", "e", "f", "g",
         "h", "i", "j", "k", "l", "m", "n",
         "o", "p", "q", "r", "s", "t", "u",
         "v", "w", "x", "y", "z"]
karakter = ["!", "@", "#", "$", "%", "^", "&",
         "*", "(", ")", "-", "_", "=", "+", 
         "{", "}", "[", "]", "|", ";", ":", "'", 
         '"', "<", ">", ",", ".", "/", "?"]
kata = ["Misop", "necro@", "lutpi", "comel", 
        "nugini", "luber"]
print("Selamat datang di pembuat sandi!")
print("Ketik 'exit' atau 'keluar' untuk berhenti.\n")

while True:
    perintah = input("Tekan ENTER untuk membuat " \
    "sandi baru atau ketik 'exit': ").strip().lower()
    
    if perintah in ["exit", "keluar"]:
        print("Terima kasih! Program selesai.")
        break

    ambil_angka = random.sample(angka, 2)
    ambil_Huruf = random.sample(Huruf, 2)
    ambil_huruf = random.sample(huruf, 2)
    ambil_karakter = random.sample(karakter, 2)
    ambil_kata = random.sample(kata, 1)

    sandi = ambil_kata + ambil_angka + ambil_Huruf + ambil_huruf + ambil_karakter 
    # random.shuffle(sandi)
    sandi_str = ''.join(str(i) for i in sandi)

    print("Sandi kamu:", sandi_str)
    print("-" * 30)

