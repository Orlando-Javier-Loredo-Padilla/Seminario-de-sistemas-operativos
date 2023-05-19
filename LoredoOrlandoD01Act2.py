# -*- coding: utf-8 -*-
"""
Created on Thu Feb  2 15:27:34 2023

@author: Orlando
"""

from tkinter import Tk, Canvas, Frame, Label, Entry, Button, W, E, Listbox, END
import tkinter
import contextlib
import io
from tkinter import font
from PIL import ImageTk, Image
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from tkinter import PhotoImage
from tkinter import *
from tkinter import ttk
#import time

ventana = tkinter.Tk()
ventana.title("procesamiento por lotes")

ventana.geometry("650x450+300+200")

###Listas y variables########################################################################

nombres = []
IDs = []
OP = []
V1 = []
V2 = []
tiempo = []

#Tnombres = []
#TIDs = []
#Toperacion = []
#Ta = []
#Tb = []
#Ttiempo = []

global con
con = 0
global error
error = 0
global lh
lh = 0
global lt
lt = 0
global tg
tg = 0
global tt
tt = 0
global j
j = 0
global loteres 
loteres = 0
global au
au = 0



###Pedir datos##################################################

def procesos(lote):
        
    Boton1.place_forget()
    n = int(lote)    
    
    ##Nombre 
    
    label = tkinter.Label(ventana, text="Procesos ingresados:")
    label.place(x=400, y=50)
    cl = tkinter.Label(ventana, text="0")
    cl.place(x=530, y=50)
    
    
    label = tkinter.Label(ventana, text="Nombre:")
    label.place(x=80, y=120)
       
    entry = Entry(ventana)
    entry.place(x=80, y=140)
    entry.focus()
    
    ###ID
    label2 = tkinter.Label(ventana, text="ID:")
    label2.place(x=240, y=120)
       
    entry2 = Entry(ventana)
    entry2.place(x=240, y=140)
    entry2.focus()
    
    ####Operaciones
 
    label3 = tkinter.Label(ventana, text="Operaciones: 1-Suma 2- Resta"  + "\n" +
                                           "3-Multiplicacion 4-Division 5-Residuo")
    label3.place(x=80, y=170)
    label3 = tkinter.Label(ventana, text="Operacion:")
    label3.place(x=80, y=210)

    label3 = tkinter.Label(ventana, text="Primer No.")
    label3.place(x=80, y=230)
    label3 = tkinter.Label(ventana, text="Segundo No.")
    label3.place(x=240, y=230)
       
    entry3 = Entry(ventana)
    entry3.place(x=80, y=250)
    entry3.focus()
    
    entry4 = Entry(ventana)
    entry4.place(x=240, y=250)
    entry4.focus()
    
    entry5 = Entry(ventana)
    entry5.place(x=160, y=210)
    entry5.focus()
    
    #####Tiempo 
    label6 = tkinter.Label(ventana, text="Tiempo estimado:")
    label6.place(x=80, y=270)
       
    entry6 = Entry(ventana)
    entry6.place(x=80, y=290)
    entry6.focus()

    ####Agregar datos
    Boton3 = tkinter.Button(ventana, text="Ingresar", command=lambda: 
                            contador(n, entry.get(), entry2.get(), entry3.get(),
                                     entry4.get(), entry5.get(), entry6.get()))
    Boton3.place(x = 300, y = 350)  
    
 #####controlar datos###############################   
    
    def contador(n, name, ID, a, b, op, t): 
        global con
        global error
        error = 0
        
        #print(con)   
        op = int(op)
        ap = int(a)
        bp = int(b)
        tp = int(t)
        
        if (op < 1 or op > 5):
            messagebox.showinfo(message="Opción no valida",
                                title="Advertencia")
            error =+ 1
            
        if op==1:
                sig = "+"
        if op==2:
                sig = "-"  
        if op==3:
                sig = "*"
        if op==4:
                sig = "/"  
        if op==5:
                sig = "%"   
                
        if ID in IDs:
            messagebox.showinfo(message="ID repetido",
                                title="Advertencia")
            error =+ 1
            
        if op == 4 or op == 5: 
            if bp == 0:  
                error =+1    
                messagebox.showinfo(message="La division no acepta 0",
                                    title="Advertencia")
        
        if tp < 1:
            messagebox.showinfo(message="Tiempo no valido", title="Advertencia")
            error =+1   
    
        
        if error == 0:
            #print("Lote agregado")
            nombres.append(name)
            IDs.append(ID)
            V1.append(ap)
            V2.append(bp)
            OP.append(sig)
            tiempo.append(tp)
            #print(nombres[con], IDs[con], V1[con], V2[con], tiempo[con])
            
            entry.delete(first=0,last='end')
            entry2.delete(first=0,last='end')
            entry3.delete(first=0,last='end')
            entry4.delete(first=0,last='end')
            entry5.delete(first=0,last='end')
            entry6.delete(first=0,last='end')
            con = con + 1   
            cl.config(text=con)
    
            if con > n-1:
                
                Boton3.place_forget()
                button4 = tkinter.Button(ventana, text="coninutar", command=mostrar(n))
                button4.place(x=290, y=350)
        else:
            print("No")


    
