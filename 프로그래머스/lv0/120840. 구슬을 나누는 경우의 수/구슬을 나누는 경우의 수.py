def solution(balls, share):
    answer = 1
    for i in range(balls - share + 1, balls + 1):
        answer *= i
    # 순서 상관 X
    for j in range(1, share + 1):
        answer //= j
        
    return answer