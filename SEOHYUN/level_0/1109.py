#우주여행을 하던 머쓱이는 엔진 고장으로 PROGRAMMERS-962 행성에 불시착하게 됐습니다. 입국심사에서 나이를 말해야 하는데, PROGRAMMERS-962 행성에서는 나이를 알파벳으로 말하고 있습니다. a는 0, b는 1, c는 2, ..., j는 9입니다. 예를 들어 23살은 cd, 51살은 fb로 표현합니다. 나이 age가 매개변수로 주어질 때 PROGRAMMER-962식 나이를 return하도록 solution 함수를 완성해주세요.
def solution(age):
    answer = ''
    num = map(int, str(age))
    for i in num:
        answer += chr(i+65).lower()
    return answer

'''
다른 사람들은?

def solution(age):
    return ''.join([chr(int(i)+97) for i in str(age)])

def solution(age):
    conv = {'0':'a','1':'b','2':'c','3':'d','4':'e'
            ,'5':'f','6':'g','7':'h','8':'i','9':'j'}
    return ''.join(conv[i] for i in str(age))
'''



#정수 num과 k가 매개변수로 주어질 때, num을 이루는 숫자 중에 k가 있으면 num의 그 숫자가 있는 자리 수를 return하고 없으면 -1을 return 하도록 solution 함수를 완성해보세요.
def solution(num, k):
    answer = 0
    slice = list(map(int, str(num)))
    for i in slice:
        if k == i:
            answer = (slice.index(i))+1
    if answer == 0 :
        answer = -1
    return answer

'''
다른 사람들은?

def solution(num, k):
    return -1 if str(k) not in str(num) else str(num).find(str(k)) + 1

def solution(num, k):
    num = list(str(num))
    answer = 0
    try:
        answer = num.index(str(k))+1
    except:
        answer = -1
    return answer
'''



#군 전략가 머쓱이는 전쟁 중 적군이 다음과 같은 암호 체계를 사용한다는 것을 알아냈습니다.
## 암호화된 문자열 cipher를 주고받습니다.
## 그 문자열에서 code의 배수 번째 글자만 진짜 암호입니다.
#문자열 cipher와 정수 code가 매개변수로 주어질 때 해독된 암호 문자열을 return하도록 solution 함수를 완성해주세요.
def solution(cipher, code):
    return cipher[code-1::code]



#문자열 my_string과 정수 num1, num2가 매개변수로 주어질 때, my_string에서 인덱스 num1과 인덱스 num2에 해당하는 문자를 바꾼 문자열을 return 하도록 solution 함수를 완성해보세요.
def solution(my_string, num1, num2):
    my_list = list(my_string)
    tmp = my_list[num1]
    my_list[num1] = my_list[num2]
    my_list[num2] = tmp
    return ''.join(my_list)

'''
다른 사람들은?

def solution(my_string, num1, num2):
    s = list(my_string)
    s[num1],s[num2] = s[num2],s[num1]
    return ''.join(s)
'''



#머쓱이는 친구들과 369게임을 하고 있습니다. 369게임은 1부터 숫자를 하나씩 대며 3, 6, 9가 들어가는 숫자는 숫자 대신 3, 6, 9의 개수만큼 박수를 치는 게임입니다. 머쓱이가 말해야하는 숫자 order가 매개변수로 주어질 때, 머쓱이가 쳐야할 박수 횟수를 return 하도록 solution 함수를 완성해보세요.
def solution(order):
    answer = 0
    reorder = list(map(int, str(order)))
    for i in reorder:
        if i == 3:
            answer += 1
        elif i == 6:
            answer += 1
        elif i == 9:
            answer += 1
    return answer

'''
다른 사람들은?

def solution(order):
    return sum(map(lambda x: str(order).count(str(x)), [3, 6, 9]))

def solution(order):
    result = 0
    for i in range(3, 10, 3):
        result += str(order).count(str(i))
    return result

def solution(order):
    answer = len([1 for ch in str(order) if ch in "369"])
    return answer

def solution(order):
    return len(list(filter(lambda v: int(v) in [3, 6, 9], [int(n) for n in str(order)])))
'''



#머쓱이는 친구에게 모스부호를 이용한 편지를 받았습니다. 그냥은 읽을 수 없어 이를 해독하는 프로그램을 만들려고 합니다. 문자열 letter가 매개변수로 주어질 때, letter를 영어 소문자로 바꾼 문자열을 return 하도록 solution 함수를 완성해보세요.
def solution(letter):
    slice = letter.split()
    morse = { 
    '.-':'a','-...':'b','-.-.':'c','-..':'d','.':'e','..-.':'f',
    '--.':'g','....':'h','..':'i','.---':'j','-.-':'k','.-..':'l',
    '--':'m','-.':'n','---':'o','.--.':'p','--.-':'q','.-.':'r',
    '...':'s','-':'t','..-':'u','...-':'v','.--':'w','-..-':'x',
    '-.--':'y','--..':'z'
    }
    return ''.join(morse[i] for i in slice)

'''
다른 사람들은?

def solution(letter):
    morse = {
        '.-':'a','-...':'b','-.-.':'c','-..':'d','.':'e','..-.':'f',
        '--.':'g','....':'h','..':'i','.---':'j','-.-':'k','.-..':'l',
        '--':'m','-.':'n','---':'o','.--.':'p','--.-':'q','.-.':'r',
        '...':'s','-':'t','..-':'u','...-':'v','.--':'w','-..-':'x',
        '-.--':'y','--..':'z'
    }

    return ''.join([morse[i] for i in letter.split(' ')])
'''