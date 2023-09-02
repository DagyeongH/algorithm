def solution(chicken):
    service = chicken // 10
    answer = service
    re_coupon = (chicken % 10) + service
    
    while re_coupon >= 10:
        service = re_coupon // 10
        answer += service
        re_coupon = re_coupon % 10 + service
        
    return answer