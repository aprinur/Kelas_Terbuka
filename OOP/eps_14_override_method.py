""""""
"""
    Override method adalah menimpa method yang ada pada super class dengan cara mendefinisikan
  nama method dengan nama yang sama yang akan dioverride pada super class
   """


class Hero:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def showinfo(self, ):
        print('showinfo di class Hero')
        print(f'{self.name} \n\thealth: {self.health}')


class Hero_intelligent(Hero):
    def __init__(self, name):
        super().__init__(name, 100)

    # override method
    def showinfo(self):
        print('showinfo di subclass Hero_intelligance')
        print(f'{self.name}\n\tTipe: intelligence \n\tHealth: {self.health}')


class Hero_strength(Hero):
    def __init__(self, name):
        super().__init__(name, 200)


marina = Hero_intelligent('marina')
alan = Hero_strength('alan')

marina.showinfo()
""" akan menampilkan showinfo dari class Hero_intelligent karena method showinfo didalam class
Hero_intelligent mengoverride method showinfo yang ada pada superclass
"""
alan.showinfo()
""" akan menampilkan showinfo dari class Hero """
