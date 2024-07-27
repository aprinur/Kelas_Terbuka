""""""
"""
    Abstract class adalah blueprint dari class, sedangkan class biasa adalah blueprint dari objek.
    Class yang menjadi instance dari abstrac class harus memiliki method yang sama yang ada pada
    abstract class. Objek tidak bisa langsung diinstance dari abstract class
"""


# Contoh class biasa
"""
class Button:

    def click(self):
        print('button click')


class PushButton(Button):
    pass


tombol1 = PushButton()

tombol1.click()  
# objek 'tombol1' dibuat dari class 'PushButton' dan class 'PushButton' mendapat 
'warisan'/inheritance dari class 'Button' jadi saat method click akan dijalankan dan tidak 
ditemukan didalam class 'PushButton' maka akan mencari di dalam class yang memberikan 
inheritance / class 'Button'.
"""


# contoh abstract class
from abc import ABC, abstractmethod  # ABC = Abstract Base Class
""" Untuk menggunakan abstrac class perlu mengimport class ABC dan fungsi abstractmethod 
dari modul abc"""


class Button(ABC):  # Abstract class

    @abstractmethod
    def click(self):
        print('Hello world')


class PushButton(Button):  # Class hasil instantiate dari abstract class
    def click(self):
        print('Hello world')
    """class yang diinstantiate dari abstract class harus memiliki method yang sama dengan yang 
    ada didalam abstract class"""


# tombol2 = Button()
# tombol2.click()
"""saat dijalankan akan error karena abstrac class tidak bisa langsung diinstantiate menjadi objek
"""
tombol3 = PushButton()
tombol3.click()
""" karena objek dibuat dari class hasil instantiate abstract class dan method yang ada pada 
abstract class sudah diimplementasikan oleh class hasil instantiatenya maka kode baru bisa 
dijalankan
"""