#자연수 n이 매개변수로 주어집니다. n을 3진법 상에서 앞뒤로 뒤집은 후, 이를 다시 10진법으로 표현한 수를 return 하도록 solution 함수를 완성해주세요.
def solution(n):
    answer = ''
    while n>0:
        n, m = divmod(n, 3)
        answer += str(m)
    answer = int(answer, 3)
    return answer

'''
다른 사람들은?

def solution(n):
    tmp = ''
    while n:
        tmp += str(n % 3)
        n = n // 3
    answer = int(tmp, 3)
    return answer

def solution(n):
    answer = ''
    result = 0
    while n >= 1:
        rest = n % 3
        n //= 3
        answer += str(rest)
    i = 0
    for idx in range(len(answer)-1, -1, -1):
        result += int(answer[idx]) * (3**i)
        i += 1
    return result

def solution(n):
    answer = []
    while True:
        n, rest = divmod(n, 3)
        answer.append(rest)

        if n == 0:
            break
    return sum([i * 3**idx for idx, i in enumerate(reversed(answer))])
'''