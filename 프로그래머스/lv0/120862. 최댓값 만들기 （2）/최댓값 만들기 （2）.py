def solution(numbers):
    answer = 0
    n_sort = sorted(numbers)
    n1 = n_sort[-1] * n_sort[-2]
    n2 = n_sort[0] * n_sort[1]
    answer = max(n1, n2)
    return answer