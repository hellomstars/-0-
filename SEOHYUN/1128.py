#정수 n을 기준으로 n과 가까운 수부터 정렬하려고 합니다. 이때 n으로부터의 거리가 같다면 더 큰 수를 앞에 오도록 배치합니다. 정수가 담긴 배열 numlist와 정수 n이 주어질 때 numlist의 원소를 n으로부터 가까운 순서대로 정렬한 배열을 return하도록 solution 함수를 완성해주세요.
def solution(numlist, n):
    answer = [numlist[0]]
    
    for i in numlist[1:]:

        if abs(i-n) < abs(answer[0]-n):
            answer.insert(0, i)
        elif abs(i-n) == abs(answer[0]-n):
            if i > answer[0]:
                answer.insert(0, i)
            else :
                answer.insert(1, i)

        else :
            for j in range(len(answer)):
                if abs(i-n) == abs(answer[j]-n):
                    if i > answer[j]:
                        answer.insert(j,i)
                        break
                    else :
                        answer.insert(j+1,i)
                        break
                elif abs(i-n) < abs(answer[j]-n):
                    answer.insert(j,i)
                    break
                elif abs(i-n) > abs(answer[-1]-n):
                    answer.append(i)

    return answer

'''
다른 사람들은?

def solution(numlist, n):
    answer = sorted(numlist,key = lambda x : (abs(x-n), n-x))
    return answer

def solution(numlist, n):
    return sorted(numlist,key = lambda x: [abs(x-n),-x])
'''