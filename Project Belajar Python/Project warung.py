'''PROJECT WARUNG SEDERHANA ELIF'''

DATA_MENU = '''
1. Nasi Goreng
2. Kwetiau Goreng
3. Kwetiau Basah
4. Mie Goreng
5. Mie Kuah
6. Pancong Lumer
7. Kopi Susu
8. Es Teh Manis
'''

# Daftar menu sebagai dictionary untuk akses cepat
menu_dict = {
    1: "Nasi Goreng",
    2: "Kwetiau Goreng",
    3: "Kwetiau Basah",
    4: "Mie Goreng",
    5: "Mie Kuah",
    6: "Pancong Lumer",
    7: "Kopi Susu",
    8: "Es Teh Manis"
}

# Menyimpan pesanan
daftar_pesanan = []

print(DATA_MENU)

while True:
    try:
        menu = int(input("Masukkan nomor pesanan (1-8): "))
    except ValueError:
        print("Input harus berupa angka!")
        continue

    if menu in menu_dict:
        pesanan = menu_dict[menu]
        print(f"{pesanan} akan disiapkan")
        daftar_pesanan.append(pesanan)  # ✅ Menyimpan pesanan ke list
    else:
        print("Maaf, nomor pesanan salah. Silakan masukkan lagi.")
        continue

    is_done = input("Apakah sudah selesai memesan? (y/n)? ")
    if is_done.lower() == "y":
        break

# ✅ Menampilkan semua pesanan setelah selesai
print("\nPesanan Anda:")
for i, item in enumerate(daftar_pesanan, 1):
    print(f"{i}. {item}")
