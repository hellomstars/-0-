// 짝수 홀수 개수
function solution(num_list) {
    return [
    num_list.filter(v =>v%2 == 0).length,
    num_list.filter(v =>v%2 != 0).length
    ]
} 
