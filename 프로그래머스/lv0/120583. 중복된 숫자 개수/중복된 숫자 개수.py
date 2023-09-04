def solution(array, n):
    answer = 0
    while n in array:
        array.pop(array.index(n))
        answer += 1
    return answer