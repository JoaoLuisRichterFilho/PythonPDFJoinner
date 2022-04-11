from ast import List
from ctypes import alignment
from dataclasses import replace
from distutils.file_util import move_file
from pathlib import Path
from pickle import FRAME
from posixpath import split
from textwrap import fill
import this
from tkinter import *
# import tkMessageBox
import tkinter
from tkinter.filedialog import askopenfilenames
from tkinter.filedialog import asksaveasfile
from tokenize import String
from turtle import color, left
from PyPDF2 import PdfFileMerger
from PIL import Image, ImageTk
import tkinter.font as font

import os

def fileDel():
    if(Lb1.size() > 0):
        try:

            selected_checkboxs = Lb1.curselection()
  
            for sb in selected_checkboxs[::-1]:
                print(Lb1.get(sb))
                Lb1.delete(sb)
                
        except:
            tkinter.messagebox.showwarning(title="Atenção!", message="Nenhum item selecionado")
    else:
        tkinter.messagebox.showwarning(title="Atenção!", message="Nenhum item selecionado")

def cleanList():
    if(Lb1.size() > 0):
        try:
            Lb1.delete(0, END)
            tkinter.messagebox.showinfo(title="Sucesso!", message="A lista foi limpa")

        except:
            tkinter.messagebox.showerror(title="Erro!", message="Não foi possível limpar a lista.")
    else:
        tkinter.messagebox.showwarning(title="Atenção!", message="Lista vazia!")

def fileAdd():
    Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
    filenames = askopenfilenames() # show an "Open" dialog box and return the path to the selected file
    # print(filenames)
    # master = Tk()
    if(filenames):
        counter = 0
        try:

            for fl in filenames:
                Lb1.insert(END, fl)
                counter+=1

        except:
            Lb1.activate(0)

        finally:
            if(counter > 0):
                Lb1.selection_set(counter - 1)
                Lb1.activate(counter - 1)
            else:
                Lb1.selection_set(0)
                Lb1.activate(0)
                
def moveUP():
    if(Lb1.size() > 0):
        if(len(Lb1.curselection()) < 2):
            try:
                text = Lb1.selection_get()
                pos  = Lb1.curselection()
                pos  = pos[0] -1
                if(pos + 1 == 0):
                    return
                Lb1.delete(Lb1.curselection())
                Lb1.insert(pos, text)
                Lb1.selection_set(pos)
                Lb1.activate(pos)

                print(pos)
                # print(text)
            except:
                tkinter.messagebox.showwarning(title="Atenção!", message="Nenhum item selecionado") 
        else:
            tkinter.messagebox.showwarning(title="Atenção!", message="Selecione apenas 1 item para mover")

    else:
        tkinter.messagebox.showwarning(title="Atenção!", message="Nenhum item selecionado") 

def moveDOWN():
    if(Lb1.size() > 0):
        if(len(Lb1.curselection()) < 2):
            try:
                text = Lb1.selection_get()
                pos  = Lb1.curselection()
                pos  = pos[0] + 1
                if(pos == Lb1.size()):
                    return
                Lb1.delete(Lb1.curselection())
                Lb1.insert(pos, text)
                Lb1.selection_set(pos)
                Lb1.activate(pos)

                print(pos)
                # print(text)
            except:
                tkinter.messagebox.showwarning(title="Atenção!", message="Nenhum item selecionado") 
        else:
            tkinter.messagebox.showwarning(title="Atenção!", message="Selecione apenas 1 item para mover")
    else:
        tkinter.messagebox.showwarning(title="Atenção!", message="Nenhum item selecionado")

def pdfJoin(pdfs, filename):
    try: 
        merger = PdfFileMerger()
        for pdf in pdfs:
            merger.append(pdf)
    
        merger.write(filename)
        merger.close()
        print(filename)
        # Path("./result.pdf").rename(filename)
        tkinter.messagebox.showinfo(title="SUCESSO!", message="PDF unificado: "+filename)
        os.startfile(filename)
    except:
        tkinter.messagebox.showerror(title="ERRO!", message="Falha ao unir os arquivos")

def mergePDFs():
    pdfs = Lb1.get(0, END)

    print(pdfs)

    if (Lb1.size() < 2 ):
        tkinter.messagebox.showwarning(title="Atenção!", message="No mínimo 2 arquivos são necessários para a união")
        return

    filename = asksaveasfile(mode='w', defaultextension=".pdf")

    if filename is None: # asksaveasfile return `None` if dialog closed with "cancel".
        return
    else:
        pdfJoin(pdfs=pdfs, filename=filename.name)

root = Tk()
root.title("Sicredi - PDFJoinner")
# root.iconbitmap("./src/sicredi-icon2.ico")
root.iconphoto(False, PhotoImage(file='./src/sicredi-icon2.ico'))
root.state("zoomed")
root.geometry("900x600")
# root.geometry("700x600")

iconAdd      = PhotoImage(file='./src/plus-icon.png', height=40, width=40)
iconDel      = PhotoImage(file='./src/remove-icon.png', height=40, width=40)
iconDelList  = PhotoImage(file='./src/remove_list-icon.png', height=40, width=40)
iconTop      = PhotoImage(file='./src/top-icon.png', height=40, width=40)
iconDown     = PhotoImage(file='./src/down-icon.png', height=40, width=40)
iconJoin     = PhotoImage(file='./src/join-icon.png', height=40, width=40)

btnFont  = font.Font(family='Helvetica', size="14")
listFont = font.Font(family='Helvetica', size="10")

Lb1 = Listbox(root, selectmode="multiple", width=110, height=25, font=listFont)
Lb1.grid(row=0, rowspan=2, column=0, padx=10, pady=10, ipadx=5, ipady=2)

panel = Frame(root, width=500, height=300)
panel.grid(row=2, column=0, pady=10, ipadx=5, ipady=2)

btnMoveUP    = Button(root, image=iconTop, text="", command=lambda: [moveUP()], compound="left")
btnMoveDOWN  = Button(root, image=iconDown, text="", command=lambda: [moveDOWN()], compound="left")
btnMoveUP.grid(    row=0, column=1, padx=10, ipadx=5, ipady=2)
btnMoveDOWN.grid(  row=1, column=1, padx=10, ipadx=5, ipady=2)

btnAddFile   = Button(panel, image=iconAdd, text="Adicionar arquivo(s)", font=btnFont, command=lambda: [fileAdd()], compound="left")
btnDelFile   = Button(panel, image=iconDel, text="Excluir arquivo(s)", font=btnFont, command=lambda: [fileDel()], compound="left")
btnCleanList = Button(panel, image=iconDelList, text="Limpar lista", font=btnFont, command=lambda: [cleanList()], compound="left")
btnJOIN      = Button(panel, image=iconJoin, text="Unir arquivos", font=btnFont, background="#3FA110", fg="#fff", command=lambda: [mergePDFs()], compound="left", width=604)

btnAddFile.grid(   row=0, column=0, padx=10, ipadx=5, ipady=2)
btnDelFile.grid(   row=0, column=1, padx=10, ipadx=5, ipady=2)
btnCleanList.grid( row=0, column=2, padx=10, ipadx=5, ipady=2)
btnJOIN.grid(      row=1, column=0, columnspan=3, padx=10, pady=20, ipadx=5, ipady=2)

root.mainloop()

