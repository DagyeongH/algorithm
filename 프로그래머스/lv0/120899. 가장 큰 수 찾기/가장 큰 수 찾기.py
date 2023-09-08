def solution(array):
    answer = []
    m = max(array)
    answer = [m, array.index(m)]
    return answer