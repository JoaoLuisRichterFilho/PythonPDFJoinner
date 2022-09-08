from ast import List
from ctypes import alignment
from dataclasses import replace
from distutils.file_util import move_file
from lib2to3.pytree import convert
from pathlib import Path
from pickle import FRAME
from posixpath import split
from textwrap import fill
import this
import base64
from tkinter import *
from tkinter import ttk
# import tkMessageBox
import tkinter
from tkinter.filedialog import askopenfilenames
from tkinter.filedialog import asksaveasfile
from tokenize import Name, String
from turtle import color, left, width
from PyPDF2 import PdfFileMerger, PdfFileReader
import PyPDF2
from PIL import Image, ImageTk, ExifTags
import tkinter.font as font

import os

def changeBtnState(btn):
    if (btn['state'] == NORMAL):
        btn['state'] = DISABLED
    else:
        btn['state'] = NORMAL

def changeMaxBar(max):
    try:
        if(max > 0):
            minha_barra['maximum'] = max
    except:
        print("Falha ao atualizar progress bar")

def changeCurrentBar(val, max):
    try:
        if(val <= max and val >= 0):
            barra.set(val)
            panel.update()
    except:
        print("Falha ao atualizar progress bar")

def img_to_pdf(path_img):
    try:
        aName = path_img.split("/");
        nameFinal = aName[ len(aName) -1 ]
        user = os.getenv('USERNAME')
        image_tmp = Image.open(r''+path_img)

        # exif = image_tmp._getexif()

        # orientation = exif[274]

        # print(orientation)

        # if orientation == 3:
        #     image_tmp=image_tmp.transpose(Image.Transpose.ROTATE_180)
        # elif orientation == 6:
        #     image_tmp=image_tmp.transpose(Image.Transpose.ROTATE_270)
        # elif orientation == 8:
        #     image_tmp=image_tmp.rotate(90, expand=False)


        # for orientation in ExifTags.TAGS.keys():
        #     print(ExifTags.TAGS[orientation])
        #     if ExifTags.TAGS[orientation]=='Orientation':
        #         break

        # image_tmp.show()
        # print(image_tmp.size)
        im_temp = image_tmp.convert('RGB')
        im_temp.save(r'C:/Users/'+user+'/AppData/Local/Temp/'+nameFinal+'.pdf')
        im_temp.close()
        return 'C:/Users/'+user+'/AppData/Local/Temp/'+nameFinal+'.pdf'
    except:
        print('Falha ao converter imagem')
        return False

   
def fileDel():
    changeCurrentBar(0, 100)
    if(Lb1.size() > 0):
        try:

            selected_checkboxs = Lb1.curselection()
  
            for sb in selected_checkboxs[::-1]:
                print(Lb1.get(sb))
                Lb1.delete(sb)
                
        except NameError:
            tkinter.messagebox.showwarning(title="Atenção!", message="Nenhum item selecionado")
    else:
        tkinter.messagebox.showwarning(title="Atenção!", message="Nenhum item selecionado")

def cleanList():
    changeCurrentBar(0, 100)
    if(Lb1.size() > 0):
        try:
            Lb1.delete(0, END)
            # tkinter.messagebox.showinfo(title="Sucesso!", message="A lista foi limpa")

        except NameError:
            tkinter.messagebox.showerror(title="Erro!", message="Não foi possível limpar a lista.")
    else:
        tkinter.messagebox.showwarning(title="Atenção!", message="Lista vazia!")

    

def fileAdd():
    Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
    file_types = [('Documento PDF e Imagem', '*.pdf;*.png;*.jpg;*.jpeg')]
    filenames = askopenfilenames(filetypes=file_types, title='Selecione dois ou mais documentos', parent=root) # show an "Open" dialog box and return the path to the selected file
    # print(filenames)
    # master = Tk()
    if(filenames):
        counter = 0
        try:
            for fl in filenames:
                name, ext = os.path.splitext(fl)
                if(ext.upper() == ".PDF"):
                    try:
                        PyPDF2.PdfFileReader(open(fl, "rb"))
                    except:
                        tkinter.messagebox.showerror(title="ERRO!", message="O seguinte arquivo PDF possui um problema e não poderá ser unificado: "+fl)
                        continue
                
                if(ext.upper() ==".PDF" or ext.upper() ==".PNG" or ext.upper() == ".JPG" or ext.upper() == ".JPEG"):
                    Lb1.insert(END, fl)
                    counter+=1
                else:
                    tkinter.messagebox.showerror(title="ERRO!", message="Um ou mais arquivos não pode ser unificado. Só são aceitos arquivos PDF e imagens (JPG, JPEG, PNG)")

        except NameError:
            Lb1.activate(0)

        finally:
            if(counter > 0):
                Lb1.selection_set(counter - 1)
                Lb1.activate(counter - 1)
                changeMaxBar(counter)
                changeCurrentBar(0, counter)
            else:
                Lb1.selection_set(0)
                Lb1.activate(0)
                
def moveUP():
    if(Lb1.size() > 0):
        if(len(Lb1.curselection()) == 1):
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
                tkinter.messagebox.showwarning(title="Atenção!", message="Falha ao mover o item selecionado") 
        elif(len(Lb1.curselection()) < 1):
            tkinter.messagebox.showwarning(title="Atenção!", message="Nenhum item selecionado")
        elif(len(Lb1.curselection()) > 1):
            tkinter.messagebox.showwarning(title="Atenção!", message="Selecione apenas 1 item para mover")
    else:
        tkinter.messagebox.showwarning(title="Atenção!", message="Nenhum item selecionado") 

def moveDOWN():
    if(Lb1.size() > 0):
        if(len(Lb1.curselection()) == 1):
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
            except NameError:
                tkinter.messagebox.showwarning(title="Atenção!", message="Falha ao mover") 
        elif(len(Lb1.curselection()) < 1):
            tkinter.messagebox.showwarning(title="Atenção!", message="Nenhum item selecionado") 
        elif(len(Lb1.curselection()) > 1):
            tkinter.messagebox.showwarning(title="Atenção!", message="Selecione apenas 1 item para mover")
    else:
        tkinter.messagebox.showwarning(title="Atenção!", message="Nenhum item selecionado")

def pdfJoin(pdfs, filename):
    changeBtnState(btnJOIN)
    try: 
        merger = PdfFileMerger()
        arrayImg = []
        arrayFiles = []
        count = 0
        for pdf in pdfs:
            name, ext = os.path.splitext(pdf)
            if(ext.upper() ==".PNG" or ext.upper() == ".JPG" or ext.upper() == ".JPEG"):
                conv = img_to_pdf(pdf)
                if(conv):
                    merger.merge(position=count, fileobj=conv)
                    arrayImg.append(conv)
            else:
                merger.merge(position=count, fileobj=pdf)
            
            arrayFiles.append(pdf)

            if(arrayFiles):
                if(len(arrayFiles) > 0):
                    changeCurrentBar(len(arrayFiles), Lb1.size())
            
            count += 1
    
        merger.write(filename)
        merger.close()
        print(filename)
        # Path("./result.pdf").rename(filename)
        changeBtnState(btnJOIN)
        tkinter.messagebox.showinfo(title="SUCESSO!", message="PDF unificado: "+filename)
        cleanList()
        os.startfile(filename)

    except NameError:
        tkinter.messagebox.showerror(title="ERRO!", message="Falha ao unir os arquivos")

    try:
        if(len(arrayImg) > 0):
            for temp in arrayImg:
                
                    os.remove(temp)
                    # print(temp)
    except:
        print('Arquivo temporário não existe')

def mergePDFs():
    pdfs = Lb1.get(0, END)

    print(pdfs)

    if (Lb1.size() < 2 ):
        tkinter.messagebox.showwarning(title="Atenção!", message="No mínimo 2 arquivos são necessários para a união")
        return

    file_types = [('Documento PDF', '*.pdf')]
    filename = asksaveasfile(mode='w', defaultextension=".pdf", filetypes=file_types)

    if filename is None: # asksaveasfile return `None` if dialog closed with "cancel".
        return
    else:
        pdfJoin(pdfs=pdfs, filename=filename.name)

root = Tk()

root.title("Python - Unificador de PDF")
root.state("zoomed")
root.geometry("900x600")


