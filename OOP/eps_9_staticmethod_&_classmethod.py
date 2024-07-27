# membuat encapsulasi untuk class

class Hero:

    # private class variabel
    __jumlah = 0

    def __init__(self, name):
        self.__name = name
        Hero.__jumlah += 1

    # method ini hanya berlaku untuk objek
    def getjumlah(self):
        return Hero.__jumlah

    # method ini tidak berlaku untuk objek tapi berlaku untuk class
    def getjumlah1():
        return Hero.__jumlah

    # method static (decorator). method yang bisa digunakan untuk class dan objek/instance
    @staticmethod  # decorator
    def getjumlah2():  # static method tidak menerima parameter 'self' atau 'cls'
        return Hero.__jumlah

    # class method. method yang hanya berfungsi pada class
    @classmethod
    def getjumlah3(cls):  # cls merujuk pada nama class
        return cls.__jumlah


sniper = Hero('sniper')
# print(Hero.__jumlah)  # tidak bisa dilakukan karena '__jumlah' adalah private variable
print(Hero.getjumlah1())  # method berjalan karena menempel dengan class

ucup = Hero('ucup')
print(Hero.getjumlah2())  # static method (decorator) menempel ke class
print(ucup.getjumlah2())  # static method (decorator) menempel ke objek

otong = Hero('otong')
print(Hero.getjumlah3())  # class method
print(otong.getjumlah3())  # class method

"""
  *  @staticmethod
  
     Staticmethod adalah metode yang tidak bergantung pada instance/objek kelas. Dengan kata 
     lain, metode ini tidak memerlukan akses ke instance/objek (self) atau kelas (cls). 
     Method ini bisa dipanggil baik dari instance/objek kelas ataupun dari kelas itu sendiri.
     
     Ciri ciri staticmethod
     - Tidak menerima parameter self atau cls.
     - Tidak bisa mengakses atau memodifikasi state dari instance atau kelas.
     - Berguna untuk fungsi yang secara logis berhubungan dengan kelas, tetapi 
       tidak perlu mengakses instance atau kelas secara langsung.
       
     Contoh staticmethod:
      class MyClass:
      
        @staticmethod
        def my_static_method(param1, param2):
            return param1 + param2

      # Memanggil static method dari kelas
      result = MyClass.my_static_method(5, 10)
      print(result)  
      # Output: 15

      # Memanggil static method dari instance
      obj = MyClass()
      result = obj.my_static_method(3, 7)
      print(result)  
      # Output: 10
      
    
  *   @classmethod
  
      Classmethod adalah metode yang menerima parameter 'cls' yang mengacu pada kelas itu 
      sendiri. Metode ini dapat memodifikasi state kelas yang mempengaruhi semua instance/objek 
      dari kelas tersebut. classmethod sering digunakan untuk membuat factory methods yang 
      bisa membuat instance kelas.
      
      Ciri - ciri classmethod:
      - Menerima parameter 'cls' sebagai argumen pertama.
      - Bisa mengakses dan memodifikasi state kelas yang mempengaruhi semua instance dari kelas
        tersebut.
      - Berguna untuk metode yang harus bekerja dengan kelas itu sendiri daripada dengan instance
        kelas.
        
      Contoh classmethod
      class MyClass:
          class_variable = 0

          def __init__(self, value):
              self.instance_variable = value

          @classmethod
          def my_class_method(cls, value):
              cls.class_variable = value

          @classmethod
          def create_instance(cls, value):
              return cls(value)

      # Memanggil class method untuk memodifikasi class variable
      MyClass.my_class_method(10)
      print(MyClass.class_variable)  # Output: 10
    
      # Menggunakan class method sebagai factory method
      new_instance = MyClass.create_instance(20)
      print(new_instance.instance_variable)  # Output: 20
      
  ** Perbedaan 'staticmethod' dan 'classmethod'
  
    * Parameter
        - 'staticmethod': Tidak menerima 'self' atau 'cls'.
        - 'classmethod': Menerima 'cls' sebagai parameter pertama.
    
    * Akses 
        - 'staticmethod': Tidak bisa mengakses atau memodifikasi state instance atau kelas.
        - 'classmethod': Bisa mengakses dan memodifikasi state kelas.
        
    * Pemanggilan 
        - Keduanya bisa dipanggil dari instance kelas atau dari kelas itu sendiri.
  
  
  ** Ringkasan
  
    State Kelas: Atribut atau data yang dimiliki oleh kelas itu sendiri dan dibagi di antara
                 semua instance dari kelas tersebut. ( Class variable)
    Factory Methods: Metode yang digunakan untuk membuat instance baru dari kelas, biasanya
                     melakukan tugas tambahan sebelum mengembalikan instance. Method yang 
                     didefinisikan dibawah @classmethod
    Instance Kelas: Objek individual yang dibuat dari kelas, memiliki state dan perilaku yang
                    didefinisikan oleh kelas tersebut. Objek yang dibuat dari atribut __init__
    State Instance: Atribut atau data yang dimiliki oleh instance individual dari kelas, 
                    unik untuk setiap instance.
"""

