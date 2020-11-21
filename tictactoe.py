import time,sys
theBoard = {   '1':' ','2':' ','3':' ',
            '4':' ','5':' ','6':' ',
            '7':' ','8':' ','9':' '    }
player_1 = ''
player_2 = ''
def checkBoard(winner):
    everyBoard = theBoard['1'] and theBoard['2'] and theBoard['3'] and theBoard['4'] and theBoard['5'] and theBoard['6'] and theBoard['7'] and theBoard['8'] and theBoard['9'] != ' '
    column_1 = theBoard['1'] == theBoard['2'] == theBoard['3'] != ' '
    column_2 = theBoard['4'] == theBoard['5'] == theBoard['6'] != ' '
    column_3 = theBoard['7'] == theBoard['8'] == theBoard['9'] != ' '
    row_1 = theBoard['1'] == theBoard['4'] == theBoard['7'] != ' '
    row_2 = theBoard['2'] == theBoard['5'] == theBoard['8'] != ' '
    row_3 = theBoard['3'] == theBoard['6'] == theBoard['9'] != ' '
    diagonal_1 = theBoard['1'] == theBoard['5'] == theBoard['9'] != ' '
    diagonal_2 = theBoard['3'] == theBoard['5'] == theBoard['7'] != ' '
    if winner == 'O':
        winner = player_1
    elif winner == 'X':
        winner = player_2
    if column_1 or column_2 or column_3 or row_1 or row_2 or row_3 or diagonal_1 or diagonal_2:
        return print(winner+' won the Game!')
    elif everyBoard:
        return print("It's a Draw!")

def tictactoe(board):
    print('+-----+-----+-----+')
    print('|  '+board['1']+'  |  '+board['2']+'  |  '+board['3']+'  |')
    print('+-----+-----+-----+')
    print('|  '+board['4']+'  |  '+board['5']+'  |  '+board['6']+'  |')
    print('+-----+-----+-----+')
    print('|  '+board['7']+'  |  '+board['8']+'  |  '+board['9']+'  |')
    print('+-----+-----+-----+')

print('Tic Tac Toe Game!!')
choice = input('Start Game? [Y/N]: ')
#Start Game
if choice == 'Y' or 'y':
    player_1 = input('Player 1[X]: ')
    player_2 = input('Player 2[O]: ')
    for i in range(4):
        print("Loading" + "." * i)
        sys.stdout.write("\033[F") # Cursor up one line
        time.sleep(1)
    turn = 'X'
    tictactoe(theBoard)
    while True:
        move = input()
        try:
            sys.stdout.write("\033[F")
            if theBoard[move] == ' ':
                theBoard[move]=turn
                if turn == 'X':
                    turn = 'O'
                else:
                    turn = 'X'
                tictactoe(theBoard)
            elif theBoard[move] == 'X' or 'O':
                print('This turn is already Occupied!!')
        except:
            print('That is not a Valid Turn!!')
        checkBoard(turn)
        

