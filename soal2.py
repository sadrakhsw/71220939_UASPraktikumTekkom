print ("===== Selamat Datang di XXV ====")
hari = input("Masukkan tanggal hari ini: ")

print("== Berikut genre film yang tersedia ==")
print("1. Horror")
print("2. Action")

harga=25000



a=int(input("silahkan pilih mau nonton film bergenre apa: "))

if a==3:
    print("Pilihan yang anda pilih tidak tersedia di bioskop ini")

print("== Pilihan film yang sedang tayang ==")



if a==1:
    print("1. The Devil's Light")
    print("2. Pengabdi Setan")
    c=int(input("Silahkan mau nonton film apa: "))
    if c==1:
        tiket=int(input("Mau memesan tiket sebanyak: "))
        print("total yang harus di bayar", tiket*harga)

    if c==2:
        tiket=int(input("Mau memesan tiket sebanyak: "))
        print("total yang harus di bayar", tiket*harga)



if a==2:
    print("1. Black Panther: Wakanda Forever")
    print("2. Avatar: The Way Of Water")
    b=int(input("Silahkan mau nonton film apa: "))
    if b==1:
        tiket=int(input("Mau memesan tiket sebanyak: "))
        print("total yang harus di bayar", tiket*harga)

    if b==2:
        tiket=int(input("Mau memesan tiket sebanyak: "))
        print("total yang harus di bayar", tiket*harga)











