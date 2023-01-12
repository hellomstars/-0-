# 세균증식
def solution(n, t):
    return n*(2**t)

# 배열 뒤집기
def solution(num_list): return list(reversed(num_list))

# 짝수 홀수 갯수
def solution(num_list):
    a=[]
    answer=[]
    for i in num_list:
        if i%2 == 0:
            a.append(i)
    answer.append(len(a))
    answer.append(len(num_list)-len(a))
    return answer

# 배열 원소의 길이
def solution(strlist):
    answer = []
    for i in strlist:
        answer.append(len(i))
    return answer

# 점의 위치 구하기
def solution(dot):
    a = 1
    for i in dot:
        a = a * i
    if a > 0 and dot[0] > 0:
        return 1
    elif a > 0 and dot[0] < 0:
        return 3
    elif a < 0 and dot[0] > 0:
        return 4
    else:
        return 2

#피자 나눠먹기(3)
def solution(slice, n):
    cnt = 1
    result = slice
    
    while(n > result):
        cnt += 1
        result = slice * cnt 
        
    return cnt

#삼각형의 완성조건(1)
def solution(sides):
    return 1 if max(sides) < (sum(sides)-max(sides)) else 2

#문자열 뒤집기
def solution(my_string):
    a = list(reversed(my_string))
    return "".join(a)