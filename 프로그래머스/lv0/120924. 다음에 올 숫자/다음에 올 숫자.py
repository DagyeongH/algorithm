def solution(common):
    answer = 0
    d = common[1] - common[0]
    
    # 등차수열인 경우
    if common[-1] == common[0] + d*(len(common)-1):
        answer = common[-1] + d
    # 등비수열인 경우
    else:
        r = common[1] // common[0]
        answer = common[-1] * r
        
    return answer