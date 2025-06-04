import random
import os
from colorama import Fore, Back, Style

#declaracion de variables 
posicion = 0    #Variable para las posiciones de la lista, se usa como contador 

#funcion for que imprime el grafico de la lista inicial
def imprimir_lista_inicial(lista):
    print(Fore.GREEN + f"lista inicial: {lista}" + Style.RESET_ALL)     #muestra la lista incial en verde con colorama
    for numero in lista_ordenada:
        print(Fore.GREEN + f"\n\n{numero} ", end ="" + Style.RESET_ALL)     #imprime los numeros de la lista
        for numero in range(numero):
            print("▢ ", end ="")    #imprime un cuadrado al lado de cada numero de la lista

#funcion que imprime los pasos mientras ordenamos
#marca en rojo los numeros que se estan comparando
def imprimir_lista_pasos_intermedios(lista_ordenada):
    global posicion
    for numero in lista_ordenada:
        if lista_ordenada[posicion] == numero:      #Si el numero a imprimir uno de los dos que estamos comparando, se imprime en rojo
            print("\n")
            print(Fore.RED + f"{numero} ", end ="")
        elif lista_ordenada[posicion+1] == numero:      #el siguiente numero que estamos comparando es posicion+1 tambien se marca en rojo
            print("\n")
            print(Fore.RED + f"{numero} ", end ="")
        else:           #si no es uno de los dos numeros, se imprime sin estilo
            print("\n")
            print(Style.RESET_ALL + f"{numero} ", end ="")
        for numero in range(numero):
            print("▢ ", end ="")


#funcion que verifica si la lista esta ordenada
def funcion_lista_esta_ordenada(lista_ordenada):
    global posicion, tamaño_lista, lista_ordenada_chequeo
    
    if lista_ordenada == lista_ordenada_chequeo:        #se chequea que la lista este ordenada

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
    #esto reinicia el ordenamiento para recorrer la lista nuevamente
    if posicion == len(lista_ordenada)-1:        
        posicion = 0

    numeros_colorama = [lista_ordenada[posicion], lista_ordenada[posicion+1]]       #guarda las dos posiciones para colorear con colorama
    #imprime la lista como se encuentra ordenada en el momento, resaltando en rojo los dos numeros que estamos comparando
    for numero in lista_ordenada:
        if numero in numeros_colorama:      #verifica que se impriman en rojo los numeros que estamos comparando
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

    #se llama a la funcion que imprime la lista mientras la estamos ordenando
    imprimir_lista_pasos_intermedios(lista_ordenada)

    posicion += 1           #se sube la posicion en un valor 
    pasos += 1      #cantidad de pasos realizados

    #se espera que el usuario presione enter para continuar
    input(Fore.YELLOW +"\n\nPresione ENTER para continuar..." + Style.RESET_ALL)
    #limpia la pantalla para que el programa sea mas facil de entender
    os.system('cls')
    
    #se llama a la funcion lista ordenada, que verifica si se logro ordenar en este paso, si no, se vuelve a realizar el ordenamiento
    funcion_lista_esta_ordenada(lista_ordenada)

def validacion_datos(numero_ingresado): #Valida que el numero ingresado sea correcto
    while True: #Se repite el loop hasta que la funcion retorne el numero
        try: #intenta pasar el ingreso a un integer
            numero = int(numero_ingresado) #si es integer, se guarda en la variable numero
            if numero > 0 and numero <= 20: #verifica que el entero sea positivo y menoro igual a 20 si no lo es, vuelve a pedir ingreso de datos
                return numero #si es entero, positivo, y menor a 999, devuelve el numero
            else:
                print("\nDatos ingresados incorrectos")
                numero_ingresado = input("Ingrese otro numero, recuerde que tiene que ser un entero positivo entre 2 y 20:\n") #volvemos a pedir ingreso
        except ValueError: #en caso de error, el ingreso no era correcto. Tenia otros caracteres o era decimal
            print("\nDatos ingresados incorrectos")
            numero_ingresado = input("Ingrese otro numero, recuerde que tiene que ser un entero positivo entre 2 y 20:\n") #volvemos a pedir ingreso


#inicio del programa titulo
print(Fore.GREEN + "\nPrograma que muestra como se ordena con Bubble Sorting una lista al azar de 6 numeros, paso a paso" + Style.RESET_ALL)
print("\nPara poder demostrar el ejemplo, ingrese un numero para elegir el total de elementos de la lista aleatoria") 
print("Por favor un numero entre 2 y 20 ya que mas de 20 el programa seria demasiado largo para su demostracion practica")
#Se solicita ingreso al usuario
numero_ingresado = input("Ingrese un numero:\n")       

#verificacion de ingreso de datos
tamaño_lista = validacion_datos(numero_ingresado)

#Se crea la lista random
lista = random.sample(range(1, tamaño_lista+1), tamaño_lista)    
lista_inicial = list(lista)     #guardamos la lista inicial
lista_ordenada = list(lista)    #vamos a utilizar esta lista para ordernarla
lista_ordenada_chequeo = sorted(lista)      #lista ordenada por python para chequear que hayamos ordenado correctamente
pasos = 0

#se llama a la funcion que imprime la lista inicial
imprimir_lista_inicial(lista)

#pausa en el programa, espera a que el usuario presione enter para continuar
input(Fore.YELLOW + "\n\nPresione Enter para comenzar a ordernar la lista..." + Style.RESET_ALL)
#limpia la pantalla para que el programa sea mas facil de entender
os.system('cls')

#inicio del ordenamiento, se llama a la funcion que verifica si la lista esta ordenada
funcion_ordenamiento(lista_ordenada)