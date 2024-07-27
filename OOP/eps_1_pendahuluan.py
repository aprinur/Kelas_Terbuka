"""
    Paradigma programming:

1. Structural/prosedural
2. Object-Oriented programming
    OOP dimasukkan untuk membuat pemrograman menjadi lebih mudah/fleksibel
3. dll

    Perbedaan antara structural dengan OOP:
Structural dieksekusi berdasarkan urutan

    Konsep OOP:
Semua dianggap object

* Untuk melakukan grouping objek yang sama maka digunakan template / class

contoh class ->                 hewan          tumbuhan
contoh object/instance ->  (kucing, anjing) (padi, jagung)

penggunaan object adalah agar masing masing object bisa saling berinteraksi kapanpun

Class dalam OOP adalah template maka akan memiliki atribut dan method
contoh atribut pada karakter game = nama, power, defence ( berupa tulisan )
contoh method pada karakter game = menyerang, bertahan, berjalan ( berupa tindakan)
contoh dalam kehidupan = motor(class) berwarna merah(atribut) berjalan maju(method)

pembuatan object pada OOP berdasarkan atribut dan method yang telah dibuat

* pada python class harus didefinisikan diatas/ sebelum program
"""


# Pembuatan Object

class Hero:  # Template/ class
    pass


hero1 = Hero()  # Object / instance
hero2 = Hero()
hero3 = Hero()

hero1.name = 'Udjang'  # atribut object
hero1.health = 100

hero2.name = 'Udcup'
hero2.health = 200

hero3.name = 'Otong'
hero3.health = 300

print(hero1)  # pengecekan apabila object sudah diletakkan pada memory
print(hero1.__dict__)  # mengakses keseluruhan atribut
print(hero1.name)  # mengakses object

