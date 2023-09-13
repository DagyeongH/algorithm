def solution(quiz):
    answer = []
    for q in quiz:
        s = '=='.join(q.split('='))
        if eval(s):
            answer.append('O')
        else:
            answer.append('X')
    return answer