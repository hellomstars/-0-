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



#한 개 이상의 항의 합으로 이루어진 식을 다항식이라고 합니다. 다항식을 계산할 때는 동류항끼리 계산해 정리합니다. 덧셈으로 이루어진 다항식 polynomial이 매개변수로 주어질 때, 동류항끼리 더한 결괏값을 문자열로 return 하도록 solution 함수를 완성해보세요. 같은 식이라면 가장 짧은 수식을 return 합니다.
def solution(polynomial):
    answer = ''
    num = 0
    number = 0
    poly_list = polynomial.split()
    print(poly_list)
    for i in poly_list:
        if 'x' in i :
            i.replace('x',' ').strip
            num = num+int(i)
        elif '+' in i:
            continue
        else : 
            number = number+int(i)
    if num != 0:
        if number != 0:
            answer = num+'x + '+number
        else :
            answer = num+'x'
    elif num == 1 :
        if number != 0:
            answer = 'x + '+number
        else :
            answer = 'x'
    else :
        answer = number    
    return answer