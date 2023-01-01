def player_position(board):
    position = 0
    while position not in ['1','2','3','4','5','6','7','8','9'] or not space_check(board, position):
        position = int(input("please select your position (1-9): "))

        if position not in ['1','2','3','4','5','6','7','8','9']:
            print("\nPlease select valid position.")
        if not space_check(board, position):
            print("Position occupied!")
    return int(position)

board = [' ']*10
print(type(player_position(board)))