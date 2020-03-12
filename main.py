
board = ['-','-','-','-','-','-','-','-','-']

def printboard(board):
    print('',board[0],'|',board[1],'|',board[2])
    print('',"---------")
    print('',board[3],'|',board[4],'|',board[5])
    print('',"---------")
    print('',board[6],'|',board[7],'|',board[8])


def p1(board,printboard):

    while True:

        printboard(board)

        print("player X ")
        try:
            pos = int(input("select a position between 0 to 8 : "))

        except(ValueError):
            print("not an integer")

        if 0<= pos <=8 :

            if board[pos] in ['x'or 'o']:
                print("sorry..",(pos),'is already taken')

            else:
                board[pos] = 'x'
                break

def p2(board):

    freespace = [i for i, x in enumerate(board) if x == "-"]
    move = 0

    for let in ['o','x']:
        for i in freespace:
            boardCopy = board[:]
            boardCopy[i] = let
            if win(boardCopy, 'o') or win(boardCopy, 'x'):
                board[i] = 'o'
                move += 1

    if move == 0:
        import random
        x = random.choice(freespace)
        board[x] = 'o'


def win(bo,le):
    return ((bo[0] == le and bo[0] == board[1] and bo[1] == bo[2])or
    (bo[0] == le and bo[0] == board[3] and bo[3] == bo[6])or
    (bo[0] == le and bo[0] == board[4] and bo[4] == bo[8])or
    (bo[2] == le and bo[2] == board[5] and bo[5] == bo[8])or
    (bo[2] == le and bo[2] == board[4] and bo[4] == bo[6])or
    (bo[6] == le and bo[6] == board[7] and bo[7] == bo[8]) or
    (bo[3] == le and bo[3] == board[4] and bo[4] == bo[5]))




def main(board,printboard,win):

    while True:

        if not (win(board,'x')):

            p1(board,printboard)


        else:
            print("player X won")
            break


        if not (win(board,"o")):
            p2(board)

        else:
            print("player o won")
            break

main(board,printboard,win)
