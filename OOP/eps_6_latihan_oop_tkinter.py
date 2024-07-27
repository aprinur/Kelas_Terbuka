import tkinter

# membuat object
main_window = tkinter.Tk()

# membuat label dan dimasukkan ke main window
label_1 = tkinter.Label(main_window, text='Label 1')
label_2 = tkinter.Label(main_window, text='Label 2 ')

# membuat tombol
tombol_1 = tkinter.Button(main_window, text='tombol 1')
tombol_2 = tkinter.Button(main_window, text='tombol 2')

# positioning method. method untuk menempatkan object yang sudah dibuat
label_1.pack()
label_2.pack()
tombol_1.pack()
tombol_2.pack()


# method untuk menampilkan GUI
main_window.mainloop()