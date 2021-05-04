

def solution(number):
    if number < 0:
        return 0
    else: 
        list = []
        sum = 0
        for i in range(number):
            list.append(i)
        for i in range(number):
            if list[i]%3 == 0 or list[i]%5 == 0:
                sum = sum + i
        return sum


def run():
    number = int(input("Dame un numero: "))
    suma = solution(number)
    print("La suma de los multiplos de 3 y 5 es: " + str(suma))


if __name__ == "__main__":
    run()






