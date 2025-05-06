def Lengths():
    units = {
        'mm': 1,
        'cm': 10,
        'dm': 100,
        'm': 1000,
        'km': 1000000,
    }

    print("\nHere are the units: mm, cm, dm, m, km")

    original_unit = input("\nEnter the original unit: ").lower()
    target_unit = input("Enter the target unit: ").lower()

    if original_unit not in units or target_unit not in units:
        print("\nInvalid unit entered!\n")
        return

    try:
        number = float(input("Enter the number to convert: "))
    except ValueError:
        print("\nInvalid number input!\n")
        return

    original_value = units[original_unit]
    target_value = units[target_unit]

    result = number * (original_value / target_value)
    print(f"\n{number} {original_unit} is equal to {result} {target_unit}\n")


def weight():
    weights = {
        'mg': 0.001,
        'g': 1,
        'kg': 1000,
        'ton': 1000000,
        'lb': 453.592,
        'oz': 28.3495,
    }

    print("\nHere are the weights: mg, g, kg, ton, lb, oz")

    original_weight = input("Enter the original weight unit: ").lower()
    target_weight = input("Enter the target weight unit: ").lower()

    if original_weight not in weights or target_weight not in weights:
        print("\nInvalid weight unit entered!\n")
        return

    try:
        number = float(input("Enter the number to convert: "))
    except ValueError:
        print("\nInvalid number input!\n")
        return

    original_value = weights[original_weight]
    target_value = weights[target_weight]

    result = number * (original_value / target_value)
    print(f"\n{number} {original_weight} is equal to {result} {target_weight}\n")


def main():
    while True:
        try:
            function = int(input("\nChoose a conversion type:\n1. Length\n2. Weight\nEnter 1 or 2: "))
        except ValueError:
            print("Please enter a number (1 or 2).")
            continue

        if function == 1:
            Lengths()
        elif function == 2:
            weight()
        else:
            print("Invalid selection. Please choose 1 or 2.")

        replay = input("\nWould you like to do another conversion? (y/n): ").lower()
        if replay == 'y':
            continue
        elif replay == 'n':
            break
        else:
            print("\nGoodbye!\n")

main()