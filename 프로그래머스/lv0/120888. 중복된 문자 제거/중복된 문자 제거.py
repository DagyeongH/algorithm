def solution(my_string):
    answer = ''
    string = []
    for s in my_string:
        if s in string:
            continue
        else:
            string.append(s)
    answer = ''.join(string)
    return answer