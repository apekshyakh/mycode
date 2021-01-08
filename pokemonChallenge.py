#!/usr/bin/env python3

"""
Use your script to print out the following:

Change the Pokemon in the URL to a Pokemon of your choice! BONUS- add input to collect what Pokemon to look up!

Print the URL to "front_default", which is a link to an image of your Pokemon! BONUS- download the image (hint: look at the wget module)!

Return a count of how many "game_indices" the selected Pokemon has been in!

Print out the "name"s of ALL the selected Pokemon's "moves".

"""
# imports always go at the top of your code
import requests

def main():
    base_API = "https://pokeapi.co/api/v2/pokemon/"
    

    pokemon = input("\n\n What pokemon would you like to look up today? ")
    pokeApi = base_API+pokemon
    
    pokemon_URL = requests.get(pokeApi).json()
    
    #pokemon Image
    pokeImage = pokemon_URL["sprites"]["front_default"]
    
    print("\n\nPlease go to this link to look at the pokemen you chose: ------> " + pokeImage)
    
    #game_indices
    print("\n\n" + pokemon + " has appereared in " + str(len(pokemon_URL["game_indices"])) + " game indices ! ")
    
    #moves of the pokemon
    moves = []
    for subDict in pokemon_URL["moves"]:
        moves.append(subDict["move"]["name"])
        
    print("\n\nMoves of " + pokemon + " are : \n " + str(moves))
    
if __name__ == "__main__":
    
    print("\n\n\n --------------- WELCOME TO THE POKEMON GAME --------------- ")
    main()
