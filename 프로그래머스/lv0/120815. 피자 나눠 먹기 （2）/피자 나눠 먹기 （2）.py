def solution(n):
    # 6과 사람수 최소공배수
    answer = 0
    six = 6
    if n % 6 == 0:
        answer = n // 6
    else:
        answer = 1
        for i in range(1, six + 1):
            if n % i == 0 and six % i == 0:
                answer *= i
                n = n // i
                six = six // i
        answer = (answer * n * six) // 6    # 피자 한 판 6조각
                
    return answer