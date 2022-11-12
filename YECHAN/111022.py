#1
def solution(num1, num2):
    answer = num1 %num2
    return answer

#2
def solution(array):
    num = int(len(array)/2)
    array.sort()
    answer = array[num]
    return answer

#3
def solution(array):
    new_array = list(sorted(set(array)))
    cnt_num=[]   
    for i in range(len(new_array)):
        cnt=0
        for j in range(len(array)):
            if array[j] == new_array[i]:
                cnt+=1
        cnt_num.append(cnt)

    cnt_max = max(cnt_num)
    
    cnt = 0
    for i in range(len(cnt_num)):
        if cnt_max == cnt_num[i]:
            cnt += 1

    if cnt > 1: 
        return -1
    
    elif cnt == 1:
        return new_array[cnt_num.index(cnt_max)]

#3_others
def solution(array):
    while len(array) != 0:
        for i, a in enumerate(set(array)):
            array.remove(a) 

        if i == 0: 
            return a
    
    return -1

#enumerate()은 인덱스와 같이 값을 출력하는 것.

#4
def solution(n):
    if n % 2 == 1:
        n = n + 1
    
    answer = []
    for i in range(1,int(n/2)+1):
        answer.append(i*2-1)
        
    return answer

#4_others
def solution(n):
    return [i for i in range(1, n+1, 2)]

메롱