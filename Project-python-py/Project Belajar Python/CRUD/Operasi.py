from time import time
from . import Database
from .Util import random_string
import time

def update(no_buku, pk, data_add, judul, penulis, tahun):
    data = Database.TEMPLATE.copy()

    data["pk"] = pk
    data["date_add"] = data_add
    data["penulis"] = penulis + Database.TEMPLATE["penulis"][len(penulis):]
    data["judul"] = judul + Database.TEMPLATE["judul"][len(judul):]
    data["tahun"] = str(tahun)

    data_str = f'{data["pk"]},{data["date_add"]},{data["penulis"]},{data["judul"]},{data["tahun"]}\n'

    try:
        # Baca semua data
        with open(Database.DB_NAME, mode="r", encoding="utf-8") as file:
            lines = file.readlines()

        # Cek validitas index
        if 0 < no_buku <= len(lines):
            lines[no_buku - 1] = data_str
            # Tulis ulang seluruh data
            with open(Database.DB_NAME, mode="w", encoding="utf-8") as file:
                file.writelines(lines)
            print("Data berhasil diupdate!")
        else:
            print("Nomor buku tidak valid")
    except Exception as e:
        print(f"Terjadi kesalahan saat update: {e}")


def create(tahun, judul, penulis):
    data = Database.TEMPLATE.copy()

    data["pk"] = random_string(6)
    data["date_add"] = time.strftime("%Y-%m-%d-%H-%M-%S%z", time.gmtime())
    data["penulis"] = penulis + Database.TEMPLATE["penulis"][len(penulis):]
    data["judul"] = judul + Database.TEMPLATE["judul"][len(judul):]
    data["tahun"] = str(tahun)

    data_str = f'{data["pk"]},{data["date_add"]},{data["penulis"]},{data["judul"]},{data["tahun"]}\n'

    try:
        with open(Database.DB_NAME, 'a', encoding="utf-8") as file:
            file.write(data_str)
    except:
        print("Data tidak ditambahkan, penambahan data gagal")


def create_first_data():
    penulis = input("Penulis: ")
    judul = input("Judul: ")
    while True:
        try:
            tahun = int(input("Tahun\t: "))
            if len(str(tahun)) == 4:
                break
            else:
                print("Tahun harus 4 digit, format (yyyy)")
        except:
            print("Tahun harus angka! Coba lagi.")

    data = Database.TEMPLATE.copy()

    data["pk"] = random_string(6)
    data["date_add"] = time.strftime("%Y-%m-%d-%H-%M-%S%z", time.gmtime())
    data["penulis"] = penulis + Database.TEMPLATE["penulis"][len(penulis):]
    data["judul"] = judul + Database.TEMPLATE["judul"][len(judul):]
    data["tahun"] = str(tahun)

    data_str = f'{data["pk"]},{data["date_add"]},{data["penulis"]},{data["judul"]},{data["tahun"]}\n'
    print(data_str)

    try:
        with open(Database.DB_NAME, 'w', encoding="utf-8") as file:
            file.write(data_str)
    except:
        print("Gagal membuat database pertama")


def read(**kwargs):
    try:
        with open(Database.DB_NAME, 'r') as file:
            content = file.readlines()
            jumlah_buku = len(content)
            print(f"Jumlah buku : {jumlah_buku}")
            if "index" in kwargs:
                index_buku = kwargs["index"] - 1
                if index_buku < 0 or index_buku >= jumlah_buku:
                    return False
                else:
                    return content[index_buku]
            else:
                return content
    except:
        print("Membaca database error")
        return False
