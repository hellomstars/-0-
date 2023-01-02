#String형 배열 seoul의 element중 "Kim"의 위치 x를 찾아, "김서방은 x에 있다"는 String을 반환하는 함수, solution을 완성하세요. seoul에 "Kim"은 오직 한 번만 나타나며 잘못된 값이 입력되는 경우는 없습니다.
def solution(seoul):
    answer = ''
    for i in range(len(seoul)):
        if 'Kim'==seoul[i]:
            answer = '김서방은 '+str(i)+'에 있다'
    return answer

'''
다른 사람들은?

answer = f'김서방은 {i}에 있다'
return ('김서방은 %d에 있다' %seoul.index('Kim'))
return "김서방은 {}에 있다".format(seoul.index('Kim'))
'''



#프로그래머스 모바일은 개인정보 보호를 위해 고지서를 보낼 때 고객들의 전화번호의 일부를 가립니다.
#전화번호가 문자열 phone_number로 주어졌을 때, 전화번호의 뒷 4자리를 제외한 나머지 숫자를 전부 *으로 가린 문자열을 리턴하는 함수, solution을 완성해주세요.
def solution(phone_number):
    return "*"*(len(phone_number)-4)+phone_number[-4:]

'''
다른 사람들은?

p = re.compile(r'\d(?=\d{4})')
return p.sub("*", phone_number, count = 0)
'''



#array의 각 element 중 divisor로 나누어 떨어지는 값을 오름차순으로 정렬한 배열을 반환하는 함수, solution을 작성해주세요.
#divisor로 나누어 떨어지는 element가 하나도 없다면 배열에 -1을 담아 반환하세요.
def solution(arr, divisor):
    answer = []
    for i in arr:
        if i%divisor==0:
            answer.append(i)
            answer.sort()
    if len(answer)==0:
        answer.append(-1)
    return answer

'''
다른 사람들은?

def solution(arr, divisor): return sorted([n for n in arr if n%divisor == 0]) or [-1]
'''



#정수를 저장한 배열, arr 에서 가장 작은 수를 제거한 배열을 리턴하는 함수, solution을 완성해주세요. 단, 리턴하려는 배열이 빈 배열인 경우엔 배열에 -1을 채워 리턴하세요. 예를들어 arr이 [4,3,2,1]인 경우는 [4,3,2]를 리턴 하고, [10]면 [-1]을 리턴 합니다.
def solution(arr) :
    if len(arr)==1 :
        return [-1]
    else :
        arr.remove(min(arr))
    return arr

'''
다른 사람들은?

return [i for i in arr if i > min(arr)]
'''