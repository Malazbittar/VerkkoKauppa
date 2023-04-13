"""
Malaz Bittar
"""

from tkinter import *
from PIL import Image


class kauppa():
    """luo ikkuna"""
    def __init__(self, root):
        self.root = root
        self.root.geometry('1250x600+1+1')
        self.root.title('ML VErkkokauppa')
        self.root.configure(background='silver')
        #ei vaihtää koko
        self.root.resizable(False,True)
        #text (paika , )
        title = Label(self.root, 
                      text = 'Tervetolua',
                      bg = '#CCCCFF',
                      font = ('monospace', 14, 'bold'),
                      fg = 'white'
            )
        title.pack(fill=X)

        manage_frame = Frame(self.root ,bg='white')
        manage_frame.place(x=0, y=30, width=1250, height=50)
        search_id = Label(manage_frame, text='Etsi tuotteet', bg ='white')
        search_id.place(x=10, y=12)
        search_Entry = Entry(manage_frame, bd='2')
        search_Entry.place(x=80, y=12)
        login = Button(manage_frame, text='Kirjaudu', bg='#9F8DE7')
        login.place(x=1050, y=12)
        shopping_basket = Button(manage_frame, text='Ostoskori', bg='#9F8DE7')
        shopping_basket.place(x=1150, y=12)

        products_frame = Frame(self.root, bg='white')
        products_frame.place(x=0, y=100 ,width=1250, height=400)
       
        
def image():
    img_menul = PhotoImage(file='img/hiiri.png')
    img_menu2 = PhotoImage(file='img/hiirimato.png')
    img_menu3 = PhotoImage(file='img/tietokoneHB.png')
    img_menu4 = PhotoImage(file='img/kuulokkeet.png')


root =Tk() 
ob = kauppa(root)       
root.mainloop()
