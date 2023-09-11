def solution(before, after):
    # 거꾸로 했을 때 같은 경우가 아닌 순서를 바꿨을 때 같은 경우를 찾는 것
    answer = 0
    after_arr = [s for s in after]
    for val in before:
        if val in after_arr:
            after_arr.pop(after_arr.index(val))
    if len(after_arr) == 0:
        answer = 1
    return answer