#머쓱이는 친구들과 동그랗게 서서 공 던지기 게임을 하고 있습니다. 공은 1번부터 던지며 오른쪽으로 한 명을 건너뛰고 그다음 사람에게만 던질 수 있습니다. 친구들의 번호가 들어있는 정수 배열 numbers와 정수 K가 주어질 때, k번째로 공을 던지는 사람의 번호는 무엇인지 return 하도록 solution 함수를 완성해보세요.
def solution(numbers, k):
    answer = 0
    while len(numbers)//2 < k:
        numbers.extend(numbers)
    answer = numbers[2*k-2]
    return answer

'''
다른 사람들은? 

def solution(numbers, k):
    return 2 * (k - 1) % numbers[-1] + 1

def solution(numbers, k):
    return numbers[2 * (k - 1) % len(numbers)]

from collections import deque
def solution(numbers, k):
    array = deque(numbers)
    array.rotate(-(k-1)*2)
    return array[0]
'''



#가장 긴 변의 길이는 다른 두 변의 길이의 합보다 작아야 합니다.
#삼각형의 세 변의 길이가 담긴 배열 sides이 매개변수로 주어집니다. 세 변으로 삼각형을 만들 수 있다면 1, 만들 수 없다면 2를 return하도록 solution 함수를 완성해주세요.
def solution(sides):
    answer = 0
    a = max(sides)
    sides.remove(max(sides))
    if sum(sides) > a:
        answer = 1
    else :
        answer = 2
    return answer

'''
다른 사람들은?

def solution(sides):
    return 1 if max(sides) < (sum(sides) - max(sides)) else 2

def solution(sides):
    sides.sort()
    return 1 if sides[0]+sides[1]>sides[2] else 2
'''



#정수 배열 numbers가 매개변수로 주어집니다. numbers의 원소 중 두 개를 곱해 만들 수 있는 최댓값을 return하도록 solution 함수를 완성해주세요.
def solution(numbers):
    answer = 0
    numbers.sort()
    if numbers[0]*numbers[1] > numbers[-1]*numbers[-2]:
        answer = numbers[0]*numbers[1]
    else :
        answer = numbers[-1]*numbers[-2]
    return answer

'''
다른 사람들은?

def solution(numbers):
    return max([k * j for i, k in enumerate(numbers) for j in numbers[i + 1:]])
'''



#외과의사 머쓱이는 응급실에 온 환자의 응급도를 기준으로 진료 순서를 정하려고 합니다. 정수 배열 emergency가 매개변수로 주어질 때 응급도가 높은 순서대로 진료 순서를 정한 배열을 return하도록 solution 함수를 완성해주세요.
def solution(emergency):
    answer = []
    emlist = []
    emlist.extend(emergency)
    emergency.sort(reverse=True)
    print(emlist)
    print(emergency)
    for i in emlist:
        for j in range(len(emlist)):
            if i == emergency[j]:
                answer.append(j+1)
    return answer

'''
다른 사람들은?

def solution(emergency):
    return [sorted(emergency, reverse=True).index(e) + 1 for e in emergency]
'''