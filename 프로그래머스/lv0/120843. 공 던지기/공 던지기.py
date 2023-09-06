def solution(numbers, k):
    idx = 0
    while k != 1:
        k -= 1
        idx += 2
        if idx >= len(numbers):
            idx = idx % len(numbers) 
    return numbers[idx]