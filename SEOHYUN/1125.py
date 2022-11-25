#프로그래머스 치킨은 치킨을 시켜먹으면 한 마리당 쿠폰을 한 장 발급합니다. 쿠폰을 열 장 모으면 치킨을 한 마리 서비스로 받을 수 있고, 서비스 치킨에도 쿠폰이 발급됩니다. 시켜먹은 치킨의 수 chicken이 매개변수로 주어질 때 받을 수 있는 최대 서비스 치킨의 수를 return하도록 solution 함수를 완성해주세요.
def solution(chicken):
    answer = 0
    left = 0
    while chicken >= 10:
        answer = answer + (chicken//10)
        left = (chicken%10) + (chicken//10)
        if left >= 10:
            answer = answer + (left//10)
            left = (left%10) + (left//10)
        chicken = left
    return answer

'''
다른 사람들은?

def solution(chicken):
    answer = (max(chicken,1)-1)//9
    return answer

def solution(chicken):
    answer = 0
    while chicken >= 10:
        chicken, mod = divmod(chicken, 10)
        answer += chicken
        chicken += mod
    return answer

def solution(chicken):
    answer = 0
    coupon = chicken
    while coupon >= 10:
        eaten = coupon//10 
        answer += eaten 
        coupon = coupon%10 + eaten 
    return answer 

def solution(chicken):
    return int(chicken*0.11111111111)
'''