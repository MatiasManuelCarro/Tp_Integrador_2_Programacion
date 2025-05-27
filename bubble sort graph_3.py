import random
import os
from colorama import init, Fore, Back, Style
init()


posicion = 0
tamaño_lista = int(input("Ingrese un numero entero para la cantidad de numeros en la lista aleatoria"))       #Tamaño de lista, lista pequeña para demostracion del metodo
lista = random.sample(range(1, tamaño_lista+1), tamaño_lista)    # Lista de números únicos
lista_inicial = list(lista)     #guardamos la lista inicial
lista_ordenada = list(lista)    #vamos a utilizar esta lista para ordernarla
lista_ordenada_chequeo = sorted(lista)      #lista ordenada por python para chequear que hayamos ordenado correctamente
pasos = 0


#inicio del programa titulo
print(Fore.GREEN + "Programa que muestra como se ordena con Bubble Sorting una lista al azar de 6 numeros, paso a paso")
print(Fore.GREEN + f"lista inicial: {lista}" + Style.RESET_ALL)

#ciclo for que imprime el grafico de la lista
for numero in lista_ordenada:
    print("\n")
    print(Fore.GREEN + f"{numero} ", end ="" + Style.RESET_ALL)
    for numero in range(numero):
        print("▢ ", end ="")

#pausa en el programa, espera a que el usuario presione enter para continuar
input(Fore.YELLOW + "\n\nPresione Enter para comenzar a ordernar la lista..." + Style.RESET_ALL)
#limpia la pantalla para que el programa sea mas facil de entender
os.system('cls')

#funcion que verifica si la lista esta ordenada
def funcion_lista_esta_ordenada(lista_ordenada):
    global posicion, tamaño_lista, lista_ordenada_chequeo
    
    if lista_ordenada == lista_ordenada_chequeo:        #se chequea que la lista este ordenada
    #if all(min(lista_ordenada) <= lista_ordenada[])
        print(Fore.GREEN + f"Lista inicial: {lista_inicial}" + Style.RESET_ALL) 

        print(Fore.YELLOW + "\nLISTA ORDENADA" + Style.RESET_ALL)
        print(Fore.YELLOW + f"{lista_ordenada}" + Style.RESET_ALL)
        #ciclo for que imprime el grafico de la lista ordenada al final
        for numero in lista_ordenada:
            print("\n")
            print(Fore.RED + f"{numero} "+ Style.RESET_ALL , end ="")
            for numero in range(numero):
                print(Fore.RED + "▢ " + Style.RESET_ALL, end = "")
        #mostramos la cantidad de iteraciones que llevo el programa para finalizar el ordenamiento
        print(Fore.YELLOW + f"\n\nCantidad de iteraciones realizadas: {pasos}" + Style.RESET_ALL)
        input(Fore.YELLOW + "\n\nPresione Enter para salir del programa..." + Style.RESET_ALL)
    
    else:       #si no esta ordenada se vuelve a llamar a la funcion que ordena
        funcion_ordenamiento(lista_ordenada)

#funcion que ordena la lista
def funcion_ordenamiento(lista_ordenada):
    #variable globales que maneja la funcion
    global posicion, lista_inicial, pasos

    #titulo con lista inicial
    print(Fore.GREEN + f"Lista inicial: {lista_inicial}" + Style.RESET_ALL) 

    print(Fore.YELLOW + f"\nOrdenando lista: " + Style.RESET_ALL, end = "")

    #si la posicion es igual al largo de la lista menos 1, se vuelve a 0 para reiniciar el ordenamiento
    #esto se realiza para volver a iniciar el ordenamiento desde el principio
    if posicion == len(lista_ordenada)-1:        
        posicion = 0

    numeros_colorama = [lista_ordenada[posicion], lista_ordenada[posicion+1]]       #coloreando numero a numero de la lista
    #imprime la lista como se encuentra ordenada en el momento, resaltando en rojo los dos numeros que estamos comparando
    for numero in lista_ordenada:
        if numero in numeros_colorama:
            print(Back.WHITE + Fore.RED + f" {str(numero)} " + Style.RESET_ALL, end = "")
        else:
            print(Back.WHITE + Fore.BLACK + f" {str(numero)} "+ Style.RESET_ALL, end = "")

    #Imprime los dos numeros que se comparan al momento 
    print(f"\nNumeros comparados en esta iteracion: " + Fore.RED + f"{lista_ordenada[posicion]} y {lista_ordenada[posicion+1]}" + Style.RESET_ALL)
    #desicion que verifica si el primer numero que esta siendo comparado es mayor al segundo numero, si lo es se rotan
    if lista_ordenada[posicion] > lista_ordenada[posicion+1]:         #se chequea si la posicion es mayor a la posicion +1
        numero_triangulado = lista_ordenada[posicion]                 #si es asi, se intercambian los valores de lugar, se utiliza una tercer variable para triangular
        lista_ordenada[posicion] = lista_ordenada[posicion+1]
        lista_ordenada[posicion+1] = numero_triangulado
        #se muestra al usuario el paso que se realizo
        print(f"Se ordenan los numeros {lista_ordenada[posicion+1]} y {lista_ordenada[posicion]} porque " + Fore.RED + f"{lista_ordenada[posicion]} es menor a {lista_ordenada[posicion+1]}" + Style.RESET_ALL)
    else:
        print(f"Estos dos numeros se encuentran ordenados correctamente")
    
    #se imprime como la lista va siendo ordenada al momento
    print(Fore.YELLOW + f"\nLista ordenada al momento: " + Style.RESET_ALL)
    print(f"{lista_ordenada}")

    #ciclo for que imprime el grafico con los numeros que estan siendo ordenados resaltados en rojo
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
            print("▢ ", end ="")
    
    posicion += 1           #se sube la posicion en un valor 
    pasos += 1      #cantidad de pasos realizados

    #se espera que el usuario presione enter para continuar
    input(Fore.YELLOW +"\n\nPresione ENTER para continuar..." + Style.RESET_ALL)
    #limpia la pantalla para que el programa sea mas facil de entender
    os.system('cls')
    
    #se llama a la funcion lista ordenada, que verifica si se logro ordenar en este paso, si no, se vuelve a realizar el ordenamiento
    funcion_lista_esta_ordenada(lista_ordenada)

#inicio del programa, se llama a la funcion que verifica si la lista esta ordenada
funcion_ordenamiento(lista_ordenada)

