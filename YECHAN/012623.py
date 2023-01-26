#문자열 안에 문자열
def solution(str1, str2):
    if str1.find(str2) >= 0:
        return 1
    else:
        return 2

#제곱수 판별하기
def solution(n):
    return 1 if (n**0.5).is_integer() else 2

#개미 군단
def solution(hp):
    ant = [5,3,1]
    cnt = 0
    a = 0
    
    for i in ant:
        a = hp // i
        cnt += a
        hp = hp % i 
        
    return cnt

#모음제거
def solution(my_string):
    mo = ['a', 'e', 'i', 'o', 'u']
    for i in mo:
        my_string = my_string.replace(i, '')
        
    return my_string 