iconAddB64 = '''\
    iVBORw0KGgoAAAANSUhEUgAAACMAAAAjCAYAAAAe2bNZAAAACXBIWXMAAAsTAAALEwEAmpwYAAATUklEQVR42gFHE7jsAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgAB/f38AgYGBBYODgwiAgIAAeXl5AHNzcwBubm4Aa2trAG5ubgBzc3MAeXl5AICAgACDg4MIgYGBBX9/fwCAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgAB/f38AgICAAYGBgQGAgIAAfHx8AHd3dwB/f38nkJCQWKGhoWeurq5rs7Oza66urmuhoaFnkJCQWH9/fyZ3d3cAfHx8AICAgACBgYEBgICAAX9/fwCAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAAICAgACAgIAAgICAAICAgACAgIAAgICAAH9/fwCAgIACgYGBAHt7ewB+fn4FlZWVbMfHx7Xh4eHi7e3t//r6+v/////////////////6+vr/7e3t/+Hh4eLGxsa1lJSUa35+fgV7e3sAgYGBAICAgAJ/f38AgICAAICAgACAgIAAgICAAICAgACAgIAAAICAgACAgIAAgICAAICAgAB/f38Af39/AICAgAF+fn4AeXl5BpqammbV1dXj+vr6/////////////////P////n9/f35/Pz8+f39/fn////5/////P//////////+vr6/9TU1OKZmZlleXl5Bn5+fgCAgIABf39/AH9/fwCAgIAAgICAAICAgACAgIAAAICAgACAgIAAgICAAICAgAB/f38AgICAA3x8fACBgYEowsLCufr6+v///////////f39/fv9/f38/f39/v7+/v7+/v7+/v7+/v7+/v7+/v7+/f39/v39/fz9/f37/////f/////6+vr/w8PDuIODgzB8fHwAgICAA39/fwCAgIAAgICAAICAgACAgIAAAICAgACAgIAAgICAAH9/fwCAgIADe3t7AIeHhz/Z2dno//////7+/vn9/f39/v7+/v7+/v7+/v7+/v7+/v7+/v/8/Pz8/Pz8+vz8/Pz+/v7//v7+/v7+/v7+/v7+/v7+/v39/f3+/v76/////9vb2+2IiIhCe3t7AICAgAN/f38AgICAAICAgACAgIAAAICAgACAgIAAf39/AICAgAF8fHwAiIiIPODg4PP//////Pz8+v7+/v7//////v7+/v7+/v7//////v7+/v////7////////////////////+/v7+/v/////+/v7+/v7+/v/////+/v7//Pz8+v/////g4ODyiYmJPXx8fACAgIABf39/AICAgACAgIAAAICAgACAgIAAgICAAX5+fgCBgYEt29vb6//////9/f38///////////+/v7+///////////+/v7+/////vb29v+9vb2tra2tX7y8vKzy8vL//////v7+/v7///////////7+/v7////+//////39/fz/////3Nzc7YGBgSt+fn4AgICAAYCAgACAgIAAAICAgAB/f38AgICAAHl5eQHDw8O5//////v7+/r+/v7//v7+/v////////////////7+/v3+/v779/f3/aCgoG11dXUCd3d3AHR0dAGgoKBt+Pj4/v7+/vv+/v79/////////////////v7+/v7+/v/8/Pz6/////8LCwrd5eXkAgICAAH9/fwCAgIAAAICAgACAgIABe3t7AJqammb4+Pj//f39+v39/f7///////////////////////////z8/Pr/////09PTxHd3dwqCgoIAgoKCBoKCggB2dnYK09PTxv/////8/Pz6///////////////////////////9/f3+/f39+vj4+P+ZmZlke3t7AICAgAGAgIAAAH9/fwB/f38AfX19BNXV1eT////9/f39/P/////+/v7+//////////////////////v7+/n+/v7+zs7Om3R0dACCgoIFgICAAIKCggV0dHQAzs7Om/7+/v77+/v5//////////////////////7+/v7//////f39/P////3W1tbifX19BX9/fwB/f38AAICAgAZ8fHwAlpaWbPz8/P/+/v79/v7+/f7+/v7///////////////////////////z8/Pr/////zs7OnXR0dACBgYEFgICAAIGBgQV0dHQAzs7Onf/////8/Pz6///////////////////////////+/v7+/v7+/f7+/v38/Pz/lJSUa3x8fACAgIACAIKCggZ2dnYAx8fHtv////79/f36/f39/v7+/v7//////v7+/vz8/Pv8/Pz6/Pz8+vn5+fX8/Pz6zMzMmnR0dACBgYEEgICAAIGBgQR0dHQAzMzMmvz8/Pr5+fn1/Pz8+vz8/Pr8/Pz7/v7+/v/////+/v7+/f39/v39/fr////+xsbGtXh4eACBgYEDAICAgAB+fn4n4+Pj4/7+/v78/Pz8/v7+///////+/v7//////P//////////////////////////1NTUqXNzcwCCgoIFgICAAIKCggVzc3MA1NTUqf///////////////////////////////P7+/v///////v7+//z8/Pz+/v7/4+Pj4n19fSOAgIAAAHl5eQCQkJBY7e3t//////z9/f3+//////7+/v7////++Pj4/9PT08TOzs6czs7OnczMzJnOzs6dsLCwYHh4eACBgYEDgICAAIGBgQN4eHgAsLCwYM7Ozp3MzMyZzs7Onc7OzpzT09PD9fX1//////7+/v7+//////39/f7+/v787e3t/46OjlJ9fX0AAHJycgChoaFn+/v7/v7+/vn+/v79/v7+/v7+/v719fX/oKCgbXZ2dgl0dHQAdHR0AHR0dAB0dHQAeHh4AIGBgQB/f38AgICAAH9/fwCBgYEAeHh4AHR0dAB0dHQAdHR0AHR0dAB2dnYJnp6ebPX19f/+/v7+/v7+/v7+/v3////5+vr6/p6enmJ6enoAAG1tbQCtra1r//////z8/Pj9/f3+/Pz8+/////+9vb2tdXV1AIKCggCCgoIGgoKCBYKCggWCgoIFgYGBA39/fwCAgIAAgICAAICAgAB/f38AgYGBA4KCggWCgoIFgoKCBYKCggaCgoIAdnZ2AL29va///////Pz8+/39/f78/Pz4/////6urq2Z4eHgAAGtrawCysrJr/v7+//v7+/n+/v7/+/v7+f7+/v6tra1fd3d3A4KCggaAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAgICAAH9/fwCCgoIFd3d3A6ysrGH+/v7++/v7+f7+/v/7+/v5/v7+/7CwsGZ3d3cAAG1tbQCtra1r//////z8/Pj9/f3+/Pz8+/////+8vLytdXV1AIKCggCCgoIGgoKCBYKCggWCgoIFgYGBA39/fwCAgIAAgICAAICAgAB/f38AgYGBA4KCggWCgoIFgoKCBYODgwaCgoIAdXV1ALy8vK7//////Pz8+/39/f78/Pz4/////6urq2Z4eHgAAHJycgChoaFn+/v7/v7+/vn+/v79/v7+/v7+/v7x8fH/oKCgbnd3dwt0dHQAdHR0AHR0dAB0dHQAeHh4AIGBgQB/f38AgICAAH9/fwCBgYEAeHh4AHR0dAB0dHQAdHR0AHNzcwB2dnYKnp6ebfLy8v/+/v7+/v7+/v7+/v3////5+vr6/p6enmJ6enoAAHl5eQCQkJBX7e3t//////z9/f3+//////7+/v7////++fn5/9PT08XOzs6czs7OnczMzJnOzs6dsLCwYHh4eACBgYEDgICAAIGBgQN4eHgAsLCwYM7Ozp3MzMyZzs7Onc3NzZzT09PF9vb2//////7+/v7+//////39/f7+/v787e3t/46OjlJ9fX0AAICAgAB+fn4m4+Pj4/7+/v/8/Pz8/v7+///////+/v7//////P//////////////////////////1NTUqXNzcwCCgoIFgICAAIKCggVzc3MA1NTUqf///////////////////////////////P7+/v///////v7+//z8/Pz+/v7/4uLi4X19fSKAgIAAAIKCggZ3d3cAxsbGtf////79/f36/f39/v7+/v7//////v7+/vz8/Pv8/Pz6/Pz8+vn5+fX8/Pz6zMzMmnR0dACBgYEEgICAAIGBgQR0dHQAzMzMmvz8/Pr5+fn1/Pz8+vz8/Pr8/Pz7/v7+/v/////+/v7+/f39/v39/fr////+xcXFs3Z2dgCBgYEDAICAgAZ8fHwAlZWVavz8/P/+/v79/v7+/f7+/v7///////////////////////////z8/Pr/////zs7OnXR0dACBgYEFgICAAIGBgQV0dHQAzs7Onf/////8/Pz6///////////////////////////+/v7+/v7+/f7+/v38/Pz/lJSUanx8fACAgIACAH9/fwB/f38AfX19A9XV1eL////9/f39/P/////+/v7+//////////////////////z8/Pn+/v7+zs7Om3R0dACCgoIFgICAAIKCggV0dHQAzs7Om/7+/v77+/v5//////////////////////7+/v7//////f39/P////3V1dXhfX19BX9/fwB/f38AAICAgACAgIABenp6AJmZmWT4+Pj//f39+v39/f7///////////////////////////v7+/r/////09PTxHV1dQmCgoIAgoKCBoKCggB2dnYK09PTxf/////8/Pz6///////////////////////////9/f3+/f39+vf39/+ZmZlhe3t7AICAgAGAgIAAAICAgAB/f38AgICAAHl5eQDCwsK3//////z8/Pr+/v7//v7+/v////////////////39/f3+/v779fX1/Z6enm12dnYCd3d3AHV1dQKenp5s9fX1/f7+/vv+/v79/////////////////v7+/v7+/v78/Pz6/////8HBwbV5eXkAgICAAH9/fwCAgIAAAICAgACAgIAAgICAAX5+fgCBgYEr2tra6//////9/f38///////////+/v7+///////////+/v7+/////vf39/+9vb2vrKysYL29va3z8/P//////v7+/v7///////////7+/v7///////////39/fz/////2dnZ6ICAgCh+fn4AgICAAYCAgACAgIAAAICAgACAgIAAf39/AICAgAF8fHwAiIiIO+Dg4PL//////Pz8+v7+/v7//////v7+/v7+/v7//////v7+/v////7////////////////////+/v7+/v/////+/v7+/v7+/v/////+/v7//Pz8+v/////g4ODyhoaGOnx8fACAgIABf39/AICAgACAgIAAAICAgACAgIAAgICAAH9/fwCAgIADe3t7AIeHhz7Z2dno//////7+/vn9/f39/v7+/v7+/v7+/v7+/v7+/v7+/v/8/Pz8/Pz8+vz8/Pz+/v7//v7+/v7+/v7+/v7+/v7+/v39/f3+/v76/////9ra2uqIiIhCe3t7AICAgAN/f38AgICAAICAgACAgIAAAICAgACAgIAAgICAAICAgAB/f38AgICAA3x8fACBgYEowcHBuPr6+v///////////f39/fv9/f38/f39/v7+/v7+/v7+/v7+/v7+/v7+/v7+/f39/v39/fz9/f37/////f/////6+vr/wsLCtoKCgit8fHwAgICAA39/fwCAgIAAgICAAICAgACAgIAAAICAgACAgIAAgICAAICAgAB/f38Af39/AICAgAF+fn4AeXl5BpmZmWTU1NTh+vr6/////////////////P////n9/f35/Pz8+f39/fn////5/////P//////////+vr6/9PT0+CZmZlieXl5BX5+fgCAgIABf39/AH9/fwCAgIAAgICAAICAgACAgIAAAICAgACAgIAAgICAAICAgACAgIAAgICAAH9/fwCAgIACgYGBAHt7ewB+fn4ElJSUasbGxrTh4eHh7e3t//n5+f/////////////////5+fn/7e3t/+Dg4ODFxcW0lJSUan19fQR7e3sAgYGBAICAgAJ/f38AgICAAICAgACAgIAAgICAAICAgACAgIAAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgAB/f38AgICAAYGBgQGAgIAAfHx8AHd3dwB+fn4jjo6OU56enmGsrKxmsbGxZqysrGaenp5hjo6OU319fSJ2dnYAfHx8AICAgACBgYEBgICAAX9/fwCAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgAB/f38AgICAAoGBgQSAgIAAfn5+AHt7ewB5eXkAeHh4AHl5eQB7e3sAfn5+AIGBgQCCgoIEgICAAn9/fwCAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAANt0BcM8TJ0kAAAAASUVORK5CYII=
'''
iconAdd0 = base64.b64decode(iconAddB64)
iconAdd  = PhotoImage(data=iconAdd0)


