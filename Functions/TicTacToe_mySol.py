

def display_board(board):
    print(board[1]+' |'+board[2]+' |'+board[3])
    print("--|--|--")
    print(board[4]+' |'+board[5]+' |'+board[6])
    print("--|--|--")
    print(board[7]+' |'+board[8]+' |'+board[9])
    


def user_marker():
    marker = 'WRONG'
    while marker not in ['X', 'O']:
        marker = input("Please select your marker X or O (not Zero): ").upper()
        
        if marker not in ['X', 'O']:
            print("Oops! Please select valid marker X or O")

    return marker



def user_input_position():
    position = 'wrong'
    while position not in ['1','2','3','4','5','6','7','8','9']:
        position = input("Please enter position (1-9): ")

        if position not in ['1','2','3','4','5','6','7','8','9']:
            print("Oops! Invalid position. Please enter valid position (0-9)")

    return int(position)



def place_marker(board, marker,position):
    while board[position] in ['X','O']:
        print("This position is occupied. Please select other position")
        position = user_input_position()
        
    if board[position] not in ['X','O']:
        board[position] = marker



def gameon_input():
    choice = 'WRONG'
    while choice not in ['Y','N']:
        choice = input('keep playing? Please enter Y or N: ')

        if choice not in ['Y','N']:
            print('Oops! Invalid Choice. Please enter Y or N')
    
    if choice == 'Y':
        return True
    else:
        return False



def win_check(board, marker):
    return (
    (board[1] == marker and board[2] == marker and board[3] == marker)
    or 
    (board[4] == marker and board[5] == marker and board[6] == marker)
    or 
    (board[7] == marker and board[8] == marker and board[9] == marker)
    or 
    (board[1] == marker and board[4] == marker and board[7] == marker)
    or 
    (board[2] == marker and board[5] == marker and board[8] == marker)
    or 
    (board[3] == marker and board[6] == marker and board[9] == marker)
    or 
    (board[1] == marker and board[5] == marker and board[9] == marker)
    or 
    (board[5] == marker and board[5] == marker and board[7] == marker)
    )



gameon = True
board = ['0','1','2','3','4','5','6','7','8','9']
while gameon :
    display_board(board)
    marker = user_marker()
    position = user_input_position()
    place_marker(board, marker,position)
    display_board(board)
    if win_check(board, marker):
        print("Player {} Winner".format(marker))
        break
    gameon = gameon_input()
