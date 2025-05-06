def number_checker():
    number = int(input("Enter the number: \n"))
    
    for i in range(2,number):
        
        if number % i== 0:
            print("Not prime!")
            break
    else:
        print("Prime")

def number_checker_2():
    # Ask for the maximum limit n
    n = int(input("Enter the maximum number to generate primes up to: "))
    
    # Step 1: Create a list to mark numbers as prime or non-prime
    primes = [True] * (n + 1)  # All numbers are initially marked as prime
    primes[0] = primes[1] = False  # 0 and 1 are not prime
    
    # Step 2: Sieve of Eratosthenes
    for i in range(2, int(n**0.5) + 1):  # We loop until the square root of n
        if primes[i]:  # If i is still marked as prime
            for j in range(i * i, n + 1, i):  # Mark all multiples of i as non-prime
                primes[j] = False
    
    # Step 3: Collect and display the primes
    prime_numbers = [i for i in range(2, n + 1) if primes[i]]
    print(f"The prime numbers up to {n} are: {prime_numbers}")
    
# Calling the function

def main():
    while True:
        try:
            function = int(input(""""Enter the function you like:
1.number_checker
2.number_checker_2 (in the list!!!)\n"""))
            if function == 1:
                number_checker()
            elif function == 2:
                number_checker_2()
            else:
                print("\nYou got nothing to do here!\n")
        except ValueError:
            print("Invalid input!")
            continue
        replay = input("Would you like to try it again? (y/n):\n")

        if replay == 'y':
            continue
        elif replay == 'n':
            break
        else:
            print("\nGoodbye\n")
            break
main()