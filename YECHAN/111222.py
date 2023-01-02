#나이 출력
def solution(age):
    answer = 2023-age
    return answer

#각도기
def solution(angle):
    if angle < 90 and angle > 0:
        answer = 1
    elif angle == 90:
        answer = 2
    elif angle > 90 and angle <180:
        answer = 3
    elif angle == 180:
        answer = 4
    return answer

#짝수의 합
def solution(n):
    answer = 0
    if n%2 == 0:
        for i in range(2, n+2, 2):
            answer += i
    
    elif n%2 == 1:
        for i in range(2, n+1, 2):
            answer += i
    return answer

#배열의 평균값
def solution(numbers):
    answer = 0
    for i in numbers:
        answer+=i
    num = answer/ len(numbers)
    return num