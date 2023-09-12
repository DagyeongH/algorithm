def solution(A, B):
    answer = 0
    while True:
        if A == B:
            break
        else:
            # 한바퀴 다 돌아도 값이 같지 않다면 빠져나감
            if answer == len(A):
                answer = -1
                break
            A = A[-1] + A[-len(A):-1]
            print(A)
            answer += 1
