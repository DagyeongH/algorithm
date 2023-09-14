def solution(arr):
    answer = arr[arr.index(2):len(arr) - arr[-1:-len(arr):-1].index(2)] if 2 in arr else [-1]
    return answer