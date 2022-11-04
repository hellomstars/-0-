#문자열 배열 strlist가 매개변수로 주어집니다. strlist 각 원소의 길이를 담은 배열을 retrun하도록 solution 함수를 완성해주세요.
def solution(strlist):
    answer = []
    for i in strlist:
        answer.append(len(i))
    return answer



#정수 배열 numbers와 정수 num1, num2가 매개변수로 주어질 때, numbers의 num1번 째 인덱스부터 num2번째 인덱스까지 자른 정수 배열을 return 하도록 solution 함수를 완성해보세요.
def solution(numbers, num1, num2):
    answer = []
    for i in range(num1, num2+1):
        answer.append(numbers[i])
    return answer

'''
다른 사람들은?

def solution(numbers, num1, num2):
    return numbers[num1:num2+1]
'''



#머쓱이는 추운 날에도 아이스 아메리카노만 마십니다. 아이스 아메리카노는 한잔에 5,500원입니다. 머쓱이가 가지고 있는 돈 money가 매개변수로 주어질 때, 머쓱이가 최대로 마실 수 있는 아메리카노의 잔 수와 남는 돈을 순서대로 담은 배열을 return 하도록 solution 함수를 완성해보세요.
def solution(money):
    answer = [money // 5500, money - (5500*(money//5500))]
    return answer

'''
다른 사람들은?

def solution(money):

    answer = [money // 5500, money % 5500]
    return answer

def solution(money):
    return divmod(money, 5500)    
'''    



#정수 배열 numbers가 매개변수로 주어집니다. numbers의 원소 중 두 개를 곱해 만들 수 있는 최댓값을 return하도록 solution 함수를 완성해주세요.
def solution(numbers):
    numbers.sort(reverse=True)
    answer = numbers[0]*numbers[1]
    return answer

'''
다른 사람들은?

def solution(numbers):
    num1 = 0
    num2 = 0
    answer = 0

    numbers.sort()

    num1 = numbers.pop()
    num2 = numbers.pop()
    answer = num1 * num2

    return answer

def solution(numbers):
    numbers.sort()
    return numbers[-2] * numbers[-1]
'''    



#문자열 my_string과 문자 letter이 매개변수로 주어집니다. my_string에서 letter를 제거한 문자열을 return하도록 solution 함수를 완성해주세요.
def solution(my_string, letter):
    answer = my_string.replace(letter,"")
    return answer