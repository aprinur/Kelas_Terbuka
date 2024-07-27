""""""
""" 
    Multiple inheritance adalah keadaan saat suatu subclass mendapatkan inheritance dari lebih 
    dari satu superclass
"""


# contoh
class A:

    def method_A(self):
        print('ini adalah method A')


class B:
    def method_B(self):
        print('ini adalah method B')


class C(A, B):
    pass


objek = C()

objek.method_A()
objek.method_B()
"""Objek yang menerima inheritance lebih dari 1 superclass dapat memanggil method dari semua 
superclass tersebut """


# contoh penggunaan multiple inheritance

class Team:  # superclass

    def setTeam(self, team):
        self.team = team

    def showTeam(self):
        print(self.team)


class Tipe_Hero:  # superclass
    def setTipe(self, tipe):
        self.tipe = tipe

    def showTipe(self):
        print(self.tipe)


class Hero(Team, Tipe_Hero):  # subclass menerima inheritance dari kedua superclass
    def __init__(self, name, health):
        self.name = name
        self.health = health


# membuat objek berdasarkan class mandiri
Ucup = Hero('Ucup', 100)

# membuat objek dari method 2 superclass yang berbeda
Ucup.setTeam('Merah')
Ucup.setTipe('Asassin')
""" karena mendapat inheritance dari 2 superclass berbeda, maka bisa membuat objek dari method 
    yang ada pada 2 class yang berbeda"""


Ucup.showTeam()
Ucup.showTipe()