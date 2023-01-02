#선분 세 개로 삼각형을 만들기 위해서는 다음과 같은 조건을 만족해야 합니다.
#가장 긴 변의 길이는 다른 두 변의 길이의 합보다 작아야 합니다.
#삼각형의 두 변의 길이가 담긴 배열 sides이 매개변수로 주어집니다. 나머지 한 변이 될 수 있는 정수의 개수를 return하도록 solution 함수를 완성해주세요.
def solution(sides):
    ans_list = []
    for i in range(1, max(sides)+1):
        if i + min(sides) > max(sides) :
            ans_list.append(i)
    for j in range(max(sides)+1,sum(sides)):
        if j < sum(sides):
            ans_list.append(j)
    return len(ans_list)

'''
다른 사람들은?

def solution(sides):
    return sum(sides) - max(sides) + min(sides) - 1

def solution(sides):
    return len(list(range(abs(sides[0]-sides[1])+1,sum(sides))))

def solution(sides):
    return 2 * min(sides) - 1
'''



#소수점 아래 숫자가 계속되지 않고 유한개인 소수를 유한소수라고 합니다. 분수를 소수로 고칠 때 유한소수로 나타낼 수 있는 분수인지 판별하려고 합니다. 유한소수가 되기 위한 분수의 조건은 다음과 같습니다.
#기약분수로 나타내었을 때, 분모의 소인수가 2와 5만 존재해야 합니다.
#두 정수 a와 b가 매개변수로 주어질 때, a/b가 유한소수이면 1을, 무한소수라면 2를 return하도록 solution 함수를 완성해주세요.
import math

def solution(a, b):
    answer = 0
    ans_list = []
    gdc = math.gcd(a, b)
    b = b/gdc
    if b == 1 :
        answer = 1
    elif a/gdc == 1 :
        for i in range(2, int(2*b)):
            if b%i == 0:
                ans_list.append(i)
            for j in ans_list:
                if j % 2 == 0 or j % 5 == 0 :
                    ans_list.remove(j)
        if len(ans_list)>0:
            answer = 2
        else:
            answer = 1
    else :
        for k in range(2,int(2*b)):
            if b%k == 0:
                ans_list.append(k)
            for l in ans_list:
                if l%2 ==0 or l%5 ==0 :
                    ans_list.remove(l)
            if len(ans_list)>0:
                answer = 2
            else :
                answer = 1
    return answer

'''
다른 사람들은?

from math import gcd
def solution(a, b):
    b //= gcd(a,b)
    while b%2==0:
        b//=2
    while b%5==0:
        b//=5
    return 1 if b==1 else 2

from math import gcd
def solution(a, b):
    b = b / gcd(a, b)
    for i in [2, 5]:
        while not b % i:
            b //= i
    return 1 if b == 1 else 2
'''



#문자열 "hello"에서 각 문자를 오른쪽으로 한 칸씩 밀고 마지막 문자는 맨 앞으로 이동시키면 "ohell"이 됩니다. 이것을 문자열을 민다고 정의한다면 문자열 A와 B가 매개변수로 주어질 때, A를 밀어서 B가 될 수 있다면 몇 번 밀어야 하는지 횟수를 return하고 밀어서 B가 될 수 없으면 -1을 return 하도록 solution 함수를 완성해보세요.
def solution(A, B):
    answer = []
    if A == B :
        return 0
    else :
        for i in range(len(A)):
            if i == 0:
                answer.append(A[-1]+A[0:len(A)-1:1])
            else :
                answer.append(answer[i-1][-1]+answer[i-1][0:len(A)-1:1])
        print(answer)
        for j in range(len(answer)):
            if B == answer[j]:
                return (j+1)
        if B not in answer:
            return -1

'''
다른 사람들은?

solution=lambda a,b:(b*2).find(a)

from collections import deque
def solution(A, B):
    a, b = deque(A), deque(B)
    for cnt in range(0, len(A)):
        if a == b:
            return cnt
        a.rotate(1)
    return -1

def solution(A, B):
    A, B = list(A), list(B)
    for i in range(len(A)):
        if A == B:
            return i
        temp = A.pop()
        A.insert(0, temp)
    return -1
'''