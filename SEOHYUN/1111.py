#약수의 개수가 세 개 이상인 수를 합성수라고 합니다. 자연수 n이 매개변수로 주어질 때 n이하의 합성수의 개수를 return하도록 solution 함수를 완성해주세요.
def solution(n):
    answer = []
    for i in range(1, n+1):
        cnt = 0
        for j in range(1,i+1):
            if i%j == 0:
                cnt+= 1
        if cnt >= 3:
            answer.append(i)
    return len(answer)

'''
다른 사람들은?

def get_divisors(n):
    return list(filter(lambda v: n % v ==0, range(1, n+1)))
def solution(n):
    return len(list(filter(lambda v: len(get_divisors(v)) >= 3, range(1, n+1))))
'''



#문자열 my_string이 매개변수로 주어집니다. my_string에서 중복된 문자를 제거하고 하나의 문자만 남긴 문자열을 return하도록 solution 함수를 완성해주세요.
def solution(my_string):
    answer = ''.join(dict.fromkeys(my_string))
    return answer

'''
다른 사람들은?

def solution(my_string):
    answer = []
    for i in my_string :
        if answer.count(i) == 0 :
            answer.append(i)
    return ''.join(answer)

def solution(my_string):
    answer = ''
    set_letter = set(my_string)
    for string in my_string:
        if string in set_letter:
            answer += string
            set_letter.remove(string)
    return answer
'''


#정수 배열 num_list와 정수 n이 매개변수로 주어집니다. num_list를 다음 설명과 같이 2차원 배열로 바꿔 return하도록 solution 함수를 완성해주세요.
#num_list가 [1, 2, 3, 4, 5, 6, 7, 8] 로 길이가 8이고 n이 2이므로 num_list를 2 * 4 배열로 다음과 같이 변경합니다. 2차원으로 바꿀 때에는 num_list의 원소들을 앞에서부터 n개씩 나눠 2차원 배열로 변경합니다.
import numpy as np

def solution(num_list, n):
    arr = np.array(num_list)
    answer = arr.reshape((len(arr)//n), n)
    answer = answer.tolist()
    return answer

'''
다른 사람들은?

import numpy as np
def solution(num_list, n):
    li = np.array(num_list).reshape(-1,n)
    return li.tolist()

def solution(num_list, n):
    return [num_list[ix-n:ix] for ix in range(n, len(num_list)+1, n)]
'''



#문자열 before와 after가 매개변수로 주어질 때, before의 순서를 바꾸어 after를 만들 수 있으면 1을, 만들 수 없으면 0을 return 하도록 solution 함수를 완성해보세요.
def solution(before, after):
    answer = 0
    cnt = 0
    for i in before:
        if before.count(i) == after.count(i):
            cnt += 1
    if cnt == len(before) :
        answer = 1
    else :
        answer = 0
    return answer

'''
다른 사람들은?

def solution(before, after):
    return 1 if sorted(before)==sorted(after) else 0
'''



#최빈값은 주어진 값 중에서 가장 자주 나오는 값을 의미합니다. 정수 배열 array가 매개변수로 주어질 때, 최빈값을 return 하도록 solution 함수를 완성해보세요. 최빈값이 여러 개면 -1을 return 합니다.
def solution(array):
    answer = 0
    cnt = []
    for i in array:
        cnt.append(array.count(i))
    if max(cnt)==min(cnt):
        if len(cnt)==1:
            answer = max(cnt)
        else :
            answer = -1
    else:
        answer = max(cnt)
    return answer



#머쓱이는 행운의 숫자 7을 가장 좋아합니다. 정수 배열 array가 매개변수로 주어질 때, 7이 총 몇 개 있는지 return 하도록 solution 함수를 완성해보세요.
def solution(array):
    answer = 0
    rearray = []
    for i in array :
        rearray.append(list(map(int, str(i))))
    for j in rearray:
        for k in range(0,len(j)):
            if 7 == j[k]:
                answer +=1
    return answer

'''
다른 사람들은?

def solution(array):
    return ''.join(map(str, array)).count('7')

def solution(array):
    return str(array).count('7')
'''



#2차원 좌표 평면에 변이 축과 평행한 직사각형이 있습니다. 직사각형 네 꼭짓점의 좌표 [[x1, y1], [x2, y2], [x3, y3], [x4, y4]]가 담겨있는 배열 dots가 매개변수로 주어질 때, 직사각형의 넓이를 return 하도록 solution 함수를 완성해보세요.
def solution(dots):
    x = []
    y = []
    for i in dots:
        x.append(i[0])
    for j in dots:
        y.append(j[1])
    return (max(x) - min(x))*(max(y)-min(y))

'''
다른 사람들은?

def solution(dots):
    return (max(dots)[0] - min(dots)[0])*(max(dots)[1] - min(dots)[1])
'''



#my_string은 "3 + 5"처럼 문자열로 된 수식입니다. 문자열 my_string이 매개변수로 주어질 때, 수식을 계산한 값을 return 하는 solution 함수를 완성해주세요.
def solution(my_string):
    split = my_string.split(' ')
    answer = int(split[0])
    for i in range(1, len(split), 2):
        if split[i] =="+":
            answer += int(split[i+1])
        elif split[i] == "-":
            answer -= int(split[i+1])
    return answer

'''
다른 사람들은?

def solution(my_string):
    return eval(my_string)

def solution(my_string):
    return sum(int(i) for i in my_string.replace(' - ', ' + -').split(' + '))
'''



#최빈값은 주어진 값 중에서 가장 자주 나오는 값을 의미합니다. 정수 배열 array가 매개변수로 주어질 때, 최빈값을 return 하도록 solution 함수를 완성해보세요. 최빈값이 여러 개면 -1을 return 합니다.
def solution(array):
    answer = 0
    cnt = []
    array.sort()
    cnt.append(array.count(array[0]))
    if len(array) != 1:
        for i in range(1, len(array)):
            if array[i] != array[i-1]:
                cnt.append(array.count(array[i]))
        if cnt.count(max(cnt)) >= 2:
            answer = -1
        else :
            for j in array:
                if array.count(j) == max(cnt):
                    answer = j
    else :
        answer = array[0]
    return answer

'''
다른 사람들은?

def solution(array):
    while len(array) != 0:
        for i, a in enumerate(set(array)):
            array.remove(a)
        if i == 0: return a
    return -1

from collections import Counter
def solution(array):
    cnt = Counter(array).items()
    li = sorted(cnt,key=lambda x: -x[1])
    if len(li)==1:
        return li[0][0]
    return li[0][0] if li[0][1]!=li[1][1] else -1

from collections import defaultdict
def solution(array):   
    mode_counts = defaultdict(list)
    for v in set(array):
        mode_counts[array.count(v)].append(v)
    return mode_counts[max(mode_counts)][0] if len(mode_counts[max(mode_counts)]) == 1 else -1
'''