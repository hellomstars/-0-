#0과 1로 이루어진 어떤 문자열 x에 대한 이진 변환을 다음과 같이 정의합니다.
#x의 모든 0을 제거합니다.
#x의 길이를 c라고 하면, x를 "c를 2진법으로 표현한 문자열"로 바꿉니다.
#예를 들어, x = "0111010"이라면, x에 이진 변환을 가하면 x = "0111010" -> "1111" -> "100" 이 됩니다.
#0과 1로 이루어진 문자열 s가 매개변수로 주어집니다. s가 "1"이 될 때까지 계속해서 s에 이진 변환을 가했을 때, 이진 변환의 횟수와 변환 과정에서 제거된 모든 0의 개수를 각각 배열에 담아 return 하도록 solution 함수를 완성해주세요.
def solution(s):
    ans_sub = 0
    ans_sum = 0
    while s != 1:
        ans_sum += s.count('0')
        print("0갯수", ans_sum)
        s = s.replace("0","")
        s = len(s)
        print("10진", s)
        s = format(int(s), 'b')
        print("2진", s)
        s = str(s)
        ans_sub += 1
        if len(s) ==1:
            break
    return [ans_sub, ans_sum]

'''
다른 사람들은?

def solution(s):
    a, b = 0, 0
    while s != '1':
        a += 1
        num = s.count('1')
        b += len(s) - num
        s = bin(num)[2:]
    return [a, b]
'''