import re
def solution(my_string):
    # 정규표현식을 사용하여 숫자가 아닌 값들 모두 공백처리
    pattern = re.compile(r'\D')
    result = pattern.sub(' ', my_string)
    arr = [int(val) for val in result.split()]
    return sum(arr)