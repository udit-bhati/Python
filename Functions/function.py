from random import shuffle

mylist = [' ', 'O', ' ']

def shuffle_list_func(listname):
    shuffle(listname)
    return listname

shuffle_list = shuffle_list_func(mylist)


def player_guess_func():
    
    guess = ''
    while guess not in ['0','1','2']:
        guess = input("Pick a number - 0, 1 or 2 : ")
    return int(guess)

player_guess = player_guess_func()


def check_guess(mylist,player_guess):
    if mylist[player_guess] == 'O':
        print("You are winner!!!")
    else:
        print("Better luck next time.")

check_guess(mylist,player_guess)
print("\nHere is the original loation : ", mylist)