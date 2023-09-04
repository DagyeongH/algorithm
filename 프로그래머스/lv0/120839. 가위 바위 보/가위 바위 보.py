def solution(rsp):
    answer = ''
    for val in rsp:
        if val == '2':
            answer += '0'
        elif val == '0':
            answer += '5'
        else:
            answer += '2'
    return answer