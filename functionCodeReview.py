#!/usr/bin/env python3

"""Make a calculator that takes two integers and adds/subtracts/divides/multiplies them!
Use FUNCTIONS to create a calculator! Your script must accept the following user input:

a float/integer
another float/integer
an operator (add, subtract, divide, multiply)
Your script should return the answer!

BONUS 1: Make the script human-error proof. Use IF/ELIF/ELSE and TRY/EXCEPT where necessary!

BONUS 2: If the user types in a bad input, have them type it in again! Use a WHILE LOOP!"""


def add(num1,num2): #function that adds num1 and num2
    print(str(num1) + " + " + str(num2) + " = "+ str(num1+num2))

def subtract(num1, num2): #function that subtracts num2 from num1
    print(str(num1) + " - " + str(num2) + "  = " + str(num1-num2))

def multiply(num1,num2): #function that multiplies num1 and num2
    print(str(num1) + " * " + str(num2) + " = " + str(num1*num2))

def divide(num1,num2): #function that divides num1 by num2
    print(str(num1)+"/"+str(num2) + " = " + str(num1/num2))

def main(): #function that calls the above functions when an operator is chosen
    operators = ["+", "-", "*", "/"] #list of operators that the calculator can perform
    
    operation = input("What opertation would you like to perform today? Please choose from +, -, * or / ").strip() #operator being taken from user, .strip() is applied to the input to exclude whitespaces
    
    if operation not in operators: #condition to check if the user has entered an invalid input
        operation = input("Invalid input, please enter +, -, * or / ").strip() #if an invalid input is provided by an user, the user is asked to enter a valid input from the given options
        

    while operation in operators: #condition to check if the user has entered a valid input (if the provided user input is present in the operators list)
        num1 = float(input(" Please enter num1 ")) #taking user input for num1 and converting it to float to perform calculation
        num2 = float(input(" Please enter num2 ")) #taking user input for num2 and converting it to floar to perform calculation

        if(operation == "+"): #condition to perform if the user entered a "+" - addition i.e. addition
            print("The operation you chose is addition.") #The user is notified of the operator that was chosen
            add(num1,num2) #add function called with the values num1 and num2 pased as arguments
            break

        elif(operation == "-"): #condition to perform if the user entered a "-" - subtraction
            print("The operation you chose is subtraction.") #The user is notified of the operator that was chosen i.e. subtraction
            subtract(num1,num2) #subtract function called with the values num1 and num2 pased as arguments
            break

        elif(operation == "*"): #condition to perform if the user entered a "*" - multiplication
            print("The operation you chose is multiplication.") #The user is notified of the operator that was chosen i.e. multiplication
            multiply(num1,num2) #multiply function called with the values num1 and num2 pased as arguments
            break

        else: #condition to perform when user enters operators other than +, - and * i.e. /
            print("The operation you chose is division.")#The user is notified of the operator that was chosen i.e. division
            divide(num1,num2) #division function called with the values num1 and num2 pased as arguments
            break
        
if __name__ == "__main__": #condition to perform if the current file is run
    print("\nWelcome to a Simple Calculator !") #Welcome greeting to the user
    calc = input("\nWould you like to perform a calculation? ").strip().lower()
    while calc == "y" or calc == "yes":
        main() #main function called
        calc = input("\nWould you like to perform a calculation? ").strip().lower() #user asked again if they want to make another calculation - to re run main() if the user enters "yes" or "y"
    
    print("Goodbye!" ) #exits the while loop if user enters anything other than "yes" or "y"


