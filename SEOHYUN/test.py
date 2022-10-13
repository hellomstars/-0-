#첫 번째 분수의 분자와 분모를 뜻하는 denum1, num1, 두 번째 분수의 분자와 분모를 뜻하는 denum2, num2가 매개변수로 주어집니다. 두 분수를 더한 값을 기약 분수로 나타냈을 때 분자와 분모를 순서대로 담은 배열을 return 하도록 solution 함수를 완성해보세요.
import math

def solution(denum1, num1, denum2, num2):
    for i in range(max(num1, num2), num1*num2+1):
        if i%num1==0 and i%num2==0:
            new_num=[]
            new_num.append(i)
            break
    child1 = denum1*(new_num[0]/num1)
    child2 = denum2*(new_num[0]/num2)
    check = math.gcd(int(child1+child2), new_num[0])
    if check != 1:
        child1 = child1/check
        child2 = child2/check
        new_num.append(check)
    answer = [int(child1+child2), new_num[0]]
    return print(new_num, answer)

solution(1,2,3,4)
solution(9,2,1,3)
solution(2,6,1,3)