#양꼬치
def solution(n, k):
    return n*12000 + ((k-(n//10))*2000)

#머쓱이보다 키 큰 사람
def solution(array, height):
    taller = []
    for i in range(len(array)):
        if array[i] > height:
            taller.append(array[i])
    return len(taller)

#중복된 숫자 갯수
def solution(array, n):
    return array.count(n)

#피자 나눠 먹기(1)
def solution(n):
    if n%7 > 0:
        return n//7+1
    else:
        return n//7