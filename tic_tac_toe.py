import numpy
board=numpy.array([['-','-','-'],['-','-','-'],['-','-','-']])
pl_1 = "X"
pl_2 = "O"
print("Player_1 is X\nPlayer_2 is O")

def check_rows(symbol):
    for r in range(3):
        count = 0
        for c in range(3):
            if board[r][c] == symbol:
                count += 1
        if count == 3:
            return True        
    return False

def check_columns(symbol):
    for c in range(3):
        count = 0
        for r in range(3):
            if board[r][c] == symbol:
                count += 1
        if count == 3:
            return True        
    return False

def check_diagonal(symbol):
    count = 0
    for r in range(3):
        for c in range(3):
            if board[r][c] == symbol and r==c :
                count += 1
    if count == 3:
        return True
    if board[0][2] == board[1][1] and board[1][1] == board[2][0] and board[1][1] == symbol:
        return True
    return False            
            


def won(symbol):
    return check_rows(symbol) or check_columns(symbol) or check_diagonal(symbol)

def place(symbol):
    print(numpy.matrix(board))
    while(1):
        row = int(input("Enter no. of rows 1,2 or 3: "))
        cols= int(input("Enter no. of coloumn 1 ,2 or 3: "))
        if row>0 and row <4 and cols >0 and cols <4 and board[row-1][cols-1] == '-':
            break
        else:
            print('Invalid Input Or ALREADY FILLED \n Try again')
    board[row-1][cols-1] = symbol            

def play():
    for turn in range(9):
        if turn%2 == 0:
            print("X turns")
            place(pl_1)
            if won(pl_1):
                print("palyer 1 has won the game")
                break
        else:
            print("O turns")
            place(pl_2)
            if won(pl_2):
                print("palyer 2 has won the game")
                break  
    if not(won(pl_1)) and not(won(pl_2)):
        print(numpy.matrix(board))
        print("Draw")                  
play()