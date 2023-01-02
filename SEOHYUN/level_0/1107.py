#문자열 my_string이 매개변수로 주어집니다. my_string안의 모든 자연수들의 합을 return하도록 solution 함수를 완성해주세요.
import re

def solution(my_string):
    answer = 0
    num = 0
    num = re.sub(r'[^0-9]', '', my_string)
    for i in num:
        answer = answer+int(i)
    return answer

'''
다른 사람들은?

def solution(my_string):
    return sum(int(i) for i in my_string if i.isdigit())

def solution(my_string):
    answer = 0
    for c in my_string:
        if c.isnumeric():
            answer += int(c)
    return answer
'''



#개미 군단이 사냥을 나가려고 합니다. 개미군단은 사냥감의 체력에 딱 맞는 병력을 데리고 나가려고 합니다. 장군개미는 5의 공격력을, 병정개미는 3의 공격력을 일개미는 1의 공격력을 가지고 있습니다. 예를 들어 체력 23의 여치를 사냥하려고 할 때, 일개미 23마리를 데리고 가도 되지만, 장군개미 네 마리와 병정개미 한 마리를 데리고 간다면 더 적은 병력으로 사냥할 수 있습니다. 사냥감의 체력 hp가 매개변수로 주어질 때, 사냥감의 체력에 딱 맞게 최소한의 병력을 구성하려면 몇 마리의 개미가 필요한지를 return하도록 solution 함수를 완성해주세요.
def solution(hp):
    j = 0
    b = 0
    i = 0
    
    j = hp//5
    if (hp%5)//3 != 0 :
        b = (hp%5)//3
        i = (hp%5)%3
    else :
        i = (hp%5)
    return j+b+i

'''
다른 사람들은?

def solution(hp):    
    return hp // 5 + (hp % 5 // 3) + ((hp % 5) % 3)
'''



#문자열 my_string이 매개변수로 주어질 때, my_string 안에 있는 숫자만 골라 오름차순 정렬한 리스트를 return 하도록 solution 함수를 작성해보세요.
def solution(my_string):
    answer = []
    for i in my_string:
        if i.isnumeric():
            answer.append(int(i))
    answer.sort()    
    return answer

'''
다른 사람들은?

def solution(my_string):
    return sorted([int(c) for c in my_string if c.isdigit()])
'''



#정수 n이 매개변수로 주어질 때, n의 약수를 오름차순으로 담은 배열을 return하도록 solution 함수를 완성해주세요.
def solution(n):
    answer = []
    for i in range(1,n+1):
        if n%i == 0:
            answer.append(i)
    return answer

'''
다른 사람들은?

def solution(n):
    return [i for i in range(1,n+1) if n%i==0]
'''



#영어에선 a, e, i, o, u 다섯 가지 알파벳을 모음으로 분류합니다. 문자열 my_string이 매개변수로 주어질 때 모음을 제거한 문자열을 return하도록 solution 함수를 완성해주세요.
import re

def solution(my_string):
    answer = re.sub('[a,e,i,o,u]', '', my_string)
    return answer

'''
다른 사람들은?

def solution(my_string):
    vowels = ['a','e','i','o','u']
    for vowel in vowels:
        my_string = my_string.replace(vowel, '')
    return my_string
'''



#정수 n과 정수 배열 numlist가 매개변수로 주어질 때, numlist에서 n의 배수가 아닌 수들을 제거한 배열을 return하도록 solution 함수를 완성해주세요.
def solution(n, numlist):
    answer = []
    for i in numlist:
        if i%n == 0:
            answer.append(i)
    return answer



#정수 배열 array가 매개변수로 주어질 때, 가장 큰 수와 그 수의 인덱스를 담은 배열을 return 하도록 solution 함수를 완성해보세요.
def solution(array):
    answer = [max(array), array.index(max(array))]
    return answer