def solution(s1, s2):
    answer = 0
    if len(s1) > len(s2):
        for val in s2:
            if val in s1:
                answer += 1
    else:
        for val in s1:
            if val in s2:
                answer += 1
    return answer