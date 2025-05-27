import time
import random
import colorama
lista_ordenada=[]
lista_esta_ordenada = False
posicion = 0

tamaño_lista = 6        #Tamaño de lista, lista pequeña para demostracion del metodo
lista = random.sample(range(1, 7), tamaño_lista)    # Lista de números únicos
primer_numero = lista[0]
lista_ordenada_chequeo = sorted(lista)

#lista =[2, 3, 4, 5, 6, 7]

print(f"lista de numeros: {lista}")
for numero in lista:
    print("\n")
    for i in range(numero):
        print("◻ ", end ="")

def funcion_lista_esta_ordenada(lista):
    global posicion, tamaño_lista, lista_esta_ordenada, primer_numero, lista_ordenada_chequeo
    
    if lista == lista_ordenada_chequeo:
        lista_esta_ordenada = True
    if lista_esta_ordenada == True:
        print(lista)
        print("LISTA ORDENADA")
    else:
        funcion_ordenamiento(lista)

def funcion_ordenamiento(lista):
    global posicion     #variable que inicia en 0
    print("\n\nordenando lista\n")

    if posicion == len(lista)-1:        #si la posicion es igual al largo de la lista menos 1, se vuelve a 0 para reiniciar el ordenamiento
        posicion = 0

    if lista[posicion] > lista[posicion+1]:         #se chequea si la posicion es mayor a la posicion +1
        numero_triangulado = lista[posicion]        #si es asi, se intercambian los valores de lugar, se utiliza una tercer variable para triangular
        lista[posicion] = lista[posicion+1]
        lista[posicion+1] = numero_triangulado
    posicion += 1           #se sube la posicion en un valor 

    print(lista)
    input("Press Enter to continue...")
    
    funcion_lista_esta_ordenada(lista)
    #for numero in lista[0:2]:
    #    print("\n")
    #    for i in range(numero):
    #        print("◻ ", end ="")

lista_ordenada = funcion_ordenamiento(lista)

