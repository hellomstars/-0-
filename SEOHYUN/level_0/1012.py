#정수 num1과 num2가 매개변수로 주어질 때, num1을 num2로 나눈 값에 1,000을 곱한 후 정수 부분을 return 하도록 soltuion 함수를 완성해주세요.
def solution(num1, num2):
    answer = int(num1/num2*1000)
    return answer

#정수 num1과 num2가 매개변수로 주어집니다. 두 수가 같으면 1 다르면 -1을 retrun하도록 solution 함수를 완성해주세요.
def solution(num1, num2):
    if num1==num2 :
        answer = 1
    else :
        answer = -1
    return answer

#첫 번째 분수의 분자와 분모를 뜻하는 denum1, num1, 두 번째 분수의 분자와 분모를 뜻하는 denum2, num2가 매개변수로 주어집니다. 두 분수를 더한 값을 기약 분수로 나타냈을 때 분자와 분모를 순서대로 담은 배열을 return 하도록 solution 함수를 완성해보세요.
new_num = []

def solution(denum1, num1, denum2, num2):
    for i in range(max(num1, num2), num1*num2+1):
        if i%num1==0 and i%num2==0:
            global new_num
            new_num.append(i)
    child1 = denum1*(new_num[0]/num1)
    child2 = denum2*(new_num[0]/num2)
    answer = [child1+child2, new_num[0]]
    return answer


#정수 배열 numbers가 매개변수로 주어집니다. numbers의 각 원소에 두배한 원소를 가진 배열을 return하도록 solution 함수를 완성해주세요.
new_num = []

def solution(numbers):
    for i in range (len(numbers)):
        new_num.append(int(numbers[i]) * 2)
    return new_num