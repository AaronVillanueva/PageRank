
import tkinter as tk
from tkinter import filedialog

print("Bienvenido al programa de PageRank v.0001")
estado = "activo"
def inicio(str,num):
    lista,numNodos=crear(str)
    listaF=procesar(lista,numNodos)
    listaLista = calcular(listaF)
    for i in range(1,int(num)):
        listaLista=calcular(listaLista)
    formatoFinal(listaLista)
    print(" ")
    input("Calculo terminado. Introduzca cualquier cosa para continuar")
    print(" ")

def formatoFinal(lista):
    for i in range(1,len(lista)):
        print(str(i)+"   "+str(lista[i][0]))

def calcular(lista):
    #Deepcopy muy importante!
    listaA=[x[:] for x in lista]
    for i in range(1,len(lista)):
    #for i in range(1, 3):
        suma = 0
        actual=listaA[i][2]
        for j in actual:
            div = len(listaA[j][1])
            if (div == 0):
                div = 1
            suma+=listaA[j][0]/div
        lista[i][0]=suma
    return(lista)

def procesar(lista,numNodos):
    #ListaF  [ r Actual, outlink, inlink   ]
    #ListaF index = nodo
    listaF=[[0,0,0]]

    for i in range(numNodos):
        listaF.append([ 1/numNodos,[],[] ])
    for i in lista:
        fuente=i[0]
        destino=i[1]
        listaF[fuente][1].append(destino)
        listaF[destino][2].append(fuente)
    return listaF

def crear(str):
    lista = str.split()
    numeroNodos=0
    for i in range(len(lista)):
        lista[i] = lista[i].replace("(", "")
        lista[i] = lista[i].replace(")", "")
        lista[i] = lista[i].split(",")
        lista[i][0] = int(lista[i][0])
        lista[i][1] = int(lista[i][1])
        if(numeroNodos<max(lista[i])):
            numeroNodos=max(lista[i])
    return lista,numeroNodos

def escritura():
    print("Introduzca el grafo")
    str = input()
    print("Introduzca el numero de repeticiones")
    num=input()
    inicio(str,num)
    #inicio("(1,2) (1,3) (3,1) (3,2) (3,5) (5,4) (5,6) (6,4) (4,5) (4,6)")

def subir():
    ventana=tk.Tk()

    path=filedialog.askopenfilename()
    ventana.withdraw()
    archivo=open(path,"r")
    string=str(archivo.read())
    num=input("Introduzca el numero de repeticiones")
    inicio(string,int(num))

while estado=="activo":
    print("1 para subir")
    print("2 para escribir")
    eleccion=int(input())
    if eleccion==1:
        subir()
    if eleccion==2:
        escritura()
    else:
        print("Finalizando programa")
        estado="salir"
