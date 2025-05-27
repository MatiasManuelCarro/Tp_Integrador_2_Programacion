import time
import random
from colorama import init, Fore, Back, Style
import os

lista_esta_ordenada = False
posicion = 0
tamaño_lista = 6        #Tamaño de lista, lista pequeña para demostracion del metodo
lista = random.sample(range(1, 7), tamaño_lista)    # Lista de números únicos
lista_inicial = list(lista)     #guardamos la lista inicial
lista_ordenada = list(lista)    #vamos a utilizar esta lista para ordernarla
lista_ordenada_chequeo = sorted(lista)      #lista ordenada por python para chequear que hayamos ordenado correctamente
pasos = 0

print(Fore.GREEN + "Programa que muestra como se ordena con Bubble Sorting una lista al azar de 6 numeros, paso a paso")
print(Fore.GREEN + f"lista inicial: {lista}" + Style.RESET_ALL)
for numero in lista_ordenada:
    print("\n")
    print(Fore.GREEN + f"{numero} ", end ="" + Style.RESET_ALL)
    for numero in range(numero):
        print("◻ ", end ="")

input(Fore.YELLOW + "\n\nPresione Enter para comenzar a ordernar la lista..." + Style.RESET_ALL)
os.system('cls')

def funcion_lista_esta_ordenada(lista_ordenada):
    global posicion, tamaño_lista, lista_esta_ordenada, lista_ordenada_chequeo
    
    if lista_ordenada == lista_ordenada_chequeo:
        lista_esta_ordenada = True
    if lista_esta_ordenada == True:
        print(Fore.GREEN + f"Lista inicial: {lista_inicial}" + Style.RESET_ALL) 

        print(Fore.YELLOW + "\nLISTA ORDENADA" + Style.RESET_ALL)
        print(Fore.YELLOW + f"{lista_ordenada}" + Style.RESET_ALL)
        for numero in lista_ordenada:
            print("\n")
            print(Fore.RED + f"{numero} "+ Style.RESET_ALL , end ="")
            for numero in range(numero):
                print(Fore.RED + "◻ " + Style.RESET_ALL, end = "")
        print(Fore.YELLOW + f"\n\nCantidad de iteraciones realizadas: {pasos}" + Style.RESET_ALL)
        input(Fore.YELLOW + "\n\nPresione Enter para salir del programa..." + Style.RESET_ALL)
    

    else:
        funcion_ordenamiento(lista_ordenada)

def funcion_ordenamiento(lista_ordenada):
    global posicion, lista_inicial, pasos

    print(Fore.GREEN + f"Lista inicial: {lista_inicial}" + Style.RESET_ALL) 

    print(Fore.YELLOW + f"\nOrdenando lista: " + Style.RESET_ALL, end = "")

    if posicion == len(lista_ordenada)-1:        #si la posicion es igual al largo de la lista menos 1, se vuelve a 0 para reiniciar el ordenamiento
        posicion = 0

    numeros_colorama = [lista_ordenada[posicion], lista_ordenada[posicion+1]]       #coloreando numero a numero de la lista
    for numero in lista_ordenada:
        if numero in numeros_colorama:
            print(Back.WHITE + Fore.RED + f" {str(numero)} " + Style.RESET_ALL, end = "")
        else:
            print(Back.WHITE + Fore.BLACK + f" {str(numero)} "+ Style.RESET_ALL, end = "")

    print(f"\nNumeros comparados en esta iteracion: " + Fore.RED + f"{lista_ordenada[posicion]} y {lista_ordenada[posicion+1]}" + Style.RESET_ALL)
    if lista_ordenada[posicion] > lista_ordenada[posicion+1]:         #se chequea si la posicion es mayor a la posicion +1
        numero_triangulado = lista_ordenada[posicion]        #si es asi, se intercambian los valores de lugar, se utiliza una tercer variable para triangular
        lista_ordenada[posicion] = lista_ordenada[posicion+1]
        lista_ordenada[posicion+1] = numero_triangulado
        print(f"Se ordenan los numeros {lista_ordenada[posicion+1]} y {lista_ordenada[posicion]} porque " + Fore.RED + f"{lista_ordenada[posicion]} es menor a {lista_ordenada[posicion+1]}" + Style.RESET_ALL)
    else:
        print(f"Estos dos numeros se encuentran ordenados correctamente")
    
    print(Fore.YELLOW + f"\nLista ordenada al momento: " + Style.RESET_ALL)
    print(f"{lista_ordenada}")


    for numero in lista_ordenada:
        if lista_ordenada[posicion] == numero:
            print("\n")
            print(Fore.RED + f"{numero} ", end ="")
        elif lista_ordenada[posicion+1] == numero:
            print("\n")
            print(Fore.RED + f"{numero} ", end ="")
        else:
            print("\n")
            print(Style.RESET_ALL + f"{numero} ", end ="")
        for numero in range(numero):
            print("◻ ", end ="")
    
    posicion += 1           #se sube la posicion en un valor 
    pasos += 1      #cantidad de pasos realizados


    input(Fore.YELLOW +"\n\nPresione ENTER para continuar..." + Style.RESET_ALL)
    os.system('cls')
    
    funcion_lista_esta_ordenada(lista_ordenada)
    #for numero in lista[0:2]:
    #    print("\n")
    #    for i in range(numero):
    #        print("◻ ", end ="")

lista_ordenada = funcion_ordenamiento(lista_ordenada)

