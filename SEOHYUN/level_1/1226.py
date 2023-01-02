#두 정수 a, b가 주어졌을 때 a와 b 사이에 속한 모든 정수의 합을 리턴하는 함수, solution을 완성하세요.
#예를 들어 a = 3, b = 5인 경우, 3 + 4 + 5 = 12이므로 12를 리턴합니다.
def solution(a, b):
    answer = 0
    if a==b :
        answer = a
    elif a > b :
        for i in range(b,a+1):
            answer += i 
    elif a < b :
        for j in range(a,b+1):
            answer += j
    return answer

'''
다른 사람들은?

return sum(range(a,b+1))
'''



#1937년 Collatz란 사람에 의해 제기된 이 추측은, 주어진 수가 1이 될 때까지 다음 작업을 반복하면, 모든 수를 1로 만들 수 있다는 추측입니다. 작업은 다음과 같습니다.
# 1-1. 입력된 수가 짝수라면 2로 나눕니다. 
# 1-2. 입력된 수가 홀수라면 3을 곱하고 1을 더합니다. 
# 2. 결과로 나온 수에 같은 작업을 1이 될 때까지 반복합니다. 
#예를 들어, 주어진 수가 6이라면 6 → 3 → 10 → 5 → 16 → 8 → 4 → 2 → 1 이 되어 총 8번 만에 1이 됩니다. 위 작업을 몇 번이나 반복해야 하는지 반환하는 함수, solution을 완성해 주세요. 단, 주어진 수가 1인 경우에는 0을, 작업을 500번 반복할 때까지 1이 되지 않는다면 –1을 반환해 주세요.ㄴ대ㅗㅛㅕㅜ
def solution(num):
    answer = []
    while num != 1:
        if num%2 ==0:
            answer.append(num//2)
            num = num//2
        elif num%2  == 1 :
            answer.append((num*3)+1)
            num = (num*3)+1
        elif num == 1:
            return 0
    while len(answer) >= 500:
        return -1
    return len(answer)

'''
다른 사람들은?

for i in range(500):
    num = num / 2 if num % 2 == 0 else num*3 + 1
    if num == 1:
        return i + 1
return -1
'''