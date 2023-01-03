print ("===== Selamat Datang di XXV ====")
hari = input("Masukkan tanggal hari ini: ")

print("== Berikut genre film yang tersedia ==")
print("1. Horror")
print("2. Action")

harga=25000



a=int(input("silahkan pilih mau nonton film bergenre apa: "))

if a==1:
    tiket=int(input("Mau memesan tiket sebanyak: "))
    print("total yang harus di bayar", tiket*harga)

if a==3:
    print("Pilihan yang anda pilih tidak tersedia di bioskop ini")




