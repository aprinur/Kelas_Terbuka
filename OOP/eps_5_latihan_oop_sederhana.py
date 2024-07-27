class Hero:

    def __init__(self, name, health, attackPower, armorNumber):
        self.name = name
        self.health = health
        self.attackPower = attackPower
        self.armorNumber = armorNumber

    def serang(self, lawan):
        print(self.name + ' menyerang ' + lawan.name)
        lawan.diserang(self, self.attackPower)
        """ 2. method 'diserang' meminta parameter 'lawan' dan 'attackPower_lawan' lalu
            parameter 'lawan' diisi 'self' dan parameter 'attackPower_lawan' diisi 
            'self.attackPower'
        """

    def diserang(self, lawan, attackPower_lawan):
        # 1. 'lawan' dan 'attackPower_lawan' adalah parameter yang diminta
        print(self.name + ' diserang ' + lawan.name)
        damage_diterima = attackPower_lawan/self.armorNumber
        """ perhitungan damage yang diterima = attack power penyerang(self) dibagi armorNumber 
            yang diserang(lawan)"""
        print('serangan terasa ' + str(damage_diterima))
        self.health -= damage_diterima
        """ lalu damage yang diterima dikurangi health yang diserang"""
        print('darah ' + self.name + ' tersisa ' + str(self.health))


# membuat objek hero
sniper = Hero('Sniper', 100, 10, 5)
kimimaru = Hero('Kimimaru', 100, 10, 10)

# melakukan serangan
sniper.serang(kimimaru)
print('\n')
kimimaru.serang(sniper)
