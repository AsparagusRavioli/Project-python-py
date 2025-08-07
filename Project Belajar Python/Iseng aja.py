
data_monitor = '''
Monitor lg 
Monitor dell
Monitor Samsung
Monitor Philips
'''
monitor_dict = {
    1:"Monitor lg",
    2:"Monitor dell",
    3:"Monitor Samsung",
    4:"Monitor Philips"
}
daftar_monitor = []
print(data_monitor)

while(True):
    try:
        monitor = int(input("Masukan nomor komputer yang anda inginkan (1-4) : "))
    except:
        print("Maaf nomor yang anda masukan tidak ada, silahkan masukan lagi")
        continue
    
    if monitor in monitor_dict:
        komputer = monitor_dict[monitor]
        print(f"{komputer} akan dikirimkan ")
        daftar_monitor.append(komputer)
    else:
        print("Maaf nomor yang anda masukan salah")
        continue
    
    is_done = input("Apakah sudah selesai memesan? (y/n)? ")
    if is_done.lower() == "y":
        break

print("\nPesanan Anda:")
for i, item in enumerate(daftar_monitor, 1):
    print(f"{i}. {item}")


        
        
        
        
            