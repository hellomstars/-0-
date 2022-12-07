#3x 마을 사람들은 3을 저주의 숫자라고 생각하기 때문에 3의 배수와 숫자 3을 사용하지 않습니다. 3x 마을 사람들의 숫자는 다음과 같습니다.
#1 > 3 , 2 > 2, 3 > 4, 4 > 5, 5 > 7, 6 > 8, 7 > 10, 8 > 11, 9 > 14, 10 > 16
#정수 n이 매개변수로 주어질 때, n을 3x 마을에서 사용하는 숫자로 바꿔 return하도록 solution 함수를 완성해주세요.
def solution(n):
    answer = 1
    for i in range(1, n):
        answer += 1
        while answer % 3 == 0 or '3' in str(answer):
            answer += 1
    return answer

'''
다른 사람들은?

def is_use_three(number):
    if "3" in str(number):
        return True
    if number % 3 == 0:
        return True
    return False
def solution(n):  
    return list(filter(lambda v: not is_use_three(v), range(200)))[n-1]
'''



#영어 점수와 수학 점수의 평균 점수를 기준으로 학생들의 등수를 매기려고 합니다. 영어 점수와 수학 점수를 담은 2차원 정수 배열 score가 주어질 때, 영어 점수와 수학 점수의 평균을 기준으로 매긴 등수를 담은 배열을 return하도록 solution 함수를 완성해주세요.
def solution(score):
    answer = []
    avg = []
    
    for i in score:
        avg.append(sum(i)/2)
        
    sortavg = sorted(avg, reverse = True)
    
    for j in avg:
        answer.append(sortavg.index(j)+1)
        
    return answer

'''
다른 사람들은?

def solution(score):
    a = sorted([sum(i) for i in score], reverse = True)
    return [a.index(sum(i))+1 for i in score]

def solution(score):
    rank = sorted([sum(s) / 2 for s in score], reverse=True)
    rankDict = {}
    for i, r in enumerate(rank):
        if r not in rankDict.keys():
            rankDict[r] = i + 1
    return [rankDict[sum(s) / 2] for s in score]

from functools import reduce
def solution(score):
    sorted_score = sorted(reduce(lambda x,y:x.append(sum(y)) or x,score,[]),reverse=True)

    return [sorted_score.index(sum(s))+1 for s in score]

def solution(score):
    av = [sum(s) for s in score]
    return [sum([1 if v > mys else 0 for v in av])+1 for mys in av]

def solution(score: list) -> list:
    dict, avg_list = {}, [sum(num) / 2 for num in score]

    for index, avg in enumerate(sorted(avg_list, reverse=True), start=1):
        if avg not in dict:
            dict[avg] = index
    return [dict[avg] for avg in avg_list]
'''