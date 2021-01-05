#!/usr/bin/env python3

play = input("Do you love the show F.R.I.E.N.D.S. and want to answer a quiz question?")

count = 0;

while play.strip().lower() == "y" or play.strip().lower() == "yes" :
    count = count+1 #incrementing count

    answer1 = input("Who is Joey's agent? ") #answer collected from user

    if answer1.lower() == "estelle": #condition to check if the provided answer is correct
        print("That's correct! AWESOME ")
        break
    elif count == 2: #condition to check if no more guesses left
        print("You have no guesses left. ")
        print("The correct answer is Estelle ")
        break
    else: #exectutes if count is not yet equal 2 and answer provided is wrong
        print("Sorry, Please make another guess !")

nextQuestion = input("Are you up for another question? ")

count = 0 #setting counter to 0 to increment for nextQuestion

while nextQuestion.strip().lower() == "y" or nextQuestion.strip().lower() == "yes" :
    count = count+1 #incrementing count

    answer2 = input("Who gave Rachel and Ross the name Emm for their daughter? ")

    if answer2.lower() == "monica": #executes if the answer provided is correct
        print("Thats correct! You are truly a fan of the show!" )
        break
    elif count == 2: #executes if no guesses left (both the guesses are incorrect)
        print("No guesses left. ")
        print("The correct answer is Monica. Fun fact: Monica wanted to name her daughter Emma but since Rachel loved the name, Monica gave the name for Rachel's daughter. ")
        break
    else: #executes if count is not equal 2 and answer provided is incorrect
        print("Wrong guess! How about one more guess? ")

