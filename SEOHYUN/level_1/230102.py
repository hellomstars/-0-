#두 정수 left와 right가 매개변수로 주어집니다. left부터 right까지의 모든 수들 중에서, 약수의 개수가 짝수인 수는 더하고, 약수의 개수가 홀수인 수는 뺀 수를 return 하도록 solution 함수를 완성해주세요.
def solution(left, right):
    answer = 0
    for i in range(left, right+1):
        cnt = 0
        for j in range(1,i+1):
            if i%j == 0:
                cnt += 1
        if cnt % 2 == 0:
            answer += i
        elif cnt % 2 == 1:
            answer -= i
    return answer

'''
다른 사람들은?

def solution(left, right):
    answer = 0
    for i in range(left,right+1):
        if int(i**0.5)==i**0.5:
            answer -= i
        else:
            answer += i
    return answer

import math
def solution(left, right):
    answer = 0
    for i in range(left, right + 1, 1):
        sqrt = math.sqrt(i)
        if int(sqrt) == sqrt:
            answer -= i
        else:
            answer += i
    return answer
'''