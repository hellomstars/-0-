#1
def solution(num1, num2):
    answer = int(num1/num2*1000)
    return answer

#2
def solution(num1, num2):
    if num1 == num2:
        answer = 1
    else:
        answer = -1
    return answer

#4
number2 = []
def solution(numbers):
    for i in range(len(numbers)):
        number2.append(2*numbers[i])
    return number2