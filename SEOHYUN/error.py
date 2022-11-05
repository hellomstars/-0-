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
    if check == 1:
        answer = [int(child1+child2), new_num[0]]
    else:
        new_child1 = child1/check
        new_child2 = child2/check
        under = new_num[0]/check
        answer = [int(new_child1+new_child2), int(under)]
    return check, answer


#가장 긴 변의 길이는 다른 두 변의 길이의 합보다 작아야 합니다.
#삼각형의 세 변의 길이가 담긴 배열 sides이 매개변수로 주어집니다. 세 변으로 삼각형을 만들 수 있다면 1, 만들 수 없다면 2를 return하도록 solution 함수를 완성해주세요.
#1 - error 3
def solution(sides):
    answer = 0
    b =[]
    a = max(sides)
    for i in sides:
        if i != a:
            b.append(int(i))
    sum_b = sum(b)
    if a < sum_b:
        answer = 1
    else :
        answer = 2
    return answer

#2 - error 2
def solution(sides):
    answer = 0
    a = 0
    b = []
    for i in range(0,2):
        if sides[i] > sides[i+1]:
            a = sides[i]
        else :
            b.append(sides[i])
            print(b)
    if sides[2] > a :
        b.append(a)
        print(b)
        a = sides[2]
    if a < int(sum(b)):
        answer = 1
    else :
        answer = 2
    return answer