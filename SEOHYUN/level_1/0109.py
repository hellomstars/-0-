#1부터 입력받은 숫자 n 사이에 있는 소수의 개수를 반환하는 함수, solution을 만들어 보세요.
#소수는 1과 자기 자신으로만 나누어지는 수를 의미합니다.
#1은 소수가 아닙니다.
def solution(n):
    answer = 0
    ans_list = [True]*(n+1)
    for i in range(2, int(n**0.5)+1):
        if ans_list[i]==True:
            for j in range(i+i, n+1, i):
                ans_list[j] = False
    for i in range(2, n+1):
        if ans_list[i]:
            answer+=1
    return answer

'''
다른 사람들은?

* for 문 두 번으로 계산 시 효율성 검증 실패 -> 에라토스테네스의 체 사용해야 한다

def solution(n):
    num=set(range(2,n+1))
    for i in range(2,n+1):
        if i in num:
            num-=set(range(2*i,n+1,i))
    return len(num)

def solution(n):
    answer = 0
    for i in range(2, n+1):
        if i == 2:
            answer += 1
            continue
        for j in range(2, int(i ** (1/2)) + 1):
            if i % j == 0:
                answer -= 1
                break
        answer += 1
    return answer
'''