#!/usr/bin/env python3

"""Make a calculator that takes two integers and adds/subtracts/divides/multiplies them!
Use FUNCTIONS to create a calculator! Your script must accept the following user input:

a float/integer
another float/integer
an operator (add, subtract, divide, multiply)
Your script should return the answer!

BONUS 1: Make the script human-error proof. Use IF/ELIF/ELSE and TRY/EXCEPT where necessary!

BONUS 2: If the user types in a bad input, have them type it in again! Use a WHILE LOOP!"""


def add(num1,num2):
    print("num1 + num2 = "+ str(num1+num2))

def subtract(num1, num2):
    print("num1 - num2 = " + str(num1-num2))
def multiply(num1,num2):
    print("num1 * num2 = " + str(num1*num2))
def divide(num1,num2):
    print("num1/num2 = " + str(num1/num2))

def main():
    
    print("Welcome to a Simple Calculator !")
    
    operation = input("What opertation would you like to perform today? Please choose from +, -, * or / ")
    
    if operation.strip() != "+" or operation.strip() != "-" or operation.strip() != "*" or operation.strip() != "/":
        input("Invalid input, please enter +, -, * or / "

    operators= ["+","-","*","/"]

    while operation.strip() in operators:
    #while operation.strip() == "+" or operation.strip() == "-" or operation.strip() == "*" or operation.strip() == "/":
        num1 = float(input(" Please enter num1 "))
        num2 = float(input(" Please enter num2 "))
        if(operation == "+"):
            print("The operation you chose is addition.")
            add(num1,num2)
            break
        elif(operation == "-"):
            print("The operation you chose os subtraction.")
            subtract(num1,num2)
            break
        elif(operation == "*"):
            print("The operation you chose is multiplication.")
            multiply(num1,num2)
            break
        else:
            divide(num1,num2)
            print("The operation you chose is division.")
            break
        
if __name__ == "__main__":
    main()

nextCalc = input("Would you like to perform another calculation? ")

while nextCalc.strip().lower() == "y" or nextCalc.strip().lower() == "yes":
    main()


