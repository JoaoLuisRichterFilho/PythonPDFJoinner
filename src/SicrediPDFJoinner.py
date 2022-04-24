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
# root.geometry("700x600")
# root.iconbitmap("./src/sicredi-icon2.ico")
logo_icon = '''\
iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAFKUlEQVRYhbVWb2wTZRh/Cxtbr13v7r3+GdeuK1s36bqu195K320KN5CBEBmrVLrh/vYEAmy3TTQQ4uwHicFM1EQToiFRIRoSPrhBNEPRGYGV+EETJTGIMZH4xQ/qSBTDn75+GNfd3XplzPEk9+He58/v9zzv+z7PC8AChKZp0tlIrvVvs++p3+McWhmz9bAsSywk1gNJ20nfJTHNYe3Xe5HDZHdw6qEToGmaFC9zGS2BwGsRDCWEBUEoUNpjjA2LToJxGZ1aAlBCGEoImxrLh5W2RDmxvGcy+Oeib48jQAdk8O0ToSwBuDf6h9LOXmuqE9McFi9zGcZldM4bINhfOVq00t4CUqkleja1CbZPTHOYeyMyS0BCWOnjeZxpVVaK8lDUfcFrE44+ZVnhs/xVosJan8u2+ZUV7zmej6oILGNLVsr6+n2ul5QEkheC/+Y9F16vt0g2bv6AVwVm+tHN4kcca7U+9K76n5V2pqby/bJu07GqiSz4FIdjZ8O4uqfysC6BrSd8aSVj2zBSkYASwsye6G8UNVtKQRAKoIQysp7eHhyXdZ3n6n5vHQ9j58HZKpkdZntOcJqmSe3pTnwWmkMgG6jR3S/7FlfZVmcJ9IW/k9etQ+iu0ofeyV/TzX79qPdUriYTeTuiS8ISqzmZTaCTm4QSwnSS/15RGTVpvewBACA5FbqTi4CY5nDZoaguCaKCiQAAQDweXwollKFafe8CAADhtvIqsm01p3TBIYSW3q+5vxNj/l82HauaQMPuI76YvdP1KCXYq01BpsrsK3JZvMtKzTXF1bbHiBDbV9LiPWp52j9mstsd2ZJbrSUAAwMAAJBbfMcVB/iGFvOhzw6mH924RyDjcrmMSp0v4UgmL4ZuLyiw1+stAvH40vvZQQlhONhwm3STtLyGMTY89ZH/G3lr5w1a5LdtpMX6H5V7qh08WiEqrbzyv9RvrkleUp+z/KgYG8jN1aPKOy5/ZHvg3HzJ8zxfSD1TN2kdQjh2Nqw63PJ5mSOmaFlvLmAoIQx38lfnA+zxeIrhtsCHWv+ql1fpV8Dj8RQzu1dd17tyzAC6CeYx402rytr1YkAJYdtzCPde5DIqJ6MXonxOUELYYrFA2Z5Ohq+Y6p1duQiYHWY70x+d1o21K/JrCXJ3z3pgYNjycRiH34xgz0gUO/YjzAzOfNYhhK3DCBN+x5NZ8Obqg1BCmO4JfZvNmmM7jCztVhJJpVJLKIqiTDZTKUmSdN6Du+PTwHW9Tth2wqd678HBmR7PDDT8k10bQLeghDDdxaUX1GQq18GNOgQyKcUjo7CcDKseIPfEkgh8oho8XdwFc6nZ9kAktPdUTHPY0ww3KG2o9rrzqvlvNzkAmGnn2r0uOxTFPV8FbwTal+/ieb7wvgQqNttjSvCO8eBPWhsoNdxWDaOGsr2yjm7zvaO6NYNIlUz3ZHC66UD50bwkEmdqr2VfuxBaVMqZiafKkjscUvUFuC/6l1KvragrTNflJSAIQoE4Fbqz7vCK97U6IzS6lMHZA9E5HY1lWULZxHouzII3vVD+al5wWUqcJUwqx4u4yAtblAT6Ls0Edq+B61VVYGGZbLPjyxAW0xze8Lp3bF7g+YTgnbvlwB3nQ9nM4qf9V7S2FosFwgF0q/3zEF49UvHW/wYHAACi2TMCpblDRUxzOOdzG2ODMwrRooADAACxZsWLW8/MBRfTHK5cSz+xaEB6IghCQeV6pq31eM0X3ZPBaTHN3RXTXCY5FboTP+3/YSEx/wPPcSTFeCWMDAAAAABJRU5ErkJggg==
'''
icon0 = base64.b64decode(logo_icon)
icon = PhotoImage(data=icon0)
root.wm_iconphoto(True, icon)

logo_gif = '''\
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
'''
root.title("Sicredi - Unificador de PDF")
root.state("zoomed")
root.geometry("900x600")

