# Password Generator Python (Terminal)

Program ini adalah **pembuat sandi (password generator) sederhana berbasis terminal** menggunakan bahasa **Python**.  
Password dihasilkan secara acak dengan kombinasi **angka, huruf besar, huruf kecil, karakter spesial, dan kata acak**.

---

## Fitur Utama
- Kombinasi:
  - Angka (0–9)
  - Huruf besar (A–Z)
  - Huruf kecil (a–z)
  - Karakter spesial (!@#$%^&* dll)
  - Kata acak
- Password berbeda setiap kali dibuat
- Interaksi langsung melalui terminal
- Loop berulang hingga user memilih keluar
- Menggunakan modul `random`

---

## Cara Kerja Program
1. Program menampilkan pesan sambutan
2. User menekan **ENTER** untuk membuat sandi baru
3. Program akan:
   - Mengambil secara acak:
     - 2 angka
     - 2 huruf besar
     - 2 huruf kecil
     - 2 karakter spesial
     - 1 kata
   - Menggabungkan semua elemen
   - Mengacak urutan sandi
4. Password ditampilkan ke layar
5. Program berhenti jika user mengetik `exit` atau `keluar`

---

## Cara Menjalankan Program

### 1. Pastikan Python sudah terpasang
```bash
python --version
