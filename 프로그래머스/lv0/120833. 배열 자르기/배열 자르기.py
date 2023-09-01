def solution(numbers, num1, num2):
    answer = []
    for num in range(num1, num2 + 1):
        answer.append(numbers[num])
    return answer