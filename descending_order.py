def descending_order(num):
    if num < 0:
        return -1
    else: 
        digit_string = str(num)
        digit_map = map(int, digit_string)
        final_list = list(digit_map)
        print(final_list)

        final_list.sort(reverse = True)
        strings = [str(integer) for integer in final_list]
        final_number = "".join(strings)
        final_number = int(final_number)
        return final_number


def descending_order_truee(num):
    return int("".join(sorted(str(num), reverse = True)))

def run():
    number = int(input("Dame un numero: "))
    final = descending_order_truee(number)
    print(str(final))

if __name__ == "__main__":
    run()


