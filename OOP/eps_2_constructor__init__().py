
# __init__() = intialization

class Hero:

    def __init__(self, inputname, inputhealth, inputpower, inputarmor):
        # __init__ adalah salah satu magic keyword dalam python.
        # __init__ akan dijalankan pertama kali saat objek dibuat.
        # parameter 'self' berfungsi menggantikan nama objek yang belum didefinisikan.
        self.name = inputname
        self.health = inputhealth
        self.power = inputpower
        self.armor = inputarmor


# Parameter yang dimasukkan sesuai dengan yang ada pada __init__
hero1 = Hero('Udjang', 50, 20, 4)
hero2 = Hero('Ksatria', 100, 100, 50)
hero3 = Hero('Udcup', 1000, 500, 400)

print(hero1)
print(hero1.__dict__)  # untuk menampilkan seluruh atribut yang dimiliki objek
print(hero2.name)  # untuk menampilkan salah satu atribut yaitu nama
print(hero2.__dict__)
