def solution(num_list, n):
    answer = []
    
    # 2차원 배열 안에 들어갈 배열
    l = []
    for num in num_list:
        l.append(num)
        if len(l) == n:
            answer.append(l)
            l = []  # 길이만큼 초기화되면 answer에 추가 후 초기화
    return answer