iconDelB64 = '''\
    iVBORw0KGgoAAAANSUhEUgAAACMAAAAjCAYAAAAe2bNZAAAACXBIWXMAAA7EAAAOxAGVKw4bAAATUklEQVR42gFHE7jsAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAgICAAIB/fwB9fn4AhICACu7l5dT//////v7+/v///////////////////////////v7+/v/////u5OTUhICACn1+fgCAf38AgICAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAgICAAIB/fwB5enoAmZOTK/38/Pr+/f38/fz8/P79/fz+/f38/v39/P79/fz+/f38/fz8/P79/fz9/Pz6mZOTK3l6egCAf38AgICAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgAF4eXkAn5eXNP//////////////////////////////////////////////////////////n5eXNHh5eQCAgIABgICAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAAICAgACAgIAAgICAAH+AgAB/f38AgYGBAoGBgQOBgYECgYGBA4GBgQN8fX0DmJGRJ+Td3cLk3d3C5N3dwuTd3cLk3d3C5N3dwuTd3cLk3d3C5N3dwuTd3cLk3d3CmJGRJ3x9fQOBgYEDgYGBA4GBgQKBgYEDgYGBAn9/fwB/gIAAgICAAICAgACAgIAAAICAgACAgIAAf39/AICAgAB/gIAAeHl5AHd3dwB3eHcAd3d3AHd3dwB3eHgAdnZ2AHNxcQBzcXEAc3FxAHNxcQBzcXEAc3FxAHNxcQBzcXEAc3FxAHNxcQBzcXEAdnZ2AHd4eAB3d3cAd3d3AHd4dwB3d3cAeHl5AH+AgACAgIAAf39/AICAgACAgIAAAICAgACAgIAAgICAAH5+fgB+fHwAop2dQKuoqFerp6hWq6ioVquoqFarqKhWq6ioVquoqFarqKhWq6ioVquoqFarqKhWq6ioVquoqFarqKhWq6ioVquoqFarqKhWq6ioVquoqFarqKhWq6ioVqunqFarqKhXop2dQH58fAB+fn4AgICAAICAgACAgIAAAICAgACAgIAAf39/AXt5egDRyMiZ/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////9HHx5l7eXkAf39/AYCAgACAgIAAAICAgACAgIAAent7AJGNjR////////////7+/v3+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v7+/v79//////////+RjY0fent7AICAgACAgIAAAICAgACAgIAAeXp6AJWTkyv///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////+Vk5MreXp6AICAgACAgIAAAICAgACAgIAAent7AJSRkSf++fn4/vr6+P76+vj++vr4/vr6+P76+vj++vr4/vr6+P76+vj++vr4/vr6+P76+vj++vr4/vr6+P76+vj++vr4/vr6+P76+vj++vr4/vr6+P76+vj++vr4/vr6+P76+vj++vr4/vr6+P75+fiUkZEnent7AICAgACAgIAAAICAgACAgIAAf39/AIOBgQSSjIwdkoyMHY+KihePiYoXj4qKF4+JihePiYoXj4mKF4+JihePiYoXj4mKF4+JihePiooXj4mKF4+JihePiYoXj4qKF4+JihePiYoXj4mKF4+JihePiYoXj4qKF4+JihePiooXkoyMHZKMjB2DgYEEf39/AICAgACAgIAAAICAgACAgIAAgICAAH9/fwB7fHwAe3x8AISEhAqFhYUMhYWFDIWFhQyFhYUMhYWFDIWFhQyFhYUMhYWFDIWFhQyFhYUMhYWFDIWFhQyFhYUMhYWFDIWFhQyFhYUMhYWFDIWFhQyFhYUMhYWFDIWFhQyEhIQKfHx8AHt8fAB/f38AgICAAICAgACAgIAAAICAgACAgIAAgICAAICAgAB+fn4AgX9/Aurk5ND49/fx9/X18Pj29vH49vbx+Pb28fj29vH49vbx+Pb28fj29vH49vbx+Pb28fj39/H49vbx+Pb28fj29vH49vbx+Pb28fj29vH49vbx9/X18Pj39/Ho4+POgX5+AX5+fgCAgIAAgICAAICAgACAgIAAAICAgACAgIAAgICAAICAgAB/f38Afnt7AOvm5tP////////////////////////////////////////////////////////////////////////////////////////////////////////////////p5OTPfXt7AH9/fwCAgIAAgICAAICAgACAgIAAAICAgACAgIAAgICAAICAgAB/f38Aenl5AOHc3L///////v39/P/+/v///////v7+/v/+/v/////////////////+/v7+//7+//7+/v7//////////////////////v7+/v///////v7//f39/P/////f2dm6eXh4AICAgACAgIAAgICAAICAgACAgIAAAICAgACAgIAAgICAAICAgACAgIABeHd3ANnU1K///////v7++////////v7//v7+/f/+/v6zrKxfpZ6eQ/z6+vj+/v7+//7+//7+/v78+vr4o52dQbWtrWL//v7//v7+/f/+/v///////v7++//////W0NCod3d3AICAgAGAgIAAgICAAICAgACAgIAAAICAgACAgIAAgICAAICAgACBgYECdnZ2ANHLzJ7//////v7+/P///////v7////////9/f2PiYkVfnx8APfy8un///////39///////z8PDnent6AJCKihn//f3////////9/f///v7//v7+/P/////Nx8eWdnZ2AIGBgQKAgIAAgICAAICAgACAgIAAAICAgACAgIAAgICAAICAgACAgIADdXV1AMnDw43//////v7+/P/+/v///v7//v7+/v/8/PyVj48ghYKCBfjz8+r+/v7+//7+//7+/v7y8PDogIGAApaQkCT//Pz//v7+/v/+/v///////v7++//////Evr6DdXV1AICBgQOAgIAAgICAAICAgACAgIAAAICAgACAgIAAgICAAICAgACBgYECdnV1AMC6unv//////v7++////////v7////////9/f2Vj48ghYKCBfjz8+r///////7+///////z8fHogIGAApaQkCT//f3////////+/v///v7//v7+/P////+6tLRxdXZ2AIGBgQKAgIAAgICAAICAgACAgIAAAICAgACAgIAAgICAAICAgACBgYECdXZ2ALexsWr//////v39/P/+/v///f3////////9/f2Vj48ghYKCBfjz8+r///////7+///////z8fHogIGAApaQkCT//f3////////+/v///f3//f39/f////+yq6tednd3AICAgAOAgIAAgICAAICAgACAgIAAAICAgACAgIAAgICAAICAgACAgIADdnd3AK6pqVj//////f7+/f/9/f///v7////////9/f2Vj48ghYKCBfjz8+r///////7+///////z8fHogICAApaQkCT//f3////////+/v///v7//v7+/v/+/v+ooqNMd3h4AIGBgQKAgIAAgICAAICAgACAgIAAAICAgACAgIAAgICAAICAgACBgYECd3h4AKagoUj//v7//v7+/v/+/v///v7////////9/f2Vj48ghYKCBfjz8+r///////7+///////z8fHogIGAApaQkCT//f3////////+/v///f3///////7///+fmpo7eHl5AICAgAGAgIAAgICAAICAgACAgIAAAICAgACAgIAAgICAAICAgACAgIABeHl5AJ6ZmTj+///////////9/f///v7////////9/f2Vj48ghYKCBfjz8+r///////7+///////z8fHogICAApaQkCT//f3////////+/v///v7//v7+/v/+/v+Yk5MreXp6AIB/fwCAgIAAgICAAICAgACAgIAAAICAgACAgIAAgICAAICAgACAf38AeXp6AJeSkin//v7//v///v/+/v///v7////////9/f2Vj48ghYKCBfjz8+r///////7+///////z8fHogH+AApaQkCT//f3////////+/v///v7///////36+vqQjIwdent7AH+AgACAgIAAgICAAICAgACAgIAAAICAgACAgIAAgICAAICAgAB/gIAAent7AJCMjBz9+vr5///////+/v///v7////////9/f2Vj48ghYKCBfjz8+r///////7+///////z8fHogICAApaQkCT//f3////////+/v/+/f3///////j19e+JhoYRe3x8AICAgACAgIAAgICAAICAgACAgIAAAICAgACAgIAAgICAAICAgACAgIAAe3x8AImGhhH49PXv//////79/f7//v7////////9/f2Vj48ghYKCBfjz8+r///////7+///////z8fHogICAApaQkCT//f3////////+/v///v7///////Pu7uOEgYEGfX19AICAgACAgIAAgICAAICAgACAgIAAAICAgACAgIAAgICAAICAgACAgIAAfX19AISBgQbz7+/k///////+/v///v7////////9/f2Vj48ghYKCBfjz8+r///////7+///////z8fHogICAApaQkCT//f3////////+/v/+/v7+/////+zn59V/fX0Afn9/AICAgACAgIAAgICAAICAgACAgIAAAICAgACAgIAAgICAAICAgACAgIAAfn5+AIB9fQDt6OjY//////7+/v7//v7//v///v/9/f2Vj48ghYKCBfjz8+r///////7+///////z8fHogICAApaQkCT//f3//v7+/v/+/v/+/v79/////+Xf38Z8enoAf39/AICAgACAgIAAgICAAICAgACAgIAAAICAgACAgIAAgICAAICAgACAgIAAf39/AHx6egDm4eHJ//////7+/v3//v7////////8/PyUjo4ehIGBBPfy8uj///////39///////y8PDmf39/AZWPjyL//Pz////////+/v/9/v78/////9zW17V4eHgAgICAAYCAgACAgIAAgICAAICAgACAgIAAAICAgACAgIAAgICAAICAgACAgIAAgICAAHl4eADe2dm5//////3+/vz//f3//v7+/v/9/f2Si4wcgXx8APn19e7+/v7+//7+//7+/v728/Ptfnt7AJSNjR///f3//v7+/v/9/f/+/v79/////9TOzqN2dnYAgYGBAoCAgACAgIAAgICAAICAgACAgIAAAICAgACAgIAAgICAAICAgACAgIAAgICAAXd3dwDW0dGp//////7+/v3//v7//v7+/f/////j3d3C3NXWs//+/v/+/v7+//7+//7+/v7//v7/3NXVsuTe3sP//////v39/f/+/v/+/v79/////8rFxZF1dXUAgYGBA4CAgACAgIAAgICAAICAgACAgIAAAICAgACAgIAAgICAAICAgACAgIAAgYGBAnZ2dgDOyMiY//////7+/v3///////7+///+/v7//////////////////v7////////+/v/+/////////////////v7///7+///////+/v79//7+/8G7u352dXUAgICAAoCAgACAgIAAgICAAICAgACAgIAAAICAgACAgIAAgICAAICAgACAgIAAgYGBA3V1dQDIwcGK//////39/fz//////v///v/////+/v79/f39/P/////+///+//7+//7///7//////f39/P7+/v3//////v///v/+/v/9/f38/////7qzs291dnYAgYGBA4CAgACAgIAAgICAAICAgACAgIAAAICAgACAgIAAgICAAICAgACAgIAAgICAAnZ3dwCyrK1g/v7+/v7+/v3//v7+//////////////////////////////////////////////////////////////////////7+/v7+/v79/v39/aagoEd3eHgAgICAAoCAgACAgIAAgICAAICAgACAgIAAAICAgACAgIAAgICAAICAgACAgIAAgH9/AH5+fgCAfX0F5tzcxf7////+/v79//////////////////////////////////////////////////////////////////7+//7+/v3/////3tLSsX16egB/f38Bf39/AICAgACAgIAAgICAAICAgACAgIAAPsPVMoHn1bMAAAAASUVORK5CYII=
'''
iconDel0 = base64.b64decode(iconDelB64)
iconDel  = PhotoImage(data=iconDel0)


