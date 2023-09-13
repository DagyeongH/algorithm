def solution(numlist, n):
    answer = []
    numlist = sorted(numlist, reverse=True)
    nums = [abs(val-n) for val in numlist]
    sort_nums = sorted(nums)
    for num in sort_nums:
        answer.append(numlist[nums.index(num)])
        numlist.pop(nums.index(num))
        nums.pop(nums.index(num))
    
    return answer