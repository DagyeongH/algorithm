def solution(box, n):
    answer = 1
    for val in box:
        v = val // n
        answer *= v
    return answer