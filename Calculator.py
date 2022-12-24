import math
import sys
import os
from time import sleep

os.system("cls")
def opening_message(msg):
    lenght = len(msg)
    print("-="*lenght)
    print(msg.center(50))
    print("-=" * lenght)
    print("\n")
    print("[1]Arithmetical Calculations", " [2]Factorial", " [3]Square Root", " [4]Exponentiation")
def arithmetical(choice):
    print("[1]Addition", "[2]Subtraction", "[3]Multiplication", "[4]Division")
    while True:
        try:
            choice = int(input("-> "))
            break
        except ValueError:
            print("\nOops! Not a valid option. Try again")
            arithmetical(choice)
    match choice:
        case 1:                                         #Addiction
            add1 = input("Type a number: ")
            add2 = input("Type another number: ")
            if add1.isnumeric() and add2.isnumeric():
                add1, add2 = float(add1), float(add2)
                math_result(add1 + add2)
            else:
                print("You need to type two numbers")
                exec_again()
        case 2:                                         #Subtraction
            minus1 = input("Type a number: ")
            minus2 = input("Typer another number: ")
            if minus1.isnumeric() and minus2.isnumeric():
                minus1, minus2 = float(minus1), float(minus2)
                math_result(minus1 - minus2)
            else:
                print("You need to type two numbers")
                exec_again()
        case 3:                                         #Multiplication
            multiply1 = input("Type a number: ")
            multiply2 = input("Type another number: ")
            if multiply1.isnumeric() and multiply2.isnumeric():
                multiply1, multiply2 = float(multiply1), float(multiply2)
                math_result(multiply1 * multiply2)
            else:
                print("You need to type two numbers")
                exec_again()
        case 4:                                         #Division
            divide1 = input("Type a number: ")
            divide2 = input("Type another number: ")
            try:
                if divide1.isnumeric() and divide2.isnumeric():
                    divide1, divide2 = float(divide1), float(divide2)
                    math_result(divide1 / divide2)
                else:
                    print("You need to type two numbers")
                    exec_again()
            except ZeroDivisionError:
                print("Division for 0 is not defined")
                ask_again()
        case _:
            print("\nOops! Not a valid option. Try again")
            arithmetical(choice)
def ask_again():
    print("Another Operation? [y]yes, [n]no")
    test = input("->")
    if test == "y":
        exec_again()
    elif test == "n":
        sys.exit()
    else:
        print("Invalid Option, digit [y]for yes or [n]for no\n")
        sleep(2)
        os.system("cls")
        ask_again()
def exec_again():    #Reinicia a calculadora
    sleep(2)
    os.system("cls")
    calculator()
def math_result(result):
    print("The result is: ", result)
    ask_again()
def calculator():
    opening_message("Which Operation Do You Want?")
    while True:  #This loop forces the user to enter a number
        while True:
            try:
                choice = int(input("-> "))
                break
            except ValueError:
                print("\nOops! Not a valid option. Try again")
                exec_again()
        if choice == 1:                                #Arithmetical Operations
            arithmetical(choice)
        elif choice == 2:                              #Factorial of a Number
            factorial = input("Type a number: ")
            if factorial.isnumeric():
                factorial = int(factorial)
                math_result(math.factorial(factorial))
            else:
                print("You need to type a number")
                exec_again()
        elif choice == 3:                              #Square Root
            root = input("Type a number: ")
            if root.isnumeric():
                root = float(root)
                math_result(math.sqrt(root))
            else:
                print("You need to type a number")
                exec_again()
        elif choice == 4:                              #Exponentiation
            base = input("Digit the base: ")
            exponent = input("Digit the exponent: ")
            if base.isnumeric() and exponent.isnumeric():
                base, exponent = int(base), int(exponent)
                math_result(math.pow(base, exponent))
            else:
                print("You need to enter a number in both the base and exponent")
                exec_again()
        else:
            print("\nOops! Not a valid option. Try again")
            exec_again()
calculator()
