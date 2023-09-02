def solution(score):
    answer = []
    score_mean = [sum(sco) / len(sco) for sco in score]
    score_mean_sort = sorted(score_mean, reverse=True)
    
    # 평균값을 내림차순으로 정렬한 리스트에서 평균값과 같은 인덱스를 찾아서 반환
    for val in score_mean:
        answer.append(score_mean_sort.index(val)+1)
        
    return answer