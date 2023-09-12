def solution(array):
    answer = 0
    for val in array:
        for s in str(val):
            if s == '7':
                answer += 1
    return answer