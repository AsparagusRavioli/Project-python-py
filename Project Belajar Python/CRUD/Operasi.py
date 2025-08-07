from time import time  # Import fungsi time dari modul time
from . import Database  # Import modul Database dari package yang sama
from .Util import random_string  # Import fungsi random_string dari modul Util
import time  # Import seluruh modul time
import os  # Import modul os untuk manipulasi file

# Fungsi untuk menghapus data berdasarkan nomor buku
def delete(no_buku):
    try:
        with open(Database.DB_NAME, mode="r", encoding="utf-8") as file:  # Buka file database untuk dibaca
            lines = file.readlines()  # Baca seluruh baris ke dalam list

        if no_buku < 1 or no_buku > len(lines):  # Validasi nomor buku
            print("Nomor buku tidak valid.")
            return

        if os.path.exists("data_temp.txt"):  # Hapus file sementara jika sudah ada
            os.remove("data_temp.txt")

        with open("data_temp.txt", mode="w", encoding="utf-8") as temp_file:  # Buat file sementara untuk data baru
            for index, line in enumerate(lines):  # Loop semua data
                if index != no_buku - 1:  # Tulis ulang semua data kecuali yang dihapus
                    temp_file.write(line)

        if os.path.exists(Database.DB_NAME):  # Hapus file database lama
            os.remove(Database.DB_NAME)

        os.rename("data_temp.txt", Database.DB_NAME)  # Ganti nama file sementara menjadi file database
        print("Data berhasil dihapus.")

    except Exception as e:
        print(f"Terjadi kesalahan saat menghapus: {e}")  # Tangani error

# Fungsi untuk mengupdate data berdasarkan nomor buku
def update(no_buku, pk, data_add, judul, penulis, tahun):
    data = Database.TEMPLATE.copy()  # Salin template

    data["pk"] = pk  # Isi primary key
    data["date_add"] = data_add  # Isi tanggal tambah
    data["penulis"] = penulis + Database.TEMPLATE["penulis"][len(penulis):]  # Format penulis
    data["judul"] = judul + Database.TEMPLATE["judul"][len(judul):]  # Format judul
    data["tahun"] = str(tahun)  # Tahun diubah ke string

    data_str = f'{data["pk"]},{data["date_add"]},{data["penulis"]},{data["judul"]},{data["tahun"]}\n'  # Gabungkan data ke string

    try:
        with open(Database.DB_NAME, mode="r", encoding="utf-8") as file:  # Buka database
            lines = file.readlines()  # Baca semua baris

        if 0 < no_buku <= len(lines):  # Validasi nomor buku
            lines[no_buku - 1] = data_str  # Ganti baris yang sesuai
            with open(Database.DB_NAME, mode="w", encoding="utf-8") as file:  # Tulis ulang database
                file.writelines(lines)
            print("Data berhasil diupdate!")
        else:
            print("Nomor buku tidak valid")
    except Exception as e:
        print(f"Terjadi kesalahan saat update: {e}")

# Fungsi untuk menambahkan data baru
def create(tahun, judul, penulis):
    data = Database.TEMPLATE.copy()  # Salin template

    data["pk"] = random_string(6)  # Buat pk random
    data["date_add"] = time.strftime("%Y-%m-%d-%H-%M-%S%z", time.gmtime())  # Tanggal otomatis
    data["penulis"] = penulis + Database.TEMPLATE["penulis"][len(penulis):]  # Format penulis
    data["judul"] = judul + Database.TEMPLATE["judul"][len(judul):]  # Format judul
    data["tahun"] = str(tahun)  # Format tahun

    data_str = f'{data["pk"]},{data["date_add"]},{data["penulis"]},{data["judul"]},{data["tahun"]}\n'  # Gabungkan data

    try:
        with open(Database.DB_NAME, 'a', encoding="utf-8") as file:  # Tambah data ke file
            file.write(data_str)
    except:
        print("Data tidak ditambahkan, penambahan data gagal")

# Fungsi untuk membuat data awal jika belum ada database
def create_first_data():
    penulis = input("Penulis: ")  # Input penulis
    judul = input("Judul: ")  # Input judul
    while True:
        try:
            tahun = int(input("Tahun\t: "))  # Input tahun
            if len(str(tahun)) == 4:  # Validasi 4 digit
                break
            else:
                print("Tahun harus 4 digit, format (yyyy)")
        except:
            print("Tahun harus angka! Coba lagi.")

    data = Database.TEMPLATE.copy()  # Salin template

    data["pk"] = random_string(6)  # Buat pk random
    data["date_add"] = time.strftime("%Y-%m-%d-%H-%M-%S%z", time.gmtime())  # Tanggal otomatis
    data["penulis"] = penulis + Database.TEMPLATE["penulis"][len(penulis):]  # Format penulis
    data["judul"] = judul + Database.TEMPLATE["judul"][len(judul):]  # Format judul
    data["tahun"] = str(tahun)  # Tahun string

    data_str = f'{data["pk"]},{data["date_add"]},{data["penulis"]},{data["judul"]},{data["tahun"]}\n'  # Gabungkan string
    print(data_str)  # Cetak hasil

    try:
        with open(Database.DB_NAME, 'w', encoding="utf-8") as file:  # Tulis ke database baru
            file.write(data_str)
    except:
        print("Gagal membuat database pertama")

# Fungsi untuk membaca data dari database
def read(**kwargs):
    try:
        with open(Database.DB_NAME, 'r') as file:  # Buka database
            content = file.readlines()  # Baca semua baris
            jumlah_buku = len(content)  # Hitung jumlah baris
            print(f"Jumlah buku : {jumlah_buku}")  # Tampilkan jumlah buku
            if "index" in kwargs:  # Jika index diminta
                index_buku = kwargs["index"] - 1
                if index_buku < 0 or index_buku >= jumlah_buku:  # Cek valid
                    return False
                else:
                    return content[index_buku]  # Kembalikan satu baris
            else:
                return content  # Kembalikan semua
    except:
        print("Membaca database error")  # Tangani error
        return False
