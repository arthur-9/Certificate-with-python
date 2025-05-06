def calculate():
    while 1:
        option = input("""Enter the choice: \n
+
-
*
/\n""")
        
        if option == '+':
            num1 = int(input("Enter the first number: \n"))
            num2 = int(input("Enter the second number: \n"))
            result = num1 + num2
            print(result)
        elif option == '-':
            num1 = int(input("Enter the first number: \n"))
            num2 = int(input("Enter the second number: \n"))
            result = num1 - num2
            print(result)
        elif option == '*':
            num1 = int(input("Enter the first number: \n"))
            num2 = int(input("Enter the second number: \n"))
            result = num1 * num2
            print(result)
        elif option == '/':
            num1 = int(input("Enter the first number: \n"))
            num2 = int(input("Enter the second number: \n"))
            if num2 == 0:
                print("Cannot divide by zero!")
                continue
            result = num1 / num2
            print(result)
        else:
            print("Invalid choice")
            continue

        replay = int(input("Do you wanna repeat it again? (1 for yes / 0 for no):\n"))
        if replay == 1:
            continue
        elif replay == 0:
            break
        
calculate()