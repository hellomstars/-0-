#머쓱이는 큰 종이를 1 x 1 크기로 자르려고 합니다. 예를 들어 2 x 2 크기의 종이를 1 x 1 크기로 자르려면 최소 가위질 세 번이 필요합니다.
#정수 M, N이 매개변수로 주어질 때, M x N 크기의 종이를 최소로 가위질 해야하는 횟수를 return 하도록 solution 함수를 완성해보세요.
def solution(M, N):
    return (M-1)+((N-1)*M)



#머쓱이는 구슬을 친구들에게 나누어주려고 합니다. 구슬은 모두 다르게 생겼습니다. 머쓱이가 갖고 있는 구슬의 개수 balls와 친구들에게 나누어 줄 구슬 개수 share이 매개변수로 주어질 때, balls개의 구슬 중 share개의 구슬을 고르는 가능한 모든 경우의 수를 return 하는 solution 함수를 완성해주세요.
import math

def solution(balls, share):
    return math.factorial(balls) / (math.factorial(balls-share)*math.factorial(share))

'''
다른 사람들은?

import math
def solution(balls, share):
    return math.comb(balls, share)
'''



#PROGRAMMERS-962 행성에 불시착한 우주비행사 머쓱이는 외계행성의 언어를 공부하려고 합니다. 알파벳이 담긴 배열 spell과 외계어 사전 dic이 매개변수로 주어집니다. spell에 담긴 알파벳을 한번씩만 모두 사용한 단어가 dic에 존재한다면 1, 존재하지 않는다면 2를 return하도록 solution 함수를 완성해주세요.
def solution(spell, dic):
    answer = 0
    a_list = []
    spell = ''.join(sorted(spell))

    for i in dic:
        dicsort = ''.join(sorted(i))
        if spell == dicsort:
            a_list.append(dicsort)

    if len(a_list) > 0:
        answer = 1
    else:
        answer = 2

    return answer

'''
다른 사람들은?

def solution(spell, dic):
    spell = set(spell) 
    for i in dic:
        if spell.issubset(set(i)):
            return 1 
    return 2

import itertools
def solution(spell, dic):
    return int(bool(list(set(map("".join, list(itertools.permutations(spell)))) & set(dic)))) or 2
'''



#머쓱이는 RPG게임을 하고 있습니다. 게임에는 up, down, left, right 방향키가 있으며 각 키를 누르면 위, 아래, 왼쪽, 오른쪽으로 한 칸씩 이동합니다. 예를 들어 [0,0]에서 up을 누른다면 캐릭터의 좌표는 [0, 1], down을 누른다면 [0, -1], left를 누른다면 [-1, 0], right를 누른다면 [1, 0]입니다. 머쓱이가 입력한 방향키의 배열 keyinput와 맵의 크기 board이 매개변수로 주어집니다. 캐릭터는 항상 [0,0]에서 시작할 때 키 입력이 모두 끝난 뒤에 캐릭터의 좌표 [x, y]를 return하도록 solution 함수를 완성해주세요.
#[0, 0]은 board의 정 중앙에 위치합니다. 예를 들어 board의 가로 크기가 9라면 캐릭터는 왼쪽으로 최대 [-4, 0]까지 오른쪽으로 최대 [4, 0]까지 이동할 수 있습니다.
def solution(keyinput, board):
    x = 0
    y = 0
    
    max_x = board[0]//2
    max_y = board[1]//2

    for i in keyinput:
        if i == "left":
            if x < 0 and x <= -max_x:
                x = -max_x
            else :
                x = x-1
        elif i == "right":
            if x > 0 and x >= max_x:
                x = max_x
            else :
                x = x+1
        elif i == "up":
            if y > 0 and y >= max_y:
                y = max_y
            else :
                y = y+1
        elif i == "down":
            if y < 0 and y <= -max_y:
                y = -max_y
            else :
                y = y-1
        
    return [x, y]

'''
다른 사람들은?

from functools import reduce
def solution(keyinput, board):
    move = {"left": [-1, 0], "right": [1, 0], "up": [0, 1], "down": [0, -1]}
    return reduce(lambda pos, key: [p+m if -(b//2) <= p+m <= b//2 else p for p, m, b in zip(pos, move[key], board)], keyinput, [0,0])

def solution(keyinput, board):
    n = (board[0]-1)//2
    m = (board[1]-1)//2
    result = [0,0]
    for k in keyinput:
        if k == 'left':
            result = [max(-n,result[0]-1),result[1]]
        elif k == 'right':
            result = [min(n,result[0]+1),result[1]]
        elif k == 'up':
            result = [result[0],min(m,result[1]+1)]
        elif k == 'down':
            result = [result[0],max(-m,result[1]-1)]
    return result

def solution(keyinput, board):
    x_lim,y_lim = board[0]//2,board[1]//2
    move = {'left':(-1,0),'right':(1,0),'up':(0,1),'down':(0,-1)}
    x,y = 0,0
    for k in keyinput:
        dx,dy = move[k]
        if abs(x+dx)>x_lim or abs(y+dy)>y_lim:
            continue
        else:
            x,y = x+dx,y+dy
    return [x,y]
'''