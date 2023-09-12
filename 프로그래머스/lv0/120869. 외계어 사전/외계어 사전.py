def solution(spell, dic):
    answer = 2
    for val in dic:
        if len(val) == len(spell):
            for s in spell:
                if s not in val:
                    answer = 2
                    break
                else:
                    answer = 1
    return answer