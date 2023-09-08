def solution(numbers, direction):
    answer = []
    for idx in range(len(numbers)):
        if direction == 'right':
            idx = (idx - 1) % len(numbers)
        elif direction == 'left':
            idx = (idx + 1) % len(numbers)
        answer.append(numbers[idx])
    return answer