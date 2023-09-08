def solution(my_string):
    answer = ''
    my_string_lower = my_string.lower()
    for s in sorted(my_string_lower):
        answer += s
    return answer