#문자열 s의 길이가 4 혹은 6이고, 숫자로만 구성돼있는지 확인해주는 함수, solution을 완성하세요. 예를 들어 s가 "a234"이면 False를 리턴하고 "1234"라면 True를 리턴하면 됩니다.
def solution(s):
    if len(s)==4 or len(s)==6:
        if s.isdigit():
            return True
        else :
            return False
    else :
        return False

'''
다른 사람들은?

return s.isdigit() and len(s) in (4, 6)
'''



#새로 생긴 놀이기구는 인기가 매우 많아 줄이 끊이질 않습니다. 이 놀이기구의 원래 이용료는 price원 인데, 놀이기구를 N 번 째 이용한다면 원래 이용료의 N배를 받기로 하였습니다. 즉, 처음 이용료가 100이었다면 2번째에는 200, 3번째에는 300으로 요금이 인상됩니다.
#놀이기구를 count번 타게 되면 현재 자신이 가지고 있는 금액에서 얼마가 모자라는지를 return 하도록 solution 함수를 완성하세요.
#단, 금액이 부족하지 않으면 0을 return 하세요.
def solution(price, money, count):
    addprice = []
    for i in range(1, count+1):
        addprice.append(i*price)
    if sum(addprice)-money < 0 :
        return 0
    else :
        return sum(addprice)-money

'''
다른 사람들은?

return max(0,price*(count+1)*count//2-money)

return abs(min(money - sum([price*i for i in range(1,count+1)]),0))

return answer-money if answer-money >0 else 0
'''



#행렬의 덧셈은 행과 열의 크기가 같은 두 행렬의 같은 행, 같은 열의 값을 서로 더한 결과가 됩니다. 2개의 행렬 arr1과 arr2를 입력받아, 행렬 덧셈의 결과를 반환하는 함수, solution을 완성해주세요.
def solution(arr1, arr2):
    answer = []
    for i in range(len(arr1)):
            answer.append([arr1[i][j] + arr2[i][j] for j in range(len(arr1[i]))])
    return answer

'''
다른 사람들은?

return [list(map(sum, zip(*x))) for x in zip(A, B)]
'''