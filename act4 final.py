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
import random
import keyboard


ventana = tkinter.Tk()
ventana.title("procesamiento por lotes")

ventana.geometry("650x450+300+200")

###Listas y variables########################################################################

#primera caja y datos originales
INDIC = []
IDs = []
OP = []
V1 = []
V2 = []
tiempo = []
ocurrido = []

#procesados
indi = []
IDs2 = []
OP2 = []
V12 = []
V22 = []
tiempo2 = []
timeres = []

global con  #agregar procesos
con = 0
global error #Contador de errores
error = 0
global lh
lh = 0
global lt
lt = 0
global tg
tg = 0
global i  # contador de lotes
i = 0
global loteres #Lotes a hacer
loteres = 0
global resto  #resto de lotes
resto = 0
global lista #limite del for
lista = 0
global resl
resl = 0
global ind #indice primera caja
ind = 0
global ind2 #indice segunda y tercera caja
ind2 = 0

global ctiempo #tiempo del proceso activo
ctiempo = 0
global box #primera caja validacion 
box = 0
global box2  #segunda caja validacion
box2 = 0
global box3 #tercera caja validacion
box3 = 0

global act  #activacion y pausa bandera
act = 1
global imp #interrupcion validacion 
imp = 1
global time_glo # tiempo global
time_glo = 0
global tt     #tiempo transcurrido 
tt = 0
global cint
cint = 0


###Pedir datos##################################################

def procesos(lote):
        
    Boton1.place_forget()
    n = int(lote)    
    
    label = tkinter.Label(ventana, text="Procesos agregados:")
    label.place(x=400, y=50)
    cl = tkinter.Label(ventana, text="0")
    cl.place(x=520, y=50)
    
    rnum = int(random.randrange(1000,2000))
    Boton3 = tkinter.Button(ventana, text="Ingresar", command=lambda: cargar(n, rnum))
        
    Boton3.place(x = 300, y = 350) 
    
    
    
 #####controlar datos###############################   
     
    def guardar(n, rnum):
        global con
        error = 0
        
        ID = int(rnum + con)       
        op = int(random.randrange(1,6))
        ap = int(random.randrange(1,100))
        bp = int(random.randrange(1,100))
        tp = int(random.randrange(5,17))
        
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
            error =+ 1
                    
        if error == 0:
            global time_glo
            
            INDIC.append(con+1)
            IDs.append(ID)
            V1.append(ap)
            V2.append(bp)
            OP.append(sig)
            tiempo.append(tp)
            time_glo = time_glo + tp
            n = n - 1   
            tv.insert("", END, text=INDIC[con], values=(ID, ap, sig, bp, tp))
            con = con + 1
           
            cl.config(text=con)
    
        
        ventana.after(100, cargar, n, rnum)
            
    def cargar(n, rnum):
        global con
        if n > 0:
            ventana.after(750, guardar, n, rnum)
        else:
            
            
            Boton3.place_forget()
            button4 = tkinter.Button(ventana, text="continuar", command=lambda: mostrar(con))
            button4.place(x=290, y=350)
            



#Mostrar procesos########################################################

        

