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
from tkinter import ttk
import random
import keyboard


ventana = tkinter.Tk()
ventana.title("FCFS")

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
lle2 = []
esp2 = []
res2 = []

#bloqueados
Bind = []
BIDs = []
BOP = []
BV1 = []
BV2 = []
Btiempo = []
Btimeres = []
timeB = []
Blle = []
Besp = []
Bresp = []

#tiempos 
TID = []
Llegada = []
Finalizacion = []
Retorno = []
Respuesta = []
Espera = []
Servicio = []


global con  #agregar procesos
con = 0
global error #Contador de errores
error = 0
global lh #procesos en listo
lh = 0
global lt
lt = 0
global tg
tg = 0
global i  # contador de lotes
i = 0
global te #tiempo error
te = 0
global e3
e3 = 0
global new #procesos en nuevo
new = 0
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
global ind3 #indice para bloqueados
ind3 = 0
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
global ActBlo #activar tiempo en bloqueados
ActBlo = 0
global ultimo 
ultimo = 0


###Pedir datos##################################################

def procesos(lote):
        
    Boton1.place_forget()
    n = int(lote)    
    
    label = tkinter.Label(ventana, text="Procesos agregados:")
    label.place(x=400, y=50)
    cl = tkinter.Label(ventana, text="0")
    cl.place(x=520, y=50)
    
    rnum = int(random.randrange(1000,2000))
    
    global con
    error = 0
    for i in range(0, n):
    
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

    button4 = tkinter.Button(ventana, text="continuar", command=lambda: mostrar(con))
    button4.place(x=290, y=350)
    
    
