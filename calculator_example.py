"""
This example creates a simple calculator with the usage of functions
"""
from calculator_methods import *

if __name__== "__main__":
    num1 = int(input("Enter the first number"))
    num2 = int(input("Enter the second number"))
    operation = input("Enter the operation (+,-,*,/)")
    result = 0
    #verify and call the right functions belonging to the operation
    if(operation == "+"):
        result = my_addition(num1,num2)
    elif(operation == "-"):
        result = my_substraction(num1, num2)
    elif(operation == "*"):
        result = my_mutliplication(num1, num2)
    elif(operation == "/"):
        result = my_division(num1, num2)
    else:
        print("Invalid operation")

    print(result)
