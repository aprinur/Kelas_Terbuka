class Hero:
    # class variable/ static variable adalah variable yang ada dalam class itu sendiri
    jumlah = 0

    def __init__(self, inputname, inputhealth, inputpower, inputarmor):
        # instance variable akan dimiliki oleh object yang akan dibuat.
        # variable dibawah adalah contoh instance variable.
        self.name = inputname
        self.health = inputhealth
        self.power = inputpower
        self.armor = inputarmor
        # salah satu contoh penggunaan class variable adalah untuk mengecek
        # jumlah object yang sudah dibuat
        Hero.jumlah += 1
        print('membuat Hero dengan nama ' + inputname)


# membuat objek dengan parameter pada __init__
hero1 = Hero('Udjang', 50, 20, 4)
print(Hero.jumlah)
hero2 = Hero('Ksatria', 100, 100, 50)
print(Hero.jumlah)
hero3 = Hero('Udcup', 1000, 500, 400)
print(Hero.jumlah)

print(hero1)
print(hero1.__dict__)  # untuk menampilkan seluruh atribut yang dimiliki objek
print(hero2.name)
print(hero2.__dict__)
