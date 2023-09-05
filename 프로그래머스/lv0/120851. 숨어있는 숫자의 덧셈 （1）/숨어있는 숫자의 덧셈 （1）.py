def solution(my_string):
    answer = 0
    for s in my_string:
        try:
            answer += int(s)
        except:
            pass
    return answer