iconDelListB64 = '''\
    iVBORw0KGgoAAAANSUhEUgAAACMAAAAjCAYAAAAe2bNZAAAACXBIWXMAAAsTAAALEwEAmpwYAAATUklEQVR42gFHE7jsAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAAICAgACAgIAAgICAAH9/fwCBgYECgoKCBYKCggWAgIABf39/AH9/fwCBgYEDgoKCBYKCggSCgoIFgoKCBYKCggWCgoIFgoKCBYKCggWCgoIFgoKCBYKCggWCgoIFgoKCBYKCggWCgoIFgoKCBYKCggWCgoIFgICAAH9/fwCAgIAAgICAAICAgACAgIAAAICAgACAgIAAf39/AIGBgQB5eXkAdHR0AHR0dAB7e3sAgICAAICAgAB3d3cAdHR0AHR0dAB0dHQAdHR0AHR0dAB0dHQAdHR0AHR0dAB0dHQAdHR0AHR0dAB0dHQAdHR0AHR0dAB0dHQAdHR0AHR0dAB0dHQAf39/AICAgACAgIAAgICAAICAgACAgIAAAICAgACAgIAAgYGBA3h4eACqqqpV0dHRo9HR0aOcnJw6enp6AHt7ewC8vLx60dHRo9DQ0KHR0dGj0dHRo9HR0aPR0dGj0dHRo9HR0aPR0dGj0dHRo9HR0aPR0dGj0dHRo9HR0aPR0dGj0dHRo9HR0aPR0dGjhoaGDX5+fgCAgIAAgICAAICAgACAgIAAAICAgACAgIAAgoKCBXNzcwDGxsaN//////////+vr69gd3d3AHh4eADk5OTK////////////////////////////////////////////////////////////////////////////////////////////////ioqKFnx8fACAgIABgICAAICAgACAgIAAAICAgACAgIAAgoKCBXNzcwDFxcWM//////////+vr69fd3d3AHh4eADk5OTJ////////////////////////////////////////////////////////////////////////////////////////////////ioqKFnx8fACAgIABgICAAICAgACAgIAAAICAgACAgIAAgICAAXx8fACQkJAhn5+fQJ+fn0CLi4sWfX19AH5+fgCXl5cvn5+fQJ+fnz+fn59An5+fQJ+fn0Cfn59An5+fQJ+fn0Cfn59An5+fQJ+fn0Cfn59An5+fQJ+fn0Cfn59An5+fQJ+fn0Cfn59AgoKCBX9/fwCAgIAAgICAAICAgACAgIAAAICAgACAgIAAf39/AICAgAB8fHwAeXl5AHl5eQB9fX0AgICAAICAgAB7e3sAeXl5AHl5eQB5eXkAeXl5AHl5eQB5eXkAeXl5AHl5eQB5eXkAeXl5AHl5eQB5eXkAeXl5AHl5eQB5eXkAeXl5AHl5eQB5eXkAf39/AICAgACAgIAAgICAAICAgACAgIAAAICAgACAgIAAf39/AICAgAB9fX0AfHx8AHx8fAB+fn4AgICAAICAgAB9fX0AfHx8AHx8fAB8fHwAfHx8AHx8fAB8fHwAfHx8AHx8fAB8fHwAfHx8AHx8fAB8fHwAfHx8AHx8fAB8fHwAfHx8AHx8fAB8fHwAf39/AICAgACAgIAAgICAAICAgACAgIAAAICAgACAgIAAgYGBBHV1dQC3t7dw6+vr1+vr69empqZNeXl5AHp6egDQ0NCh6+vr1+np6dXr6+vX6+vr1+vr69fr6+vX6+vr1+vr69fr6+vX6+vr1+vr69fr6+vX6+vr1+vr69fr6+vX6+vr1+vr69fr6+vXiIiIEX19fQCAgIAAgICAAICAgACAgIAAAICAgACAgIAAgoKCBXNzcwDExMSK//////////+urq5ed3d3AHh4eADj4+PH////////////////////////////////////////////////////////////////////////////////////////////////ioqKFXx8fACAgIABgICAAICAgACAgIAAAICAgACAgIAAgYGBBHR0dADAwMCC/f39+/39/fusrKxZeHh4AHl5eQDd3d28/f39+/v7+/j9/f37/f39+/39/fv9/f37/f39+/39/fv9/f37/f39+/39/fv9/f37/f39+/39/fv9/f37/f39+/39/fv9/f37iYmJFH19fQCAgIAAgICAAICAgACAgIAAAICAgACAgIAAgICAAH9/fwCFhYUKiYmJE4mJiRODg4MHf39/AH9/fwCHh4cOiYmJE4mJiROJiYkTiYmJE4mJiROJiYkTiYmJE4mJiROJiYkTiYmJE4mJiRKJiYkSiYmJE4mJiROJiYkTiYmJE4mJiRKJiYkSgYGBAoCAgACAgIABgICAAH9/fwCAgIAAAICAgACAgIAAf39/AICAgAB9fX0Ae3t7AHt7ewB+fn4AgICAAICAgAB8fHwAe3t7AHt7ewB7e3sAe3t7AHt7ewB7e3sAe3t7AHt7ewB7e3sAfHx8AH19fQB9fX0Ae3t7AHt7ewB7e3sAfn5+AH19fQB+fn4AfX19AH19fQB9fX0Af39/AICAgACAgIAAAICAgACAgIAAgICAAH9/fwCEhIQKiYmJE4mJiRODg4MHf39/AH9/fwCHh4cOiYmJE4mJiROJiYkTiYmJE4mJiROJiYkTiYmJE4mJiROJiYkThISECH9/fwB/f38Ah4eHDomJiROJiYkTe3t7AIODgwZ7e3sAh4eHD4mJiRKIiIgRgICAAH9/fwCAgIAAAICAgACAgIAAgYGBBHR0dADAwMCC/f39+/39/fusrKxZeHh4AHl5eQDd3d28/f39+/v7+/j9/f37/f39+/39/fv9/f37/f39+/r6+vX9/f37r6+vYHd3dwB4eHgA2tratv39/fz+/v79sbGxZWpqagCWlpYt9vb27f7+/v319fXrgYGBA39/fwCAgIAAAICAgACAgIAAgoKCBXNzcwDExMSK//////////+urq5ed3d3AHh4eADj4+PH////////////////////////////////////////////////srKyZnZ2dgB3d3cA39/fwP39/fz+/v79/////8jIyJ319fXr//////7+/v36+vr2goKCBH5+fgCAgIAAAICAgACAgIAAgYGBBHV1dQC3t7dw6+vr1+vr69empqZNeXl5AHp6egDQ0NCh6+vr1+np6dXr6+vX6+vr1+vr69fr6+vX6+vr1+jo6NLr6+vXqKioUnh4eAB4eHgAz8/Pnv/////9/f37/v7+/f///////////f39+//////s7OzZf39/An9/fwCAgIAAAICAgACAgIAAf39/AICAgAB9fX0AfHx8AHx8fAB+fn4AgICAAICAgAB9fX0AfHx8AHx8fAB8fHwAfHx8AHx8fAB8fHwAfHx8AHx8fAB8fHwAfn5+AICAgAB/f38Be3t7ANHR0aT//////f39/Pz8/Pr8/Pz6/f39/OTk5MmIiIgbfHx8AoCAgAGAgIAAAICAgACAgIAAf39/AICAgAB8fHwAeXl5AHl5eQB9fX0AgICAAICAgAB7e3sAeXl5AHl5eQB5eXkAeXl5AHl5eQB5eXkAeXl5AHl5eQB5eXkAfX19AICAgACBgYEDcnJyAJmZmTT//////Pz8+v/////7+/v4/////76+vn1sbGwAgoKCBYCAgACAgIAAAICAgACAgIAAgICAAXx8fACQkJAhn5+fQJ+fn0CLi4sWfX19AH5+fgCXl5cvn5+fQJ+fnz+fn59An5+fQJ+fn0Cfn59An5+fQJ+fnz6fn59AjIyMGH19fQB8fHwAmZmZM/j4+PP+/v7+/v7+/f39/fz+/v79/f39+v39/fyysrJne3t7AYCAgAKAgIAAAICAgACAgIAAgoKCBXNzcwDFxcWM//////////+vr69fd3d3AHh4eADk5OTJ////////////////////////////////////////////////srKyZ3Z2dgB3d3cA4ODgwv7+/vz6+vr1/////////////////Pz8+f39/fv7+/v5goKCBH5+fgCAgIAAAICAgACAgIAAgoKCBXNzcwDGxsaN//////////+vr69gd3d3AHh4eADk5OTK////////////////////////////////////////////////s7OzaHZ2dgB3d3cA4eHhxP//////////7e3t3IqKiizS0tKm///////////+/v7/goKCBH5+fgCAgIAAAICAgACAgIAAgYGBA3h4eACqqqpV0dHRo9HR0aOcnJw6enp6AHt7ewC8vLx60dHRo9DQ0KHR0dGj0dHRo9HR0aPR0dGj0dHRo8/Pz5/R0dGjnp6ePnp6egB6enoAu7u7dtHR0aPR0dGji4uLGHZ2dgB8fHwAysrKlNHR0aPMzMyZgYGBAn9/fwCAgIAAAICAgACAgIAAf39/AIGBgQB5eXkAdHR0AHR0dAB7e3sAgICAAICAgAB3d3cAdHR0AHR0dAB0dHQAdHR0AHR0dAB0dHQAdHR0AHR0dAB0dHQAe3t7AICAgACAgIAAd3d3AHR0dAB0dHQAfn5+AIGBgQKAgIAAdXV1AHR0dAB0dHQAf39/AICAgACAgIAAAICAgACAgIAAgICAAH9/fwCBgYECgoKCBYKCggWAgIABf39/AH9/fwCBgYEDgoKCBYKCggSCgoIFgoKCBYKCggWCgoIFgoKCBYKCggSCgoIFgICAAX9/fwB/f38AgYGBA4KCggWCgoIFgICAAH9/fwCAgIAAgoKCBIKCggWCgoIEgICAAH9/fwCAgIAAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAoxqsVDrhtCgAAAAASUVORK5CYII=
'''
iconDelList0 = base64.b64decode(iconDelListB64)
iconDelList  = PhotoImage(data=iconDelList0)


