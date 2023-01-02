#정수 n이 주어질 때, n이하의 짝수를 모두 더한 값을 return 하도록 solution 함수를 작성해주세요.

def solution(n) :
    answer = 0
    for i in range(0,n+1,2):
        answer += i
    return print(answer)

'''
다른 사람들은?

def solution(n):
  return sum([i for i in range(2, n + 1, 2)])
'''



#머쓱이는 40살인 선생님이 몇 년도에 태어났는지 궁금해졌습니다. 나이 age가 주어질 때, 2022년을 기준 출생 연도를 return 하는 solution 함수를 완성해주세요.
def solution(age):
    answer = 0
    answer = 2022-age+1
    return answer



# 각에서 0도 초과 90도 미만은 예각, 90도는 직각, 90도 초과 180도 미만은 둔각 180도는 평각으로 분류합니다. 각 angle이 매개변수로 주어질 때 예각일 때 1, 직각일 때 2, 둔각일 때 3, 평각일 때 4를 return하도록 solution 함수를 완성해주세요.
def solution(angle):
    if angle > 0 and angle < 90:
        return 1
    elif angle == 90:
        return 2
    elif angle > 90 and angle < 180:
        return 3
    elif angle == 180:
        return 4 

'''
다른 사람들은?

def solution(angle):
    answer = (angle // 90) * 2 + (angle % 90 > 0) * 1
    return answer
'''



#머쓱이네 양꼬치 가게는 10인분을 먹으면 음료수 하나를 서비스로 줍니다. 양꼬치는 1인분에 12,000원, 음료수는 2,000원입니다. 정수 n과 k가 매개변수로 주어졌을 때, 양꼬치 n인분과 음료수 k개를 먹었다면 총얼마를 지불해야 하는지 return 하도록 solution 함수를 완성해보세요.
def solution(n, k):
    answer = n*12000+(k-int(n/10))*2000
    return answer

'''
다른 사람들은?

def solution(n, k):
    return 12000 * n + 2000 * (k - n // 10)
'''