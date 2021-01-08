#!/usr/bin/end python3

def gameslist():
    availableGames = ["1. Multiple Choice Quiz Game", "2. Tic-Tac-Toe","3. Rock Paper Scissor"]
    for game in availableGames:
        print(game)

if __name__ == "__main__":
    print("\n\nWelcome to AK Companies of games! What game would you like to play today? ")
    print("\nPlease choose from the following available games: ")
    gameslist()
    gameChoice = input()