iconTopB64 = '''\
    iVBORw0KGgoAAAANSUhEUgAAACMAAAAjCAYAAAAe2bNZAAAACXBIWXMAAAsTAAALEwEAmpwYAAATUklEQVR42gFHE7jsAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAAICAgACAgIAAgICAAICAgACAgIAAgICAAH9/fwCAgIABgYGBAoCAgACAgIABgICAAYCAgAGAgIABgICAAYCAgAGAgIABgICAAYCAgAGAgIABgICAAYCAgAGAgIABgICAAYCAgAGAgIAAgYGBAoCAgAF/f38AgICAAICAgACAgIAAgICAAICAgACAgIAAAICAgACAgIAAgICAAICAgACAgIAAf39/AICAgAB9fX0AeXl5AHt7ewB6enoAe3t7AHt7ewB7e3sAe3t7AHt7ewB7e3sAe3t7AHt7ewB7e3sAe3t7AHt7ewB7e3sAe3t7AHp6egB7e3sAeXl5AH19fQCAgIAAf39/AICAgACAgIAAgICAAICAgACAgIAAAICAgACAgIAAgICAAICAgACAgIAAgICAAX19fQCJiYkW1NTUqeDg4MHf39/A4ODgweDg4MHg4ODB4ODgweDg4MHg4ODB4ODgweDg4MHg4ODB4ODgweDg4MHg4ODB4ODgwd/f38Dg4ODB1NTUqYmJiRZ9fX0AgICAAYCAgACAgIAAgICAAICAgACAgIAAAICAgACAgIAAgICAAICAgACAgIAAgoKCBHV1dQDBwcGC/////////////////////////////////////////////////////////////////////////////////////////////////////8HBwYJ1dXUAgoKCBICAgACAgIAAgICAAICAgACAgIAAAICAgACAgIAAgICAAICAgACAgIAAgYGBAnl5eQChoaFF+Pj48v7+/v7////////////////////////////////////////////////////////////////////////////////+/v7++Pj48qGhoUV5eXkAgYGBAoCAgACAgIAAgICAAICAgACAgIAAAICAgACAgIAAgICAAICAgACAgIAAf39/AICAgAB7e3sAj4+PH5eXly+Xl5cul5eXL5eXly+Xl5cvl5eXL5eXly+Xl5cvmJiYMJeXly+Xl5cvl5eXL5eXly+Xl5cvl5eXL5eXly6Xl5cvj4+PH3t7ewCAgIAAf39/AICAgACAgIAAgICAAICAgACAgIAAAICAgACAgIAAgICAAICAgACAgIAAgICAAH9/fwCAgIABfHx8AHp6egB6enoAenp6AHp6egB6enoAenp6AHt7ewB6enoAd3d3AHp6egB7e3sAenp6AHp6egB6enoAenp6AHp6egB6enoAfHx8AICAgAF/f38AgICAAICAgACAgIAAgICAAICAgACAgIAAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgAB/f38AgICAAYGBgQKAgIABgYGBAoGBgQKAgIABgoKCA39/fwB+fn4AjIyMGH5+fgB/f38AgoKCA4CAgAGBgYECgYGBAoCAgAGBgYECgICAAX9/fwCAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAgICAAH9/fwCBgYEBfX19AH5+fgXW1tau+fn58tbW1q5+fn4FfX19AIGBgQF/f38AgICAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAf39/AIGBgQF9fX0Afn5+Bdvb27b//////v7+/P/////b29u2fn5+BX19fQCBgYEBf39/AICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgAB/f38AgYGBAX19fQB9fX0E29vbtv/////8/Pz5/v7+/vz8/Pn/////29vbtn19fQR9fX0AgYGBAX9/fwCAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAgICAAH9/fwCBgYEBfX19AH5+fgXb29u2//////v7+/j//////v7+/v/////7+/v4/////9vb27Z+fn4FfX19AIGBgQF/f38AgICAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAf39/AIGBgQF9fX0AfX19BNvb27b//////Pz8+P/////+/v7+//////7+/v7//////Pz8+P/////b29u2fX19BH19fQCBgYEBf39/AICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgAB/f38AgYGBAX19fQB+fn4F29vbtv/////7+/v2/////8TExInv7+/e/////+/v797ExMSJ//////v7+/b/////29vbtn5+fgV9fX0AgYGBAX9/fwCAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAAICAgACAgIAAgICAAICAgACAgIAAgICAAH9/fwCBgYEBfX19AH19fQTb29u2//////r6+vb/////vb29e3t7ewDz8/Pn//////Pz8+d7e3sAvb29e//////6+vr2/////9vb27Z9fX0EfX19AIGBgQF/f38AgICAAICAgACAgIAAgICAAICAgACAgIAAAICAgACAgIAAgICAAICAgACAgIAAf39/AICAgAB9fX0Afn5+Bdvb27b/////+vr69v////+/v79/dHR0AIaGhg3z8/Pn//////Pz8+eGhoYNdHR0AL+/v3//////+vr69v/////b29u2fn5+BX19fQCAgIAAf39/AICAgACAgIAAgICAAICAgACAgIAAAICAgACAgIAAgICAAICAgACAgIAAgICAAH9/fwF+fn4I29vbtv/////6+vr2/////7+/v352dnYAf39/AYWFhQvy8vLm//////Ly8uaFhYULf39/AXZ2dgC/v79+//////r6+vb/////29vbtn5+fgh/f38BgICAAICAgACAgIAAgICAAICAgACAgIAAAICAgACAgIAAgICAAICAgACAgIAAgYGBBHZ2dgC4uLhx//////r6+vT/////vr6+fnZ2dgCBgYEEfn5+AISEhArz8/Pn//////Pz8+eEhIQKfn5+AIGBgQR2dnYAvr6+fv/////6+vr0/////7i4uHF2dnYAgYGBBICAgACAgIAAgICAAICAgACAgIAAAICAgACAgIAAgICAAICAgACAgIAAgYGBA3d3dwCxsbFl//////////++vr5+dXV1AICAgAOAgIABfX19AIWFhQvz8/Pn//////Pz8+eFhYULfX19AICAgAGAgIADdXV1AL6+vn7//////////7GxsWV3d3cAgYGBA4CAgACAgIAAgICAAICAgACAgIAAAICAgACAgIAAgICAAICAgACAgIAAgICAAH9/fwB9fX0Aq6urWKmpqVJ5eXkAgICAAoCAgAB/f38Afn5+AIWFhQvz8/Pn//////Pz8+eFhYULfn5+AH9/fwCAgIAAgICAAnl5eQCpqalSq6urWH19fQB/f38AgICAAICAgACAgIAAgICAAICAgACAgIAAAICAgACAgIAAgICAAICAgACAgIAAf39/AICAgAB/f38Ad3d3AHh4eACAgIABgICAAH9/fwCAgIABfn5+AIWFhQvz8/Pn//////Pz8+eFhYULfn5+AICAgAF/f38AgICAAICAgAF4eHgAd3d3AH9/fwCAgIAAf39/AICAgACAgIAAgICAAICAgACAgIAAAICAgACAgIAAgICAAICAgACAgIAAgICAAH9/fwCAgIAAgYGBA4GBgQN/f38Af39/AICAgACAgIABfn5+AIWFhQvz8/Pn//////Pz8+eFhYULfn5+AICAgAGAgIAAf39/AH9/fwCBgYEDgYGBA4CAgAB/f38AgICAAICAgACAgIAAgICAAICAgACAgIAAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIABfn5+AIWFhQvz8/Pn//////Pz8+eFhYULfn5+AICAgAGAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIABfn5+AIWFhQvz8/Pn//////Pz8+eFhYULfn5+AICAgAGAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIABfn5+AIWFhQvz8/Pn//////Pz8+eFhYULfn5+AICAgAGAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIABfn5+AIWFhQvz8/Pn//////Pz8+eFhYULfn5+AICAgAGAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIABfn5+AIWFhQvz8/Pn//////Pz8+eFhYULfn5+AICAgAGAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAfn5+AISEhAry8vLm//////Ly8uaEhIQKfn5+AICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIABfX19AIWFhQvy8vLm/f39+/Ly8uWFhYULfX19AICAgAGAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAfn5+AIKCggj19fXs//////b29u2CgoIIfn5+AICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAgICAAnp6egCsrKxa39/fvrGxsWJ6enoAgICAAYCAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAf39/AICAgAB6enoAenp6AHl5eQCAgIAAf39/AICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAgICAAH9/fwCBgYECgICAAYGBgQJ/f38AgICAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAxXv5thJU+MAAAAAASUVORK5CYII=
'''
iconTop0 = base64.b64decode(iconTopB64)
iconTop  = PhotoImage(data=iconTop0)