#Mostrar procesos########################################################

        

###Crear segunda pantalla 
def mostrar(n):
     
    user1 = tkinter.Toplevel(ventana)

    user1.title("Procesamiento por lotes")
    user1.geometry("900x600+50+50")
    
    
    l = n
    lh = 0
    lt = 0
    tr = 0
    tg = 0
    ventana.withdraw() 
    
    label = tkinter.Label(user1, text="No. Lotes totales:")
    label.place(x=50, y=10)
    
    
    label = tkinter.Label(user1, text="Procesos en espera:")
    label.place(x=50, y=30)
    
    lt = tkinter.Label(user1, text=lh)
    lt.place(x=180, y=30)
    
    
    label = tkinter.Label(user1, text="Tiempo restante:")
    label.place(x=50, y=330)
    
    labeltr = tkinter.Label(user1, text=tr)
    labeltr.place(x=160, y=330)
    
    
    label = tkinter.Label(user1, text="Tiempo global:")
    label.place(x=500, y=150)
    
    labeltg = tkinter.Label(user1, text=tg)
    labeltg.place(x=700, y=150)
    
    label = tkinter.Label(user1, text="No. Procesos Terminados:")
    label.place(x=500, y=180)
    
    labelh = tkinter.Label(user1, text=lh)
    labelh.place(x=700, y=180)
    
    #####Procesos
    tv1 = ttk.Treeview(user1, columns=("col1","col2","col3", "col4", "col5"))
    tv1.place(x = 50, y = 50)

    tv1.column("#0",width=30)
    tv1.column("col1",width=70,anchor=CENTER)
    tv1.column("col2",width=70,anchor=CENTER)
    tv1.column("col3",width=70,anchor=CENTER)
    tv1.column("col4",width=70,anchor=CENTER)
    tv1.column("col5",width=70,anchor=CENTER)
    
    tv1.heading("#0", text="No.")# anchor=CENTER)
    tv1.heading("col1", text="Nombre")# anchor=CENTER)
    tv1.heading("col2", text="ID")# anchor=CENTER)
    tv1.heading("col3", text="No.1")# anchor=CENTER)
    tv1.heading("col4", text="No.2")# anchor=CENTER)
    tv1.heading("col5", text="Tiempo")# anchor=CENTER)

    #Procesos tabajando
    tv2 = ttk.Treeview(user1, columns=("col1","col2","col3", "col4", "col5"))
    tv2.place(x = 50, y = 355)

    tv2.column("#0",width=30)
    tv2.column("col1",width=70,anchor=CENTER)
    tv2.column("col2",width=70,anchor=CENTER)
    tv2.column("col3",width=70,anchor=CENTER)
    tv2.column("col4",width=70,anchor=CENTER)
    tv2.column("col5",width=70,anchor=CENTER)
    
    tv2.heading("#0", text="No.")# anchor=CENTER)
    tv2.heading("col1", text="Nombre")# anchor=CENTER)
    tv2.heading("col2", text="ID")# anchor=CENTER)
    tv2.heading("col3", text="No.1")# anchor=CENTER)
    tv2.heading("col4", text="Op")# anchor=CENTER)
    tv2.heading("col5", text="No.2")# anchor=CENTER)
    
    
    #Procesos terminados
    tv3 = ttk.Treeview(user1, columns=("col1","col2","col3", "col4"))
    tv3.place(x = 500, y = 200)

    tv3.column("#0",width=30)
    tv3.column("col1",width=70,anchor=CENTER)
    tv3.column("col2",width=70,anchor=CENTER)
    tv3.column("col3",width=70,anchor=CENTER)
    tv3.column("col4",width=70,anchor=CENTER)
    
    tv3.heading("#0", text="No.")# anchor=CENTER)
    tv3.heading("col1", text="Nombre")# anchor=CENTER)
    tv3.heading("col2", text="ID")# anchor=CENTER)
    tv3.heading("col3", text="Resultado")# anchor=CENTER)
    tv3.heading("col4", text="Tiempo")# anchor=CENTER)
    
        
    def tercera_caja(i, x):
        global lt
        global loteres
        global au 
        
        tv2.delete(tv2.get_children()[0])
        if OP[i+au]=="+":
                res = V1[i+au]+V2[i+au]
        if OP[i+au]=="-":
              res = V1[i+au]-V2[i+au]
        if OP[i+au]=="*":
              res = V1[i+au]*V2[i+au]
        if OP[i+au]=="/":
              res = V1[i+au]/V2[i+au]
        if OP[i+au]=="%":
              res = V1[i+au]%V2[i+au]           
        tv3.insert("", END, text=i+au+1, values=(nombres[i+au], IDs[i+au], res, tiempo[i+au]))
        lt = lt + 1
        labelh.config(text=lt)    
        i = i + 1
        if x > 0:
            user1.after(2000, segunda_caja, i , x)
        else:
            au = au + 4
            loteres = loteres - 1
            user1.after(1000, iniciar, loteres)   
    
    def time(tt, i, x): 
        tt = tt - 1
        if tt > -1:
            global tg
            labeltr.config(text=tt)
            tg = tg + 1
            labeltg.config(text=tg)
            user1.after(1000, time, tt, i, x)
        else: 
            user1.after(1000, tercera_caja, i, x)
             
    
    def segunda_caja(i, x):
        global au
        tv1.delete(tv1.get_children()[0])
        x = x - 1
        lt.config(text=x)
        tv2.insert("", END, text=i+1, values=(nombres[i+au], IDs[i+au], V1[i+au], OP[i+au], V2[i+au]))
        tt = tiempo[i+au] 
        labeltr.config(text=tt)
        user1.after(1000, time, tt, i, x)
       
    def primera_caja(jc):
        global j
        if jc < 4:
            tv1.insert("", END, text=j+1, values=(nombres[j], IDs[j], V1[j], V2[j], tiempo[j]))
            j = j + 1
            jc = jc + 1  
            lt.config(text=j)
            user1.after(1000, primera_caja, jc)
        else:
            x = jc
            i = 0
            user1.after(2000, segunda_caja, i , x)

    
    global loteres
    loteres = l//4
    
    label = tkinter.Label(user1, text=loteres)
    label.place(x=170, y=10)
    
    Boton3 = tkinter.Button(user1, text="Iniciar", command=lambda: iniciar(loteres))
    Boton3.place(x = 300, y = 20)  
       
    def iniciar(l):
        
        if l > 0:
            jc = 0
            user1.after(1000, primera_caja, jc)
        else:
            finl = tkinter.Label(user1, text="Lotes procesados")
            finl.place(x=600, y=50)
            b1 = tkinter.Button(user1, text="Salir")# command=terminar(user1))
            b1.place(x=650, y=70)
            
            
    
    user1.mainloop()

###Ventana principal##################################################

label = tkinter.Label(ventana, text="No. Procesos:")
label.place(x=80, y=40)
   
entry_lote = Entry(ventana)
entry_lote.place(x=80, y=60)
entry_lote.focus()
    
Boton1 = tkinter.Button(ventana, text="Ingresar", command=lambda: procesos(entry_lote.get()))
Boton1.place(x = 200, y = 60)     

bsalir=Button(ventana,text="Salir", command=ventana.destroy)
bsalir.place(x= 500, y = 350)
                            

ventana.mainloop()