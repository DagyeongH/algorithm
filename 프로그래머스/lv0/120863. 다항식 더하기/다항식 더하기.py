import re
def solution(polynomial):
    answer = ''
    res = re.sub('[^0-9x]', ' ', polynomial).split()
    ans_x = 0
    ans_not_x = 0
    
    for r in res:
        # x항 값 구하기
        if 'x' in r:
            if len(r) == 1:
                ans_x += 1
            else:
                ans_x += int(r[:len(r)-1])
        else:
            ans_not_x += int(r)   
    
    # x항 조건
    if not ans_x:
        ans_x = ''
    elif ans_x == 1:
        ans_x = 'x'
    else:
        ans_x = str(ans_x) + 'x'
    # 상수항 조건
    if not ans_not_x:
        ans_not_x = ''
    else:
        ans_not_x = str(ans_not_x)
        
    # x, 상수항 묶어줄 때 조건
    if ans_x and ans_not_x:
        answer = ans_x + ' + ' + ans_not_x
    else:
        answer = ans_x + ans_not_x
        
    return answer