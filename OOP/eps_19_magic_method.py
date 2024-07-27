""""""
""" Magic method adalah method yang diawalai dengan double underscore dan diakhiri dengan double 
    underscore. Magic method disebut juga 'dunder method', 'dunder' singkatan dari 
    'double underscore'. Untuk menemukan magic method apa saja yang ada pada python bisa 
    dilakukan dengan menggunakan kode print(dir(int)) 
    """


class Buah:

    # contoh - contoh magic method
    def __init__(self, nama, jenis, jumlah):
        self.nama = nama
        self.jenis = jenis
        self.jumlah = jumlah
        """ init akan dijalankan pertamakali saat mendefinisikan objek"""

    def __repr__(self):
        return f'{self.nama} {self.jenis} berjumlah {self.jumlah}'
    """ __repr__ digunakan untuk menampilkan deskripsi objek sesuai kebutuhan, __repr__ digunakan 
        saat masih proses debugging"""

    def __str__(self):
        return f'{self.nama} {self.jenis} berjumlah {self.jumlah}'
    """  __str__ digunakan untuk menampilkan deskripsi objek sesuai kebutuhan, __str__ digunakan 
        saat program sudah selesai dibuat"""

    def __add__(self, other):
        return self.jumlah + other.jumlah
    """ method __add__ berfungsi untuk menjumlahkan atribut yang bisa dijumlahkan pada objek. 
        Dalam python memiliki method yang sejenis seperti __sub__ untuk mengurangi, __div__ untuk
        membagi dan __mul__ untuk perkalian dll"""

    @property  # untuk mendefinisikan method __dict__ perlu menggunakan @property
    def __dict__(self):
        return 'objek ini memiliki nama, jenis dan jumlah'


mangga = Buah('Mangga', 'Arummanis', 10)
jeruk = Buah('Jeruk', 'Bali', 30)
print(mangga.jenis)

print(mangga)
print(jeruk)
""" jika tidak ada method __repr__ di dalam class pembuatan objek maka akan menampilkan lokasi 
    penyimpanan objek pada memori seperti berikut 
    <__main__.Buah object at 0x00000179CD249670>, namun jika ada __repr__ maka akan menampilkan 
    apa yang direturn oleh method __repr__.
"""

print(mangga + jeruk)

print(mangga.__dict__)
""" magic method __dict__ digunakan untuk menampilkan atribut objek dengan format dictionary. 
    Jka __dict__ didefinisikan didalam class maka yang dieksekusi adalah method yang ada didalam
    class
"""