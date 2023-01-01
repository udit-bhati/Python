
def display_board(board):
    print(' '+board[1]+' |'+' '+board[2]+' |'+' '+board[3])
    print("---|---|---")
    print(' '+board[4]+' |'+' '+board[5]+' |'+' '+board[6])
    print("---|---|---")
    print(' '+board[7]+' |'+' '+board[8]+' |'+' '+board[9])



def player_marker():
    mark = ''
    while mark != 'X' and mark != 'O':
        mark = input("Player 1 Please select mark X or O: ").upper()
    player1_mark = mark

    if player1_mark == 'X':
        player2_mark = 'O'
    else:
        player2_mark = 'X'
    
    return (player1_mark, player2_mark)




def place_marker(board, mark, position):
        board[position] = mark




def win_check(board, mark):
    return ((board[1] == mark and board[2] == mark and board[3] == mark)
    or 
    (board[4] == mark and board[5] == mark and board[6] == mark)
    or 
    (board[7] == mark and board[8] == mark and board[9] == mark)
    or 
    (board[1] == mark and board[4] == mark and board[7] == mark)
    or 
    (board[2] == mark and board[5] == mark and board[8] == mark)
    or 
    (board[3] == mark and board[6] == mark and board[9] == mark)
    or 
    (board[1] == mark and board[5] == mark and board[9] == mark)
    or 
    (board[3] == mark and board[5] == mark and board[7] == mark)
    )




import random

def choose_player():

    flip = random.randint(0,1)

    if flip == 0:
        return 'Player 1'
    else:
        return 'Player 2'



def space_check(board, position):
    return board[position] == ' '



def full_board_check(board):
    for i in range(1,10):
        if space_check(board, i):
            return False 
    return True



def player_position(board):
    position = 0
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
        position = int(input("please select your position (1-9): "))

        if position not in [1,2,3,4,5,6,7,8,9]:
            print("\nPlease select valid position.")
        if not space_check(board, position):
            print("Position occupied!")
    return position



def replay():
    choice = input("Wanna Play again ? Enter Y or N : ").upper()
    return choice == 'Y'



while True:

    print("Welcome to Tic Tac Toe.")

    # board = ['0','1','2','3','4','5','6','7','8','9']
    board = [' ']*10

    player1_mark, player2_mark = player_marker()

    turn = choose_player()
    print('Player 1 Mark : '+player1_mark)
    print('Player 2 Mark : '+player2_mark)
    print(turn + ' will go first')

    play_game = input("Ready to play game ? Enter Y or N : ").upper()

    if play_game == 'Y':
        gameon = True
    else:
        gameon = False
    
    while gameon:
        if turn == 'Player 1':
            display_board(board)

            print("Player 1 turn. Your mark is {}".format(player1_mark))

            position = player_position(board)

            place_marker(board, player1_mark, position)

            if win_check(board,player1_mark):
                display_board(board)
                print("player 1 Won!!")
                gameon = False
            else:
                if full_board_check(board):
                    display_board(board)
                    print("This is a Tie Game!!")
                    # gameon == False
                    break
                else:
                    turn = 'Player 2'

        else:
            display_board(board)

            print("Player 2 turn. Your mark is {}".format(player2_mark))

            position = player_position(board)

            place_marker(board, player2_mark, position)

            if win_check(board,player2_mark):
                display_board(board)
                print("player 2 Won!!")
                gameon = False
            else:
                if full_board_check(board):
                    display_board(board)
                    print("This is a Tie Game!!")
                    # gameon == False
                    break
                else:
                    turn = 'Player 1'
    if not replay():
        break
