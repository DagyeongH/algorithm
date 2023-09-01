import math
def solution(numer1, denom1, numer2, denom2):
    denom = denom1 * denom2
    numer = (numer1 * denom2) + (numer2 * denom1)
    m = max(denom, numer)
    
    # 최대공약수 구해서 기약분수로 나타내기
    for i in range(m, 0, -1):
        if denom % i == 0 and numer % i == 0:
            denom = denom // i
            numer = numer // i
            break
    answer = [numer, denom]
    return answer