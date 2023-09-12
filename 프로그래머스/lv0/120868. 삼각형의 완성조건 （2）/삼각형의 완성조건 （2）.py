def solution(sides):
    answer = 0
    MAX = max(sides)
    MIN = min(sides)
    # sides에 있는 큰 수가 가장 긴 변인 경우
    for i in range(1, MAX+1):
        if MIN + i > MAX:
            answer += 1
    # 나머지 한 변이 가장 긴 변인 경우
    answer += (sum(sides) - MAX - 1)
    return answer