import time
import os

def factorial(number):
    fact = 1
    if number < 0:
        return 0
    if number == 0:
        return 1
    while(number > 1):
        fact *= number
        number -= 1
    
    return fact


def is_it_prime(numero):
    wilson  = factorial(numero - 1)
    wilson += 1
    
    if numero == 0:
        return False
    if wilson % numero == 0:
        return True
    else:
        return False


def clear_screen():
    if os.name == "posix":
        os.system("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        os.system("cls")


def run():
    
    exit = False

    while not exit:
        menu = """ 
 
                    Numeros Primos

*** Si deseas salir, escribe -1.


Escribe el numero y descubre si es un numero primo: """
        
        numero = int(input(menu))
        
        if numero == -1:
            exit = True
        elif is_it_prime(numero):
            print(" ")
            print("El numero " + str(numero) + " es un número primo.")
            time.sleep(3)
            clear_screen()
        else:
            print("El numero " + str(numero) + " NO es un número primo.")
            time.sleep(3)
            clear_screen()

    print("Done")


if __name__ == "__main__":
    run()





