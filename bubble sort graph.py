import time
import random
from colorama import  Fore, Back, Style
import os

lista_esta_ordenada = False
posicion = 0
tamaño_lista = 6        #Tamaño de lista, lista pequeña para demostracion del metodo
lista = random.sample(range(1, 7), tamaño_lista)    # Lista de números únicos
lista_inicial = list(lista)     #guardamos la lista inicial
lista_ordenada = list(lista)    #vamos a utilizar esta lista para ordernarla
lista_ordenada_chequeo = sorted(lista)      #lista ordenada por python para chequear que hayamos ordenado correctamente

#lista =[2, 3, 4, 5, 6, 7]

print(f"lista de numeros: {lista}")
for numero in lista_ordenada:
    print("\n")
    print(f"{numero} ", end ="")
    for numero in range(numero):
        print("◻ ", end ="")

input("\n\nPress Enter para comenzar a ordernar la lista...")
os.system('cls')

def funcion_lista_esta_ordenada(lista_ordenada):
    global posicion, tamaño_lista, lista_esta_ordenada, lista_ordenada_chequeo
    
    if lista_ordenada == lista_ordenada_chequeo:
        lista_esta_ordenada = True
    if lista_esta_ordenada == True:
        print(lista_ordenada)
        print("LISTA ORDENADA")
    else:
        funcion_ordenamiento(lista_ordenada)

def funcion_ordenamiento(lista_ordenada):
    global posicion, lista_inicial
    print("\n\nordenando lista")

    if posicion == len(lista_ordenada)-1:        #si la posicion es igual al largo de la lista menos 1, se vuelve a 0 para reiniciar el ordenamiento
        posicion = 0

    if lista_ordenada[posicion] > lista_ordenada[posicion+1]:         #se chequea si la posicion es mayor a la posicion +1
        numero_triangulado = lista_ordenada[posicion]        #si es asi, se intercambian los valores de lugar, se utiliza una tercer variable para triangular
        lista_ordenada[posicion] = lista_ordenada[posicion+1]
        lista_ordenada[posicion+1] = numero_triangulado

    print(f"Lista inicial: {lista_inicial}")
    print(f"\nLista ordenada al momento: ")
    print(f"{lista_ordenada}")

    for numero in lista_ordenada:
        if numero == posicion:
            print(Fore.RED + f"{numero} ", end ="" + Style.RESET_ALL)
        else:
            print("\n")
            print(f"{numero} ", end ="")
        for numero in range(numero):
            print("◻ ", end ="")
    posicion += 1           #se sube la posicion en un valor 


    input("\n\nPress Enter to continue...")
    os.system('cls')
    
    funcion_lista_esta_ordenada(lista_ordenada)
    #for numero in lista[0:2]:
    #    print("\n")
    #    for i in range(numero):
    #        print("◻ ", end ="")

lista_ordenada = funcion_ordenamiento(lista_ordenada)

