# Data siswa disimpan dalam bentuk string multiline
data_siswa1 = '''
Nama   : Farel
Kelas  : 12
Tinggi : 190 cm
Berat  : 70 kg
'''
data_siswa2 = '''
Nama   : fino
Kelas  : 9 
Tinggi : 170 cm
Berat  : 45 kg
'''
data_siswa3 = '''
Nama   : oyen
Kelas  : 1
Tinggi : 80 cm
Berat  : 10 kg
'''
data_siswa4 = '''
Nama   : Anya
Kelas  : 12
Tinggi : 155 cm
Berat  : 46 kg
'''

# Program berjalan terus-menerus sampai pengguna keluar
while True:
    try:
        siswa = int(input("Masukkan nomor siswa (1-4): "))  # Meminta input angka
    except ValueError:
        print("Input harus berupa angka!")  # Menangani input selain angka
        continue

    if siswa == 1:
        print(f"\nData Siswa yang anda cari:\n{data_siswa1}")  # Menampilkan data siswa 1
    elif siswa == 2:
        print(f"\nData Siswa yang anda cari:\n{data_siswa2}")  
    elif siswa == 3:
        print(f"\nData Siswa yang anda cari:\n{data_siswa3}")  
    elif siswa == 4:
        print(f"\nData Siswa yang anda cari:\n{data_siswa4}")  
    else:
        print("Data yang anda cari tidak ada, silakan masukkan ulang.")  # Jika input selain 1/2
        continue

    # Konfirmasi apakah ingin lanjut
    is_done = input("Apakah ingin mencari data lain? (y/n): ")
    if is_done.lower() == "n":
        break  # Keluar dari loop jika pengguna selesai

print("Terima kasih telah menggunakan program data siswa!")
