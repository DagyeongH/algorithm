def solution(array):
    answer = 0
    array = sorted(array)
    print(array)
    if len(array) % 2 ==0:
        answer = (array[(len(array)//2)-1] + array[len(array)//2]) / 2
    else:
        answer = array[len(array)//2]
    return answer