#머쓱이네 피자가게는 피자를 일곱 조각으로 잘라 줍니다. 피자를 나눠먹을 사람의 수 n이 주어질 때, 모든 사람이 피자를 한 조각 이상 먹기 위해 필요한 피자의 수를 return 하는 solution 함수를 완성해보세요.
def solution(n):
    answer = n//7
    if n%7 > 0:
        answer += 1
    return answer



#정수가 담긴 리스트 num_list가 주어질 때, num_list의 원소 중 짝수와 홀수의 개수를 담은 배열을 return 하도록 solution 함수를 완성해보세요.
def solution(num_list):
    answer = [0,0]
    for i in num_list:
        if i % 2 == 0:
            answer[0] += 1
        else :
            answer[1] += 1
    return answer

'''
다른 사람들은?

def solution(num_list):
    div_num_list = list(map(lambda v: v % 2, num_list))
    return [div_num_list.count(0), div_num_list.count(1)]
'''



#정수가 들어 있는 배열 num_list가 매개변수로 주어집니다. num_list의 원소의 순서를 거꾸로 뒤집은 배열을 return하도록 solution 함수를 완성해주세요.
def solution(num_list):
    answer = []
    for i in range(len(num_list)-1,-1,-1):
        answer.append(num_list[i])
    return answer

'''
다른 사람들은?

def solution(num_list):
    return num_list[::-1]

def solution(num_list):
    num_list.reverse()
    return num_list
'''



#문자열 my_string이 매개변수로 주어집니다. my_string을 거꾸로 뒤집은 문자열을 return하도록 solution 함수를 완성해주세요.
def solution(my_string):
    return my_string[::-1]

'''
다른 사람들은?

def solution(my_string):
    answer = ''

    for i in range(len(my_string)-1, -1, -1) :
        answer += my_string[i]
    return answer
'''

#머쓱이네 피자가게는 피자를 두 조각에서 열 조각까지 원하는 조각 수로 잘라줍니다. 피자 조각 수 slice와 피자를 먹는 사람의 수 n이 매개변수로 주어질 때, n명의 사람이 최소 한 조각 이상 피자를 먹으려면 최소 몇 판의 피자를 시켜야 하는지를 return 하도록 solution 함수를 완성해보세요.
def solution(slice, n):
    answer = n//slice
    if n%slice !=0:
        answer += 1
    return answer