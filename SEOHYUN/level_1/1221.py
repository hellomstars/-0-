#임의의 양의 정수 n에 대해, n이 어떤 양의 정수 x의 제곱인지 아닌지 판단하려 합니다.
#n이 양의 정수 x의 제곱이라면 x+1의 제곱을 리턴하고, n이 양의 정수 x의 제곱이 아니라면 -1을 리턴하는 함수를 완성하세요.

import math

def solution(n):
    if int(math.sqrt(n))*int(math.sqrt(n)) == n :
        answer = (math.sqrt(n)+1)**2
    else :
        answer = -1
    return answer



#대문자와 소문자가 섞여있는 문자열 s가 주어집니다. s에 'p'의 개수와 'y'의 개수를 비교해 같으면 True, 다르면 False를 return 하는 solution를 완성하세요. 'p', 'y' 모두 하나도 없는 경우는 항상 True를 리턴합니다. 단, 개수를 비교할 때 대문자와 소문자는 구별하지 않습니다.
#예를 들어 s가 "pPoooyY"면 true를 return하고 "Pyy"라면 false를 return합니다.
def solution(s):
    p_num=0
    y_num=0
    for i in s:
        if i == "p" or i =="P":
            p_num +=1
        elif i == "y" or i == "Y":
            y_num +=1
    if p_num == y_num:
        return True
    else :
        return False

'''
다른 사람들은?

def solution(s):
    s= s.lower()
    return False if s.count('p')!=s.count('y') else True
'''