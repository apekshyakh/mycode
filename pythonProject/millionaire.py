#!/usr/bin/python3

"""

Final week project: A program that replicates the show - "Who wants to be a Millionaire"

"""

import crayons
import time
from art import *

def playerInfo():
    #asks the player for their name
    name = input("Please enter your name > ")
    #Welcome message to the player
    print(crayons.red(f"\nWelcome {name}! "))

def game_instructions():
    moneyBank = ["1,000,000", "500,000", "250,000","125,000","64,000","32,000","16,000","8,000","4,000","2,000","1,000","500","300","200","100"]
    
    #message displaying the instructions of the game
    print("""
    
    You will be asked 15 questions. The money value grows from $500 all the way up to $1 MILLION. 
    
    Every question correctly answered moves you one step closer to that top prize. Remember you can always walk away with that money you have earned up to that point.
    
    You can type "walk away" anytime you choose to walk away with the amout you have earned!
    
    An incorrect answer and you walk away with nothing until you get to those two thresholds - $1,000 then again at $32,000. """)
    
    time.sleep(5)
    
    #loops through moneyBank list to show the user the money ladder
    for i in range(0,15):

        #condition is executed when i is 5 or 10 (threshold value)
        if i == 5 or i == 10: 
            print(crayons.red("\n$"+str(moneyBank[i]) + "- THRESHOLD VALUE")) #prints the threshold value in red
        else:
            print("\n$"+str(moneyBank[i]))

    time.sleep(1)
    print( """\n You have one  lifeline:

    THE SWAP LIFELINE: This lifeline will allow you to  discard the current question and receive a new question. You can type "swap" anytime to use this lifeline!

    """)
    time.sleep(2)


def help_func(help):
  
    help_options = ["a", "b"]
    #condition executes if the value of help is either a or b
    if help in help_options:
        #if the value of help is a, game_instructions function is called
        if help == "a":
            game_instructions()
        
        #condition is executed if the value of help is b
        else: 
            print("Proceeding to the game")

    #condition is executed if the user enters anything other than a or b
    else: 
        helpO = ""
        while helpO not in help_Options:
            help = input("Invalid input. Please enter a valid entry > ")
        #once user enters a valid option (a or b), the help_func is called with the new input value passed as an argument
        help_func(help)
                        

def swapQ():
    global swapUsed
    
    print("\nYou have chosen to swap your current question with a next question. Here is your next question:  ")
    #opening and reading swap.txt
    with open("swap.txt","r") as configfile:
        #reads the file and puts each line in a list
        configlist = configfile.read()
    
    #removed the option - SWAP - from lifelLineAvailable list as it has been used
    lifeLineAvailable.remove("SWAP")
    #adds the option - SWAP - from lifeLineUsed list
    lifeLineUsed.append("SWAP")
    
    #prints the updated value of lifeLineAvailable and lifeLineUsed lists
    print("\nLifeline available = " + str(lifeLineAvailable))       
    print("Lifeline used = " + str(lifeLineUsed)+"\n")

    #prints the content of the list of lines stored in configlist
    print(crayons.cyan(configlist,bold=True))


#function to check if the winning_Money value is less than, greater than or equal to the threshold values
def lose():
    #condition is executed when the winning_Money is less than $1,000
    if winning_Money < 1000:
        print("\nYou won $0.\n ")
        
    #condition is executed when the winning_Money is greater or equal to $1,000 and winning_Money is less than $32,000
    elif winning_Money < 32000 and winning_Money >= 1000:
        print("\nYou won 1000!\n ")
    
    #condition is executed when the winning_Money is greater than or equal to $32,000
    else:
        print("\nYou won $32000.\n")


