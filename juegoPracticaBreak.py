import random
import os
import time

def clear_screen():
    if os.name == "posix":
        os.system("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        os.system("cls")


def set_public_bounds(bound1, bound2, lor):
    if lor == False:
        if bound1 <= bound2:
            return bound1
        else: 
            return bound2
    else:
        if bound1 >= bound2: 
            return bound1
        else:
            return bound2


def levels(opcion):
    if opcion == 1:
        bound1 = random.randint(random.randint(0,1), random.randint(2,3))
        bound2 = random.randint(random.randint(4,5), random.randint(6,7))
        win_number = random.randint(bound1, bound2) 
	
        print("Advina el numero entre esté rango: " + str(bound1) + " " + str(bound2) + ".")
        attempt = int(input(": "))
	
        if attempt == win_number:
            print("You win OwO")
        else: 
            print("You lose :c, the win number was: " + str(win_number) + ".")

    if opcion == 2:
        bound11 = random.randint(random.randint(0,1), random.randint(6,10))
        bound21 = random.randint(random.randint(10,15), random.randint(15,30))
        win_number1 = random.randint(bound11, bound21) 
	
        bound12 = random.randint(random.randint(0,1), random.randint(6,10))
        bound22 = random.randint(random.randint(10,15), random.randint(15,30))
        win_number2 = random.randint(bound12, bound22) 
	
        if win_number1 == win_number2:
            win_number2 += 1
        
        boundleft = set_public_bounds(bound11, bound12, False)
        boundright = set_public_bounds(bound21, bound22, True)        

        print("Advina el numero entre esté rango: " + str(boundleft) + " " + str(boundright) + ".")
        attempt = (input(": "))
	
        if attempt == win_number1 or attempt == win_number2:
            print("You win OwO")
        else: 
            print("You lose :c, the win numbers were: " + str(win_number1) + " and " + str(win_number2) + ".")

    if opcion == 3:
        bound11 = random.randint(random.randint(0,1), random.randint(6,50))
        bound21 = random.randint(random.randint(50,51), random.randint(55,100))
        win_number1 = random.randint(bound11, bound21) 
	
        bound12 = random.randint(random.randint(0,1), random.randint(6,50))
        bound22 = random.randint(random.randint(50,51), random.randint(55,100))
        win_number2 = random.randint(bound12, bound22) 
	
        bound13 = random.randint(random.randint(0,1), random.randint(6,50))
        bound23 = random.randint(random.randint(50,51), random.randint(55,100))
        win_number3 = random.randint(bound13, bound23) 
      
        boundleft_1 = set_public_bounds(bound11, bound12, False)
        boundleft_F = set_public_bounds(boundleft_1, bound13, False)

        boundright_1 = set_public_bounds(bound21, bound22, True)        
        boundright_F = set_public_bounds(boundright_1, bound23, True)        

        print("Advina el numero entre esté rango: " + str(boundleft_F) + " " + str(boundright_F) + ".")
        attempt = (input(": "))
	
        if attempt == win_number1 or attempt == win_number2:
            print("You win OwO")
        else: 
            print("You lose :c, the win numbers were: " + str(win_number1) + ", " + str(win_number2) + " and " + str(win_number3) + ".")


def run():
    salir = False

    while not salir:
        menu = """
    
    		Game
    
    Intena atinarle al número.
       1 - Nivel fácil (1 entre 10 chances)
       2 - Nivel medio (2 entre 30 chances)
       3 - Nivel díficil (3 entre 100 chances)
       4 - Salir
    
    Selecione una opcion: """
    
        opcion = int(input(menu))
         
        if opcion > 4 or opcion < 1:
            print("Escribe un numero correcto")
            break
    
        if opcion == 4: 
            salir = True
        else: 
            levels(opcion)
            time.sleep(3)
            clear_screen()

    print("Done")


     

if __name__ == "__main__":
    run()