iconDownB64 = '''\
    iVBORw0KGgoAAAANSUhEUgAAACMAAAAjCAYAAAAe2bNZAAAACXBIWXMAAAsTAAALEwEAmpwYAAATUklEQVR42gFHE7jsAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAgICAAH9/fwCBgYECgICAAYGBgQJ/f38AgICAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAf39/AICAgAB5eXkAenp6AHp6egCAgIAAf39/AICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAgICAAXp6egCxsbFi39/fvqysrFp6enoAgICAAoCAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAfn5+AIKCggj29vbt//////X19eyCgoIIfn5+AICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIABfX19AIWFhQvy8vLl/f39+/Ly8uaFhYULfX19AICAgAGAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAfn5+AISEhAry8vLm//////Ly8uaEhIQKfn5+AICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIABfn5+AIWFhQvz8/Pn//////Pz8+eFhYULfn5+AICAgAGAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIABfn5+AIWFhQvz8/Pn//////Pz8+eFhYULfn5+AICAgAGAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIABfn5+AIWFhQvz8/Pn//////Pz8+eFhYULfn5+AICAgAGAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIABfn5+AIWFhQvz8/Pn//////Pz8+eFhYULfn5+AICAgAGAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIABfn5+AIWFhQvz8/Pn//////Pz8+eFhYULfn5+AICAgAGAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAAICAgACAgIAAgICAAICAgACAgIAAgICAAH9/fwCAgIAAgYGBA4GBgQN/f38Af39/AICAgACAgIABfn5+AIWFhQvz8/Pn//////Pz8+eFhYULfn5+AICAgAGAgIAAf39/AH9/fwCBgYEDgYGBA4CAgAB/f38AgICAAICAgACAgIAAgICAAICAgACAgIAAAICAgACAgIAAgICAAICAgACAgIAAf39/AICAgAB/f38Ad3d3AHh4eACAgIABgICAAH9/fwCAgIABfn5+AIWFhQvz8/Pn//////Pz8+eFhYULfn5+AICAgAF/f38AgICAAICAgAF4eHgAd3d3AH9/fwCAgIAAf39/AICAgACAgIAAgICAAICAgACAgIAAAICAgACAgIAAgICAAICAgACAgIAAgICAAH9/fwB9fX0Aq6urWKmpqVJ5eXkAgICAAoCAgAB/f38Afn5+AIWFhQvz8/Pn//////Pz8+eFhYULfn5+AH9/fwCAgIAAgICAAnl5eQCpqalSq6urWH19fQB/f38AgICAAICAgACAgIAAgICAAICAgACAgIAAAICAgACAgIAAgICAAICAgACAgIAAgYGBA3d3dwCxsbFl//////////++vr5+dXV1AICAgAOAgIABfX19AIWFhQvz8/Pn//////Pz8+eFhYULfX19AICAgAGAgIADdXV1AL6+vn7//////////7GxsWV3d3cAgYGBA4CAgACAgIAAgICAAICAgACAgIAAAICAgACAgIAAgICAAICAgACAgIAAgYGBBHZ2dgC4uLhx//////r6+vT/////vr6+fnZ2dgCBgYEEfn5+AISEhArz8/Pn//////Pz8+eEhIQKfn5+AIGBgQR2dnYAvr6+fv/////6+vr0/////7i4uHF2dnYAgYGBBICAgACAgIAAgICAAICAgACAgIAAAICAgACAgIAAgICAAICAgACAgIAAgICAAH9/fwF+fn4I29vbtv/////6+vr2/////7+/v352dnYAf39/AYWFhQvy8vLm//////Ly8uaFhYULf39/AXZ2dgC/v79+//////r6+vb/////29vbtn5+fgh/f38BgICAAICAgACAgIAAgICAAICAgACAgIAAAICAgACAgIAAgICAAICAgACAgIAAf39/AICAgAB9fX0Afn5+Bdvb27b/////+vr69v////+/v79/dHR0AIaGhg3z8/Pn//////Pz8+eGhoYNdHR0AL+/v3//////+vr69v/////b29u2fn5+BX19fQCAgIAAf39/AICAgACAgIAAgICAAICAgACAgIAAAICAgACAgIAAgICAAICAgACAgIAAgICAAH9/fwCBgYEBfX19AH19fQTb29u2//////r6+vb/////vb29e3t7ewDz8/Pn//////Pz8+d7e3sAvb29e//////6+vr2/////9vb27Z9fX0EfX19AIGBgQF/f38AgICAAICAgACAgIAAgICAAICAgACAgIAAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgAB/f38AgYGBAX19fQB+fn4F29vbtv/////7+/v2/////8TExInv7+/e/////+/v797ExMSJ//////v7+/b/////29vbtn5+fgV9fX0AgYGBAX9/fwCAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAf39/AIGBgQF9fX0AfX19BNvb27b//////Pz8+P/////+/v7+//////7+/v7//////Pz8+P/////b29u2fX19BH19fQCBgYEBf39/AICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAgICAAH9/fwCBgYEBfX19AH5+fgXb29u2//////v7+/j//////v7+/v/////7+/v4/////9vb27Z+fn4FfX19AIGBgQF/f38AgICAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgAB/f38AgYGBAX19fQB9fX0E29vbtv/////8/Pz5/v7+/vz8/Pn/////29vbtn19fQR9fX0AgYGBAX9/fwCAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAf39/AIGBgQF9fX0Afn5+Bdvb27b//////v7+/P/////b29u2fn5+BX19fQCBgYEBf39/AICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAgICAAH9/fwCBgYEBfX19AH5+fgXW1tau+fn58tbW1q5+fn4FfX19AIGBgQF/f38AgICAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgAB/f38AgICAAYGBgQKAgIABgYGBAoGBgQKAgIABgoKCA39/fwB+fn4AjIyMGH5+fgB/f38AgoKCA4CAgAGBgYECgYGBAoCAgAGBgYECgICAAX9/fwCAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAAICAgACAgIAAgICAAICAgACAgIAAgICAAH9/fwCAgIABfHx8AHp6egB6enoAenp6AHp6egB6enoAenp6AHt7ewB6enoAd3d3AHp6egB7e3sAenp6AHp6egB6enoAenp6AHp6egB6enoAfHx8AICAgAF/f38AgICAAICAgACAgIAAgICAAICAgACAgIAAAICAgACAgIAAgICAAICAgACAgIAAf39/AICAgAB7e3sAj4+PH5eXly+Xl5cul5eXL5eXly+Xl5cvl5eXL5eXly+Xl5cvmJiYMJeXly+Xl5cvl5eXL5eXly+Xl5cvl5eXL5eXly6Xl5cvj4+PH3t7ewCAgIAAf39/AICAgACAgIAAgICAAICAgACAgIAAAICAgACAgIAAgICAAICAgACAgIAAgYGBAnl5eQChoaFF+Pj48v7+/v7////////////////////////////////////////////////////////////////////////////////+/v7++Pj48qGhoUV5eXkAgYGBAoCAgACAgIAAgICAAICAgACAgIAAAICAgACAgIAAgICAAICAgACAgIAAgoKCBHV1dQDBwcGC/////////////////////////////////////////////////////////////////////////////////////////////////////8HBwYJ1dXUAgoKCBICAgACAgIAAgICAAICAgACAgIAAAICAgACAgIAAgICAAICAgACAgIAAgICAAX19fQCJiYkW1NTUqeDg4MHf39/A4ODgweDg4MHg4ODB4ODgweDg4MHg4ODB4ODgweDg4MHg4ODB4ODgweDg4MHg4ODB4ODgwd/f38Dg4ODB1NTUqYmJiRZ9fX0AgICAAYCAgACAgIAAgICAAICAgACAgIAAAICAgACAgIAAgICAAICAgACAgIAAf39/AICAgAB9fX0AeXl5AHt7ewB6enoAe3t7AHt7ewB7e3sAe3t7AHt7ewB7e3sAe3t7AHt7ewB7e3sAe3t7AHt7ewB7e3sAe3t7AHp6egB7e3sAeXl5AH19fQCAgIAAf39/AICAgACAgIAAgICAAICAgACAgIAAAICAgACAgIAAgICAAICAgACAgIAAgICAAH9/fwCAgIABgYGBAoCAgACAgIABgICAAYCAgAGAgIABgICAAYCAgAGAgIABgICAAYCAgAGAgIABgICAAYCAgAGAgIABgICAAYCAgAGAgIAAgYGBAoCAgAF/f38AgICAAICAgACAgIAAgICAAICAgACAgIAAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAANE/5trYlCQ4AAAAASUVORK5CYII=
'''
iconDown0 = base64.b64decode(iconDownB64)
iconDown  = PhotoImage(data=iconDown0)


