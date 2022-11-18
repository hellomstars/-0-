#소인수분해란 어떤 수를 소수들의 곱으로 표현하는 것입니다. 예를 들어 12를 소인수 분해하면 2 * 2 * 3 으로 나타낼 수 있습니다. 따라서 12의 소인수는 2와 3입니다. 자연수 n이 매개변수로 주어질 때 n의 소인수를 오름차순으로 담은 배열을 return하도록 solution 함수를 완성해주세요.
def solution(n):
    answer = []
    for i in range(2, n+1):
        if n%i == 0:
            answer.append(i)
            
    for j in answer:
        for k in range(2, 10000):
            if j*k in answer:
                answer.remove(j*k)
    return answer

'''
다른 사람들은?

def solution(n):
    answer = []
    d = 2
    while d <= n:
        if n % d == 0:
            n /= d
            if d not in answer:
                answer.append(d)
        else:
            d += 1
    return answer

def solution(n):
    answer = []
    Primes = []
    for i in range(2,n+1):
        for p in Primes:
            if i%p == 0:
                break
        else:
            Primes.append(i)
            if n%i == 0:
                answer.append(i)
    return answer
'''



#문자열 my_str과 n이 매개변수로 주어질 때, my_str을 길이 n씩 잘라서 저장한 배열을 return하도록 solution 함수를 완성해주세요.
def solution(my_str, n):
    answer = []
    for i in range(len(my_str)):
        if n < len(my_str):
            answer.append(my_str[:n])
            my_str = my_str[n:]
    if len(my_str)>0:
        answer.append(my_str)
    return answer

'''
다른 사람들은?

def solution(my_str, n):
    return [my_str[i: i + n] for i in range(0, len(my_str), n)]
'''



#문자열 my_string이 매개변수로 주어집니다. my_string은 소문자, 대문자, 자연수로만 구성되어있습니다. my_string안의 자연수들의 합을 return하도록 solution 함수를 완성해주세요.
import re

def solution(my_string):
    numbers = re.findall(r'\d+', my_string)
    answer = list(map(int, numbers))
    return sum(answer)

'''
다른 사람들은?

def solution(my_string):
    s = ''.join(i if i.isdigit() else ' ' for i in my_string)
    return sum(int(i) for i in s.split())

import re
def solution(my_string):
    return sum([int(i) for i in re.findall(r'[0-9]+', my_string)])

import re
def solution(my_string):
    return sum(map(int, re.findall(r"\d+", my_string)))

'''



#영어가 싫은 머쓱이는 영어로 표기되어있는 숫자를 수로 바꾸려고 합니다. 문자열 numbers가 매개변수로 주어질 때, numbers를 정수로 바꿔 return 하도록 solution 함수를 완성해 주세요.
def solution(numbers):
    numbers = numbers.replace('zero', '0')
    numbers = numbers.replace('one', '1')
    numbers = numbers.replace('two','2')
    numbers = numbers.replace('three', '3')
    numbers = numbers.replace('four', '4')
    numbers = numbers.replace('five', '5')
    numbers = numbers.replace('six', '6')
    numbers = numbers.replace('seven', '7')
    numbers = numbers.replace('eight', '8')
    numbers = numbers.replace('nine', '9')
    numbers = int(''.join(numbers))
    return numbers

'''
다른 사람들은?

def solution(numbers):
    for num, eng in enumerate(["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]):
        numbers = numbers.replace(eng, str(num))
    return int(numbers)

def solution(numbers):
    dic = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    i=0
    for word in dic:
        numbers = numbers.replace(word, str(i))
        i+=1
    return int(numbers)

def solution(numbers):
    r = {'zero': '0', 'one': '1', 'two': '2', 'three': '3', 'four': '4',\
         'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}
    for k in r.keys():
        numbers = numbers.replace(k, r[k])
    return int(numbers)
'''