def main():

    #list containing valid answers
    validAnswers = ["A", "B", "C", "D", "SWAP", "WALK AWAY"]
    
    global lifeLineAvailable
    lifeLineAvailable = ["SWAP"] #SWAP lifeline is available when the program first runs
    
    global lifeLineUsed
    lifeLineUsed = [] #no lifeline has been used when the program is first run
    
    global winning_Money 
    winning_Money = 0 #winning_Money is set to zero as the player starts the game with $0

    #list of correct answers
    #For example: the answer to Question1.txt would be "B", answert to Question2.txt would be "B" and so on.
    correctAnswerList = ["B", "B","C","D","A","C","B","C","D","C","D","A","C","C","B"] 
    
    #answer to the SWAP question
    swapAnswer = "D"
    
    #The steps of money ladder - from $100 which is the last element of the list to $1 Million which is the first element
    moneyBank = ["1000000", "500000", "250000","125000","64000","32000","16000","8000","4000","2000","1000","500","300","200","100"]
  
    #Takes input from the user to whether read instruction or to proceed to the game 
    help = input(""" 
    Would you like to read the instructions of the game? Please select from the following options:
            
            a : Yes, Show me instruction about the game
            
            b: No, skip instruction and proceed to the game
            
   >> """ ).strip().lower()
    
    #calls the help function and passes the input received from the user as an argument
    help_func(help)

    time.sleep(2) 
    
    #Goodluck message to notify the beginning of the game
    tprint("GOOD LUCK", font="cybermedium")
    
    time.sleep(2)
    
    #The value of correctAnswer is initialized to 0 in the beginning of the game.
    correctAnswer = 0
    
    #As long as correctAnswer is 0 or greater than 0, loop through the questions
    while correctAnswer >= 0: 
        for i in range(1,16): #Need to loop through 15 questions to win the max amount
            #In each loop, the value of filename gets updated
            #For example when i=1, filename = question1 
            filename = "question%d"%i
            #the file (.txt file) is open, reads the line and stores it in a list
            with open(filename+".txt","r") as configfile:
                configlist = configfile.read()
            
            #During each loop lifeline available and lifeline used is shown to the user
            print("\nLifeline available = " + str(lifeLineAvailable))
            print("Lifeline used = " + str(lifeLineUsed) + "\n")
            
            print(f"\nQuestion {i}:") 
            #The content of the list (the question and the answer choices) is displayed
            print(crayons.cyan(configlist,bold=True))
            
            answers = ""
            #The loop is exited when the user enters an input that is a Valid answer
            while answers not in validAnswers:
                answers = input(">>").strip().upper() #taking in answer1
            
            #condition is executed if the user enters "SWAP"
            if answers == "SWAP":
                
                #Condition is executed if SWAP lifeline has already been used
                if "SWAP" not in lifeLineAvailable:
                    print("You've already used your swap! ")

                #Condition is executed if SWAP lieline has not been used before
                else:
                    #swapQ function is called
                    swapQ()
                    ans = ""
                    #The loop is exited when the user enters an input that is a Valid answer
                    while ans not in validAnswers:
                        ans = input(">>").strip().upper()

                    #loop executes if swap is entered and the swap lifeline has not been used
                    if "SWAP" in lifeLineAvailable and ans == "SWAP":
                        ans = input("Swap lifeline is not available! Please either choose A, B, C or D").strip().upper()
                    #condition executes if user enters the correct answer to the swap question
                    if ans == swapAnswer:
                        print(crayons.green(f"\n\nAwesome! Correct Answer. You won ${moneyBank[len(moneyBank)-i]}. "))
                    #condition executes if user enters an incorrect answer to the swap question
                    else:
                        #lose function is called
                        lose()
                        #terminates the program
                        exit()
            elif answers == "WALK AWAY":
                print("You chose to walk away with the amount you have earned so far! ")
                lose()
                exit()

            #condition is executed when user enters correct answer to the given question
            elif answers == correctAnswerList[i-1]: 
                #correctAnswer is incremented
                correctAnswer += 1
                #the value of winning_Money is updated 
                winning_Money = float(moneyBank[len(moneyBank)-i])
                #Message to the user that the answer chosen is correct
                print(crayons.green(f"\n\nAwesome! Correct Answer. You won ${moneyBank[len(moneyBank)-i]}. "))
            
            #condition is executed when user enters an incorrect answer to the given question
            else: 
                #Message to the user that the answer chosen is incorrect
                print(crayons.red(f"\n\nIncorrect Answer! The correct option is {correctAnswerList[i-1]} "))
                #lose function is called
                lose()
                #terminates the program
                exit()                
            
            #condition is executed when user answers all 15 questions + 1 swap question (total = 16 questions) correct
            if correctAnswer == 16 and "SWAP" in lifeLineUsed:
                print(crayons.green("""
                                \n\n CONGRATULATIONS!!! YOU WON A MILLION DOLLARS!!!! \n\n""", bold = True))
                #terminates the program
                exit()
            
            #condition is executed when user has answered all 15 questions correctly and has not used the swap lifeline
            if correctAnswer == 15 and "SWAP" in lifeLineAvailable:
                print(crayons.green("""
                            \n\nCONGRATULATIONS!!! YOU WON A MILLION DOLLARS!!!!\n\n""", bold = True))
                #terminates the program
                exit()

if __name__ == "__main__": #executes when the program is run directly
    
    #Greet Message
    print(""" 
    \n\n\n\nGet ready because you have been chosen to play a game for the life-changing  money that most of us just dream about. 

    This is :

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------            
                             """)
    print(text2art("WHO WANTS TO BE A MILLIONAIRE? ", font="small"))
    print("""

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    """)
    #calls function playerInfo
    playerInfo()
    
    #calls function main
    main()
