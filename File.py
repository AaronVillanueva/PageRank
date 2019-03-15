print("Bienvenido al programa de PageRank v.0001")

estado = "activo"

def inicio(str):
    lista,numNodos=crear(str)
    listaF=procesar(lista,numNodos)
    calcular(listaF)

def calcular(lista):
    listaA=list(lista[:]).copy()
    #for i in range(1,len(lista)):
    for i in range(1, 3):
        print("   ")
        suma = 0
        actual=listaA[i][2]
        for j in actual:
            print(j)
            div = len(listaA[j][1])
            if (div == 0):
                div = 1
            print(listaA[j][0])
            suma+=listaA[j][0]/div
            print(suma)
        #lista[i][0]=suma
    print(" ")
    print(lista[1])
    print(lista)

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
    inicio(str)

def subir():

    inicio(list)

while estado=="activo":
    print("1 para subir")
    print("2 para escribir")
    #eleccion=int(input())
    eleccion=2
    if eleccion==1:
        print("a")
    if eleccion==2:
        #escritura()
        inicio("(1,2) (1,3) (3,1) (3,2) (3,5) (5,4) (5,6) (6,4) (4,5) (4,6)")
        break
    else:
        print("Finalizando programa")
        estado="salir"
  
