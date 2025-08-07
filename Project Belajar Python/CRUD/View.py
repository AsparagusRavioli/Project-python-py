from . import Operasi  # Mengimpor modul Operasi dari folder yang sama

# Fungsi untuk menghapus data buku dari database
def delete_console():
    read_console()  # Menampilkan seluruh data buku
    while True:
        print("Silahkan pilih nomor buku yang ingin di delete")
        try:
            no_buku = int(input("Nomor buku: "))  # Meminta input nomor buku
        except ValueError:  # Menangani jika input bukan angka
            print("Harus angka, coba lagi!")
            continue

        data_buku = Operasi.read(index=no_buku)  # Membaca data buku berdasarkan index
        
        if data_buku:
            data_break = data_buku.strip().split(",")  # Memisahkan data menjadi list
            pk = data_break[0]  # Primary key
            data_add = data_break[1]  # Tanggal data ditambahkan
            penulis = data_break[2]  # Nama penulis
            judul = data_break[3]  # Judul buku
            tahun = data_break[4].strip()  # Tahun terbit, menghapus newline

            print("\n\n" + "="*100)
            print("Silahkan pilih data yang ingin anda hapus")
            print(f"1. Judul  : {judul:.40}")  # Menampilkan judul
            print(f"2. Penulis: {penulis:.40}")  # Menampilkan penulis
            print(f"3. Tahun  : {tahun:.4}")  # Menampilkan tahun
            is_done = input("Apakah data yakin ingin di hapus? (y/n)? ")  # Konfirmasi
            if is_done.lower() == "y":
                Operasi.delete(no_buku)  # Hapus data jika "y"
                break
        else:
            print("Nomor tidak valid, silakan masukkan ulang.")
              
    print("data berhasil dihapus")  # Konfirmasi data telah dihapus
   

# Fungsi untuk mengubah data buku
def update_console():
    read_console()  # Menampilkan seluruh data buku
    while True:
        print("Silahkan pilih nomor buku yang ingin di update")
        try:
            no_buku = int(input("Nomor buku: "))  # Input nomor buku
        except ValueError:
            print("Harus angka, coba lagi!")  # Validasi input
            continue

        data_buku = Operasi.read(index=no_buku)  # Membaca data berdasarkan index
        
        if data_buku:
            data_break = data_buku.strip().split(",")
            if len(data_break) < 5:
                print("Data buku tidak lengkap, tidak bisa diupdate.")
                return  # Keluar dari fungsi jika data tidak lengkap
            break
        else:
            print("Nomor tidak valid, silakan masukkan ulang.")

    pk = data_break[0]  # Primary key
    data_add = data_break[1]  # Tanggal ditambahkan
    penulis = data_break[2]  # Penulis lama
    judul = data_break[3]  # Judul lama
    tahun = data_break[4].strip()  # Tahun lama

    while True:
        print("\n\n" + "="*100)
        print("Silahkan pilih data yang ingin anda update")
        print(f"1. Judul  : {judul:.40}")
        print(f"2. Penulis: {penulis:.40}")
        print(f"3. Tahun  : {tahun:.4}")

        user_option = input("Pilih data [1,2,3]: ")  # Memilih data yang ingin diubah
        print("\n" + "="*100)

        match user_option:  # Menggunakan match-case untuk pilihan user
            case "1":
                judul = input("Judul baru: ")  # Update judul
            case "2":
                penulis = input("Penulis baru: ")  # Update penulis
            case "3":
                while True:
                    try:
                        tahun_input = int(input("Tahun baru (yyyy): "))  # Input tahun baru
                        if len(str(tahun_input)) == 4:  # Validasi tahun 4 digit
                            tahun = str(tahun_input)
                            break
                        else:
                            print("Tahun harus 4 digit (yyyy)!")
                    except:
                        print("Input harus angka!")
            case _:
                print("Pilihan tidak valid.")  # Jika pilihan tidak ada
                
        print("data baru anda")
        print(f"1. Judul  : {judul:.40}")
        print(f"2. Penulis: {penulis:.40}")
        print(f"3. Tahun  : {tahun:.4}")
        is_done = input("Apakah selesai update (y/n)? ")  # Konfirmasi selesai update
        if is_done.lower() == "y":
            break

    Operasi.update(no_buku, pk, data_add, judul, penulis, tahun)  # Proses update data


# Fungsi untuk menambahkan data baru
def create_console():
    print("\n\n" + "="*100)
    print("Silahkan tambah data buku\n")

    penulis = input("Penulis: ")  # Input penulis
    judul = input("Judul  : ")  # Input judul

    while True:
        try:
            tahun = int(input("Tahun  : "))  # Input tahun
            if len(str(tahun)) == 4:  # Validasi tahun 4 digit
                break
            else:
                print("Tahun harus 4 digit (yyyy)!")
        except:
            print("Tahun harus angka!")

    Operasi.create(tahun, judul, penulis)  # Menyimpan data ke file
    print("\nBerikut adalah data baru anda:")
    Operasi.read()  # Menampilkan data setelah ditambah


# Fungsi untuk membaca dan menampilkan semua data
def read_console():
    data_file = Operasi.read()  # Membaca semua data

    index_header = "No"
    judul_header = "Judul"
    penulis_header = "Penulis"
    tahun_header = "Tahun"

    print("\n" + "="*100)
    print(f"{index_header:4} | {judul_header:40} | {penulis_header:40} | {tahun_header:5}")
    print("-"*100)

    for index, data in enumerate(data_file):  # Looping setiap baris data
        data_break = data.strip().split(",")

        # Skip jika data tidak lengkap
        if len(data_break) < 5:
            continue

        pk = data_break[0]  # Primary key
        date_add = data_break[1]  # Tanggal dibuat
        penulis = data_break[2]  # Penulis
        judul = data_break[3]  # Judul
        tahun = data_break[4].strip()  # Tahun

        print(f"{index+1:4} | {judul:.40} | {penulis:.40} | {tahun:4}")  # Cetak setiap baris

    print("="*100 + "\n")  # Penutup
