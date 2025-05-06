def decimal_to_bin():
    number = int(input("Enter the number:\n"))
    print(bin(number))

def bin_to_decimal():
    binary = input("Enter a binary number (e.g. 1010): ")

    if not all(digit in '01' for digit in binary):
        print("Invalid binary number! Only 0s and 1s are allowed.")
        return

    decimal = int(binary, 2)
    print(f"The decimal value of {binary} is {decimal}")


def decimal_to_Hexadecimal():
    number = int(input("Enter the number: \n"))
    print(hex(number))


def Hexadecimal_to_decimal():
    hex_number = input("Enter a hexadecimal number (e.g. 1A3): ")

    try:
        decimal = int(hex_number, 16)
        print(f"The decimal value of {hex_number} is {decimal}")
    except ValueError:
        print("Invalid hexadecimal number!")

def decimal_to_octal():
    number = int(input("Enter the number: \n"))
    print(oct(number))

def octal_to_decimal():
    octal = input("Enter an octal number (e.g. 17): ")

    try:
        decimal = int(octal, 8)
        print(f"The decimal value of {octal} is {decimal}")
    except ValueError:
        print("Invalid octal number!")


def main():
    while True:
        try:
            function = int(input("Enter the function: \n "))
        except ValueError:
            print("Invalid input!")
            continue

        if function == 1:
            decimal_to_bin()
        elif function == 2:
            bin_to_decimal()
        elif function == 3:
            decimal_to_Hexadecimal()
        elif function == 4:
            Hexadecimal_to_decimal()
        elif function == 5:
            decimal_to_octal()
        elif function == 6:
            octal_to_decimal()
        else:
            print("\nInvalid function!\n")

        replay = input("Do you wanna convert another number? (y/n):\n")

        if replay == 'y':
            continue
        elif replay == 'n':
            break
        else:
            print("\nYou got nothing here, goodbye!\n")

main()