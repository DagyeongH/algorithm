def solution(board):
    answer = 0
    big_board = []
    big_board.append([0]*(len(board)+2))
    for row in board:
        rows = [0] + row + [0]
        big_board.append(rows)
    big_board.append([0]*(len(board)+2))
    
    for i in range(1, len(big_board)-1):
        for j in range(1, len(big_board)-1):
            if big_board[i][j] % 2 == 1:     
                big_board[i-1][j-1] += 2
                big_board[i-1][j] += 2
                big_board[i-1][j+1] += 2
                big_board[i][j-1] += 2
                big_board[i][j+1] += 2
                big_board[i+1][j-1] += 2
                big_board[i+1][j] += 2
                big_board[i+1][j+1] +=2
    
    for i in range(1, len(big_board)-1):
        for j in range(1, len(big_board)-1):
            if big_board[i][j] == 0:
                answer += 1
    return answer