#길이가 같은 배열 A, B 두개가 있습니다. 각 배열은 자연수로 이루어져 있습니다.
#배열 A, B에서 각각 한 개의 숫자를 뽑아 두 수를 곱합니다. 이러한 과정을 배열의 길이만큼 반복하며, 두 수를 곱한 값을 누적하여 더합니다. 이때 최종적으로 누적된 값이 최소가 되도록 만드는 것이 목표입니다. (단, 각 배열에서 k번째 숫자를 뽑았다면 다음에 k번째 숫자는 다시 뽑을 수 없습니다.)
#예를 들어 A = [1, 4, 2] , B = [5, 4, 4] 라면
#A에서 첫번째 숫자인 1, B에서 첫번째 숫자인 5를 뽑아 곱하여 더합니다. (누적된 값 : 0 + 5(1x5) = 5)
#A에서 두번째 숫자인 4, B에서 세번째 숫자인 4를 뽑아 곱하여 더합니다. (누적된 값 : 5 + 16(4x4) = 21)
#A에서 세번째 숫자인 2, B에서 두번째 숫자인 4를 뽑아 곱하여 더합니다. (누적된 값 : 21 + 8(2x4) = 29)
#즉, 이 경우가 최소가 되므로 29를 return 합니다.
#배열 A, B가 주어질 때 최종적으로 누적된 최솟값을 return 하는 solution 함수를 완성해 주세요.
#제한사항
#배열 A, B의 크기 : 1,000 이하의 자연수
#배열 A, B의 원소의 크기 : 1,000 이하의 자연수
def solution(A,B):
    answer = 0
    A.sort()
    B.sort()
    for i in A:
        answer += i*B[-1]
        B.pop()
    return answer

'''
다른 사람들은?

return sum(a*b for a, b in zip(sorted(A), sorted(B, reverse = True)))
'''



#괄호가 바르게 짝지어졌다는 것은 '(' 문자로 열렸으면 반드시 짝지어서 ')' 문자로 닫혀야 한다는 뜻입니다. 예를 들어
#"()()" 또는 "(())()" 는 올바른 괄호입니다.
#")()(" 또는 "(()(" 는 올바르지 않은 괄호입니다.
#'(' 또는 ')' 로만 이루어진 문자열 s가 주어졌을 때, 문자열 s가 올바른 괄호이면 true를 return 하고, 올바르지 않은 괄호이면 false를 return 하는 solution 함수를 완성해 주세요.
#제한사항
#문자열 s의 길이 : 100,000 이하의 자연수
#문자열 s는 '(' 또는 ')' 로만 이루어져 있습니다.
def solution(s):
    ans_list = ["("]
    if s[0] ==")":
        return False
    else:
        for i in s[1:]:
            if i=='(':
                ans_list.append(i)
            elif not ans_list or ans_list.pop()!='(':
                return False
        return False if ans_list else True

'''
다른 사람들은?

from collections import deque
def solution(s):
    stack = deque()
    tmp = 0
    for i in s:
        if i == "(":
            stack.append(i)
            tmp += 1
        else:
            if stack:
                stack.pop()
                tmp -= 1
            else:
                return False
    answer = True if tmp == 0 else False
    return answer

def solution(s):
    stack = []
    for string in s:
        stack.append(string)
        if len(stack) >= 2 and stack[-1] == ")" and stack[-2] == "(":
            stack.pop()
            stack.pop()
    return len(stack) == 0
'''