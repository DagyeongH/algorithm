def solution(nums):
    s = set(nums)
    answer = len(s) if len(s) < len(nums)//2 else len(nums)//2
    return answer