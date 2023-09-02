def solution(keyinput, board):
    a = 0
    b = 0
    
    for key in keyinput:
        # 이동
        if key == 'left':
            a -= 1
        elif key == 'right':
            a += 1
        elif key == 'up':
            b += 1
        elif key == 'down':
            b -= 1
        
        # board 크기 넘어가면 조정 
        if a < -(board[0] // 2):
            a = -(board[0] // 2)
        elif a > board[0] // 2:
            a = board[0] // 2
        
        if b < -(board[1] // 2):
            b = -(board[1] // 2)
        elif b > board[1] // 2:
            b = board[1] // 2
            
    answer = [a, b]
    return answer