#정수 배열 numbers가 매개변수로 주어집니다. numbers의 원소의 평균값을 return하도록 solution 함수를 완성해주세요.
def solution(numbers):
    answer = 0
    sum = 0
    for i in range(0,len(numbers)):
        sum += numbers[i]
    answer = sum / len(numbers)
    return answer

'''
다른 사람들은?

def solution(numbers):
    return sum(numbers) / len(numbers)

import numpy as np
def solution(numbers):
    return np.mean(numbers)
'''



#정수가 담긴 배열 array와 정수 n이 매개변수로 주어질 때, array에 n이 몇 개 있는 지를 return 하도록 solution 함수를 완성해보세요.
def solution(array, n):
    answer = 0
    for i in range (0,len(array)):
        if n == array[i]:
            answer += 1
    return answer

'''
다른 사람들은?

def solution(array, n):
    return array.count(n)

def solution(array, n):
    count = 0
    for i in array:
        if i==n :
            count +=1
    return count
'''



#머쓱이는 학교에서 키 순으로 줄을 설 때 몇 번째로 서야 하는지 궁금해졌습니다. 머쓱이네 반 친구들의 키가 담긴 정수 배열 array와 머쓱이의 키 height가 매개변수로 주어질 때, 머쓱이보다 키 큰 사람 수를 return 하도록 solution 함수를 완성해보세요.
def solution(array, height):
    answer = 0
    for i in array:
        if height < i:
            answer += 1
    return answer

'''
다른 사람들은?

def solution(array, height):
    return len(list(filter(lambda v: v > height, array)))
'''



#머쓱이는 할머니께 생신 축하 편지를 쓰려고 합니다. 할머니가 보시기 편하도록 글자 한 자 한 자를 가로 2cm 크기로 적으려고 하며, 편지를 가로로만 적을 때, 축하 문구 message를 적기 위해 필요한 편지지의 최소 가로길이를 return 하도록 solution 함수를 완성해주세요.
def solution(message):
    answer = len(message)*2
    return answer