def luas_segitiga():
    a = int(input("Masukan alas segitiga:"))
    t = int(input("Masukan tinggi segitiga:"))
    luas = a * t / 2
    print("Luas segitiga adalah: ", luas)

luas_segitiga()

def luas_persegi_panjang():
    p = int(input("Masukan panjang persegi panjang:"))
    l = int(input("Masukan lebar persegi panjang:"))
    luas = p * l
    print("Luas Persegi Panjang adalah: ", luas)

luas_persegi_panjang()

#Hitung Luas Lingkaran
def luas_lingkaran():
    r = int(input("Masukan jari-jari lingkaran:"))
    luas = 3.14 * r * r
    print("Luas Lingkaran adalah: ", luas)
    
luas_lingkaran()
