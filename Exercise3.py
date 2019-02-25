
def check_for_winner(board):
    for c in range(0, 3):
        #check 1
        if board[c][0] == 1 and board[c][1] == 1 and board[c][2] == 1:
            return 1
        elif board[0][c] == 1 and board[1][c] == 1 and board[2][c] == 1:
            return 1
        elif board[0][0] == 1 and board[1][1] == 1 and board[2][2] == 1:
            return 1
        elif board[0][2] == 1 and board[1][1] == 1 and board[2][0] == 1:
            return 1
        #check 2
        elif board[c][0] == 2 and board[c][1] == 2 and board[c][2] == 2:
            return 2
        elif board[0][c] == 2 and board[1][c] == 2 and board[2][c] == 2:
            return 2
        elif board[0][0] == 2 and board[1][1] == 2 and board[2][2] == 2:
            return 2
        elif board[0][2] == 2 and board[1][1] == 2 and board[2][0] == 2:
            return 2
    else:
        return 0


board=[0,2,0],\
      [0,2,0],\
      [2,1,2]
who_win=check_for_winner(board)
if(who_win==1):
    print(str(who_win) + ' ' + 'is the winner!!!!! \n')
elif (who_win == 2):
        print(str(who_win) + ' ' + 'is the winner!!!! \n')
else:
    print('draw!!!!!!')