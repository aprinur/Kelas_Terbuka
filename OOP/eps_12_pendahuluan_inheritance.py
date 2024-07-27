""""""
""" 
    Inheritance 

        Inheritance adalah mekanisme dalam OOP yang memungkinkan kelas baru untuk mewarisi 
    sifat/atribut dan perilaku/method dari kelas/class yang sudah ada. Inheritance belaku antar
    class. Salah satu fungsi inheritance adalah menghindari perulangan pada program
        
    Tujuan Inheritance
    - Reuse         : Meningkatkan penggunaan kembali kode dengan mewarisi atribut dan metode dari 
                      kelas induk
    - Hierarchy     : Membentuk hierarki kelas yang terstruktur dengan baik
    - Extensibility : Memperluas fungsionalitas kelas induk dengan menambahkan atau mengubah 
                      perilaku di kelas turunan
                      
    Jenis Inheritance 
    1. Single Inheritance
        Kelas turunan mewarisi dari satu kelas induk
    2. Multiple Inheritance
        Kelas turunan mewarisi lebih dari satu kelas induk
    3. Multilevel Inheritance
        Kelas turunan mewarisi dari kelas induk yang juga merupakan kelas turunan dari kelas lain
    4. Hierarchial Inheritance
        Beberapa kelas turunan mewarisi dari satu kelas induk 
"""


# Contoh Inheritance
class Hero:  # sebagai superclass

    def __init__(self, name, health):
        self.name = name
        self.health = health


class Hero_Intelegance(Hero):  # subclass
    pass
    # superclass diwariskan ke subclass dengan cara memasukkan nama superclass sebagai
    # parameter pada subclass.


class Hero_Strength(Hero):  # subclassN
    pass


udjang = Hero('udjang', 100)
# objek baru yang diwarisi diisi parameter yang sama dari superclass
otong = Hero_Intelegance('otong', 100)
dudung = Hero_Strength('dudung', 100)

print(udjang.name)
print(otong.name)

# mengecek inheritance
print(help(otong))
