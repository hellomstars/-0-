#아이스 아메리카노
def solution(money):
    a = money//5500
    return [a, money-a*5500]

#옷가게 할인 받기
def solution(price):
    if (price >= 100000) & (price < 300000):
        price = int(price*0.95)
    elif (price >= 300000) & (price < 500000):
        price = int(price*0.9)
    elif (price >= 500000):
        price = int(price*0.8)
        
    return price

#직각삼각형 출력하기
n = int(input())
for i in range(n):
    print('*' *(i+1))

#문자 반복 출력하기
def solution(my_string, n):
    arr = list(my_string)
    arr2 = []
    for i in arr:
        arr2.append(i*n)
    answer = "".join(arr2)
    return answer

def solution(my_string, n):
    return ''.join(i*n for i in my_string)

#최대값 만들기(1)
def solution(numbers):
    numbers = list(reversed(sorted(numbers)))
    return int(numbers[0])*int(numbers[1])

#특정 문자 제거하기
def solution(my_string, letter):
    arr = list(my_string)
    while letter in arr:
            arr.remove(letter)
    return "".join(arr)

def solution(my_string, letter):
    return my_string.replace(letter, '')

#배열 자르기
def solution(numbers, num1, num2):
    arr = []
    for i in range(num1, num2+1):
        arr.append(numbers[i])
    return arr

def solution(numbers, num1, num2):
    return numbers[num1:num2+1]

#편지
def solution(message):
    answer = list(message)
    return len(answer)*2

#순서쌍의 개수
def solution(n):
    arr = []
    for i in range(1,n+1):
        if (n % i) == 0:
            arr.append(i)
    return len(arr)

#배열의 유사도
def solution(s1, s2):
    cnt = 0
    for i in s1:
        for j in s2:
            if i == j:
                cnt+=1
        return cnt

def solution(s1, s2):
    return len(set(s1)&set(s2))

#자리수 더하기
def solution(n):
    answer = list(str(n))
    a = 0
    for i in answer:
        a += int(i)
    return a


