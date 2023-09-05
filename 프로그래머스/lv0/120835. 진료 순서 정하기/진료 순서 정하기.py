def solution(emergency):
    answer = []
    sort_emer = sorted(emergency, reverse = True)
    for val in emergency:
        answer.append(sort_emer.index(val) + 1)
    return answer