""""""
""" Method resolution order adalah urutan pengeksekusian program. Urutan pengeksekusian program 
 berdasarkan urutan penulisan nama superclass didalam parameter subclass. """


# Contoh
class A:
    def show(self):
        print('ini adalah show A')


class B:
    def show(self):
        print('ini adalah show B')


class C(A, B):
    pass
    """ jika dalam beberapa class memiliki method dengan nama yang sama, maka yang akan dijalankan
        adalah method dari class yang penulisannya paling awal. Dalam class tersebut penulisan 
        superclass A berada diawal oleh karena itu maka method yang ada didalam class A yang 
        akan dijalankan, begitu pula sebaliknya """


objek = C()
objek.show()
# help(objek)  # mengecek method resolution order
""" saat dicek urutannya adalah C -> A -> B, namun karena class C berisi pass maka yang 
    dijalankan adalah A"""