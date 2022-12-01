print("========================")
print("operasi mataematika")

print("1.jumlah        [+]")
print("2.pengurangan   [-}")
print("3.perkalian     [*]")
print("4.pembagian     [/]")
print("========================")
operasi = input("pilih oprasi(1/2/3/4): ")
print("========================")
satu = eval(input("masukan bilangan pertama: "))
dua = eval(input("masukan bilangan kedua: "))
def penjumlahan(bil1,bil2):
    jumlah =bil1 + bil2
    return jumlah

def pengurangan(bil1,bil2):
    kurang =bil1 - bil2
    return kuarang

def perkalian(bil1,bil2):
    kali =bil1 * bil2
    return kali

def pembagian(bil1,bil2):
    bagi = bil1 / bil2
    return bagi
    
if pilih == "1":
    print("hasil operasi dari",bil1,"+",bil2,"=",penjumlahan(bil1,bil2))

elif pilih == "2":
    print("hasil operasi dari",bil1,"-",bil2,"=",pengurangan(bil1,bil2))

elif pilih == "3":
    print("hasil operasi dari",bil1,"*",bil2,"=",perkalian(bil1,bil2))

elif pilih == "4":
    print("hasil operasi dari",bil1,"/",bil2,"=",pembagian(bil1,bil2))
