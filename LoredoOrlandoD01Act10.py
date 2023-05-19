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
from tkinter import messagebox


ventana = tkinter.Tk()
ventana.title("Round-Robin")

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

#tabla 
Tid = []
TOP = []
TV1 = []
TV2 = []
Ttiempo = []
Tres = []
Tresb = []
Tresultado = []
estado = []
TLlegada = []
TFinalizacion = []
TRetorno = []
TRespuesta = []
TEspera = []
TServicio = []
bloqueos = []

#########Variables################################## 

global con  #agregar procesos
con = 0
global lh #procesos en listo
lh = 0
global lt
lt = 0
global tg
tg = 0
global te #tiempo error
te = 0
global e3
e3 = 0
global new #procesos en nuevo
new = 0
global lista #limite del for
lista = 0
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
global memoria
memoria = 0
global total
total = 0
global indice 
indice = 0
global tabla 
tabla = 0
global tabla2
tabla2 = 0
global ins
ins = 0
global quantum
quantum = 0
global qt
qt = 0

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
    global indice
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
        
        #Tabla
        Tid.append(ID)
        TV1.append(ap)
        TV2.append(bp)
        TOP.append(sig)
        TServicio.append(tp)        
        Tres.append(0)
        estado.append("Nuevo")
        Tresultado.append("-")
        TLlegada.append("-")
        TFinalizacion.append("-")
        TRetorno.append("-")
        TRespuesta.append("-")
        TEspera.append("-")

        n = n - 1   
        tv.insert("", END, text=INDIC[con], values=(ID, ap, sig, bp, tp))
        con = con + 1
         
        indice = ID
        cl.config(text=con)
        
    ###quantum 
    label = tkinter.Label(ventana, text="Quantum")
    label.place(x=250, y=40)
       
    entry_quantum = Entry(ventana)
    entry_quantum.place(x=250, y=60)
    entry_quantum.focus()
    
    Boton2 = tkinter.Button(ventana, text="Ingresar Quantum", command=lambda: 
                            validacion(entry_quantum.get()))
    Boton2.place(x = 270, y = 350)  
        
    def validacion(q):
       
       qv = int(q)
       if qv > 0:
           Boton2.place_forget()
           global quantum
           quantum = qv
           button4 = tkinter.Button(ventana, text="Continuar", command=lambda: mostrar(con))
           button4.place(x=290, y=350)
       else:
           messagebox.showinfo(message="Quantum no puede ser menor a 1",
                                    title="Advertencia")        
    
    
    
####pantalla de tiempos########################################################


def salir(ventana_a_cerrar):
    global act
    act = 1
    ventana_a_cerrar.destroy()
    #user1.deiconify()
    
