def solution(s):
    ss = s.split(' ')
    while 'Z' in ss:
        # 'Z'가 있는 idx를 찾아서 그 앞의 값과 'Z'를 제거
        z_idx = ss.index('Z')
        ss.pop(z_idx-1)
        ss.pop(z_idx-1)
    ss_arr = [int(val) for val in ss]
    answer = sum(ss_arr)
    return answer