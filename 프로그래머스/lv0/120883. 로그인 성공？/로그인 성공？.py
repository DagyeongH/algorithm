def solution(id_pw, db):
    answer = ''
    for val in db:
        if val[0] == id_pw[0]: 
            if val[1] == id_pw[1]:
                answer = 'login'
            else:
                answer = 'wrong pw'
            break    # id가 같은 경우가 나온 이후에 실행되면 fail이 됨
        else:
            answer = 'fail'
                
    return answer