inLogoB64 = '''\
    iVBORw0KGgoAAAANSUhEUgAAAFkAAAAkCAYAAADit5awAAAACXBIWXMAAA7EAAAOxAGVKw4bAAAgAElEQVR42gE0MsvNAFZgZ/9WYGf/VmBn/1ZgZ/9WYGf/VmBn/1ZgZ/9WYGf/VmBn/1ZgZ/9WYGf/VmBn/1ZgZ/9WYGf/VmBn/1ZgZ/9WYGf/VmBn/1ZgZ/9WYGf/VmBn/1ZgZ/9WYGf/VmBn/1ZgZ/9WYGf/VmBn/1ZgZ/9WYGf/VmBn/1ZgZ/9WYGf/VmBn/1ZgZ/9WYGf/VmBn/1ZgZ/9WYGf/VmBn/1ZgZ/9WYGf/VmBn/1ZgZ/9WYGf/VmBn/1ZgZ/9WYGf/VmBn/1ZgZ/9WYGf/VmBn/1ZgZ/9WYGf/VmBn/1ZgZ/9WYGf/VmBn/1ZgZ/9WYGf/VmBn/1ZgZ/9WYGf/VmBn/1ZgZ/9WYGf/VmBn/1ZgZ/9WYGf/VmBn/1ZgZ/9WYGf/VmBn/1ZgZ/9WYGf/VmBn/1ZgZ/9WYGf/VmBn/1ZgZ/9WYGf/VmBn/1ZgZ/9WYGf/VmBn/1ZgZ/9WYGf/VmBn/1ZgZ/9WYGf/AFZgZ/9WYGf/VmBn/1ZgZ/9WYGf/VmBn/1ZgZ/9WYGf/VmBn/1ZgZ/9WYGf/VmBn/1ZgZ/9WYGf/VmBn/1ZgZ/9WYGf/VmBn/1ZgZ/9WYGf/VmBn/1ZgZ/9WYGf/VmBn/1ZgZ/9WYGf/VmBn/1ZgZ/9WYGf/VmBn/1ZgZ/9WYGf/VmBn/1ZgZ/9WYGf/VmBn/1ZgZ/9WYGf/VmBn/1ZgZ/9WYGf/VmBn/1ZgZ/9WYGf/VmBn/1ZgZ/9WYGf/VmBn/1ZgZ/9WYGf/VmBn/1ZgZ/9WYGf/VmBn/1ZgZ/9WYGf/VmBn/1ZgZ/9WYGf/VmBn/1ZgZ/9WYGf/VmBn/1ZgZ/9WYGf/VmBn/1ZgZ/9WYGf/VmBn/1ZgZ/9WYGf/VmBn/1ZgZ/9WYGf/VmBn/1ZgZ/9WYGf/VmBn/1ZgZ/9WYGf/VmBn/1ZgZ/9WYGf/VmBn/1ZgZ/9WYGf/VmBn/1ZgZ/9WYGf/AFZgZ/9WYGf/VmBn/1ZgZ/9WYGf/VmBn/1ZgZ/9WYGf/VmBn/1ZgZ/9WYGf/VmBn/1ZgZ/9WYGf/VmBn/1ZgZ/9WYGf/VmBn/1ZgZ/9WYGf/VmBn/1ZgZ/9WYGf/VmBn/1ZgZ/9WYGf/VmBn/1ZgZ/9WYGf/VmBn/1ZgZ/9WYGf/VmBn/1ZgZ/9WYGf/VmBn/1ZgZ/9WYGf/VmBn/1ZgZ/9WYGf/VmBn/1ZgZ/9WYGf/VmBn/1ZgZ/9WYGf/VmBn/1ZgZ/9WYGf/VmBn/1ZgZ/9WYGf/VmBm/1VfZ/9WYGb/VV9m/1VfZv9WYGb/VV9m/1VfZv9VX2b/VmBm/1VfZ/9WYGf/VmBn/1ZgZ/9WYGf/VmBn/1ZgZ/9WYGf/VmBn/1ZgZ/9WYGf/VmBn/1ZgZ/9WYGf/VmBn/1ZgZ/9WYGf/VmBn/1ZgZ/9WYGf/VmBn/1ZgZ/9WYGf/VmBn/1ZgZ/9WYGf/AFZgZ/9WYGf/VmBn/1ZgZ/9WYGf/VmBn/1ZgZ/9WYGf/VmBn/1ZgZ/9WYGf/VmBn/1ZgZ/9WYGf/VmBn/1ZgZ/9WYGf/VmBn/1ZgZ/9WYGf/VmBn/1ZgZ/9WYGf/VmBn/1ZgZ/9WYGf/VmBn/1ZgZ/9WYGf/VmBn/1ZgZ/9WYGf/VmBn/1ZgZ/9WYGf/VmBn/1ZgZ/9WYGf/VmBn/1ZgZ/9WYGf/VmBn/1ZgZ/9WYGf/VmBn/1ZgZ/9WYGf/VmBn/1ZgZ/9WYGf/VmBn/1ZgZ/9WYGb/VV9n/1ZgZv9VX2f/VmBn/1ZgZ/9VX2f/VmBn/1ZgZ/9WYGf/VV9n/1ZgZ/9WYGb/VmBn/1ZgZ/9WYGf/VmBn/1ZgZ/9WYGf/VmBn/1ZgZ/9WYGf/VmBn/1ZgZ/9WYGf/VmBn/1ZgZ/9WYGf/VmBn/1ZgZ/9WYGf/VmBn/1ZgZ/9WYGf/VmBn/1ZgZ/9WYGf/AFZgZ/9WYGf/VmBn/1ZgZ/9WYGf/VmBn/1VfZv9WYGf/VV9m/1VfZv9VX2b/VV9m/1ZgZ/9VX2b/VmBn/1ZgZ/9WYGf/VmBn/1ZgZ/9WYGf/VmBn/1ZgZ/9WYGf/VmBn/1ZgZ/9WYGf/VmBn/1ZgZ/9WYGf/VmBn/1ZgZ/9WYGf/VmBn/1ZgZ/9WYGf/VmBn/1ZgZ/9WYGf/VmBn/1ZgZ/9WYGf/VmBn/1ZgZ/9WYGf/VmBn/1ZgZ/9WYGf/VmBn/1ZgZ/9WYGf/VmBn/1ZgZ/9VX2f/VmBm/1VfZ/9WYGb/VV9m/1VfZv9YYWX/VV9m/1ReZv9VX2X/VmBm/1VfZ/9WYGf/VmBn/1ZgZ/9WYGf/VmBn/1ZgZ/9WYGf/VmBn/1ZgZ/9WYGf/VmBn/1ZgZ/9WYGf/VmBn/1ZgZ/9WYGf/VmBn/1ZgZ/9WYGf/VmBn/1ZgZ/9WYGf/VmBn/1ZgZ/9WYGf/AFZgZ/9WYGf/VmBn/1ZgZ/9WYGf/VmBn/1ZgZ/9WYGf/VmBn/1ZgZ/9WYGf/VmBn/1VfZv9WYGf/VV9m/1ZgZ/9WYGf/VmBn/1ZgZ/9WYGb/VV9n/1ZgZv9VX2b/VV9m/1ZgZv9VX2b/VmBm/1VfZv9VX2f/VV9m/1ZgZv9WX2b/VmBm/1ZgZv9WYGb/VmBm/1ZgZv9WYGb/VmBm/1ZgZv9WYGb/VmBm/1ZgZv9WYGb/VV9n/1VfZv9VX2b/VV9m/1ZgZv9VX2b/VV9m/1ZgZv9WYGb/VV9m/1VfZv9VX2X/Vl9l/1ZgZf9OWmb/VV9l/1VfZf9UXmb/VV9l/1VfZ/9VX2b/VmBm/1ZgZv9VX2b/VV9m/1ZgZv9WYGb/Vl9m/1VfZv9WYGb/VmBm/1VfZv9VX2b/VmBm/1ZgZv9VX2b/VV9m/1ZgZ/9WYGb/VmBn/1ZgZ/9WYGf/VmBn/1ZgZ/9WYGf/AFZgZ/9WYGf/VmBn/1ZgZ/9WYGf/VV9m/1VfZv9VX2b/VV9m/1VfZv9VX2b/VV9m/1ZgZ/9VX2b/VmBn/1VfZv9WYGf/VmBn/1ZgZ/9VX2f/VmBm/1VfZ/9WYGf/VmBn/1VfZ/9WYGf/VV9n/1ZgZ/9WYGb/VmBn/1VfZ/9VYGf/VV9n/1VfZ/9VX2f/VV9n/1VfZ/9VX2f/VV9n/1VfZ/9VX2f/VV9n/1VfZ/9VX2f/VmBn/1ZgZ/9WYGf/VmBn/1VfZ/9WYGf/VmBn/1VfZ/9UXmb/VV9m/1VfZv9WX2b/Ulxm/0xYZv9fZmX/Tlpm/1BbZv9VYGX/VF5m/1VfZv9WYGb/VV9n/1VfZ/9WYGf/VmBn/1VfZ/9VX2f/VWBn/1ZgZ/9VX2f/VV9n/1ZgZ/9WYGf/VV9n/1VfZ/9WYGf/VmBn/1ZgZv9VX2f/VmBm/1ZgZ/9WYGf/VmBn/1ZgZ/9WYGf/AFZgZ/9WYGf/VmBn/1ZgZ/9WYGf/VmBn/1ReZf9WYGf/VF5l/1ReZv9UXmX/VV9m/1VfZv9VX2b/VV9m/1ZgZ/9WYGf/VmBn/1ZgZ/9WYGb/VV9n/1ZgZv9VX2b/VV9m/1ZgZf9VX2b/VmBm/1VfZv9UXmf/VV9m/1ZgZf9WX2b/V2Bm/1dhZv9WYGb/V2Fm/1ZgZv9WYGb/V2Fm/1dgZv9XYGb/V2Fm/1ZgZv9WYGX/VV9n/1VfZv9VX2b/VV9m/1ZgZf9VX2b/VV9m/1ZgZf9XYGb/VmBl/1ZfZf9SXWb/Vl9l/5ONYP+4qVz/nJRf/1phZf9SXGX/VmBm/1NdZ/9VX2b/VmBl/1ZgZf9VX2b/VV9m/1ZgZf9YYWX/Vl9m/1RfZv9WYGX/VmBm/1VfZv9VX2b/VmBm/1dgZf9VX2b/VV9m/1ZgZ/9WYGb/VmBn/1ZgZ/9WYGf/VmBn/1ZgZ/9WYGf/AFZgZ/9WYGf/VmBn/1ZgZ/9VX2b/VV9m/1VfZv9VX2b/VF5l/01XX/9QWmH/T1ph/1ZgZ/9VX2b/VV9m/1VfZv9VX2b/VmBn/1VfZv9VX2b/VV9m/1VfZv9WX2X/UVxm/01ZZv9WX2X/SlZm/1FcZv9XYGb/Ulxl/01ZZv9RXGX/SlZm/0hUZ/9HVWb/SFRm/01ZZf9RW2b/RlRn/0lWZv9IVWb/SFZn/1JcZv9MWGX/VF5n/1ReZv9VX2X/U11l/0xYZv9UXmX/VV5m/0lWZv9IVGf/R1Rn/1NeZf9SXWX/UFtl/2BmZP9QXGX/YGdk/1ReZf9PWmf/TFdm/1ZgZv9WYGb/T1tl/05aZv9XYWX/UFxm/0hUZv9IVGf/S1dm/1VgZv9PWmb/Tlpm/1ZfZv9WYGX/TVpm/0tXZv9VX2X/VF5l/1ZgZv9VX2b/VmBm/1ZgZ/9WYGf/VmBn/1ZgZ/9WYGf/AFZgZ/9WYGf/VV9n/1ZgZv9VX2b/VV9m/1ReZf9WYGf/SFNb/4ySlv/LztD/XGVs/0tVXf9YYmn/VF5l/1VfZv9VX2b/VV9m/1ZgZ/9VX2b/VV9m/1dhZf9MWGb/aG1j/4GAYf9RXGb/ioZg/11kZP9NWWb/X2Vk/318Yv9xc2L/oppf/62iXv+pnV7/r6Nd/4mFYf9pbWP/saRd/6icXv+roV7/pZxe/2VrZP+EgWH/WGFm/1ReZf9PW2b/XGRl/4SBYf9dZGX/SVZm/4qHYf+sol3/mZNf/1VfZf9OWmb/iohg/6qgXv+imF//qqFe/4uJYf9pbmP/g4Bh/0tZZv9RXGb/cXNj/3t8Yv9IVWf/YGhl/56YXv+sol7/fn1i/0dUZv9zdmL/eHli/09aZv9LV2b/fn1i/4qGYf9OWWb/VF5m/1VfZv9VX2b/VV9m/1ZgZ/9WYGf/VmBn/1ZgZ/9WYGf/AFZgZ/9VX2f/VmBm/1VfZ/9WYGf/VF5l/1dhaP9JVFv/gIeM////////////1NbZ/1tkbP9MVl3/WWNq/1VfZv9VX2b/VV9m/1VfZv9WYGX/VF5n/1pjZf9BUGf/goFh/76tXP9IVGb/58xZ/62hXf84SGj/bHBk/76tW/9zdWL/aW9j/6ygXf/Qulv/f39i/2hsY/+XkF//ybZb/3N2Yf+IhmH/enti/2RpZP/Lt1v/XWRl/1RdZf9KVmX/ZWxk/8azW/9YYWX/jopg/8e1Wv97fGL/tKVd/8GvXP9NWWX/w7Jc/6WcXv92d2L/iohg/2dtY/+Bf2H/+NxY/19nZP9AT2f/n5Ve/6ecX/9GVGb/xrNb/6GYX/99fWH/0rxa/4GAYf+MiGH/rqFd/0VTZ/9GU2b/xLFc/+TJWf9QWmX/UVxl/1VfZf9VX2f/VV9l/1VgZ/9WYGf/VmBn/1ZgZ/9WYGf/AFZgZ/9WYGb/VV9n/1ZgZv9VX2f/Vl9l/1pjZv9SXF//anN5/9zf4P///////////9TX2f9dZm3/SlZc/1ljav9VXmX/VV9m/1VfZv9VX2b/VV9n/1liZv9EUmb/f31i/7KkXv9NWWX/x7Rb/+TJWP9TXWX/X2Zl/7urXP9kamT/LEBo/3p5Yv+toV3/Pk1n/0FQZv+YkV7/lo9g/yc9aP9KV2b/Q1Jm/1lhZf/DsVz/XGRm/1VeZv9KV2b/Zmxk/7eoXf9eZWT/t6ld/3V3Yv8zRmj/RlNm/5+VX/9haGT/r6Jd/2VqZP8uQmj/TVhm/0BPZv97e2L/7NRY/6qdXv82SGf/npVf/5GLYf9wc2P/vKpc/0ZTZ/84SWf/dnhh/5CKYP+Fg2H/qZ5f/zlKaP9qbmP/sqRd/8e0W/9ydWP/TFll/1ZfZP9VXmb/VmBm/1ZfZv9WYGf/VmBn/1ZgZ/9WYGf/AFZgZ/9VX2f/VV9m/1VfZv9WX2b/UFtm/0ZSZv9JV2n/RVBY/1xka//W2dr///////7+/v/W2Nr/Xmhv/0tVXf9ZY2n/VF5l/1VfZv9WYGb/VV9n/1pjZf9DUWf/gH9i/7SlXf9TXGX/s6Ve/62gXv+hmF//Ul1l/7+uXP9obWP/P05n/4iEYf+2p13/UFxm/0xYZv+Vj1//s6Vd/1pjZP9kamP/Ul1l/11lZf/Fs1z/XWVl/1VfZf9LWGf/Zmxl/7mpXf9jaWT/r6Jd/3l6Yv9UX2X/ZGtj/0ZTZv9UX2X/ualc/4yJYf9aY2X/YWdj/0lVZv+FgmH/taVd/7qpXP9nbGT/j4pg/5iRYP9xc2P/s6Rd/1VfZf9WYGT/Ulxl/0NRZ/+Wj2D/qp5e/y5Caf+YkWD/m5Rf/5iQYP+lml//R1Rm/1ZgZf9UX2f/VV9l/1VgZ/9WYGb/VmBn/1ZgZ/9WYGf/AFZgZ/9VX2b/VV9m/1ZgZv9PWmb/ZWpk/4uKYf+KhmD/YGZp/0xWXP9eaG3/1tna////////////19rc/15ob/9KVVv/WWNp/1ReZf9VX2b/VF5m/1pjZv9EUmf/gH5i/7WmXv9RW2b/vq1c/21xY/+6q1z/e3th/6+jXf9scGT/OUpo/4WCYv+0pl7/TVln/0hWZ/+TjGD/2cJa/6GZXv91dmL/SFVn/15lZv/Gslz/XGRm/1ReZv9LV2f/ZWtl/7mpXP9haGX/tKVc/3FzYv90dWL/tKlc/7CjXv9XYGX/uKpd/8W3W/+TjmD/YGZk/0JRZ/+KhWH/p51e/359Yv+vol3/iIZh/5eRYP9xc2T/t6hc/1FdZP9QWmX/Vl9k/0tXZv+Wj2H/pZpe/zZIaP+xpF7/cHNj/1BcZv+/rFz/UVxl/1RfZv9UXmb/VmBm/1RfZv9WYGf/VmBn/1ZgZ/9WYGf/AFZgZ/9WYGX/VF5n/1liZf9GVGb/gn1h//jiVv/84Vf/a21j/0hWav9KVF3/W2Vs/8nP2f///////////9nb3v9eaG7/SFNb/1hiaf9UXmX/VV9n/1liZf9DUWf/gH9i/7SlXf9QW2b/wrBc/11lZP+CgWH/xrNc/6mcXv9rb2P/O0tn/4WCYf+0pl3/TVpn/0pVZv+XkF//r6Jd/1FdZP9jaWP/U15l/1xkZv/Gs1v/YWhl/1liZf9PW2b/Z2xk/7ioXf9jaWT/sKJd/3d5Yv9XYWX/cnZi/8i1W/9nbGP/r6Je/4eFYv9TXWb/YWhj/0lWZv+IhGL/sKJe/0dVZv+1p13/v65c/4SCYf93eGL/sqNd/1VgZf9XYWT/Ul1l/0RSZ/+akmD/nZRf/0xYZv/LuFr/jopg/25yYv/YwVr/bHBi/0xYZf9WYGT/VV9m/1VfZv9WYGb/VmBn/1ZgZ/9WYGf/AFZgZ/9VX2b/VV9m/1ZfZv9WX2X/Tllk/66kXv//4lb/aW5j/2ZsZP9dZWj/TVdc/3d6av/U1db////////////b3t//Xmdt/0pVXf9YYmn/U11m/1pjZv9EUmb/f35i/7KkXv9RXGX/wa5d/2NpZP9LV2b/z7xb/9G/W/9bY2T/P09m/4OAYv+ypV7/TFpm/0pWZ/+XkF7/lY5g/yY8aP9IVWX/QE9m/1piZf/Ar1z/S1dn/0NRZ/88S2f/YWhk/7mpXf9dZGT/uKhd/3Z3Yv8uQmj/RlNn/8CwXP9jamP/rZ9d/2NpZP8tQWj/SlZm/ztLZ/+Gg2H/s6Ve/zlLZ/99fWH//dtX/4eEYP9wc2L/vaxc/0ZTZ/82SGf/eXph/5GMYP+LhmD/l5Bg/2xvZP/Nu1r/ppxe/5qSYP/MuVv/lo9g/0NSZv9YYmT/VF5m/1ZgZv9WYGb/VmBn/1ZgZ/9WYGf/AFZgZ/9VX2b/Vl9m/1ReZv9bYmT/P05n/5ePXv/+4Ff/X2Zk/8y4W/+vol3/XmZp/8GtVP9haWr/zNDY////////////3t/h/15obv9JU1v/VmBn/1liZP9CUGf/g4Bh/7yrXP9QW2b/yrVb/2luYv8+Tmf/jYpg/+XMWf9eZWX/PE1n/4iEYP+8q1z/TFhm/0hVZ/+akl//0bxa/4GAYv+Uj2D/h4Zg/2JoZP/Vvlr/lpBg/5CLYP+AgmH/dHZj/8CuXP9aYmX/jYhg/8u3W/+AgGH/uatc/7KkXv9JVmb/xbNb/6+kXf+DgWL/l5Jf/29zYv+JhmH/u6tc/0JQZ/9RW2X/1b5a/6+iXf9BT2f/yLVb/6adXv+Af2H/0btb/39+Yf+OiWD/oZde/56UX/+akl//RVNm/0tXZv90dWL/zLhc/0pXZv9VXmX/VV9m/1VfZv9VX2b/VmBn/1ZgZ/9WYGf/AFZgZ/9WYGb/VV9m/1VfZv9aYmX/RFJn/5+VX///4Vf/YGdk/8OxW//r0lf/iINg/76uYP9ZYF3/T1to/8zPzv/+/v7//////+Lk5f9qcnn/Tlhg/1hiZv9OWmb/ZGlk/3d4Yv9TXWb/fX1i/1tkZP9OWmb/WGFl/3p7Yv9cY2X/S1dm/2ZsZP94eWL/U11m/1BcZv9rb2P/oplf/5+WX/+gmF//nZZf/15mZf+KhmD/o5pe/6KZXv+XlV//bXBj/3N1Y/9dZWT/SlZm/4eEYf+poV3/lZBg/1VfZf9PWmb/gYFi/6ScXv+dlV//opxf/4aFYf9ma2P/dHdj/0hVZv9PWmb/am9j/3V2Y/9IVmf/YWhk/56WX/+ooF3/e3tj/0hVZv9scGP/cHNi/3J0Yv9jaWT/TFhm/1FcZf9VXmX/f35i/1VfZf9TXWX/VmBl/1ReZ/9WYGX/VmBm/1ZgZ/9WYGf/AFZgZ/9VX2f/VmBl/1VfZ/9bY2b/Q1Jm/52UYP//4Vf/ZWtk/7CkXv+qnl7/3sZY/72uX/9aYWH/RFBc/77Cwv/9/f3///////T19f94gIX/S1Zd/1ZgaP9VX2X/Ulxm/05aZ/9UXmb/S1dm/1NeZv9WX2X/VF5m/01ZZ/9UXmb/V2Bm/1FcZ/9OWmf/VF5m/1ReZv9RXGb/SFVn/0hWZv9JVmf/SVZn/1NdZf9LV2b/R1Vm/0hVZ/9LV2b/UVxl/05aZv9UXmX/VV9l/0xXZv9IVGf/R1Vn/1FcZf9VX2b/Tlpm/0hVZ/9HVWf/SVZn/01ZZv9QWmX/V2Bl/4iFYP9haGT/S1hm/1FbZv9XYGX/T1pm/0pWZv9JVmf/TVhm/1ZgZv9RXGb/T1pm/01ZZ/9SXWX/VmBl/1dgZf9VXmX/Sldn/1VfZf9VYGb/VF5n/1ZgZv9VX2b/VmBn/1ZgZ/9WYGf/AFZgZ/9WYGb/Vl9m/1VfZv9bYmX/Q1Fn/56VX///4lf/Y2lk/8GwXP9xc2L/xbhf/9nMVP9MVGH/vcLH////////////8PHy/3V9gv9GUFj/V2Fo/1VfZf9UXmb/Vl9l/1BcZv9NWWb/UFtm/0tYZv9TXmb/VmBl/1NdZv9NWGf/VF5m/1dgZf9QXGb/Tlpm/09bZv9MWWb/VV5l/1hiZf9RXWb/Tlpn/1VfZf9WYGX/VmBl/1ZfZv9OWmb/U15l/1hhZP9QWmb/U11m/1JcZv9PWmb/UFtl/09aZv9TXWX/U15l/05aZv9PWmb/T1tm/1dhZf9NWGb/aG5j/4SBYf9LWGb/V2Fl/1ReZf9MWGb/Tlpm/05ZZv9WYGX/UFtn/1RfZv9SXWb/TVln/05ZZv9PWmb/VV9l/1FcZv9MWGb/UVtm/05ZZv9UXmb/VV9m/1VfZf9VX2f/VmBm/1ZgZ/9WYGf/AFZgZ/9WYGf/VmBm/1VfZ/9aYmb/RFJn/5yTYP/93Vj/ZWtk/5uSX/9pbmf/ZGld/62gW//Bxcb////////////t7u//dHyD/0VRWP9YYmn/U15k/1VfZ/9XYWX/TVlm/3F0Y/+YkmD/lpFf/4OBYf9TXmX/TVpm/2dsY/+CgGL/Vl9k/0pXZv93eGP/mZNf/5aRYP9/f2H/U11l/0xYZv9pbmT/gH9h/1NeZv9TXWX/U15l/1VeZf96emL/WmNl/0tYZv90dmL/YWdl/2xxY/+YkmD/lI5f/5mTX/9tcWP/VF5l/4yJYP+Ykl//a29j/0xYZv9YYWT/iIZh/4mIYf9wc2P/S1hm/1VfZf+CgGH/m5Vf/3d5Y/9MWWb/eHli/1piZf9VX2b/iohg/5mSX/9vcWP/S1hm/1tjZP+RjWD/l5Jg/3x8Yv9SXGX/VV9k/1VfZv9VX2f/VmBl/1ZgZ/9WYGf/AFZgZ/9WYGf/VWBm/1VfZ/9aY2X/QlFn/6KXX///51b/bXFi/0lXa/9OWmD/TVhi/7q/yf///////f39/+nq6/91fIP/RVBY/1liaP9VX2b/VWBm/1ReZv9aYmX/QlBn/6mdXv+uo13/fn5h/7qqXP+NiGD/Nkho/5mRX//jyVn/Y2lk/zpLZ/+1pl3/qJ5e/4OCYf+3qV3/jIdg/zRGaP+hmF7/4MZa/1piZf9OWmX/Ulxl/1FcZf/ZwVr/n5Ze/y9DaP+vol3/eXhi/5yUX/+vpF3/g4Jg/4WEYf9kamT/npVe/6meXf+HhWD/z7pa/15kZP+ck17/qp5e/4mIYf+/rlz/XWVk/4mFYf+1p1z/fH1h/8azXP91dmL/rqFd/2htY/+Wj1//rKFd/4SDYf/Arlv/XmZk/6GXX/+YkF//iIZg/5GMYP9TXWX/VF5l/1ZgZv9UXmf/VV9l/1ZgZ/9WYGf/AFZgZ/9WYGf/VmBl/1ReZ/9ZYmX/RVNm/5aOYP/k0Vj/a3Jm/0lUYP9SXGP/xsnK///////7+/v/6Onq/3N7gP9FUVj/WGJp/1ReZf9VX2b/VV9m/1VfZ/9YYWb/RFJm/6SaYP9wcmP/JTpp/2ltY/+zpF3/RVRn/6CXXv/Arlz/fn5h/z5OZv+rn13/YWZk/x42av+BgGH/rqBd/0VTZ/+imF//wa9c/3Z3Yv9OWWb/Ulxm/09bZf/DsVz/zLdb/0pXZv+clF//eXlj/5qSX/9qbmP/L0Nn/z1MZv9WX2X/tadd/11lZP8kOWn/dHVi/2JpY/+7q1z/VV5m/zlJaP+ZkWD/jYhg/5uTX/96eWL/Kj5o/3Z3Yf9wc2L/pZpf/3J1Y/+rn13/ZWpk/yk9af+qnl7/fHxh/76sW/9qbmP/LUBo/0NSZf9YYbbnqqMAABI/SURBVGX/VF5m/1ZgZv9UX2f/VmBm/1ZgZ/9WYGf/AFZgZ/9WYGf/VWBm/1VfZ/9VX2b/Ul1n/1tkZP9qbWX/TVdc/1FbYv/Gycv///////z8/P/o6er/c3uA/0ZRWf9YYmn/VF5l/1VfZv9WYGf/VV9l/1VfZ/9ZYmX/RFJn/6OaX/+WkF//YGdk/6qdXv+PimD/Ymhk/5+WXv+Af2H/oZhf/0NSZ/+onV//rKFd/4iGYP+ypV3/b3Jj/2xwY/+akl7/g4Fh/5uTX/9QW2b/UFpl/1lhZP+lml//qZ1e/4WCYf+VkF//eXpi/5ePYP+0qV3/h4Vg/1NdZf9hZ2T/qZ5e/2ltY/96fWH/fH1i/1JdZP+0plz/YGdk/09aZv+UjV//jIdg/5aPYP98e2H/TVlm/1ReZf9LV2b/rKFe/3F0Y/+kml7/bXFj/0BOZ/+nm13/eHli/3R2Yf+/sVz/qJ5e/2BnZP9NWWb/V2Bl/1VfZf9VYGf/VV9m/1ZgZ/9WYGf/AFZgZ/9WYGf/VWBm/1VfZ/9VX2b/Vl9m/1FdZv9HVWP/W2Rt/8nLzf///////f39/+jp6/9xeH//RlFZ/1hjaf9WX2b/VV9m/1VfZv9VX2b/VmBm/1VfZ/9aY2X/Q1Fn/6KZXv+6rVz/npZe/5mRX/9NWWb/iYZg/5eRX/9SXGX/uKlc/1JdZf+kmV7/npde/7+vXP+bk1//MUVo/5iRX/+Ri2D/VF5l/7aoXf9cZGX/TFhm/1tjZf+pnV3/dHZj/56VX/+2p1z/am9j/5yTX/+poF3/enth/1BbZf9fZmP/q59d/2xuY/9xdmL/y7lb/3V2Yv+uoV7/YWhk/01YZv+YkGD/i4dg/5iPYP99fGH/SVZm/1ReZf9IVWb/raFd/3B0Yv+mm17/bXFj/z1NZ/+onF3/gYBh/0NSZ/9gZ2T/nJVf/72tXP9UXmX/U11k/1ZgZv9VX2f/VV9l/1ZgZ/9WYGf/AFZgZ/9WYGf/VmBm/1VfZ/9WYGb/VF5l/1liZ/9KU1j/l5yg////////////6err/212e/9HUln/WWNq/1VeZv9VX2b/VV9m/1VfZv9WYGf/VV9m/1VfZ/9ZYmb/Q1Fn/6SaX/+CgGH/TVhl/0xXZf9JV2b/qp5e/8S0XP+XkV//2cNZ/2luY/+hl17/bnFj/2hsZP+1plz/Q1Jn/6+iXf/Fs1v/mJJf/9nBWv9zdWP/SFVm/1hhZf+zpVz/WWFl/359Yf/u0Vj/am5k/5qSX/92dmP/O0xn/0NSZf9aYmT/saRd/2FnZf8pPWn/q59d/3x8Yv+zpV7/VmBl/0BPZ/+VjmD/jolf/5mRX/94eWL/MENn/3R2Yv9wc2P/pZte/3N1Y/+onV3/Zmtk/y5CaP+mm17/hoJg/0dVZ/9ATmb/Pk5o/7OlXf93eGL/RlRl/1liZf9UXmf/VmBm/1ZgZ/9WYGf/AFZgZ/9WYGf/VWBn/1ZgZ/9VX2b/VV9m/1VfZv9UXWX/T1lg/7S4u//p6uv/a3V7/0dSWP9YYmj/VF5l/1VfZv9VX2b/VV9m/1ZgZ/9WYGf/Vl9l/1ReZ/9ZYmX/Q1Fm/6mdX/+EgWH/SVVm/01YZv9mbGP/ualc/2VrZP9DUWf/l49g/5WNYP+rn17/eXpi/0VSZ/+jmV7/qp5e/6KYXv9qb2P/Q1Fn/5WOX/+kmV//RlNm/1hhZP+6ql3/YGdk/0tXZv/jyVn/enti/5eQX/+onl7/enth/35/Yf9iaGP/pZpf/6KZX/94emL/xLJc/1hgZP+imV7/ople/3h7Yf/CsFv/YGZk/46JYf+1p13/a3Bi/8WyXP94eWL/rKBe/2huZP+bk1//p5xf/3h6Yf+/rlz/a3Bj/6SaXv+GhGD/iIZh/7yrXf9ZYmT/UVtl/1dgZf9VX2f/VV9l/1ZgZ/9WYGf/AFZgZ/9WYGf/VmBm/1VfZ/9VX2b/VV9m/1VfZv9VX2b/UFti/1JcY/9hanH/S1Zd/1ZgZ/9VX2b/VV9m/1VfZv9VX2b/VmBn/1VfZv9WYGf/VWBm/1VfZ/9WYGb/Tlpm/3J0ZP9la2T/U11m/1JcZv9gZ2T/dXdi/1BbZv9OWWb/X2Zl/29zY/90dmP/Ymhk/05aZv9eZWX/hYJh/2xwY/9SXGX/Tllm/15lZf92eGP/UFtl/1VfZv92d2P/XGRl/0pXZ/9ydGP/YWdk/2twY/+dmF//npVf/5+YX/9xc2L/Ulxm/5WQX/+mnV7/bHBk/0xYZv9VX2X/lpBg/6GcXv9zdGL/Sldn/1VfZf+Jh2H/qZ9e/3l6Yv9LV2b/eHhi/1ljZf9VXmb/ko5f/6adXv9wc2P/SVZm/25yY/+imV//oppe/2ZrZP9NWWb/V2Bl/1VfZv9VX2f/VV9m/1ZgZ/9WYGf/AFZgZ/9WYGf/VmBn/1ZgZ/9WYGf/VV9m/1VfZv9VX2b/VV9m/1NeZf9QWmH/VV9m/1ReZf9WYGf/VF5l/1ZgZ/9WYGf/VmBn/1ZgZ/9WYGf/VWBm/1VfZ/9VX2b/VmBm/05aZv9RW2b/VV9m/1VfZv9RXGb/TFll/1VfZv9VX2b/Ulxl/05aZv9NWmb/UVxm/1ZgZf9RXGb/Sldm/09aZf9UXmb/VV9m/1JcZf9MWWb/Vl5m/1ReZf9NWWb/U11l/1ZgZf9NWWb/Ulxm/09bZv9HU2b/RlNn/0ZSZv9PWmb/U15l/0hUZv9FU2j/Tlpm/1ZgZf9TXWb/R1Rn/0ZTZ/9MWWb/V2Bl/1NdZf9JVWb/RVNo/0xYZv9WYGX/TFlm/1NeZf9TXmX/SFVm/0VTaP9NWWb/VmFl/05aZv9GU2f/RlRm/09aZv9XYGX/VV9m/1VfZf9VX2f/VmBm/1ZgZ/9WYGf/AFZgZ/9WYGf/VmBn/1ZgZ/9VX2b/VmBn/1VfZv9WYGf/VV9m/1ZgZ/9WYGf/VF5l/1VfZv9VX2b/VV9m/1VfZv9WYGf/VmBn/1ZgZ/9WYGf/VmBm/1VfZ/9WYGb/VV9m/1dgZv9WYGX/VV9m/1ReZv9VX2b/V2Bl/1VfZv9UXmf/Vl9m/1dgZf9XYGb/Vl9m/1VfZv9WYGX/WGJm/1ZgZf9VX2b/VF5n/1VfZv9XYGX/VV5n/1VfZv9XYWX/VV9m/1VfZv9XYGX/VV9m/1ZgZv9ZYmX/WWFm/1liZf9WYGb/VV9m/1hiZf9ZYmb/VmBl/1RfZv9VX2b/WWJl/1liZv9XYGX/VF9m/1VfZv9YYWX/WmJm/1hhZf9VX2b/V2Bl/1VfZv9VX2b/WGJl/1liZv9XYGX/VF9m/1ZgZv9ZYmX/WWJl/1ZgZv9VX2b/VmBl/1VfZv9WYGf/VV9m/1ZgZ/9WYGf/AFZgZ/9WYGf/VmBn/1ZgZ/9WYGf/VV9m/1ZgZ/9VX2b/VmBn/1VfZv9VX2b/VmBn/1ZgZ/9WYGf/VmBn/1ZgZ/9WYGf/VmBn/1ZgZ/9WYGf/VWBn/1ZgZ/9VX2f/VmBn/1VfZ/9VX2f/VmBn/1ZgZ/9WYGf/VV9n/1ZgZ/9WYGb/VWBn/1VfZ/9VX2f/VWBn/1ZgZ/9VX2f/VV9n/1VfZ/9WYGf/VmBm/1ZgZ/9VX2f/VmBm/1ZgZ/9VX2f/VmBn/1ZgZ/9VX2f/VmBn/1VfZ/9VX2f/VV9n/1VfZ/9VX2f/VmBn/1VfZ/9VX2f/VV9n/1ZgZ/9WYGf/VV9n/1VfZ/9VX2f/VmBn/1ZgZ/9VX2f/VV9n/1VfZ/9WYGf/VV9n/1ZgZ/9WYGf/VV9n/1VfZ/9VX2f/VmBn/1VfZ/9VX2f/VV9n/1VfZ/9WYGf/VV9n/1ZgZ/9VX2f/VmBn/1ZgZ/9WYGf/AFZgZ/9WYGf/VmBn/1ZgZ/9WYGf/VmBn/1VfZv9WYGf/VV9m/1ZgZ/9WYGf/VV9m/1VfZv9WYGf/VV9m/1ZgZ/9WYGf/VmBn/1ZgZ/9WYGf/VmBm/1VfZ/9WYGb/VV9m/1ZgZv9WYGb/VV9m/1VfZv9VX2b/VmBm/1VfZv9VX2f/Vl9m/1ZgZv9WYGb/Vl9m/1VfZv9WYGb/VmBm/1ZgZv9VX2b/VV9n/1VfZv9WYGb/VV9n/1VfZv9WYGb/VV9m/1VfZv9WYGb/VV9m/1ZgZv9WYGb/VmBm/1ZgZv9WYGb/VV9m/1ZgZv9WYGb/VmBm/1VfZv9VX2b/VmBm/1ZgZv9WYGb/VV9m/1VfZv9WYGb/VmBm/1ZgZv9VX2b/VmBm/1VfZv9VX2b/VmBm/1ZgZv9WYGb/VV9m/1ZgZv9WYGb/VmBm/1ZgZv9VX2b/VmBm/1VfZv9WYGf/VmBm/1ZgZ/9WYGf/AFZgZ/9WYGf/VmBn/1ZgZ/9WYGf/VmBn/1ZgZ/9WYGf/VmBn/1ZgZ/9WYGf/VmBn/1ZgZ/9WYGf/VmBn/1ZgZ/9WYGf/VmBn/1ZgZ/9WYGf/VmBn/1ZgZ/9WYGf/VmBn/1ZgZ/9WYGf/VmBn/1ZgZ/9WYGf/VmBn/1ZgZ/9WYGf/VmBn/1ZgZ/9WYGf/VmBn/1ZgZ/9WYGf/VmBn/1ZgZ/9WYGf/VmBn/1ZgZ/9WYGf/VmBn/1ZgZ/9WYGf/VmBn/1ZgZ/9WYGf/VmBn/1ZgZ/9WYGf/VmBn/1ZgZ/9WYGf/VmBn/1ZgZ/9WYGf/VmBn/1ZgZ/9WYGf/VmBn/1ZgZ/9WYGf/VmBn/1ZgZ/9WYGf/VmBn/1ZgZ/9WYGf/VmBn/1ZgZ/9WYGf/VmBn/1ZgZ/9WYGf/VmBn/1ZgZ/9WYGf/VmBn/1ZgZ/9WYGf/VmBn/1ZgZ/9WYGf/VmBn/1ZgZ/9WYGf/AFZgZ/9WYGf/VmBn/1ZgZ/9WYGf/VmBn/1ZgZ/9WYGf/VmBn/1ZgZ/9WYGf/VmBn/1ZgZ/9WYGf/VmBn/1ZgZ/9WYGf/VmBn/1ZgZ/9WYGf/VmBn/1ZgZ/9WYGf/VmBn/1ZgZ/9WYGf/VmBn/1ZgZ/9WYGf/VmBn/1ZgZ/9WYGf/VmBn/1ZgZ/9WYGf/VmBn/1ZgZ/9WYGf/VmBn/1ZgZ/9WYGf/VmBn/1ZgZ/9WYGf/VmBn/1ZgZ/9WYGf/VmBn/1ZgZ/9WYGf/VmBn/1ZgZ/9WYGf/VmBn/1ZgZ/9WYGf/VmBn/1ZgZ/9WYGf/VmBn/1ZgZ/9WYGf/VmBn/1ZgZ/9WYGf/VmBn/1ZgZ/9WYGf/VmBn/1ZgZ/9WYGf/VmBn/1ZgZ/9WYGf/VmBn/1ZgZ/9WYGf/VmBn/1ZgZ/9WYGf/VmBn/1ZgZ/9WYGf/VmBn/1ZgZ/9WYGf/VmBn/1ZgZ/9WYGf/AFZgZ/9WYGf/VmBn/1ZgZ/9WYGf/VmBn/1ZgZ/9WYGf/VmBn/1ZgZ/9WYGf/VmBn/1ZgZ/9WYGf/VmBn/1ZgZ/9WYGf/VmBn/1ZgZ/9WYGf/VmBn/1ZgZ/9WYGf/VmBn/1ZgZ/9WYGf/VmBn/1ZgZ/9WYGf/VmBn/1ZgZ/9WYGf/VmBn/1ZgZ/9WYGf/VmBn/1ZgZ/9WYGf/VmBn/1ZgZ/9WYGf/VmBn/1ZgZ/9WYGf/VmBn/1ZgZ/9WYGf/VmBn/1ZgZ/9WYGf/VmBn/1ZgZ/9WYGf/VmBn/1ZgZ/9WYGf/VmBn/1ZgZ/9WYGf/VmBn/1ZgZ/9WYGf/VmBn/1ZgZ/9WYGf/VmBn/1ZgZ/9WYGf/VmBn/1ZgZ/9WYGf/VmBn/1ZgZ/9WYGf/VmBn/1ZgZ/9WYGf/VmBn/1ZgZ/9WYGf/VmBn/1ZgZ/9WYGf/VmBn/1ZgZ/9WYGf/VmBn/1ZgZ/9WYGf/AFZgZ/9WYGf/VmBn/1ZgZ/9WYGf/VmBn/1ZgZ/9WYGf/VmBn/1ZgZ/9WYGf/VmBn/1ZgZ/9WYGf/VmBn/1ZgZ/9WYGf/VmBn/1ZgZ/9WYGf/VmBn/1ZgZ/9WYGf/VmBn/1ZgZ/9WYGf/VmBn/1ZgZ/9WYGf/VmBn/1ZgZ/9WYGf/VmBn/1ZgZ/9WYGf/VmBn/1ZgZ/9WYGf/VmBn/1ZgZ/9WYGf/VmBn/1ZgZ/9WYGf/VmBn/1ZgZ/9WYGf/VmBn/1ZgZ/9WYGf/VmBn/1ZgZ/9WYGf/VmBn/1ZgZ/9WYGf/VmBn/1ZgZ/9WYGf/VmBn/1ZgZ/9WYGf/VmBn/1ZgZ/9WYGf/VmBn/1ZgZ/9WYGf/VmBn/1ZgZ/9WYGf/VmBn/1ZgZ/9WYGf/VmBn/1ZgZ/9WYGf/VmBn/1ZgZ/9WYGf/VmBn/1ZgZ/9WYGf/VmBn/1ZgZ/9WYGf/VmBn/1ZgZ/9WYGf/mFjSorfA67EAAAAASUVORK5CYII=/7VKNGlgWWBaXRWqIxoYmtNvWl7UMbQRTQLSDs8rPI/szs8mNNkD6ZJtpYk5qoSQFtiqmxrRa1WvcHaMBo9cGaxopFBfUBrLN7e747M7uzu7MLtj704eTsvXPP950995xz74zg9/uF/4s812LJLwl+SdGiXzJJCcnRfqvz8XUv3hkOzMFN+N3l9Qs97gCXbo8yhtbmMFadMUmq/X92RvcPc6B73H4hIEqCs8+bV3G4o3LzgKt3w1Db0fLTrSegN/e79tH8VmefzxIQlfV6+/kitZBo5HQTqCRJpspDHVvW/thy3hpxPLP82sQgBWOOuGhz9FymdRdofQXsuD3fyuxRyuKIBAdyejr8gn2/e/0bw82RPJCPOpgt7GDFIWdUJ7J+jOdYh/VryM6+37MeOMDTor0wZ7RwkmEX5cGHR9td+WOKE0QU08j477CTpQnN65yNwQ72hNMOPH8Wh9JyRIsIEvK9Adc+83iTFolYqhMYF4YaWUFoF9f8eZJTqg45mHm8kQEPuNg6jStzZNRkQ0g/ONbuAgABRY2iAALospEOtm7Ew7V+PiH4Aw44FAUeIg18UU3qbJHhyUp7XIbQZnIEUhRqYivDLSx47wa7P/2Ia4wxb7x9ikPApRws05La0BkKneAX+Ra9REk3UTDaBIBocdhhCG4NNrJSIr829QeTH8tcY4x5Q2cUh6LApWKYAI/Kl+yM0lFFE8JH5fgxqqA46IjaMjiiRaY03Mwmpm6zucdPucY4Y2TUHAMu8InnI2W7RJOWO0mRCfgkgfrDZfI+lm2LEs60pDjTktUZNZkRnRjxXAKfYWTQwh193lw0rKKwg2WLyr92Ro0O8K1hhww+8CZFRtuiisO7qyxjTfEeoVUHCKwkRTopCO5iK0JONv7X79wZaIwxr1+n2cWrjPcqRxQ84NO2Sh8ZE84ROls+o0UxW9D5TF+m+Mel4dYkWRFqZqvDbTwis4/muMYY86lrYa/HAz54iK+vx60ewDpneJPbMNR6PF+JjAwjNLOyyG4WnLzBrlO1gFAvV0nuTU+zBzOPuL6a8hwCO9gDB3hqdGTwgI83QbXEVWdEodMrCeXftZ5Q2z53Jj/YwNaOuNkUkclPomzuyVOd/M31g5nHbGp6hmv9vCawgz1wgKc5Ax7wgRf8SQncSR6Wn2oZVPpLcmSu3LnOrt29zcYnbyXk7i02QXry4UPuCPSEOq9fBzvYp0YGPODr9KQlMB2Kbkl46xvnQP5YIjLYY9svTaxwsJoV9m9j1oHtccnvr2Ilg7Vs/M9bbJYiAI0x5vXrYAd74OiSWAYP+MArpmwTT+CNx51fIMu1BFaSja4Dw5+wgp+SxXJuJ7MN17Pxe2o1kcYY86lrYQ+cROPjCczApySwrpp4adN18f2DzW15o40oPUQm0fAizWmCXlEaaVX6jFpNGGPeaL2u13B88IAPvGKyM1RN3oCwo9e1znK5ntkiyrGfTXAGraQy1vcZjDE/ny3wLZfrWG1v2zrwpmwTHQV0Z3VL3ldKhux3rKP8hI0lRefFdGCOC3zwgA+8aWcT3ypPQNh0sGGfOVgHQzn9bpJ+al+/T6f2E5nr+U5tFU/OJfyNxLPHk9iitIOySwwIzu6OxXlD22eLIkp01AgZ32doW67c/Y1NPZzhGuNMkdGwgGsZqp4lnte6RH/6QRmPjiTm7PF2Cps/b/AuPVfDSiLNsrrPhjc9VMjr39axVYN2rjE2iqbqCMdbRrjABw/4jC9X2p1UpAsz3VFXHam+uHx4R5pDejL8zju7k5l/qOU69VmqI8ADLvA5T8o9OO0OLOI64fML7V3eV23Hqm4uP1ur5E9EAS5OkCTKfiRRvonGpvwB2MEeOLZj224CF/iiwRuC4RskL3VfQGjr9iwuObptbOnpKlZ0iVp5hK4WkXivMCxb1dkYX0frYQd74AAvXsoGb5gZX2n5EUH/wNPpW1R+yP7lkpNbWO6ZGlZ0sQEdVKZIyBQRItWJMsYLnYx1WL/kZAUj+8PAUSOS8VV33nds9AFEqbqv7e3VX9UMLxusYEtPbWVmIso/Z2eF5+uY9UI91xibv6/hz7EO68nuHdir/STrO/eCPn/wdymvAmjvbV/z7oGGvUT0s/V41WTe15Vz5v7KKDTGq4/UXNp0oH6vvdf1ZgAfC8hO/WQy72eS5/kmo3yJoH+JsgRRR5dvUcsez2LHp+5caIwxj+dYl/QFQpJe3MciXS6ZfAHpZZrLQZMEMScnwRhr8FxUv+UsxAlN/gEn2vnPMkkMaAAAAABJRU5ErkJggg==
'''
inLogo0 = base64.b64decode(inLogoB64)
inLogo  = PhotoImage(data=inLogo0)


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
    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
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

gif_image = tkinter.PhotoImage(data=logo_gif)
gif_label = Label(panelInfo, image=gif_image)
gif_label.grid(row=0, column=0, padx=5, sticky="e", ipady=2)

gif_label = Label(panelInfo, image=inLogo)
gif_label.grid(row=0, column=1, padx=5, sticky="w", ipady=2)

sign_coop_label = Label(panelInfo, text="Sicredi das Culturas RS/MG", font="Helvetica 9 bold")
sign_coop_label.grid( row=1, columnspan=2, column=0, ipady=2)

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