def tiempos_pantalla(anterior):
     
    global time_glo
    global tt
    global lh
    global con
    user2 = tkinter.Toplevel(anterior)

    user2.title("Tiempos")
    user2.geometry("900x350+400+25")
    
    label = tkinter.Label(user2, text="Tabla de procesos")
    label.place(x=50, y=25)
    
    tv6 = ttk.Treeview(user2, columns=("col1","col2","col3", "col4",
                                       "col5", "col6", "col7", "col8", "col9", "col10"))
    tv6.place(x = 50, y = 50)

    tv6.column("#0",width=70, anchor=CENTER)
    tv6.column("col1",width=70,anchor=CENTER)
    tv6.column("col2",width=70,anchor=CENTER)
    tv6.column("col3",width=70,anchor=CENTER)
    tv6.column("col4",width=70,anchor=CENTER)
    tv6.column("col5",width=70,anchor=CENTER)
    tv6.column("col6",width=70,anchor=CENTER)
    tv6.column("col7",width=70,anchor=CENTER)
    tv6.column("col8",width=70,anchor=CENTER)
    tv6.column("col9",width=70,anchor=CENTER)
    tv6.column("col10",width=70,anchor=CENTER)
    
    
    tv6.heading("#0", text="ID")# anchor=CENTER)
    tv6.heading("col1", text="Estado")# anchor=CENTER)
    tv6.heading("col2", text="Operacion")# anchor=CENTER)
    tv6.heading("col3", text="Resultado")# anchor=CENTER)
    tv6.heading("col4", text="Llegada")# anchor=CENTER)
    tv6.heading("col5", text="Finalizacion")# anchor=CENTER)
    tv6.heading("col6", text="Retorno")# anchor=CENTER)
    tv6.heading("col7", text="Respuesta")# anchor=CENTER)
    tv6.heading("col8", text="Espera")# anchor=CENTER)
    tv6.heading("col9", text="Servicio")# anchor=CENTER)
    tv6.heading("col10", text="Restante")# anchor=CENTER)
    
    global tabla2
    #print("en tabla ", tabla2)
    for t2 in range (0, tabla2):
        if estado[t2] != "Perdido":
            tv6.insert("", END, text=Tid[t2], values=(estado[t2], (TV1[t2], TOP[t2], TV2[t2]), Tresultado[t2], 
                                                       TLlegada[t2], TFinalizacion[t2], TRetorno[t2], 
                                                     TRespuesta[t2], TEspera[t2],  TServicio[t2], Tres[t2]))
                                                      
       
    btns = tkinter.Button(user2, text="Regresar", command=lambda: salir(user2))
    btns.place(x=620, y=300)  
       
    user2.mainloop()

        
