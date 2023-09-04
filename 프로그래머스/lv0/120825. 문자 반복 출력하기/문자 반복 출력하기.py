def solution(my_string, n):
    answer = ''
    n_my_string = [s * n for s in my_string]
    for val in n_my_string:
        answer += val
    return answer