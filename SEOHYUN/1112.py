#1부터 13까지의 수에서, 1은 1, 10, 11, 12, 13 이렇게 총 6번 등장합니다. 정수 i, j, k가 매개변수로 주어질 때, i부터 j까지 k가 몇 번 등장하는지 return 하도록 solution 함수를 완성해주세요.
def solution(i, j, k):
    return ''.join(map(str, [x for x in range(i,j+1)])).count(str(k))

'''
다른 사람들은?

def solution(i, j, k):
    answer = sum([ str(i).count(str(k)) for i in range(i,j+1)])
    return answer

def solution(i, j, k):
    return sum(map(lambda v: str(v).count(str(k)), range(i, j+1)))
'''



#i팩토리얼 (i!)은 1부터 i까지 정수의 곱을 의미합니다. 예를들어 5! = 5 * 4 * 3 * 2 * 1 = 120 입니다. 정수 n이 주어질 때 다음 조건을 만족하는 가장 큰 정수 i를 return 하도록 solution 함수를 완성해주세요.
import math

def solution(n):
    answer = 0
    for i in range (1, n+1):
        if math.factorial(i) <= n :
            answer = i
        elif math.factorial(i) > n :
            break
    return answer

'''
다른 사람들은?

from math import factorial

def solution(n):
    k = 10
    while n < factorial(k):
        k -= 1
    return k
'''



#정수 배열 array와 정수 n이 매개변수로 주어질 때, array에 들어있는 정수 중 n과 가장 가까운 수를 return 하도록 solution 함수를 완성해주세요.
def solution(array, n):
    array.sort()
    arr = []
    for i in array:
        arr.append(abs(i-n))
    answer = array[arr.index(min(arr))]
    return answer

'''
다른 사람들은?

solution=lambda a,n:sorted(a,key=lambda x:(abs(x-n),x))[0]

def solution(array, n):
    array.sort()
    answer = [abs(i-n) for i in array].index(min([abs(i-n) for i in array]))
    return array[answer]
'''



#문자열 s가 매개변수로 주어집니다. s에서 한 번만 등장하는 문자를 사전 순으로 정렬한 문자열을 return 하도록 solution 함수를 완성해보세요. 한 번만 등장하는 문자가 없을 경우 빈 문자열을 return 합니다.
def solution(s):
    s = ''.join(sorted(s))
    answer = ''
    for i in s :
        if s.count(i) == 1:
            answer += i
    return answer

'''
다른 사람들은?

def solution(s):
    answer = "".join(sorted([ ch for ch in s if s.count(ch) == 1]))
    return answer
'''