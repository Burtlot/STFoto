from distutils import command
from fileinput import filename
from tkinter import *
import tkinter as tk
from turtle import bgcolor
#from typing_extensions import Self
from PIL import ImageTk, Image
from tkinter import filedialog
import os.path
import os




def openfn() :
    # Dovrei cancellare prima i valori perché magari mi stanno richiamando e non è la prima volta
    viewname.set("")
    newname.set("")
        
    filename = filedialog.askopenfilename(title='open')
    # visualizza SOLO il nome del file appena sotto la foto
    folder.set(os.path.dirname(filename))
    print("folder:",folder)
    oldname = os.path.basename(filename)
    
   
    oldfilename = Label(root, textvariable=viewname, bg = "dark green", fg='yellow').place(x=20, y=300)
    viewname.set(oldname)
    newname.set(oldname)
    # inserisce il nome del file dentro la casella per la modifica
    enewfilename = Entry(root,width=30,border=1, borderwidth=1,textvariable=newname).place(y=325,x=5)
    return filename

def open_img():
    x = openfn()

    img = Image.open(x)
    img = img.resize((250, 250), Image. ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    #print(img)
    panel = Label(root, image=img, text=x).place(x=20, y=45)
    panel.image = img
    
    #panel.grid(row=2)
    #panel.grid(row = 1, column = 1, columnspan = 2, rowspan = 2, padx = 5, pady = 5)
    #panel.grid(row = 1, column = 0, padx = 5, pady = 5, sticky = EW)
    #panel.place(x=25,y=60, bordermode='outside')

def renamefile() :
    cartella = folder.get()
    vecchiofile = viewname.get()
    nuovofile = newname.get()
    vf = cartella+"/"+vecchiofile
    nf = cartella+"/"+nuovofile
    print(cartella, vecchiofile,nuovofile)
    os.rename(vf,nf)
    open_img()

def closeprg () :
    root.destroy()    

root = Tk()
root.title("ST Foto - Rel. 0.9 - 11.02.2022")

#root.geometry("550x300+300+150")
root.geometry("300x400")
root.resizable(width=False, height=False)

folder = StringVar() # nome del file con path
viewname = StringVar() # solo il nome del file aperto
newname = StringVar() # solo il nome del file aperto

btnOpenImg = Button (root, 
                     text='Apri Foto',
                     command=open_img, 
                     width=10, 
                     height=2, 
                     padx=10,
                     highlightbackground='#10FF10'
                     ).place(x=5, y=5)
btnClose = Button (root, 
                   text='Chiudi', 
                   bg='#FF1010', 
                   command=closeprg, 
                   width=10, 
                   height=2, 
                   padx=10, 
                   highlightbackground='#FF1010',
                   ).place(x=183, y=5)

btnRename = Button (root, text='Rinomina',command=renamefile, width=30, height=2, highlightbackground='#1010FF',).place(x=10,y=350)
copyright = Label(root, text="2022 - A.I.A.C. Service s.r.l. Unipersonale", font="Arial 6", width=30).place(x=80, y=386)
#e1 = tk.Entry(root, width=30,border=1,borderwidth=1)
#enewfilename = tk.Entry(root,width=30,border=1, borderwidth=1).place(y=330,x=8)

#textEntry = tk.StringVar()
#textEntry.set("Default Text")
#textExample = tk.Entry(root,textvariable = textEntry)

root.mainloop()