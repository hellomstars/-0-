#문자열 my_string이 매개변수로 주어질 때, 대문자는 소문자로 소문자는 대문자로 변환한 문자열을 return하도록 solution 함수를 완성해주세요.
def solution(my_string):
    answer = ''
    for i in my_string:
        if i.isupper():
            answer += i.lower()
        else :
            answer += i.upper()
    return answer

'''
다른 사람들은?

def solution(my_string):
    return ''.join([x.lower() if x.isupper() else x.upper() for x in my_string])
'''



#"*"의 높이와 너비를 1이라고 했을 때, "*"을 이용해 직각 이등변 삼각형을 그리려고합니다. 정수 n 이 주어지면 높이와 너비가 n 인 직각 이등변 삼각형을 출력하도록 코드를 작성해보세요.
n = int(input())

for i in range(1,n+1):
    print('*'*i)

'''
다른 사람들은?

n = int(input())
print("\n".join(["*" * (i+1) for i in range(n)]))
'''



#가위는 2 바위는 0 보는 5로 표현합니다. 가위 바위 보를 내는 순서대로 나타낸 문자열 rsp가 매개변수로 주어질 때, rsp에 저장된 가위 바위 보를 모두 이기는 경우를 순서대로 나타낸 문자열을 return하도록 solution 함수를 완성해보세요.
def solution(rsp):
    answer = ''
    for i in rsp:
        if i == '2' : answer += '0'
        elif i == '0' : answer += '5'
        elif i == '5' : answer += '2'
    return answer

'''
다른 사람들은?

def solution(rsp):
    d = {'0':'5','2':'0','5':'2'}
    return ''.join(d[i] for i in rsp)

def solution(rsp):
    win_rsp = {"2": "0", "0": "5", "5": "2"}
    return "".join(map(lambda v: win_rsp[v], rsp))

def solution(rsp):
    rsp =rsp.replace('2','s')
    rsp =rsp.replace('5','p')
    rsp =rsp.replace('0','r')
    rsp =rsp.replace('r','5')
    rsp =rsp.replace('s','0')
    rsp =rsp.replace('p','2')
    return rsp
'''



#머쓱이는 직육면체 모양의 상자를 하나 가지고 있는데 이 상자에 정육면체 모양의 주사위를 최대한 많이 채우고 싶습니다. 상자의 가로, 세로, 높이가 저장되어있는 배열 box와 주사위 모서리의 길이 정수 n이 매개변수로 주어졌을 때, 상자에 들어갈 수 있는 주사위의 최대 개수를 return 하도록 solution 함수를 완성해주세요.
def solution(box, n):
    answer = []
    for i in box:
        answer.append(i//n)
    return answer[0]*answer[1]*answer[2]



#영어 대소문자로 이루어진 문자열 my_string이 매개변수로 주어질 때, my_string을 모두 소문자로 바꾸고 알파벳 순서대로 정렬한 문자열을 return 하도록 solution 함수를 완성해보세요.
def solution(my_string):
    return "".join(sorted(my_string.lower()))



#정수가 담긴 배열 numbers와 문자열 direction가 매개변수로 주어집니다. 배열 numbers의 원소를 direction방향으로 한 칸씩 회전시킨 배열을 return하도록 solution 함수를 완성해주세요.
def solution(numbers, direction):
    answer = []
    for i in range(len(numbers)):
        if direction == "right":
            answer.append(numbers[i-1])
        else :
            answer.append(numbers[i-len(numbers)+1])
    return answer

'''
다른 사람들은?

def solution(numbers, direction):
    return [numbers[-1]] + numbers[:-1] if direction == 'right' else numbers[1:] + [numbers[0]]

from collections import deque
def solution(numbers, direction):
    numbers = deque(numbers)
    if direction == 'right':
        numbers.rotate(1)
    else:
        numbers.rotate(-1)
    return list(numbers)

from collections import deque
def solution(numbers, direction):
    queue = deque(numbers)
    if direction == 'right':
        queue.appendleft(queue.pop())
        return list(queue)
    queue.append(queue.popleft())
    return list(queue)
'''



#머쓱이네 피자가게는 피자를 여섯 조각으로 잘라 줍니다. 피자를 나눠먹을 사람의 수 n이 매개변수로 주어질 때, n명이 주문한 피자를 남기지 않고 모두 같은 수의 피자 조각을 먹어야 한다면 최소 몇 판을 시켜야 하는지를 return 하도록 solution 함수를 완성해보세요.
def solution(n):
    answer = []
    for i in range(1,100):
        if (n*i) % 6 == 0 :
            answer.append((n*i)//6)
    return answer[0]

'''
다른 사람들은?

import math
def solution(n):
    return (n * 6) // math.gcd(n, 6) // 6

def solution(n):
    answer = 1
    while answer * 6 % n != 0:
        answer += 1
    return answer
'''