import random  # Mengimpor modul random untuk menghasilkan nilai acak
import string  # Mengimpor modul string untuk mendapatkan kumpulan karakter alfabet

def random_string(panjang: int) -> str:  # Fungsi untuk membuat string acak sepanjang 'panjang'
    hasil_string = ''.join(               # Menggabungkan karakter-karakter acak menjadi satu string
        random.choice(string.ascii_letters)  # Memilih satu karakter secara acak dari huruf A-Z dan a-z
        for i in range(panjang)              # Melakukan pengulangan sebanyak 'panjang' kali
    )
    return hasil_string  # Mengembalikan hasil string acak
