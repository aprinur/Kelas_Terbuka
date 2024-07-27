"""
    Empat Konsep Dasar dalam OOP:

    1. Enkapsulasi (Encapsulation)
    2. Abstraksi (Abstaction)
    3. Pewarisan (Inheritance)
    4. Polimorfisme (Polimorphism)



        Encapsulasi

    Encapsulasi  merujuk pada konsep menggabungkan data(atribut) dan perilaku(method) yang
    beroperasi pada data tersebut dalam satu unit yaitu class. Selain itu, enkapsulasi juga
    mengendalikan akses ke data tersebut untuk menjaga keamanan dan integritas, biasanya dengan
    menggunakan modifier akses seperti private, protected dan public.

    Tujuan enkapsulasi
    - Menyembunyikan Detail Implementasi
        * Pengguna kelas tidak perlu mengetahui detail implementasi internal dari kelas tersebut.
          Mereka hanya perlu tahu bagaimana cara menggunakannya.
        * Ini membantu mengurangi kompleksitas dan meningkatkan modularitas kode.

    - Pengendalian Akses
        * Dengan enkapsulasi, akses ke data dapat dikendalikan dan dibatasi. Ini melindungi data
          dari perubahan yang tidak diinginkan atau tidak disengaja.
        * Modifier akses seperti private dan protected digunakan untuk mencapai tujuan ini.

    - Memfasilitasi Pemeliharaan dan Pembaruan
        * Enkapsulasi mempermudah pemeliharaan kode karena perubahan pada implementasi internal
          kelas tidak mempengaruhi kode yang menggunakan kelas tersebut, selama antarmuka publik
          tetap konsisten.
"""

"""
    Aturan Encapsulasi:
    1. buat semua variabel private
    2. menggunakan getter dan setter
    getter = fungsi/method untuk mengambil nilai variabel
    setter = fungsi/method untuk mengubah nilai variabel
"""


# Contoh enkapsulasi:
class Hero:

    def __init__(self, name, health, attackPower):
        self.__name = name
        self.__health = health
        self.__attackPower = attackPower

    # method getter
    def getname(self):
        return self.__name

    def gethealth(self):
        return self.__health

    # setter
    def diserang(self, serangPower):
        self.__health -= serangPower

    def setattpower(self, nilaibaru):
        self.__attackPower = nilaibaru


# awal dari game
udcup = Hero('Udcup', 100, 10)

print(udcup.__dict__)  # key yang keluar adalah private
# print(udcup.__name)  tidak bisa dilakukan karena __name adalah private variable

# game berjalan
print(udcup.getname())  # cara mendapatkan nilai nama dengan getter
print(udcup.gethealth())  # cara mendapatkan nilai health dengan getter
udcup.diserang(10)  # mengubah nilai dengan setter
print(udcup.gethealth())
udcup.diserang(30)
print(udcup.gethealth())

