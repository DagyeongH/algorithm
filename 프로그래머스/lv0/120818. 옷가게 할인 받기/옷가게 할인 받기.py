import math

def solution(price):
    answer = 0
    if price >= 500_000:
        answer = price * 0.8
    elif price >= 300_000:
        answer = price * 0.9
    elif price >= 100_000:
        answer = price * 0.95
    else:
        answer = price
    return math.floor(answer)