theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
            'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
            'low-L': ' ', 'low-M': ' ', 'low-R': ' '}
def printBoard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])
turn = 'X'
def whichMove(player):
    printBoard(theBoard)
    print('Turn for ' + player + '. Move on which space?')
    move = input()
    return move
for i in range(9):
    move = whichMove(turn)
    if move in theBoard:

        theBoard[move] = turn
        printBoard(theBoard)
    else:
        whichMove(turn)
    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'
printBoard(theBoard)
