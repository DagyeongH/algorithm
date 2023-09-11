def solution(array, n):
    array = sorted(array)
    sub_arr = [abs(val-n) for val in array]
    MIN = min(sub_arr)
    answer = array[sub_arr.index(MIN)]
    return answer