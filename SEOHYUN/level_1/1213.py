#정수 n을 입력받아 n의 약수를 모두 더한 값을 리턴하는 함수, solution을 완성해주세요.
def solution(n):
    ans_list = []
    for i in range(1,n+1):
        if n%i ==0:
            ans_list.append(i)
    return sum(ans_list)



#자연수 N이 주어지면, N의 각 자릿수의 합을 구해서 return 하는 solution 함수를 만들어 주세요.
#예를 들어 N = 123이면 1 + 2 + 3 = 6을 return 하면 됩니다.
def solution(n):
    return sum(list(map(int,str(n))))