def solution(my_str, n):
    answer = []
    # my_str을 길이 n만큼 잘라서 저장
    while len(my_str) >= n:
        answer.append(my_str[:n])
        my_str = my_str[n:]
    # my_str이 n으로 나눠 떨어지면 값이 모두 들어가지면, 그렇지 않은 경우 남은 문자열 추가
    if len(my_str) != 0:
        answer.append(my_str)
    return answer