##
## Tic Tac Toe 
##
from random import randrange

def display_board(board):
    # The function accepts one parameter containing the board's current status
    # and prints it out to the console.
    print('+-------+-------+-------+')
    print('|       |       |       |')
    print('|   ' + board[0][0] +   '   |   ' + board[0][1] +  '   |   ' + board[0][2] + '   |')
    print('|       |       |       |')
    print('+-------+-------+-------+')
    print('|       |       |       |')
    print('|   ' + board[1][0] +   '   |   ' + board[1][1] +  '   |   ' + board[1][2] + '   |')
    print('|       |       |       |')
    print('+-------+-------+-------+')
    print('|       |       |       |')
    print('|   ' + board[2][0] +   '   |   ' + board[2][1] +  '   |   ' + board[2][2] + '   |')
    print('|       |       |       |')
    print('+-------+-------+-------+')


def enter_move(board):
    # The function accepts the board's current status, asks the user about their move, 
    # checks the input, and updates the board according to the user's decision.
    while True:

        move = int(input('Please pick a number between (1-9): '))

        if move < 1 or move > 9:
            print('Please pick a number between the range 1-9')
            continue
        elif str(move) not in board[0] and str(move) not in board[1] and str(move) not in board[2]:
            print('Sorry, square taken! Please select another square!')
            continue

        for row in range(0,3):
            for column in range(0,3):
                if board[row][column] == str(move):
                    board[row][column] = 'O'
        break

def make_list_of_free_fields(board):
    # The function browses the board and builds a list of all the free squares; 
    # the list consists of tuples, while each tuple is a pair of row and column numbers.
    global free_squares
    free_squares = [ ]

    for row in range(0,3):
        for column in range(0,3):
            if board[row][column] == 'X' or board[row][column] == 'O':
                pass
            else:
                free_squares.append(([row], [column]))
        print(free_squares)

def victory_for(board, sign):
    # The function analyzes the board's status in order to check if 
    # the player using 'O's or 'X's has won the game
    print('Checking to see if Player', sign,' is the winner!')
    if board[0][0] == sign and board[0][1] == sign and board[0][2] == sign:
        return sign
    elif board[1][0] == sign and board[1][1] == sign and board[1][2] == sign:
        return sign
    elif board[2][0] == sign and board[2][1] == sign and board[2][2] == sign:
        return sign
    elif board[0][0] == sign and board[1][0] == sign and board[2][0] == sign:
        return sign
    elif board[0][1] == sign and board[1][1] == sign and board[2][1] == sign:
        return sign
    elif board[0][2] == sign and board[1][2] == sign and board[2][2] == sign:
        return sign
    elif board[0][0] == sign and board[1][1] == sign and board[2][2] == sign:
        return sign
    elif board[2][0] == sign and board[1][1] == sign and board[0][2] == sign:
        return sign
    else:
        print('We do not have a winner yet')

def draw_move(board):
 # The function draws the computer's move and updates the board.
    while True:

        row = randrange(3)
        column = randrange(3)

        if ([row], [column]) not in free_squares:
            continue
        else:
            board[row][column] = 'X'
            return

board = [ ['1', '2', '3'], ['4', 'X', '6'], ['7', '8', '9'] ]
numberOfMoves = 1
human = 'O'
computer = 'X'

display_board(board)
enter_move(board)
display_board(board)
make_list_of_free_fields(board)
victory_for(board, human)
victory_for(board, computer)
draw_move(board)
victory_for(board, human)
victory_for(board, computer)
display_board(board)

enter_move(board)
display_board(board)
make_list_of_free_fields(board)
victory_for(board, human)
victory_for(board, computer)
draw_move(board)
victory_for(board, human)
victory_for(board, computer)

enter_move(board)
display_board(board)
make_list_of_free_fields(board)
victory_for(board, human)
victory_for(board, computer)
draw_move(board)
victory_for(board, human)
victory_for(board, computer)

enter_move(board)
display_board(board)
make_list_of_free_fields(board)
victory_for(board, human)
victory_for(board, computer)
draw_move(board)
victory_for(board, human)
victory_for(board, computer)

enter_move(board)
display_board(board)
make_list_of_free_fields(board)
victory_for(board, human)
victory_for(board, computer)
draw_move(board)
victory_for(board, human)
victory_for(board, computer)