iconJoinB64 = '''\
    iVBORw0KGgoAAAANSUhEUgAAACMAAAAjCAYAAAAe2bNZAAAACXBIWXMAAA7EAAAOxAGVKw4bAAAFm0lEQVR42u1Y7U+bVRR/2s5EF4OOD4ZosixqXDJfov+AiV9m/B9M/KDJtkDmF56+0FdKC4yXUUop++RwwPgko+MtAxJKuwJmibKJUNAh5WVDJi+dJoO+PPX+nuc53dNaoJPGGOMNN5f73HPPOffcc37n3HI2m417ll5ZWanWarXc2NiYNcVaMplMCIIgjpjjO9ZB96y8uf+VOYoyVquVFNHY7fZjOp1Ow4Ta9lHGhnXQgV65/8jKECOLxcLhxEwQV1payg0PD/MQnkgk4lAGI+b4jnXQgR778lUoL41NRiPX3OJ5fWpqqjkUCtX5/f76SCRyG8KZIkkogxFzfMc66EDvbvG8aWT7C3hNFpXFYn1+aWUtmMrRoEyutryyFmL7XsD+gl6TsaKCc1bXvhx9/Mcq848kWUKQmjiSpeA/jG6N0Z+oYPv+9jXJm1RKBhiZM6q0PM9d6+o+q3BcQamMIGkiOnJHV/cnoMc+JR9ZjiqXcjmtAB+xWMy5GKl4JmDi2zsNpBBZRzmfnLrjAp1SKB0IDm2SfShbob9oZzaZuFZv2xlHdc1xvV6fxot0VJnNKrPFqnmwvvGdpIDkwBgxf7i+Mc3Wj4FO5PkUFtQGxs/hrDnuaW07AzkHWga4gBMFAoFqMG1yuU/z5eVszZpxbWDq8V55OxZPPJFcRHShZDye2G31XnkP69nXwvPl3OUm92l2iO/Bn5euUJOhDDSmzoDqOYYP6pGRET1OubsXi97w9X+h0+lF09K1gRbM+oduXZCxJoZxYOhWmSxETddiMhk57O/p7ft8dze2AzrwhxzIU8oXgYk6AdrQ0NCXgiJe787MXmfXVqyTYJ6spNbrDdyP4YUe0MyFF3yY47tsZZVOp8W1FN/9YbZLAQMC+CuBkTo3OTnpog6QCgaDrixAE31haye62H6t82Oel1AVwhDudQ2NrywurYzVNzSWIIzJSUF39evOs1vb0fvZvMAfciBPKZ9L5dGICdp4cKLaZLZo9LJfMEflbJVVajNG2Z/YutofCDlz7T+ocQhH6gRYWYAmKMENbWl5NeDxtn1gliOG8g/mLFLeX4qsBmQtUln7M4CRRup5WiYlMWF/bJOYENcfbU7bq5xFZBGM9ipH0cNfN6elkEcCTQlKHCqkZdKmvjcz1117qa7kqSKmtEI1tXUlzGGvZ19RwSxDgLYXi//u6xs8p2NRYzSKzioqUHup/gRGzPFdx/ym9+bAOdDLyJyfzwwODl6kjpDz+XwXw+HwTfkECTrN8uqDCbfH+64E8xKGGAx6Vlq0vrHx21aYlQpvYS6FvlVMG+4W7zsRlrkps4Mf/gd/yIE8pXwx1qkjQsrKyghn0qcJ3J6sRQTJwtSy06qMJrOKObNYVkSWV0Nsrsb3NPwbxMjSsAisUV4b+EMO5Cnl50Tg0dFRg4Qtj2Vs4cXEaUsjsE1EYH8wVCkhcDImhX3IoURgWxpz+AzMAf+cCJwrN/nHx+0LPy8OAj2VxTVBPE7xVXvHh3J0JZCaRIdkgq62d3yEdWXGpyK+ylFdPP/T/QHwJ6UPzNo4SePlptcsVhs5aUbtYWLZ1u5wvsis9guCXUJWihohtb0TjVQ5nEUmRVamQ4Af+DY0Nr1K2HRoPYP0nl0QUT2jZadmuaozs56hqJPm92Zmu0GXXc/QSFBwaD2jJMgujFBOfNPb92l2YSVbJqPAutHb91k5o9+n0uMOrfQOqIFVyDmNTa6TT3b3doDC8rUImcpQ5ZmMM7oooz8l5zBVwZ4qCFdA/cbm9tw+6SJne7S5Nc/2vUThXph3E/Ohpmb3SeBDf3//+Z6envPz8/N9hK5QhlAW37HO6C6A3tXsPmXKUWIe6akCuEd4EjBmvihTGS9KAjTQU/4q2DUd/tZO/TNv7fx+hUj9m34S+Q8q8ydp2gS+0VDQEgAAAABJRU5ErkJggg==
'''
iconJoin0 = base64.b64decode(iconJoinB64)
iconJoin  = PhotoImage(data=iconJoin0)

