import random
import time
import os


#Funcion para limpiar la pantalla de la terminal 
def clear_screen():
    if os.name == "posix": 
        os.system("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        os.system("cls")


#Funcion que checa si el número esta en el rango de 1 a 100
def checar_numero(numero_elegido):
    while numero_elegido < 0 or numero_elegido > 100:
        print(" ")
        print("    El numero es demasiado grande o pequeño")
        print(" ")
        numero_elegido = int(input("Elige un número del 1 al 100: "))

    return numero_elegido


def run():
    numero_aleatorio = random.randint(1, 100)
    numero_anterior = 0
    mostrar_ganaste = True
    ingresar_texto = "Elige un numero: "
    mensaje_inicial = """

           Juego de adivinar el numero

    0 - Salir del juego 
    Intenta adivinar un número entre el 1 al 100
    en la menor cantidad de intentos posible.
                                                """
 
    print(mensaje_inicial)
    numero_elegido = int(input(ingresar_texto))
    numero_elegido = checar_numero(numero_elegido) #Se checa siempre si esta entre 1 a 100
    numero_anterior = numero_elegido #Se guarda el valor anterior
    contador_intentos = 1 #Se cuentan los intentos 

    exit = False #Se crea el menu con un while not
    while not exit:
        while numero_elegido != numero_aleatorio: 
            if numero_elegido == 0: #condicion para salir del menu
                mostrar_ganaste = False 
                break
            elif numero_elegido < numero_aleatorio:
                clear_screen()
                print(mensaje_inicial)
                print("El número anterior era: " + str(numero_anterior) + ".")
                print(" ")
                print("Elige un número más GRANDE")
                print(" ")
            else:
                clear_screen()
                print(mensaje_inicial)
                print("El número anterior era: " + str(numero_anterior) + ".")
                print(" ")
                print("Elige un número más PEQUEñO")
                print(" ")

            numero_elegido = int(input("Elige otro número: "))
            numero_elegido = checar_numero(numero_elegido)
            contador_intentos += 1
            numero_anterior = numero_elegido

        if mostrar_ganaste: 
            print(" ")
            print("         ¡Ganaste!")
            print("El total de intentos fue: " + str(contador_intentos) + ".")
            print(" ") 
            time.sleep(3)

        exit = True

    print("Done") 


if __name__ == "__main__":
    run()
