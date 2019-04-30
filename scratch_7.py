from tkinter import *


def main():
    txt.delete(0.0,'end')
    str = ent1.get()
    key = ent2.get()
    crypto = var_chk.get()
    if crypto == 1:
        encrypted = ''
        i = len(key)
        f = 0
        for x in str:
            if f == i:
                f = 0
            indx = (ord(x) + int(key[f])) % 256
            if indx > 126:
                indx = indx - 95
            encrypted = encrypted + chr(indx)
            f = f + 1
        txt.insert(0.0,encrypted)
    else:
        decrypted = ''
        i = len(key)
        f = 0
        for x in str:
            if f == i:
                f = 0
            indx = (ord(x) - int(key[f])) % 256
            if indx < 32:
                indx = indx + 95
            decrypted = decrypted + chr(indx)
            f = f + 1
        txt.insert(0.0,decrypted)

root = Tk()
root.geometry("300x300")


#creating widgts

message = Label(root , text = "Message:")
keyBtn = Label(root , text = "key:")

ent1 = Entry(root, width = 37)
ent2 = Entry(root, width = 37)

var_chk = IntVar()

rb1 = Radiobutton(root , text = "encrypt" , variable = var_chk , value = 1)
rb2 = Radiobutton(root , text = "decrypt" , variable = var_chk , value = 2)

bt = Button(root , text = "Submit" , bg = "purple" , fg= "white" ,  command = main)

txt = Text(root , width = 37 , height = 12 , wrap = WORD)


#placing them on screen

message.grid(row = 0 , column = 0 , sticky = E)
keyBtn.grid( row = 1 , column = 0 , sticky = E)

ent1.grid( row = 0 , column = 1)
ent2.grid( row = 1 , column = 1)

rb1.grid( row = 2 , column = 0)
rb2.grid( row = 2 , column = 1)

bt.grid(row = 3 , columnspan = 2 )

txt.grid( row = 4 , columnspan = 2 , sticky = W)

root.mainloop()