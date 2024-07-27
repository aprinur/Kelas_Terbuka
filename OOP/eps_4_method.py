
# Contoh 1 :
"""
    class Hero:
    # class variabel
    jumlah_hero = 0

    def __init__(self, inputname, inputhealth, inputpower, inputarmor):
        # instance variable
        self.name = inputname
        self.health = inputhealth
        self.power = inputpower
        self.armor = inputarmor
        Hero.jumlah_hero += 1

    # void function, method tanpa return tanpa argumen
    def siapa(self):
        print('namaku adalah ' + self.name)

    # method dengan argumen tanpa return
    def healthup(self, increase):  # parameter increase diisi health yang akan ditambahkan
        self.health += increase

    # method dengan return
    def gethealth(self):
        return self.health


hero1 = Hero('Udcup', 100, 10, 5)
hero2 = Hero('Otong', 90, 5, 10)

print(hero1.__dict__)
print(hero2.__dict__)

hero2.siapa()
hero1.healthup(20)

print(hero1.health)
print(hero1.gethealth()) """


# Contoh 2

class Car:  # penulisan nama class disarankan diawali dengan huruf kapital
    # class bisa disebut sebagai blueprint atau template dalam pembuatan object
    def __init__(self, make, model, year, color):
        # make, model, year dan color adalah parameter yang harus diisi untuk membuat atribute
        """ saat dijalankan tidak perlu memasukkan parameter self karena merujuk pada objek
            yang akan dibuat"""
        self.make = make  # Atribbute
        self.model = model  # Atribbute
        self.year = year  # Atribbute
        self.color = color  # Atribbute

    def drive(self):  # method
        print('This', self.make, self.model + ' is driving')
        # self akan secara otomatis tergantikan saat method dipanggil

    def stop(self):  # method
        print(f'This {self.make} {self.model} is stop')


# membuat object
car_1 = Car('Nissan', 'GTR R35 NISMO', 2023, 'White')
car_2 = Car('Toyota', 'GR Supra 3.0L', 2023, 'Red')


# Menampilkan attribut object
print(car_1.make)
print(car_1.model)
print(car_1.year)
print(car_1.color)


# Menjalankan method
car_1.drive()
car_1.stop()

car_2.drive()
car_2.stop()
