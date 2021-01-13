#!/usr/bin/python3

"""

Final week project: A program that replicates the show - "Who wants to be a Millionaire"

"""
import crayons
import time
from playerInfo import *
#from gameInstructions import *
#from help_func import *


def game_instructions():
    moneyBank = ["1,000,000", "500,000", "250,000","125,000","64,000","32,000","16,000","8,000","4,000","2,000","1,000","500","300","200","100"]

    print("""
    
    You will be asked 15 questions. The money value grows from $500 all the wayup to $1 MILLION. 
    
    Every question correctly answered moved you one step closer to that top prize. Remember you can always walk away with that money you have earned up to that point.
    
    An incorrect answer and you walk away with nothing until you get to those two thresholds - $1,000 then again at $32,000. """)
    time.sleep(5)
    for i in moneyBank:
        print("\n$"+i)

    time.sleep(1)
    print( """\n You have two lifelines:
    One, you can either choose to swap questions which will allow you to  discard the current question and receive a new question. You can type "swap" anytime to use this lifeline!

    Second, you have 50:50 which is an option that takes away two incorrect answers""")
    time.sleep(2)


def help_func(help):
  
    help_options = ["a", "b"]

    if help in help_options:
        if help == "a":
            game_instructions()
        elif help == "b": # Option b
            print("Proceeding to the game")
    else: #if user enters anything other than a or b
        help = input("Invalid input. Please enter a valid entry > ")
        help_func(help)
                        

def swapQ():
    global swapUsed
    if swapUsed == 0:
        print("\nYou have chosen to swap your current question with a next question. Here is your next question:  ")
        with open("swap.txt","r") as configfile:
            configlist = configfile.read()#print the content of the file
            
        print(crayons.cyan(configlist,bold=True))
        swapUsed += 1
    else:
        print("You have used the swap lifeline already")
        

def lose():
    if winning_Money <= 1000:
        print("\nYou won $0. ")
        
    elif winning_Money <= 32000 and winning_Money >= 1000:
        print("\nYou won 1000! ")
        
    else:
        print("\nYou won $32000.")
      


def main():
    
    validAnswers = ["A", "B", "C", "D", "SWAP", "50-50"]

    lifeLineAvailable = ["swap","50-50"]
    
    lifeLineUSed = []
    
    global swapUsed 
    swapUsed = 0
    
    fiftyFifty =0

    global winning_Money 
    winning_Money = 0

    correctAnswerList = ["B", "B","C","D","A","C","B","C","D","C","D","A","C","C","B"]

    swapAnswer = "D"

    moneyBank = ["1000000", "500000", "250000","125000","64000","32000","16000","8000","4000","2000","1000","500","300","200","100"]
  
    help = input(""" 
    Would you like to read the instructions of the game? Please select from the following options:
            
            a : Yes, Show me instruction about the game
            
            b: No, skip instruction and proceed to the game
            
   >> """ ).strip().lower()

    help_func(help)
    time.sleep(2) 
    print("\nGood luck!\n")
    time.sleep(2)

    correctAnswer = 0
    
    #As long as correctAnswer is 0 or greater than 0, loop through the answers
    while correctAnswer >= 0: #Whenever an incorrect answer is chosen, set correctAnswer == -1
        for i in range(1,16): #Need to loop from last element of moneyBank to first element of monetBank
            filename = "question%d"%i
            with open(filename+".txt","r") as configfile:
                configlist = configfile.read()#print the content of the file
            print(crayons.cyan(configlist,bold=True))
           
            answers = input(">>").strip().upper() #taking in answer1
            if answers not in validAnswers:
                answers = input("Not a valid entry! >> ")

            if answers == correctAnswerList[i-1] or answers == "SWAP":
                if answers == "SWAP":
        
                    swapQ()
                    print(f"swapUsed is now: {swapUsed}")
                    ans = input(">>").strip().upper()
                    
                    if ans == swapAnswer:
                        print(crayons.green(f"\n\nAwesome! Correct Answer. You won ${moneyBank[len(moneyBank)-i]}. "))
                    else:
                        lose()
            
                else: #answers == correctAnswerList[i-1]
                    correctAnswer += 1
                    winning_Money = float(moneyBank[len(moneyBank)-i])
                    print(crayons.green(f"\n\nAwesome! Correct Answer. You won ${moneyBank[len(moneyBank)-i]}. "))
                
            else: #inccorect answer
                print(crayons.red(f"\n\nIncorrect Answer! The correct option is {correctAnswerList[i-1]} "))
                lose()
        break
    
                
        
    
    if correctAnswer == 15:
        print(crayons.green("""
    
    
            CONGRATULATIONS!!! YOU WON A MILLION DOLLARS!!!


        """, bold=True))



if __name__ == "__main__":
    
    print("""
    Get ready because you have been chosen to play a game for the life-changing  money that most of us just dream about. 

    This is : 

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------            
                             WHO WANTS TO BE A MILLIONAIRE?

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    """)

    playerInfo()
    
    main()
