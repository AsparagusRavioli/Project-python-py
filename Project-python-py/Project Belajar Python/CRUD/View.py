from . import Operasi

def update_console():
    read_console()
    while True:
        print("Silahkan pilih nomor buku yang ingin di update")
        try:
            no_buku = int(input("Nomor buku: "))
        except ValueError:
            print("Harus angka, coba lagi!")
            continue

        data_buku = Operasi.read(index=no_buku)
        
        if data_buku:
            data_break = data_buku.strip().split(",")
            if len(data_break) < 5:
                print("Data buku tidak lengkap, tidak bisa diupdate.")
                return
            break
        else:
            print("Nomor tidak valid, silakan masukkan ulang.")

    pk = data_break[0]
    data_add = data_break[1]
    penulis = data_break[2]
    judul = data_break[3]
    tahun = data_break[4].strip()  # hapus newline

    while True:
        print("\n\n" + "="*100)
        print("Silahkan pilih data yang ingin anda update")
        print(f"1. Judul  : {judul:.40}")
        print(f"2. Penulis: {penulis:.40}")
        print(f"3. Tahun  : {tahun:.4}")

        user_option = input("Pilih data [1,2,3]: ")
        print("\n" + "="*100)

        match user_option:
            case "1":
                judul = input("Judul baru: ")
            case "2":
                penulis = input("Penulis baru: ")
            case "3":
                while True:
                    try:
                        tahun_input = int(input("Tahun baru (yyyy): "))
                        if len(str(tahun_input)) == 4:
                            tahun = str(tahun_input)
                            break
                        else:
                            print("Tahun harus 4 digit (yyyy)!")
                    except:
                        print("Input harus angka!")
            case _:
                print("Pilihan tidak valid.")
                
                
        print("data baru anda")
        print(f"1. Judul  : {judul:.40}")
        print(f"2. Penulis: {penulis:.40}")
        print(f"3. Tahun  : {tahun:.4}")
        is_done = input("Apakah selesai update (y/n)? ")
        if is_done.lower() == "y":
            break

    Operasi.update(no_buku, pk, data_add, judul, penulis, tahun)

def create_console():
    print("\n\n" + "="*100)
    print("Silahkan tambah data buku\n")

    penulis = input("Penulis: ")
    judul = input("Judul  : ")

    while True:
        try:
            tahun = int(input("Tahun  : "))
            if len(str(tahun)) == 4:
                break
            else:
                print("Tahun harus 4 digit (yyyy)!")
        except:
            print("Tahun harus angka!")

    Operasi.create(tahun, judul, penulis)
    print("\nBerikut adalah data baru anda:")
    Operasi.read()

def read_console():
    data_file = Operasi.read()

    index_header = "No"
    judul_header = "Judul"
    penulis_header = "Penulis"
    tahun_header = "Tahun"

    print("\n" + "="*100)
    print(f"{index_header:4} | {judul_header:40} | {penulis_header:40} | {tahun_header:5}")
    print("-"*100)

    for index, data in enumerate(data_file):
        data_break = data.strip().split(",")

        # Skip jika data tidak lengkap
        if len(data_break) < 5:
            continue

        pk = data_break[0]
        date_add = data_break[1]
        penulis = data_break[2]
        judul = data_break[3]
        tahun = data_break[4].strip()

        print(f"{index+1:4} | {judul:.40} | {penulis:.40} | {tahun:4}")

    print("="*100 + "\n")
