# assignment: programming assignment 3
# author: Alejandra Sicairos
# date: 11/14/2020
# file: calculator.py is a program that takes 2 numbers from the user and either adds, subtracts, multiplies, or divides the two numbers.
# input:User Data
# output: String Data

done = False

def isfloat (token) :
    dot = False
    minus = False
    for char in token :
        if char.isdigit() :  # allow many digits in a string
            continue
        elif char == "." :   # allow only one dot in a string
            if not dot :
                dot = True
            else :                                   
                return False
        elif char == "-" and token[0] == "-": # allow one minus in front
            if not minus :
                minus = True
            else :
                return False
        else :               # do not allow any other characters in a string
            return False
    return True

def add (num1, num2):
    solution = num1 + num2
    print(f"{num1} + {num2} = {solution}")

def subtract (num1, num2):
    solution = num1 - num2
    print(f"{num1} - {num2} = {solution}")

def multiply (num1, num2):
    solution = num1 * num2
    print(f"{num1} x {num2} = {solution}")

def divide (num1, num2):
    solution = float(num1 / num2)
    new_solution = format(solution, 2)
    print(f"{num1} / {num2} = {new_solution}")

def format(num, precision = 2):
    formatted_float = '{:.2f}'.format(num)
    num = formatted_float
    return num

while not done:
    while True:
        letters = ["A", "a", "S", "s", "M", "m", "D", "d"]
        print("Welcome to the Calculator Program!")
        print("Please choose one of the following operations:")
        print("Addition – A")
        print("Subtraction - S")
        print("Multiplication - M")
        print("Division - D")
        choice = input(" > ")
     
        if choice in letters:
            break
        else:
            print("You did not choose correctly.")

    if choice == "A" or choice == "a":
        print("You chose addition.")
        num1=int(input("Please enter the first number:"))
        print(f"The first number is {num1}")

        num2=int(input("Please enter the second number:"))
        print(f"The second number is {num1}")
        add(num1, num2)
        
    elif choice == "S" or choice == "s":
        print("You chose subtraction.")
        num1=int(input("Please enter the first number:"))
        print(f"The first number is {num1}")

        num2=int(input("Please enter the second number:"))
        print(f"The second number is {num1}")
        subtract(num1, num2)
    elif choice == "M" or choice == "m":
        print("You chose multiplication.")
        num1=int(input("Please enter the first number:"))
        print(f"The first number is {num1}")

        num2=int(input("Please enter the second number:"))
        print(f"The second number is {num1}")
        multiply(num1, num2)
    elif choice == "D" or choice == "d":
        print("You chose division.")
        num1=int(input("Please enter the first number:"))
        print(f"The first number is {num1}")

        num2=int(input("Please enter the second number:"))
        print(f"The second number is {num1}")
        divide(num1, num2)
        
    playAgain= input("Do you want to continue? [Y/N] ")
    if playAgain == "n":
        break
print("Goodbye!")
