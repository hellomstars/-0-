#정수 n이 주어질 때, n이하의 짝수를 모두 더한 값을 return 하도록 solution 함수를 작성해주세요.

#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

def solution(n) :
    answer = 0
    for i in range(0,n+1,2):
        answer += i
    return print(answer)

#통과 못 함 다시 해야 함 ... 왜? ㅠㅠ