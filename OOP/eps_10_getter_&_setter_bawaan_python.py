class Hero:

    def __init__(self, name, health, armor):
        self.__name = name
        self.__health = health
        self.__armor = armor
        # salah satu cara menampilkan private variable
        # self.info = 'name {} : \n\thealth: {}'.format(self.__name, self.__health)
        self.__info = 'name {} : \n\thealth: {}'.format(self.__name, self.__health)

    # getter tanpa fungsi bawaan python
    def gethealth(self):
        return self.__health

    # getter dengan fungsi bawaan python
    @property  # berfungi merubah sebuah method menjadi seperti variable
    def info(self):  # method info dianggap variable
        return 'name {} : \n\thealth: {}'.format(self.__name, self.__health)

    @property
    def info1(self):
        return self.__info
        # cara lainnya adalah dengan membuat private variabel ( contoh diatas adalah '__info'),
        # lalu mereturnnya pada method yang dibuat pada decorator property.

    @property  # pendefinisian fungsi sebagai property sebelum getter dan setter
    def armor(self):
        pass

    @armor.getter
    def armor(self):
        return self.__armor

    @armor.setter
    def armor(self, input_user):
        self.armor = input_user


sniper = Hero('sniper', 100, 10)

# menggunakan getter yang bukan fungsi bawaan python
# print(sniper.gethealth())

# menampilkan private variable dengan atribut tambahan
# print(sniper.info)
''' menampilkan private variable dengan atribut tambahan seperti diatas tidak disarankan 
karena memerlukan public variable yang dapat diubah oleh orang lain'''
# sniper.info = 'public variable "info" telah diubah '  # mengubah public variable info
# print(sniper.info)  # saat dipanggil akan berubah

# memanggil method yang dianggap variabel (@property)
print(sniper.info)
print(sniper.info1)
""" keunggulan menggunakan decorator @property adalah apabila terjadi perubaha maka perubahan 
    bisa terjadi secara otomatis, namun apabila melakukan perubahan dengan cara menambah atribut 
    perubahan hanya terjadi saat pembuatan objek/instance. Hal itu terjadi karena method dari 
    decorator @property dianggap sebagai variabel jadi bisa diubah ubah
"""

print('\n Getter dan setter untuk armor:')
print(sniper.armor)
print(sniper.__dict__)
sniper.armor = 50
print(sniper.armor)
print(sniper.__dict__)

# sebelum menggunakan getter dan setter