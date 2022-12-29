#0부터 9까지의 숫자 중 일부가 들어있는 정수 배열 numbers가 매개변수로 주어집니다. numbers에서 찾을 수 없는 0부터 9까지의 숫자를 모두 찾아 더한 수를 return 하도록 solution 함수를 완성해주세요.
def solution(numbers):
    return 45-sum(numbers)



#단어 s의 가운데 글자를 반환하는 함수, solution을 만들어 보세요. 단어의 길이가 짝수라면 가운데 두글자를 반환하면 됩니다.
def solution(s):
    answer = ''
    i = len(s)//2
    if len(s)%2 ==1 :
        answer = s[i]
    else :
        answer = s[i-1]+s[i]
    return answer

'''
다른 사람들은?

return str[(len(s)-1)//2:len(s)//2+1]
'''



#길이가 n이고, "수박수박수박수...."와 같은 패턴을 유지하는 문자열을 리턴하는 함수, solution을 완성하세요. 예를들어 n이 4이면 "수박수박"을 리턴하고 3이라면 "수박수"를 리턴하면 됩니다.
def solution(n):
    if n%2 == 0:
        answer = "수박"*(n//2)
    else :
        answer = "수박"*(n//2)+"수"
    return answer