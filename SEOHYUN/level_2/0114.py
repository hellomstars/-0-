#Finn은 요즘 수학공부에 빠져 있습니다. 수학 공부를 하던 Finn은 자연수 n을 연속한 자연수들로 표현 하는 방법이 여러개라는 사실을 알게 되었습니다. 예를들어 15는 다음과 같이 4가지로 표현 할 수 있습니다.
#1 + 2 + 3 + 4 + 5 = 15
#4 + 5 + 6 = 15
#7 + 8 = 15
#15 = 15
#자연수 n이 매개변수로 주어질 때, 연속된 자연수들로 n을 표현하는 방법의 수를 return하는 solution를 완성해주세요.
#제한사항
#n은 10,000 이하의 자연수 입니다.
def solution(n):
    answer = 0
    for i in range(1, n+1):
        ans_list = 0
        for j in range(i, n+1):
            ans_list += j
            if ans_list == n:
                answer += 1
            elif ans_list > n:
                break
    return answer

'''
다른 사람들은?

def solution(n):
    answer = 0
    for i in range(1, n+1):
        answer += func(i, 0, n)
    return answer
def func(i, total, n):
    if total == n:
        return True
    elif total > n:
        return False
    else:
        return func(i+1, total+i, n)

def solution(n):
    count = 0
    for i in range(1, n + 1):
        nums = []
        j = 0
        while sum(nums) < n:
            nums.append(i + j)
            j += 1
        if sum(nums) == n:
            count += 1
    return count

def solution(n):
    import math
    answer= []
    for k in range(1,n+1):
        if n%k == 0:
            if k%2 !=0:
                answer.append(k)
    return len(answer)
'''