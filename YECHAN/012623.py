#문자열 안에 문자열
def solution(str1, str2):
    if str1.find(str2) >= 0:
        return 1
    else:
        return 2

#제곱수 판별하기
def solution(n):
    return 1 if (n**0.5).is_integer() else 2