btnFont  = font.Font(font='Helvetica 12 bold')
listFont = font.Font(font='Helvetica 12')

Lb1 = Listbox(root, selectmode="multiple", width=90, height=20, font=listFont)
Lb1.grid(row=0, rowspan=2, column=0, padx=10, pady=10, ipadx=5, ipady=2)

btnMoveUP    = Button(root, image=iconTop, text="", bg="#6293DB", command=lambda: [moveUP()], compound="left")
btnMoveDOWN  = Button(root, image=iconDown, text="", bg="#EADB3B", command=lambda: [moveDOWN()], compound="left")
btnMoveUP.grid(    row=0, column=1, padx=10, pady=50, ipadx=6, ipady=5, sticky="s")
btnMoveDOWN.grid(  row=1, column=1, padx=10, pady=50, ipadx=6, ipady=5, sticky="n")

panelInfo = Frame(root, width=500, height=40)
panelInfo.grid(row=0, column=3, padx=70, pady=5, sticky="n")

sign_coop_label = Label(panelInfo, text="Unificador de PDFs", font="Helvetica 15 bold")
sign_coop_label.grid( row=2, columnspan=2, column=0, ipady=2)


text_label = Label(panelInfo, text="Versão 3.0 / 2022", font="Helvetica 9")
text_label.grid( row=3, column=0, columnspan=2, padx=10, ipady=2)

panel = Frame(root, width=750, height=300)
panel.grid(row=2, column=0, pady=10, ipadx=5, ipady=2)

panelBar = Frame(panel, width=750, height=40)
panelBar.grid(row=0, column=0, columnspan=3, pady=5, ipady=2)

barra = tkinter.DoubleVar()
minha_barra = ttk.Progressbar(panelBar, variable=barra, maximum=100)
minha_barra.place(x=3, y=0, width=745)

btnAddFile   = Button(panel, image=iconAdd, height=40, width=215, text=" Adicionar arquivo(s)", font=btnFont, bg="#5D6FE5", fg="#fff", command=lambda: [fileAdd()], compound="left")
btnDelFile   = Button(panel, image=iconDel, height=40, width=215, text=" Excluir arquivo(s)", font=btnFont, bg="#FFC136", fg="#fff", command=lambda: [fileDel()], compound="left")
btnCleanList = Button(panel, image=iconDelList, height=40, width=215, text=" Limpar lista", font=btnFont, bg="#EA6A3B", fg="#fff", command=lambda: [cleanList()], compound="left")
btnJOIN      = Button(panel, image=iconJoin, height=60, text=" Unir arquivos", font=btnFont, bg="#43C46A", fg="#fff", command=lambda: [mergePDFs()], compound="left", width=730)

btnAddFile.grid(   row=1, column=0, padx=12, ipadx=5, ipady=5)
btnDelFile.grid(   row=1, column=1, padx=12, ipadx=5, ipady=5)
btnCleanList.grid( row=1, column=2, padx=12, ipadx=5, ipady=5)
btnJOIN.grid(      row=2, column=0, columnspan=3, padx=10, pady=20, ipadx=5, ipady=2)

root.mainloop()

