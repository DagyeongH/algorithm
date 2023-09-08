def solution(n):
    answer = 1
    num = 1
    while answer < n:
        num += 1
        answer *= num
    # 위의 반복문 돌린 answer값이 n보다 같으면 그대로, 크면 -1 후 출력
    if answer > n:
        num -= 1
    return num