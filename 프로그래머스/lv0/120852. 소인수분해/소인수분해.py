def solution(n):
    answer = []
    for i in range(2, n+1):
        a = 0
        for j in range(2, i):
            if i % j == 0:
                a += 1 
                break
        if n % i == 0 and a == 0:
            answer.append(i)
    list(set(answer))
    return answer