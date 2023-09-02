import math

def solution(n):
    answer = 0
    for i in range(1, math.floor(math.sqrt(n)) + 1):
        if n % i == 0:
            if i ** 2 == n:
                answer += 1
                continue
            answer += 2
    return answer