###Crear segunda pantalla 
def mostrar(con):
     
    global time_glo
    global tt
    global lh
    user1 = tkinter.Toplevel(ventana)

    user1.title("Procesamiento por lotes")
    user1.geometry("1200x600+50+50")
    
    
    l = con
    lh = 0
    lt = 0
    tr = 0
    tg = 0
    
    ventana.withdraw() 
    
    label = tkinter.Label(user1, text="No. lotes pendientes:")
    label.place(x=50, y=10)
    
    
    label = tkinter.Label(user1, text="Procesos trabajando:")
    label.place(x=50, y=30)
    
    lt = tkinter.Label(user1, text=lh)
    lt.place(x=200, y=30)
    
    
    #segunda caja
    label = tkinter.Label(user1, text="Tiempo restante:")
    label.place(x=50, y=330)
    
    labeltr = tkinter.Label(user1, text=tr)
    labeltr.place(x=160, y=330)
    
    label = tkinter.Label(user1, text="Tiempo transcurrido:")
    label.place(x=250, y=330)
    
    labeltgc = tkinter.Label(user1, text=tt)
    labeltgc.place(x=370, y=330)
    
        
    #tercera caja
    label = tkinter.Label(user1, text="Tiempo maximo estimado:")
    label.place(x=750, y=120)
    
    label = tkinter.Label(user1, text=time_glo)
    label.place(x=950, y=120)
    
    label = tkinter.Label(user1, text="Tiempo global transcurrido:")
    label.place(x=750, y=150)
    
    labeltg = tkinter.Label(user1, text=tg)
    labeltg.place(x=950, y=150)
    
    label = tkinter.Label(user1, text="No. procesos Terminados:")
    label.place(x=750, y=180)
    
    labelh = tkinter.Label(user1, text=lh)
    labelh.place(x=950, y=180)
    
    #####Procesos
    tv1 = ttk.Treeview(user1, columns=("col1","col2","col3", "col4"))
    tv1.place(x = 50, y = 50)

    tv1.column("#0",width=50)
    tv1.column("col1",width=70,anchor=CENTER)
    tv1.column("col2",width=70,anchor=CENTER)
    tv1.column("col3",width=70,anchor=CENTER)
    tv1.column("col4",width=70,anchor=CENTER)
    
    tv1.heading("#0", text="No.")# anchor=CENTER)
    tv1.heading("col1", text="ID")# anchor=CENTER)
    tv1.heading("col2", text="No.1")# anchor=CENTER)
    tv1.heading("col3", text="No.2")# anchor=CENTER)
    tv1.heading("col4", text="Tiempo")# anchor=CENTER)

    #Procesos tabajando
    tv2 = ttk.Treeview(user1, columns=("col1","col2","col3", "col4"))
    tv2.place(x = 50, y = 355)

    tv2.column("#0",width=50)
    tv2.column("col1",width=80,anchor=CENTER)
    tv2.column("col2",width=80,anchor=CENTER)
    tv2.column("col3",width=80,anchor=CENTER)
    tv2.column("col4",width=80,anchor=CENTER)
    
    tv2.heading("#0", text="No.")# anchor=CENTER)
    tv2.heading("col1", text="ID")# anchor=CENTER)
    tv2.heading("col2", text="No.1")# anchor=CENTER)
    tv2.heading("col3", text="Op")# anchor=CENTER)
    tv2.heading("col4", text="No.2")# anchor=CENTER)
    
    
    #Procesos terminados
    tv3 = ttk.Treeview(user1, columns=("col1","col2","col3"))
    tv3.place(x = 750, y = 210)

    tv3.column("#0",width=50)
    tv3.column("col1",width=90,anchor=CENTER)
    tv3.column("col2",width=90,anchor=CENTER)
    tv3.column("col3",width=90,anchor=CENTER)
    
    tv3.heading("#0", text="No.")# anchor=CENTER)
    tv3.heading("col1", text="ID")# anchor=CENTER)
    tv3.heading("col2", text="Resultado")# anchor=CENTER)
    tv3.heading("col3", text="Tiempo")# anchor=CENTER)
    
    def fin():
        finl = tkinter.Label(user1, text="Lotes procesados")
        finl.place(x=600, y=50)
        b1 = tkinter.Button(user1, text="Salir")# command=terminar(user1))
        b1.place(x=650, y=70)
        
    def tercera_caja(e3):
        global lt
        global loteres
        global i
        global resto
        global ind2
        global box
        global box2
        global box3
        global tt
        global imp
        global cint
        global ind3
        
        if imp == 0: 
        
            user1.after(2000, segunda_caja)
        if imp == 1:
            if box2 == 1:
                if box3 == 0:
                    tv3.insert("", END, text="Lote", values=(i, "******", "********"))
                    
                box3 = 1
                tv2.delete(tv2.get_children()[0])
                #print("Restantes", box)
                if box > -1: 
                    
                    if OP2[ind2]=="+":
                            res = V12[ind2]+V22[ind2]
                    if OP2[ind2]=="-":
                          res = V12[ind2]-V22[ind2]
                    if OP2[ind2]=="*":
                          res = V12[ind2]*V22[ind2]
                    if OP2[ind2]=="/":
                          res = V12[ind2]/V22[ind2]
                    if OP2[ind2]=="%":
                          res = V12[ind2]%V22[ind2]  
                    if e3 == 1:
                        res = "ERROR"
                     
                    rei = 0
                    tt  = 0
                    labeltgc.config(text=rei)    
                    tv3.insert("", END, text=indi[ind2], values=(IDs2[ind2], res, tiempo2[ind2]))
                    ind2 = ind2 + 1 
                    lt = lt + 1
                    labelh.config(text=lt)    
                
            box2 = 0
            if e3 == 0: 
                if box > 0:
                    user1.after(2000, segunda_caja)
                elif loteres == 0:
                    resto = 0
                    user1.after(1000, iniciar, loteres, resto)
                else:
                    loteres = loteres - 1
                    user1.after(1000, iniciar, loteres, resto)  
            if e3 == 1:
                global act 
                act = 1
                user1.after(2000, segunda_caja)  
    
    def key(event):
         global act 
         global ctiempo
         global tt
         global box
         global box2
         global imp
         global ind2
         global lh
         global cint
         global con
         if (event.char == "p"):
             act = 0
             #label = tkinter.Label(user1, text="pausa")
             #label.place(x=400, y=50)   
         if (event.char == "c"):
             act = 1
             #label = tkinter.Label(user1, text="continuar")
             #label.place(x=400, y=50)  
         if (event.char == "i"):
             #label = tkinter.Label(user1, text="interrupcion")
             #label.place(x=400, y=50)
             if  box2 == 1:
                 tv2.delete(tv2.get_children()[0])
                 fal = ctiempo #tiempo faltante
                 ctiempo = 0   
                 tt  = 0
                 imp = 0  #interruptor de interrupciones
                 box2 = 0
                 labeltgc.config(text=tt) 
                 labeltr.config(text=ctiempo)
                 
                 indi.append(indi[ind2])
                 IDs2.append(IDs2[ind2])
                 V12.append(V12[ind2])
                 V22.append(V22[ind2])
                 OP2.append(OP2[ind2])
                 tiempo2.append(tiempo2[ind2])
                 timeres.append(fal)
                 
                 #print("agregado ind", ind2,"pro", IDs2[ind2])
                 tv1.insert("", END, text=indi[ind2], values=(IDs2[ind2], V12[ind2], V22[ind2], fal))
           
                 lh = lh + 1
                 lt.config(text=lh)
                 box = box + 1
                 ind2 = ind2 + 1 
                 e3 = 0
                 act = 1
                 user1.after(1000, tercera_caja, e3)

                 
         if (event.char == "e"):
            ctiempo = 0
            tt = 0
            #label = tkinter.Label(user1, text="error")
            #label.place(x=400, y=50)       
            labeltr.config(text=ctiempo)
            labeltgc.config(text=ctiempo)
            e3 = 1
            tercera_caja(e3)
            
  
    
    def time(): 
        global ctiempo
        global act
        global tt
        if act == 1: 
            ctiempo = ctiempo - 1
            tt = tt + 1
            if ctiempo > -1:
                    global tg
                    #ocurrido 
                    labeltgc.config(text=tt)
                    #restante
                    labeltr.config(text=ctiempo)
                    tg = tg + 1
                    labeltg.config(text=tg)
                    user1.after(1000, time)    
            else: 
                    e3 = 0
                    user1.after(1000, tercera_caja, e3)
        if act == 0:
            user1.after(1000, time)
        user1.bind("<KeyRelease>", key)

                     
    def segunda_caja():
        global ind2
        global ind3
        global ctiempo
        global box
        global box2
        global box4
        global imp 
        global cint
        global lh
        global tt
        if box2 == 0:
              if box != 0:   
                    imp = 1 
                    tv1.delete(tv1.get_children()[0])
                    box = box - 1
                    lh = lh - 1
                    lt.config(text=lh)
                    tv2.insert("", END, text=indi[ind2], values=(IDs2[ind2], V12[ind2], OP2[ind2], V22[ind2]))
                    #print("trabajando el indice:", ind2, "Pro:", IDs2[ind2])
                    box2 = 1  #Activar los metodos de la caja 1 y 2
                    ctiempo = 0
                    tt = 0
                    ctiempo = timeres[ind2] 
                    labeltr.config(text=ctiempo)
                    user1.after(200, time)  
                    
                    
    def primera_caja(jc):
        global lista
        global ind
        global loteres
        global box
        global lh
        if jc < lista:
                tv1.insert("", END, text=INDIC[ind], values=(IDs[ind], V1[ind], V2[ind], tiempo[ind]))
                labeltgc.config(text=tt) 
                labeltr.config(text=ctiempo)
                #agregar datos
                indi.append(INDIC[ind])
                IDs2.append(IDs[ind])
                V12.append(V1[ind])
                V22.append(V2[ind])
                OP2.append(OP[ind])
                tiempo2.append(tiempo[ind])
                timeres.append(tiempo[ind])
                ind = ind + 1
                jc = jc + 1 
                lh = lh + 1
                lt.config(text=lh)
                user1.after(1000, primera_caja, jc)
        else:
                box = jc
                user1.after(2000, segunda_caja)


    
    global loteres
    global resto
    global resl
    loteres = l//4
    resto   = l-(loteres*4) 
    if resto == 0:
      resl = loteres
    else: 
        resl = loteres + 1 
 
    
    labelp = tkinter.Label(user1, text=resl)
    labelp.place(x=200, y=10)
    

    Boton3 = tkinter.Button(user1, text="Iniciar", command=lambda: iniciar(loteres, resto))
    Boton3.place(x = 300, y = 20)  
       
    def iniciar(l, r):
        global lista
        global i 
        global resl
        global box3
        global cint 
        cint = 0
        i = i + 1
        i2 = resl - i
        box3 = 0
        if l > 0:
            labelp.config(text=i2)
            lista = 4
            jc = 0
            user1.after(1000, primera_caja, jc)
        elif r > 0:
            labelp.config(text=i2)
            lista = resto
            jc = 0
            user1.after(1000, primera_caja, jc)
        else:
            fin()
            
            
    
    user1.mainloop()

