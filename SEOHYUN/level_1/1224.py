#함수 solution은 정수 x와 자연수 n을 입력 받아, x부터 시작해 x씩 증가하는 숫자를 n개 지니는 리스트를 리턴해야 합니다. 다음 제한 조건을 보고, 조건을 만족하는 함수, solution을 완성해주세요.
def solution(x, n):
    answer = []
    for i in range(n):
        answer.append(x*(i+1))
    return answer



#문자열 s를 숫자로 변환한 결과를 반환하는 함수, solution을 완성하세요.
def solution(s):
    return int(s)



#양의 정수 x가 하샤드 수이려면 x의 자릿수의 합으로 x가 나누어져야 합니다. 예를 들어 18의 자릿수 합은 1+8=9이고, 18은 9로 나누어 떨어지므로 18은 하샤드 수입니다. 자연수 x를 입력받아 x가 하샤드 수인지 아닌지 검사하는 함수, solution을 완성해주세요.
def solution(x):
    x_sum=[]
    for i in range(len(str(x))):
        x_sum.append(int(str(x)[i]))
    if x%sum(x_sum)==0:
        return True
    else :
        return False



#자연수 n이 매개변수로 주어집니다. n을 x로 나눈 나머지가 1이 되도록 하는 가장 작은 자연수 x를 return 하도록 solution 함수를 완성해주세요. 답이 항상 존재함은 증명될 수 있습니다.
def solution(n):
    answer = []
    for i in range(1,n):
        if n%i == 1:
            answer.append(i)
    return answer[0]