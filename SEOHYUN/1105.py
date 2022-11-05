#x 좌표 (x, y)를 차례대로 담은 정수 배열 dot이 매개변수로 주어집니다. 좌표 dot이 사분면 중 어디에 속하는지 1, 2, 3, 4 중 하나를 return 하도록 solution 함수를 완성해주세요.
def solution(dot):
    answer = 0
    if dot[0]>0 and dot[1]>0:
        answer = 1
    elif dot[0]<0 and dot[1]>0:
        answer = 2
    elif dot[0]<0 and dot[1]<0:
        answer = 3
    elif dot[0]>0 and dot[1]<0 :
        answer = 4
    return answer

'''
다른 사람들은?

def solution(dot):
    answer = 0
    if dot[0] > 0:
        if dot[1] > 0:
            answer = 1
        else:
            answer = 4
    else:
        if dot[1] > 0:
            answer = 2
        else:
            answer = 3
    return answer

def solution(dot):
    quad = [(3,2),(4,1)]
    return quad[dot[0] > 0][dot[1] > 0]
'''



#문자열 str1, str2가 매개변수로 주어집니다. str1 안에 str2가 있다면 1을 없다면 2를 return하도록 solution 함수를 완성해주세요.
def solution(str1, str2):
    answer = 0
    if str2 in str1:
        answer = 1
    else :
        answer = 2
    return answer



#어떤 자연수를 제곱했을 때 나오는 정수를 제곱수라고 합니다. 정수 n이 매개변수로 주어질 때, n이 제곱수라면 1을 아니라면 2를 return하도록 solution 함수를 완성해주세요.
def solution(n):
    answer = 0
    if n**(1/2) == int(n**(1/2)):
        answer = 1
    else:
        answer = 2
    return answer

'''
다른 사람들은?

from math import sqrt

def solution(n):
    if int(sqrt(n))**2 == n:
        return 1
    else:
        return 2
'''



#머쓱이네 옷가게는 10만 원 이상 사면 5%, 30만 원 이상 사면 10%, 50만 원 이상 사면 20%를 할인해줍니다.
#구매한 옷의 가격 price가 주어질 때, 지불해야 할 금액을 return 하도록 solution 함수를 완성해보세요.
def solution(price):
    answer = 0
    if price >500000 or price == 500000:
        answer = int(price*0.8)
    elif price >300000 or price == 300000:
        answer = int(price*0.9)
    elif price >100000 or price == 100000:
        answer = int(price*0.95)
    else :
        answer = price
    return answer

'''
다른 사람들은?

def solution(price):
    discount_rates = {500000: 0.8, 300000: 0.9, 100000: 0.95, 0: 1}
    for discount_price, discount_rate in discount_rates.items():
        if price >= discount_price:
            return int(price * discount_rate)
'''



#정수 n이 매개변수로 주어질 때 n의 각 자리 숫자의 합을 return하도록 solution 함수를 완성해주세요
def solution(n):
    answer = sum(map(int, str(n)))
    return answer

'''
다른 사람들은?

def solution(n):
    return sum(int(i) for i in str(n))
'''


#문자열 my_string과 정수 n이 매개변수로 주어질 때, my_string에 들어있는 각 문자를 n만큼 반복한 문자열을 return 하도록 solution 함수를 완성해보세요.
def solution(my_string, n):
    answer = ''
    a = []
    a = list(my_string)
    for i in a:
        answer += str(i)*n
    return str(answer)

'''
다른 사람들은?

def solution(my_string, n):
    return ''.join(i*n for i in my_string)

def solution(my_string, n):
    answer = ''
    for s in my_string:
        answer += s * n
    return answer
'''



#두 배열이 얼마나 유사한지 확인해보려고 합니다. 문자열 배열 s1과 s2가 주어질 때 같은 원소의 개수를 return하도록 solution 함수를 완성해주세요.
def solution(s1, s2):
    answer = 0
    for i in s1:
        for j in s2:
            if i == j:
                answer += 1
    return answer

'''
다른 사람들은?

def solution(s1, s2):
    return len(set(s1)&set(s2));
'''    



#어떤 세균은 1시간에 두배만큼 증식한다고 합니다. 처음 세균의 마리수 n과 경과한 시간 t가 매개변수로 주어질 때 t시간 후 세균의 수를 return하도록 solution 함수를 완성해주세요.
def solution(n, t):
    answer = n*(2**t)
    return answer

'''
다른 사람들은?

def solution(n, t):
    return n << t
'''



#순서쌍이란 두 개의 숫자를 순서를 정하여 짝지어 나타낸 쌍으로 (a, b)로 표기합니다. 자연수 n이 매개변수로 주어질 때 두 숫자의 곱이 n인 자연수 순서쌍의 개수를 return하도록 solution 함수를 완성해주세요.
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n//i * i == n:
            answer += 1
    return answer

'''
다른 사람들은?

def solution(n):
    return len(list(filter(lambda v: n % (v+1) == 0, range(n))))
'''