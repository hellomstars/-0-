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

