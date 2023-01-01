
# show the game list
def show_game_list(game_list):
    print("Here is the game list: ")
    print(game_list)


# ask user to enter position number of the list
def position_choice():
    choice = 'WRONG'

    while choice not in ['0','1','2']:

        choice = input("Enter a position 0, 1, 2: ")

        if choice not in ['0','1','2']:
            print("Oops! Invalid Choice. Please enter a valid position (0,1,2)")
    return int(choice)

# replace the list value with user's entered string at inserted position
def replacement_choice(game_list, position):
    user_placement = input("Please enter a string: ")

    game_list[position] = user_placement

    return game_list


# Ask user if want to keep playing game or not.
def gameon_choice():
    choice = 'WRONG'
    while choice not in ['Y', 'N']:
        choice = input("Wanna keep playing ? (Y or N): ")
        if choice not in ['Y', 'N']:
            print("Oops! Wrong Choice. Please enter Y or N.")
    if choice == 'Y':
        return True
    else:
        return False

gameon = True
game_list = [0,1,2]

# call all the function in proper order
while gameon:
    show_game_list(game_list)

    position = position_choice()

    game_list = replacement_choice(game_list, position)

    show_game_list(game_list)

    gameon = gameon_choice()