###Ventana principal##################################################

label = tkinter.Label(ventana, text="No. Procesos:")
label.place(x=80, y=40)
   
entry_lote = Entry(ventana)
entry_lote.place(x=80, y=60)
entry_lote.focus()

tv = ttk.Treeview(ventana, columns=("col1","col2","col3", "col4", "col5"))
tv.place(x = 70, y = 100)

tv.column("#0",width=40)
tv.column("col1",width=90,anchor=CENTER)
tv.column("col2",width=90,anchor=CENTER)
tv.column("col3",width=90,anchor=CENTER)
tv.column("col4",width=90,anchor=CENTER)
tv.column("col5",width=90,anchor=CENTER)

tv.heading("#0", text="No.")# anchor=CENTER)
tv.heading("col1", text="ID")# anchor=CENTER)
tv.heading("col2", text="No.1")# anchor=CENTER)
tv.heading("col3", text="OP")# anchor=CENTER)
tv.heading("col4", text="No.2")# anchor=CENTER)
tv.heading("col5", text="Tiempo")# anchor=CENTER)
    
Boton1 = tkinter.Button(ventana, text="Ingresar", command=lambda: procesos(entry_lote.get()))
Boton1.place(x = 200, y = 60)     

bsalir=Button(ventana,text="Salir", command=ventana.destroy)
bsalir.place(x= 750, y = 350)
                            

ventana.mainloop()