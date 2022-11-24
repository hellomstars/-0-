#숫자들이 공백으로 구분된 문자열이 주어집니다. 문자열에 있는 숫자를 차례대로 더하려고 합니다. 이 때 “ Z”가 나오면 바로 전에 더했던 숫자를 뺀다는 뜻입니다. 숫자와 “Z”로 이루어진 문자열 s가 주어질 때, 머쓱이가 구한 값을 return 하도록 solution 함수를 완성해보세요.
def solution(s):
    answer = 0
    ans_list = s.split(' ')
    for i in range(len(ans_list)):
        if i == 0 and ans_list[i] == 'Z':
            answer = 0
        elif ans_list[i] != 'Z':
            answer = answer + int(ans_list[i])
        elif ans_list[i] and ans_list[i-1] == 'Z':
            answer = answer - int(ans_list[i-3])
        else :
            answer = answer - int(ans_list[i-1])
    return answer
    # 현재 경우 Z Z Z 세 번 이상 반복되는 경우 실행 안 됨

'''
다른 사람들은?

def solution(s):
    stack = []
    for a in s.split():
        if a != 'Z':
            stack.append(int(a))
        else:
            if stack:
                stack.pop()
    return sum(stack)
'''



#머쓱이는 프로그래머스에 로그인하려고 합니다. 머쓱이가 입력한 아이디와 패스워드가 담긴 배열 id_pw와 회원들의 정보가 담긴 2차원 배열 db가 주어질 때, 다음과 같이 로그인 성공, 실패에 따른 메시지를 return하도록 solution 함수를 완성해주세요.
#아이디와 비밀번호가 모두 일치하는 회원정보가 있으면 "login"을 return합니다.
#로그인이 실패했을 때 아이디가 일치하는 회원이 없다면 “fail”를, 아이디는 일치하지만 비밀번호가 일치하는 회원이 없다면 “wrong pw”를 return 합니다.
def solution(id_pw, db):
    answer = ''
    for i in db:
        if id_pw == i :
            return 'login'
    for a in db:
        dic = {a[0]: a[1]}
        if id_pw[0] in dic and id_pw[1] != dic[id_pw[0]]:
            return "wrong pw"
    return 'fail'

'''
다른 사람들은?

def solution(id_pw, db):
    if db_pw := dict(db).get(id_pw[0]):
        return "login" if db_pw == id_pw[1] else "wrong pw"
    return "fail"

def solution(id_pw, db):
    answer = ''
    a, b = id_pw[0], id_pw[1]
    for pk, pw in db:
        if pk == a and pw == b:
            return "login"
    for pk, pw in db:
        if pk == a:
            return "wrong pw"
    return "fail"

def solution(id_pw, db):
    dic = dict(db)
    if dic.get(id_pw[0],-1) == id_pw[1]:
        return "login"
    elif dic.get(id_pw[0],-1) == -1:
        return "fail"
    else:
        return "wrong pw"
'''