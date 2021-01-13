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
