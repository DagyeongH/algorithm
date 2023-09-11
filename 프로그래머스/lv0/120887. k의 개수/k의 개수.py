def solution(i, j, k):
    # ex) 11은 1이 2개
    answer = 0
    ks = str(k)
    for val in range(i, j+1):
        # 자릿수의 값 중 k와 같은게 몇 개 있는지 확인
        for v in str(val):
            if v == ks:
                answer += 1
    return answer