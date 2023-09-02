def solution(sides):
    answer = 0
    m = max(sides)
    if m < sum(sides) - m:
        answer = 1
    else:
        answer = 2
    return answer