###Crear segunda pantalla################################################################################ 
def mostrar(con):
     
    global time_glo
    global tt
    global lh
    global total
    global tabla2
    global quantum
    
    user1 = tkinter.Toplevel(ventana)

    user1.title("FCFS")
    user1.geometry("1000x600+25+25")
    
    total = con
    tabla2 = con
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
    
    label = tkinter.Label(user1, text="Quantum:")
    label.place(x=50, y=300)
    
    labelq = tkinter.Label(user1, text=0)#quantum)
    labelq.place(x=160, y=300)
        
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
        global tabla
        #print("en tabla ", tabla)
        for t in range (0, tabla):
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
        global memoria
        global total
        global tabla 
        global ins
        
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

                    #tabla 
                    estado[ind2] = 'Finalizado'
                    TFinalizacion[ind2] = tg
                    Tresultado[ind2] = res  
                    TRetorno[ind2] = tg - lle2[ind2]
                    TServicio[ind2] = s
                               
                    #Aumenetar tiempos
                    ind2 = ind2 + 1 
                    lt = lt + 1
                    labelh.config(text=lt)  
                    memoria = memoria - 1
                    #print(memoria)
                    box2 = 0
                    act = 1
                    e3 = 0
                    
                    if ind < total:
                        tv1.insert("", END, text=IDs[ind], values=(tiempo[ind], tiempo[ind]))
         
                        #agregar datos
                        i = len(indi)
                        indi.append(INDIC[ind])
                        IDs2.append(IDs[ind])
                        V12.append(V1[ind])
                        V22.append(V2[ind])
                        OP2.append(OP[ind])
                        tiempo2.append(tiempo[ind])
                        timeres.append(tiempo[ind])
                        lle2.append(tg)
                        
                        #Tabla 
                        TLlegada[i] = tg
                        estado[i] = 'Listo'
                       # ins = ins + 1
                         
                        new = new - 1
                        memoria = memoria + 1
                       
                       # print(memoria)
                        labelp.config(text=new)
                        
                        lh = lh + 1
                        pl.config(text=lh)
                        
                        ind = ind + 1
                        box = box + 1
                    tabla = tabla + 1 
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
         global ind
         global memoria
         global total
         global new
         global con
         global indice
         global tabla2
         
         
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
                Tres[ind2] = 0
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
                 
                 estado[ind2] = 'Bloqueado'
                 Tres[ind2] = 8
                 bloqueos.append(ind2)
                 
                 tv4.insert("", END, text=IDs2[ind2], values=(8))
                 box3 = box3 + 1
                 ind3 = ind3 + 1
                 ind2 = ind2 + 1  
                
         if (event.char == "n"):
            
            indice = indice + 1  
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
            
            Tid.append(indice)
            TV1.append(ap)
            TV2.append(bp)
            TOP.append(sig)
            TServicio.append(tp)  
            Tres.append(0)
            Tresultado.append("-")
          
            TFinalizacion.append("-")
            TRetorno.append("-")
            TRespuesta.append("-")
            TEspera.append("-")
            
            tabla2 = tabla2 + 1
            
            if memoria >= 4:
                con = con + 1
                INDIC.append(con)
                IDs.append(indice)
                V1.append(ap)
                V2.append(bp)
                OP.append(sig)
                tiempo.append(tp)
                estado.append("Nuevo")
                TLlegada.append("-")
                total = total + 1
                new = new + 1
                labelp.config(text=new) 
            
            else:
                con = con + 1
                indi.append(con)
                IDs2.append(indice)
                V12.append(ap)
                V22.append(bp)
                OP2.append(sig)
                tiempo2.append(tp)
                timeres.append(tp)
                lle2.append(tg)
                tv1.insert("", END, text=indice, values=(tp, tp))
                box = box + 1
                memoria = memoria + 1
                lh = lh + 1
                pl.config(text=lh)
                TLlegada.append(tg)
                estado.append("Listo")       
                
         if (event.char == "t"):
             act = 0          
             tiempos_pantalla(user1)

            
    def bloqueo():
        global tt
        global ind2
        global ActBlo
        global box
        global ind3 
        global box3
        global lh
        global ultimo 
        global ctiempo
        global b2 
        global tg
        global tabla2
        global memoria
        global ins
  
        x = tv4.get_children()
        delete = 0
        for b in range (0, box3):
             timeB[b] = timeB[b] - 1
             Tres[bloqueos[b]] = timeB[b]
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
                
                ins = len(indi)
                indi.append(Bind[b])
                IDs2.append(BIDs[b])
                V12.append(BV1[b])
                V22.append(BV2[b])
                OP2.append(BOP[b])
                tiempo2.append(Btiempo[b])
                timeres.append(Btimeres[b])
                lle2.append(Blle[b])
                estado[bloqueos[b]] = 'Perdido'
                
                tabla2 = tabla2 + 1
                
                #agregar datos en tabla
                Tid.insert(ins, BIDs[b])
                TV1.insert(ins, BV1[b])
                TV2.insert(ins, BV2[b])
                TOP.insert(ins, BOP[b])
                TServicio.insert(ins, Btiempo[b])
                Tres.insert(ins, Blle[b])
                estado.insert(ins, "Listo")
                Tresultado.insert(ins, "-")
                TLlegada.insert(ins, Blle[b])
                       
                TFinalizacion.insert(ins,"-")
                TRetorno.insert(ins, "-")
                TRespuesta.insert(ins, "-")
                TEspera.insert(ins, "-")

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
            bloqueos.pop(0)
            delete = 0
         
            box = box + 1
            box3 = box3 - 1
            if ultimo == 1:
                ctiempo = 0
                ultimo = 0
                user1.after(2000, segunda_caja)  
        if ultimo == 1:
             user1.after(1000, time_ultimo) 
    
    
    def quantum_time():
        global qt
        global ind2
        global box
        global ctiempo
        global qa
        global memoria
        global lh
        global tabla2
        
        qt = qt - 1
        if qt != 0:
            labelq.config(text=qt)
        else:      
            labelq.config(text=qt)
            tv2.delete(tv2.get_children()[0])
            fal = ctiempo
            
            ins = len(indi)
           
            indi.append(indi[ind2])
            IDs2.append(IDs2[ind2])
            V12.append(V12[ind2])
            V22.append(V22[ind2])
            OP2.append(OP2[ind2])
            tiempo2.append(tiempo2[ind2])
            timeres.append(fal)
            trans = tiempo2[ind2] - fal 
          
            lle2.append(lle2[ind2])
            estado[ind2] = 'Perdido'
            
            tabla2 = tabla2 + 1
            #agregar datos en tabla      
            Tid.insert(ins, IDs2[ind2])
            TV1.insert(ins, V12[ind2])
            TV2.insert(ins, V22[ind2])
            TOP.insert(ins, OP2[ind2])
            TServicio.insert(ins, tiempo2[ind2])
            Tres.insert(ins, fal)
            estado.insert(ins, "Listo")
            Tresultado.insert(ins, "-")
            TLlegada.insert(ins, lle2[ind2])
            TFinalizacion.insert(ins,"-")
            TRetorno.insert(ins, "-")
            TRespuesta.insert(ins, "-")
            TEspera.insert(ins, "-")
        
            tv1.insert("", END, text=IDs2[ind2], values=(tiempo2[ind2], trans))
                        
            lh = lh + 1
            pl.config(text=lh)
            box = box + 1
            qa = 1
            #Blle.append(lle2[ind2])
            ind2 = ind2 + 1 

    
    
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
        global box2
        global box3
        global lh
        global tg #tiempo global transcurrido
        global ultimo
        global imp
        global qt
        global qa
        qa = 0
        if act == 1:         
            ctiempo = ctiempo - 1
            tt = tt + 1  
        
            if box3 > 0:
                    bloqueo()     
            if ctiempo > -1:
                    #ocurrido 
                    Tres[ind2] = ctiempo
                    labeltgc.config(text=tt)
                    #restante
                    labeltr.config(text=ctiempo)
                    tg = tg + 1
                    labeltg.config(text=tg)
                    
                    quantum_time()
                    if qa == 0: 
                       user1.after(2000, time) 
                    else:
                       box2 = 0
                       user1.after(2000, segunda_caja)   
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
        global quantum
        global qt 
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
                                TRespuesta[ind2] = res2[rind]
                            rind =  int(r) 
                    if re == 1:  
                       res2.append(tg)
                       TRespuesta[ind2] = tg
                    esp2.append(tg)
                    TEspera[ind2] = tg
                    box2 = 1  #Activar los metodos de la caja 1 y 2
                    estado[ind2] = 'Ejecucion'
                    ctiempo = 0
                    tt = 0
                    ctiempo = timeres[ind2] 
                    qt = quantum
                    labelq.config(text=qt)
                    labeltr.config(text=ctiempo)
                    user1.after(1000, time) 
 
            
    def primera_caja(jc):
        global lista
        global ind
        global box
        global lh
        global tg
        global new
        global memoria
        global ins
        if jc < lista:
                #tv1.insert("", END, text=IDs[ind], values=(tiempo[ind], tiempo[ind]))
                tv1.insert("", END, text=IDs[ind], values=(tiempo[ind], 0))
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
                TLlegada[ind] = tg
                #modificar datos
                new = new - 1
                memoria = memoria + 1
                estado[jc] = 'Listo'
                ins = ins + 1
                labelp.config(text=new)
                ind = ind + 1
                jc = jc + 1 
                lh = lh + 1
                pl.config(text=lh)
                user1.after(1000, primera_caja, jc)
        else:
                box = jc
                user1.after(2000, segunda_caja)


    global new
    loteres = l//4
    resto   = l-(loteres*4) 
    new = l
    labelp = tkinter.Label(user1, text=new)
    labelp.place(x=200, y=10)
    

    Boton3 = tkinter.Button(user1, text="Iniciar", command=lambda: iniciar(loteres, resto))
    Boton3.place(x = 300, y = 20)  
       
    def iniciar(l, r):
        global lista
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
Boton1.place(x = 500, y = 60)     
                            

ventana.mainloop()