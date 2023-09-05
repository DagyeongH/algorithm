def solution(array, height):
    answer = 0
    sort_array = sorted(array)
    for i in range(len(sort_array)):
        if sort_array[i] > height:
            answer = len(array) - i
            break
    return answer