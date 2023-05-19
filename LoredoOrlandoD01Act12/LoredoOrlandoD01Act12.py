# -*- coding: utf-8 -*-
"""
Created on Thu Feb  2 15:27:34 2023

@author: Orlando
"""

from tkinter import Tk, Canvas, Frame, Label, Entry, Button, W, E, Listbox, END
import tkinter
import contextlib
import io
import tkinter as tk
from tkinter import ttk
from tkinter import *
import random
import keyboard
from tkinter import messagebox


ventana = tkinter.Tk()
ventana.title("Producto-Consumidor")
ventana.geometry("800x550+100+100")


image = tk.PhotoImage(file="fondo.png")
Ifon = ttk.Label(image=image)
Ifon.place(x = 0, y = 0) 

image2 = tk.PhotoImage(file="image.png")
IPro = ttk.Label(image=image2)
IPro.place(x = 80, y = 60) 

image3 = tk.PhotoImage(file="image2.png")
Icon = ttk.Label(image=image3)
Icon.place(x = 600, y = 60) 

estilo = ttk.Style()

estilo.configure("mystyle.Treeview", highlightthickness=0,
                 bd=0, background='light green', font=('Arial', 10), rowheight=22)


tv = ttk.Treeview(ventana, columns=("col1"), style="mystyle.Treeview", selectmode='extended', height=22)
tv.place(x = 300, y = 10)


tv.column("#0",width=50, anchor=CENTER) 
tv.column("col1",width=200,anchor=CENTER)

tv.heading("#0", text="No.", anchor=CENTER)
tv.heading("col1", text="Contenedor", anchor=CENTER)


###Listas y variables###########################################################################################
global i #indice listos
i = 0
global i2 #indice vacios
i2 = 0
global ig #indice listos
ig = 0
global i2g #indice vacios
i2g = 0
global t  #Turnos
t = 0
global j #contador de turnos
j = 0
global pc #primer conteo
pc = 0

ID = []

###Pedir datos############################################################################################

def producir():
    global t
    global j
    global i
    global ig
    global ic
      
    for t2 in range (0, 22):
        if ID[t2] == "Lleno":
              ic = ic + 1
    if ic == 22:   
            #print("Limite")
            lit.config(text="Contenedor lleno")
            j = 0
            ventana.after(2000, procesos) 
    else:    
        ic = 0
        if i == 22: 
           # print("Reiniciar ciclo")
            i = 0
    
        ID[i] = "Lleno"
    
        for r in range (0, 22):
            tv.delete(tv.get_children()[0])
            tv.insert("", END, text=r+1, values=(ID[r]))
        
        #aumentar indices  
        i = i + 1
        ig = ig + 1
          
        cnum.config(text=j+1)
        
        if j < t-1:
             j = j + 1
             ventana.after(2000, producir) 
        else: 
           #  print("Fin producir")
             j = 0
             tur.config(text="Decidiendo turno")
             ventana.after(2000, procesos) 
    
    
def consumir():
    global t 
    global j
    global i2
    global ig
    global i2g
    
    if ig == i2g:  
       # print("Limite")
        lit.config(text="Contenedor vacio")
        j = 0
        ventana.after(2000, procesos) 
        
    else:
        if i2 == 22:
          # print("Reiniciar ciclo")
           i2 = 0
        
        ID[i2] = "Vacio"
        
        for r in range (0, 22):
            tv.delete(tv.get_children()[0])
            tv.insert("", END, text=r+1, values=(ID[r]))
            
        i2 = i2 + 1
        i2g = i2g + 1
        
       
        cnum.config(text=j+1)
        
        if j < t-1:
             j = j + 1
             ventana.after(2000, consumir) 
        else: 
           #  print("Fin consumir")
             tur.config(text="Decidiendo turno")
             j = 0
             ventana.after(2000, procesos) 
         

def procesos():
    global i
    global t  
    global pc
    global ic
    ic = 0
    
   # print(ID)
    moneda = int(random.randrange(0,11))
    t = int(random.randrange(3,7))
    
    if  pc == 0:
        moneda = 0
        pc = 1
        
    for t2 in range (0, 22):
        if ID[t2] == "Lleno":
            ic = ic + 1
    if ic == 22:
       # print("vaciar")
        moneda = 7
    ic = 0
    
    num.config(text=t)
    cnum.config(text="0")
    de = tkinter.Label(ventana, text="de",
                        font=("arial", 20),  bg="light yellow")
    de.place(x=120, y=370)
    lit.config(text="")
    
    if moneda < 6:
        tur.config(text="Turno del productor")
        Ptext.config(text="Activo", bg="green")
        Ctext.config(text="Inactivo",  bg="red") 
       # print("Produce", "Turnos", t)
        ventana.after(2000, producir) 
        
    else:
        tur.config(text="Turno del consumidor")
        Ctext.config(text="Activo", bg="green")
        Ptext.config(text="Inactivo",  bg="red")
       # print("Consume", "Turnos", t)
        ventana.after(2000, consumir)
        
        
def cargar():
    Boton1.place_forget()
    tur.config(text="Decidiendo turno")
    est = tkinter.Label(ventana, text="Estado",
                        font=("arial", 20),  bg="light yellow")
    est.place(x=100, y=280)    
    for r in range (0, 22):
       ID.append("Vacio") 
       tv.insert("", END, text=r+1, values=(ID[r]))
       
    ventana.after(2000, procesos) 
 
    
def key(event):   
   if event.keysym == 'Escape':
      #  print("fin")   
        ventana.destroy()
     
###Ventana principal#################################################################################

    
 

Ptitle = tkinter.Label(ventana, text="Productor", font=("arial", 20),  bg="light green")#foreground="red",  
Ptitle.place(x=90, y=20)

Ctitle = tkinter.Label(ventana, text="Consumidor", font=("arial", 20),  bg="light blue")
Ctitle.place(x=600, y=20)

Ptext = tkinter.Label(ventana, text="Inactivo", font=("arial", 20),  bg="red")
Ptext.place(x=100, y=220)

Ctext = tkinter.Label(ventana, text="Inactivo", font=("arial", 20),  bg="red")
Ctext.place(x=620, y=220)

fon = tkinter.Label(ventana, text="    ",
                    font=("arial", 150),  bg="light yellow")
fon.place(x=30, y=280)

tur = tkinter.Label(ventana, text="",  #Turno
                    font=("arial", 16),  bg="light yellow")
tur.place(x=40, y=330)

num = tkinter.Label(ventana, text="", #numero de turnos
                    font=("arial", 20),  bg="light yellow")
num.place(x=170, y=370)

cnum = tkinter.Label(ventana, text="", #Contador
                    font=("arial", 20),  bg="light yellow")
cnum.place(x=90, y=370)

lit = tkinter.Label(ventana, text="", #Limite 
                    font=("arial", 18),  bg="light yellow")
lit.place(x=40, y=410)

Boton1 = tkinter.Button(ventana, text="Iniciar",  font=("arial", 15), command=lambda: cargar())
Boton1.place(x = 110, y = 300)    

ventana.bind("<KeyRelease>", key)                            

ventana.mainloop()