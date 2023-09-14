def solution(dots):
    answer = 0
    if modd(dots[0], dots[1]) == modd(dots[2], dots[3]):
        answer = 1
    if modd(dots[0], dots[2]) == modd(dots[1], dots[3]):
        answer = 1
    if modd(dots[0], dots[3]) == modd(dots[1], dots[2]):
        answer = 1
    return answer
            
def modd(a, b):
    return (a[0] - b[0]) / (a[1] - b[1])