####Mostrar procesos########################################################

        
###Crear segunda pantalla 
def mostrar(con):
     
    global time_glo
    global tt
    global lh
    user1 = tkinter.Toplevel(ventana)

    user1.title("FCFS")
    user1.geometry("1000x600+25+25")
    
    l = con
    lh = 0
    lt = 0
    tr = 0
    tg = 0
    
    ventana.withdraw() 
    
    label = tkinter.Label(user1, text="Procesos en Nuevo:")
    label.place(x=50, y=10)
    
    
    label = tkinter.Label(user1, text="Procesos en listo:")
    label.place(x=50, y=30)
    
    pl = tkinter.Label(user1, text=lh)
    pl.place(x=200, y=30)
    
    
    #segunda caja
    label = tkinter.Label(user1, text="Tiempo restante:")
    label.place(x=50, y=330)
    
    labeltr = tkinter.Label(user1, text=tr)
    labeltr.place(x=160, y=330)
    
    label = tkinter.Label(user1, text="Tiempo transcurrido:")
    label.place(x=200, y=330)
    
    labeltgc = tkinter.Label(user1, text=tt)
    labeltgc.place(x=320, y=330)
    
        
    #tercera caja
    label = tkinter.Label(user1, text="Tiempo maximo estimado:")
    label.place(x=650, y=10)
    
    label = tkinter.Label(user1, text=time_glo)
    label.place(x=900, y=10)
    
    label = tkinter.Label(user1, text="Tiempo global transcurrido:")
    label.place(x=650, y=40)
    
    labeltg = tkinter.Label(user1, text=tg)
    labeltg.place(x=900, y=40)
    
    label = tkinter.Label(user1, text="Procesos en terminados:")
    label.place(x=650, y=70)
    
    labelh = tkinter.Label(user1, text=lh)
    labelh.place(x=900, y=70)
    
    #bloqueados
    label = tkinter.Label(user1, text="Bloqueados")
    label.place(x=400, y=30)
    
    
    #bloqueados
    label = tkinter.Label(user1, text="Tiempos de procesos")
    label.place(x=400, y=330)
    
    
    #####Procesos
    tv1 = ttk.Treeview(user1, columns=("col1","col2"))
    tv1.place(x = 50, y = 50)

    tv1.column("#0",width=90)
    tv1.column("col1",width=100,anchor=CENTER)
    tv1.column("col2",width=100,anchor=CENTER)
    
    tv1.heading("#0", text="ID")# anchor=CENTER)
    tv1.heading("col1", text="T. Maximo")# anchor=CENTER)
    tv1.heading("col2", text="T. transcurrido")# anchor=CENTER)

    #Procesos tabajando
    tv2 = ttk.Treeview(user1, columns=("col1","col2","col3"))
    tv2.place(x = 50, y = 355)

    tv2.column("#0",width=50)
    tv2.column("col1",width=80,anchor=CENTER)
    tv2.column("col2",width=80,anchor=CENTER)
    tv2.column("col3",width=80,anchor=CENTER)
    
    tv2.heading("#0", text="ID")# anchor=CENTER)
    tv2.heading("col1", text="No.1")# anchor=CENTER)
    tv2.heading("col2", text="Op")# anchor=CENTER)
    tv2.heading("col3", text="No.2")# anchor=CENTER)
    
    
    #Procesos terminados
    tv3 = ttk.Treeview(user1, columns=("col1","col2", "col3"))
    tv3.place(x = 600, y = 100)

    tv3.column("#0",width=90)
    tv3.column("col1",width=90,anchor=CENTER)
    tv3.column("col2",width=90,anchor=CENTER)
    tv3.column("col3",width=90,anchor=CENTER)
    
    tv3.heading("#0", text="ID")# anchor=CENTER)
    tv3.heading("col1", text="Operacion")# anchor=CENTER)
    tv3.heading("col2", text="Resultado")# anchor=CENTER)
    tv3.heading("col3", text="Tiempo")# anchor=CENTER)
    
    #####bloqueados
    tv4 = ttk.Treeview(user1, columns=("col1"))
    tv4.place(x = 400, y = 50)

    tv4.column("#0",width=80)
    tv4.column("col1",width=80,anchor=CENTER)
    
    tv4.heading("#0", text="ID")# anchor=CENTER)
    tv4.heading("col1", text="Restante")# anchor=CENTER)
    
    
   #####tiempos
    tv5 = ttk.Treeview(user1, columns=("col1","col2","col3", "col4", "col5", "col6"))
    tv5.place(x = 400, y = 355)

    tv5.column("#0",width=80)
    tv5.column("col1",width=80,anchor=CENTER)
    tv5.column("col2",width=80,anchor=CENTER)
    tv5.column("col3",width=80,anchor=CENTER)
    tv5.column("col4",width=80,anchor=CENTER)
    tv5.column("col5",width=80,anchor=CENTER)
    tv5.column("col6",width=80,anchor=CENTER)
    
    tv5.heading("#0", text="ID")# anchor=CENTER)
    tv5.heading("col1", text="Llegada")# anchor=CENTER)
    tv5.heading("col2", text="Finalizacion")# anchor=CENTER)
    tv5.heading("col3", text="Retorno")# anchor=CENTER)
    tv5.heading("col4", text="Respuesta")# anchor=CENTER)
    tv5.heading("col5", text="Espera")# anchor=CENTER)
    tv5.heading("col6", text="Servicio")# anchor=CENTER)
    
    
    ###########Metodos
    def fin():
        for t in range (0, l):
            tv5.insert("", END, text=TID[t], values=(Llegada[t], Finalizacion[t], Retorno[t], 
                                                     Respuesta[t], Espera[t], Servicio[t]))
        finl = tkinter.Label(user1, text="Procesos terminados")
        finl.place(x=250, y=20)
        
    def tercera_caja():
        global lt
        global ind
        global ind2
        global box
        global box2
        global tt
        global imp
        global ind3
        global tg
        global lh
        global new
        global te
        global e3
        global act 
        global resp
        
        if imp == 0: 
            user1.after(1000, segunda_caja)
        if imp == 1:
            if box2 == 1:
                tv2.delete(tv2.get_children()[0])
                if box > -1: 
                    
                    if OP2[ind2]=="+":
                            res = V12[ind2]+V22[ind2]
                    if OP2[ind2]=="-":
                          res = V12[ind2]-V22[ind2]
                    if OP2[ind2]=="*":
                          res = V12[ind2]*V22[ind2]
                    if OP2[ind2]=="/":
                          res = "{0:.4f}".format(V12[ind2]/V22[ind2])
                    if OP2[ind2]=="%":
                          res = "{0:.4f}".format(V12[ind2]%V22[ind2])
                    if e3 == 1:
                        res = "ERROR"
                     
                    rei = 0
                    labeltgc.config(text=rei)    
                    tv3.insert("", END, text=IDs2[ind2], values=((V12[ind2], OP2[ind2], V22[ind2]), 
                                                                 res, tiempo2[ind2]))
                    #tiempos 
                    TID.append(IDs2[ind2])
                    Llegada.append(lle2[ind2])
                    Finalizacion.append(tg)
                    Retorno.append(tg - lle2[ind2])     
                     
                    Respuesta.append(res2[ind2])  
                    
                    Espera.append(esp2[ind2])
                    s = tiempo2[ind2]
                    if e3==1:
                        s = te
                    Servicio.append(s)           
         
                    tt  = 0                                       
                    #Aumenetar tiempos
                    ind2 = ind2 + 1 
                    lt = lt + 1
                    labelh.config(text=lt)  
                    
                    box2 = 0
                    act = 1
                    e3 = 0
                    
                    if ind < l:
                        tv1.insert("", END, text=IDs[ind], values=(tiempo[ind], tiempo[ind]))
         
                        #agregar datos
                        indi.append(INDIC[ind])
                        IDs2.append(IDs[ind])
                        V12.append(V1[ind])
                        V22.append(V2[ind])
                        OP2.append(OP[ind])
                        tiempo2.append(tiempo[ind])
                        timeres.append(tiempo[ind])
                        lle2.append(tg)
                        
                        new = new - 1
                        labelp.config(text=new)
                        
                        lh = lh + 1
                        pl.config(text=lh)
                        
                        ind = ind + 1
                        box = box + 1
                    
                    user1.after(2000, segunda_caja)
 
    
    def key(event):
         global act 
         global ctiempo
         global tt
         global box
         global box2
         global imp
         global ind2
         global ind3
         global lh
         global ActBlo
         global te
         global e3 
         
         if (event.char == "p"):
             act = 0  
         if (event.char == "c"):
             act = 1
         if (event.char == "e"):
                te = tt
                ctiempo = 0
                tt = 0      
                labeltr.config(text=ctiempo)
                labeltgc.config(text=ctiempo)
                e3 = 1
         if (event.char == "i"):
             if  box2 == 1:
                 global box3
                 tv2.delete(tv2.get_children()[0])
                 fal = ctiempo #tiempo faltante
                 ctiempo = 0   
                 tt  = 0
                 imp = 0  #interruptor de interrupciones
                 box2 = 0
                 ActBlo = 1 #activar el bloqueo

                 labeltgc.config(text=tt) 
                 labeltr.config(text=ctiempo)
                 
                 Bind.append(indi[ind2])
                 BIDs.append(IDs2[ind2])
                 BV1.append(V12[ind2])
                 BV2.append(V22[ind2])
                 BOP.append(OP2[ind2])
                 Btiempo.append(tiempo2[ind2])
                 Btimeres.append(fal)
                 timeB.append(9)
                 Blle.append(lle2[ind2])
                 #Bresp.append(res2[ind2])
                 
                 tv4.insert("", END, text=IDs2[ind2], values=(8))
                 box3 = box3 + 1
                 ind3 = ind3 + 1
                 ind2 = ind2 + 1     

            
    def bloqueo():
        global tt
        global ActBlo
        global box
        global ind3 
        global box3
        global lh
        global ultimo 
        global ctiempo
        global b2 
        global tg
  
        x = tv4.get_children()
        delete = 0
        for b in range (0, box3):
             timeB[b] = timeB[b] - 1
        b2 = 0
        for item in x: 
            tv4.item(item, values=(timeB[b2]))
            b2 = b2 + 1   
        for b in range (0, box3):    
            if timeB[b] == -1:
                tv4.delete(tv4.get_children()[0])
                trans = Btiempo[b] - Btimeres[b]
                tv1.insert("", END, text=BIDs[0], values=(Btiempo[0], trans))
                #agregar datos
                lh = lh + 1
                pl.config(text=lh)
                indi.append(Bind[b])
                IDs2.append(BIDs[b])
                V12.append(BV1[b])
                V22.append(BV2[b])
                OP2.append(BOP[b])
                tiempo2.append(Btiempo[b])
                timeres.append(Btimeres[b])
                lle2.append(Blle[b])
                delete = 1
                
        if delete == 1:
            #eliminar datos 
            BIDs.pop(0)
            timeB.pop(0)
            Bind.pop(0)
            BV1.pop(0)
            BV2.pop(0)
            BOP.pop(0)
            Btiempo.pop(0)
            Btimeres.pop(0)
            Blle.pop(0)
            delete = 0
            box = box + 1
            box3 = box3 - 1
            if ultimo == 1:
                ctiempo = 0
                ultimo = 0
                user1.after(2000, segunda_caja)  
        if ultimo == 1:
             user1.after(1000, time_ultimo) 
    
    def time_ultimo():
        #global tg
        #tg = tg + 1
        #labeltg.config(text=tg)
        user1.after(1000, bloqueo)
    
    def time(): 
        global ctiempo
        global act
        global tt
        global ActBlo
        global box
        global ind3 
        global box3
        global lh
        global tg #tiempo global transcurrido
        global ultimo
        global imp
        
        if act == 1: 
            ctiempo = ctiempo - 1
            tt = tt + 1      
            if box3 > 0:
                    bloqueo()                         
            if ctiempo > -1:
                    #ocurrido 
                    labeltgc.config(text=tt)
                    #restante
                    labeltr.config(text=ctiempo)
                    tg = tg + 1
                    labeltg.config(text=tg)
                    user1.after(1000, time)    
            else: 
                    user1.after(1000, tercera_caja)
        if act == 0:
            user1.after(1000, time)
        user1.bind("<KeyRelease>", key)
        
        
    def segunda_caja():
        global ind2
        global ctiempo
        global box
        global box2
        global imp 
        global lh
        global tt
        global tg
        global ultimo
        #global re 
        #re = 0
        if box2 == 0:  
              if box == 0 and box3 == 0:
                    fin()               
              if box == 0 and box3 != 0: 
                  ultimo = 1
                  user1.after(1000, time_ultimo) 
              if box != 0:  
                    imp = 1 
                    tv1.delete(tv1.get_children()[0])
                    box = box - 1
                    lh = lh - 1
                    pl.config(text=lh)
                    tv2.insert("", END, text=IDs2[ind2], values=(V12[ind2], OP2[ind2], V22[ind2]))
                    re = 0
                    for r, t in enumerate(indi):
                        if indi[ind2] == t:
                            re = re + 1    
                            if re == 2:
                                res2.append(res2[rind])  
                            rind =  int(r) 
                    if re == 1:  
                       res2.append(tg)  
                    esp2.append(tg)
                    box2 = 1  #Activar los metodos de la caja 1 y 2
                    ctiempo = 0
                    tt = 0
                    ctiempo = timeres[ind2] 
                    labeltr.config(text=ctiempo)
                    user1.after(1000, time) 
 
            
    def primera_caja(jc):
        global lista
        global ind
        global loteres
        global box
        global lh
        global tg
        global new
        if jc < lista:
                tv1.insert("", END, text=IDs[ind], values=(tiempo[ind], tiempo[ind]))
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
                lle2.append(tg)
                #modificar datos
                new = new - 1
                labelp.config(text=new)
                ind = ind + 1
                jc = jc + 1 
                lh = lh + 1
                pl.config(text=lh)
                user1.after(1000, primera_caja, jc)
        else:
                box = jc
                user1.after(2000, segunda_caja)


    
    global loteres
    global resto
    global resl
    global new
    loteres = l//4
    resto   = l-(loteres*4) 
    if resto == 0:
      resl = loteres
    else: 
        resl = loteres + 1 
 
    new = l
    labelp = tkinter.Label(user1, text=new)
    labelp.place(x=200, y=10)
    

    Boton3 = tkinter.Button(user1, text="Iniciar", command=lambda: iniciar(loteres, resto))
    Boton3.place(x = 300, y = 20)  
       
    def iniciar(l, r):
        global lista
        global resl
        global box3
        box3 = 0
        Boton3.place_forget()
        if l > 0:
            lista = 4
            jc = 0
            user1.after(1000, primera_caja, jc)
        elif r > 0:
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
                            

ventana.mainloop()