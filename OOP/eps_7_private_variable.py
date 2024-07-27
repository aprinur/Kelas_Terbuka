class Hero:
    # contoh class variable
    jumlah = 0

    def __init__(self, name, health):
        # public variable
        self.name = name
        self.health = health

        # private variable diawali dengan dua underscore '__'
        self.__private = 'private variable "_"'

        # protected variable diawali dengan satu underscore '_'
        self._protected = 'protected variable "__"'


rey = Hero('rey', 100)

print(rey.__dict__)
# print(rey.__private) variable private tidak bisa diakses
print(rey._protected)  # meski protected variable bisa diakses dari luar tapi tidak disarankan

"""
    variabel private dan variabel protected digunakan untuk 
    mengontrol akses ke atribut dan metode dalam sebuah kelas, ini membantu dalam memastikan 
    enkapsulasi
    
    
    - Private variable
    Adalah atribut atau method yang tidak dapat diakses langsung dari luar kelas. Dalam python
    private variable ditandai dengan dua underscore '__' diawal nama variabel
    
    Tujuan:
    * Enkapsulasi : menyembunyikan detail internal dari sebuah kelas/class
    * Keamanan : melindungi data dari perubahan yang tidak diinginkan atau tidak disengaja
    
    
    - Protected variabel
    Adalah atribut atau method yang dimaksudkan untuk digunakan dalam class itu sendiri atau 
    subclassnya, tetapi tidak seharusnya diakses dari luar. Dalam python, protected variable 
    ditandai dengan satu underscore '_' diawal nama variabel
    
    Tujuan:
    * Enkapsulasi parsial : melindungi data sambil tetap memungkinkan akses dalam hierarki 
    pewarisan
    * Pedoman : menginformasikan kepada pengguna kelas bahwa atribut ini seharusnya tidak 
    diakses dari luar kelas atau subkelasnya
    
    
    - Kesimpulan  
    Private Variable:
    * Ditandai dengan dua underscore (__) di awal nama.
    * Tidak dapat diakses langsung dari luar kelas.
    * Digunakan untuk enkapsulasi penuh dan keamanan data.
    
    Protected Variable:
    * Ditandai dengan satu underscore (_) di awal nama.
    * Dimaksudkan untuk digunakan dalam kelas itu sendiri dan subkelasnya.
    * Tidak seharusnya diakses dari luar kelas atau subkelasnya, meskipun tidak sepenuhnya 
      dibatasi oleh Python.
"""