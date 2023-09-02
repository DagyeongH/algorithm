def solution(dots):
    answer = 0
    a = dots[0]
    for val in dots:
        if val[0] != a[0] and val[1] != a[1]:
            answer = (a[1] - val[1]) * (a[0] - val[0])
    if answer < 0:
        answer *= -1
    return answer