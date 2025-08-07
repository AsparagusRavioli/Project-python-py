from . import Operasi  # Mengimpor modul Operasi dari folder/module yang sama

DB_NAME = "data.txt"  # Nama file database tempat menyimpan data buku

TEMPLATE = {  # Template struktur data buku
    "pk": "XXXXXX",  # Primary key (unik) default
    "date_add": "yyyy-mm-dd",  # Tanggal penambahan data
    "judul": 255 * " ",  # Alokasi 255 karakter kosong untuk judul (biar seragam panjangnya)
    "penulis": 255 * " ",  # Alokasi 255 karakter kosong untuk penulis
    "tahun": "yyyy"  # Tahun terbit (format: 4 digit)
}

def init_console():  # Fungsi untuk inisialisasi program: cek apakah database sudah ada
    try:
        with open(DB_NAME, "r") as file:  # Mencoba membuka file database
            print("Database tersedia, init done!")  # Jika berhasil, tampilkan pesan bahwa database sudah ada
    except:  # Jika file tidak ditemukan atau error
        print("Database tidak ditemukan, silahkan membuat database baru")  #
