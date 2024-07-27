class Hero:
    def __init__(self, name, health):  # super method
        self.name = name  # super method
        self.health = health  # super method

    def showinfo(self):  # super method
        print(f'{self.name} memiliki health {self.health}')  # super method


class Hero_intelligent(Hero):
    def __init__(self, name):
        # self.name = name   # --> Tidak efisien karena terjadi perulangan
        # self.health = health  # --> Tidak efisien karena terjadi perulangan

        # Hero.__init__(self, name, 100)  # cara 1

        super().__init__(name, 100)  # cara 2
        ''' dengan super().__init__ berarti mengambil method init dari superclass'''

        Hero.showinfo(self)  # salah satu cara memanggil method
        ''' kekurangannya adalah apabila nama class diubah maka perlu merubah nama saat memanggil
        method
        '''

        super().showinfo()  # memanggil method showinfo


class Hero_strength(Hero):
    def __init__(self, name):
        #     self.name = name  # --> Tidak efisien karena terjadi perulangan
        #     self.health = health  # --> Tidak efisien karena terjadi perulangan

        # Hero.__init__(self, name, 200)  # cara 1
        super().__init__(name, 200)  # cara 2
        ''' parameter name masih perlu diisi saat membuat objek namun health akan secara otomatis
        terisi 200'''
        ''' dengan super().__init__ berarti mengambil method ___init___ dari superclass'''


marina = Hero_intelligent('marina')
alan = Hero_strength('alan')

