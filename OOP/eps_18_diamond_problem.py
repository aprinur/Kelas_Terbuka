""""""
""" Diamond problem adalah salah satu masalah yang terjadi dalam multiple inheritance. Disebut 
    diamond karena saat diilustrasikan membentuk seperti diamond
"""


# contoh

class A:
    def show(self):
        print('ini adalah show dari class A')


class B(A):
    def show(self):
        print('ini adalah show dari class B')

 
class C(A):
    # def show(self):
    #     print('ini adalah show dari class C')
    pass


class D(B, C):
    # def show(self):
    #     print('ini adalah show dari class D')
    pass


objek = D()
objek.show()
""" Saat menjalankan sebuah method, maka akan mencari didalam class D terlebih dahulu 
    jika tidak ada maka akan dilanjutkan mencari berdasarkan method resolution order.
    Untuk mencari method resolution order bisa menggunakan method help(nama_objek)  """


#
#  contoh diatas jika diilustrasikan maka akan berbentuk seperti berikut
#
#                         A
#                        / \
#                       /   \
#                      /     \
#                     B       C
#                      \     /
#                       \   /
#                        \ /
#                         D
#
#
#     class D mendapat inheritance dari class B dan C, sedangkan B dan C mendapat inheritance
#     dari A.
#
#