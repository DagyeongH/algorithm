def solution(num, k):
    answer = -1
    str_num = str(num)
    for idx in range(len(str_num)):
        if str_num[idx] == str(k):
            answer = idx + 1
            break
    return answer