class Hero:
    # private class variable
    __jumlah = 0

    def __init__(self, name, health, attPower, armor):
        self.__name = name
        self.__healthstandar = health
        self.__attPowerStandar = attPower
        self.__armorStandar = armor
        self.__level = 1
        self.__exp = 0

        self.__healthMax = self.__healthstandar * self.__level
        self.__attPower = self.__attPowerStandar * self.__level
        self.__armor = self.__armorStandar * self.__level

        self.__health = self.__healthMax

        Hero.__jumlah += 1

    @property
    def info(self):
        return (f"{self.__name} level {self.__level} : \n\t health = {self.__health}/{self.__healthMax} \n\t "
                f"attack = {self.__attPower} \n\t armor  = {self.__armor}")

    @property
    def gainexp(self):
        pass

    @gainexp.setter
    def gainexp(self, addexp):
        self.__exp += addexp
        if self.__exp >= 100:
            print(self.__name, 'level up')
            self.__level += 1
            self.__exp -= 100

            self.__healthMax = self.__healthstandar * self.__level
            self.__attPower = self.__attPowerStandar * self.__level
            self.__armor = self.__armorStandar * self.__level

    def attack(self, musuh):
        self.gainexp = 50  # setiap melakukan serangan akan mendapatkan 50 exp


udin = Hero('Udin', 100, 5, 10)
otong = Hero('Otong', 100, 5, 10)
print(udin.info)

udin.attack(otong)
udin.attack(otong)
udin.attack(otong)
print(udin.info)


