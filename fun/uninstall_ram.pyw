from tkinter import *

def uninstall_ram():
    sussy_ram = bytearray(int(s1.get()*(2**30)))
    while True:
        sussy_ram

root = Tk()
root.geometry("500x300")

Label(text = "Select amount of RAM to be uninstalled [GiB]:").pack()
s1 = Scale(root, from_=0, to=64, length=400, tickinterval=10, orient=HORIZONTAL)
s1.set(0)
s1.pack()
Button(root, text='Apply', command=uninstall_ram).pack()

mainloop()
