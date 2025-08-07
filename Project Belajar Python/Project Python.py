import os                            # Import modul os untuk berinteraksi dengan sistem operasi
import CRUD as CRUD                 # Import modul CRUD (Create, Read, Update, Delete)

if __name__ == "__main__":         # Mengecek apakah file ini dijalankan langsung, bukan diimpor
    sistem_operasi = os.name       # Mengambil nama sistem operasi (nt untuk Windows, posix untuk Linux/Mac)

    match sistem_operasi:          # Membersihkan terminal sesuai sistem operasi
        case "posix": os.system("clear")  # Linux/Mac
        case "nt": os.system("cls")      # Windows

    print("SELAMAT DATANG DI PROGRAM")  # Tampilkan header program
    print("DATABASE PERPUSTAKAAN")
    print("=========================")

    CRUD.init_console()            # Mengecek apakah database sudah ada, jika belum maka dibuat

    while(True):                   # Loop utama program
        match sistem_operasi:      # Bersihkan layar setiap awal loop
            case "posix": os.system("clear")
            case "nt": os.system("cls")
        
        print("SELAMAT DATANG DI PROGRAM")  # Tampilkan ulang menu
        print("DATABASE PERPUSTAKAAN")
        print("=========================")

        print(f"1. Read Data")     # Opsi baca data
        print(f"2. Create Data")   # Opsi tambah data
        print(f"3. Update Data")   # Opsi ubah data
        print(f"4. Delete Data\n") # Opsi hapus data

        user_option = input("Masukan opsi: ")  # Ambil input user untuk memilih menu

        match user_option:         # Pilih fungsi berdasarkan input user
            case "1": CRUD.read_console()     # Baca data
            case "2": CRUD.create_console()   # Tambah data
            case "3": CRUD.update_console()   # Ubah data
            case "4": CRUD.delete_console()   # Hapus data

        is_done = input("Apakah Selesai (y/n)? ")  # Tanya apakah user ingin keluar
        if is_done == "y" or is_done == "Y":
            break                                # Keluar dari program jika user jawab y

    print("Program Berakhir, Terima Kasiih friends")  # Pesan penutup
