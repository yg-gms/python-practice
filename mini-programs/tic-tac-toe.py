import sys

board = [

    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' ']

]

def print_board(board):

    for i, row in enumerate(board):

        row_str = ""

        for j, value in enumerate(row):

            row_str += value
            if j != len(row) - 1:

                row_str += ' | '

        print(row_str)

        if i != len(board) - 1:
            print("---------")

def get_move(turn, board):

    while True:

        row = int(input("Row? (1, 2, 3) "))
        column = int(input("Column? 1, 2 or 3 "))
        print()

        if row < 1 or row > len(board):
            print("Enter a correct row input!")
            
        elif column < 1 or column > len(board[row - 1]):
            print("Enter a correct column input!")
            
        elif board[row - 1][column - 1] != ' ':
            print("Block is already taken!")
        else:
            break
    
    board[row - 1][column - 1] = turn

def check_win(board, turn):

    lists = [

            [(0, 0), (0, 1), (0, 2)], [(1, 0), (1, 1), (1, 2)], [(2, 0), (2, 1), (2, 2)],
            [(0, 0), (1, 0), (2, 0)], [(0, 1), (1, 1), (2, 1)], [(0, 2), (1, 2), (2, 2)],
            [(0, 0), (1, 1), (2, 2)], [(0, 2), (1, 1), (2, 0)]
            
            ]
    
    for list in lists:

        win = True

        for position in list:
            row, column = position
            if board[row][column] != turn:
                win = False
                break

        if win:
            return win
    
    return False

def main():

    try:

        turn = 'X'
        turn_number = 0
        print_board(board)
        print()

        while True:
            print(f"It is the {turn} players turn, please select your move!")

            get_move(turn, board)
            turn_number += 1
            print_board(board)

            win = check_win(board, turn)

            if win == True:
                sys.exit(f"{turn} Wins!")
            
            if turn == 'X':
                turn = 'O'

            elif turn == 'O':
                turn = 'X'

            if turn_number == 9:
                sys.exit("Tie!")

    except (EOFError, KeyboardInterrupt):
        sys.exit("File has unexpectedly crashed.")


if __name__ == "__main__":
    main()




    