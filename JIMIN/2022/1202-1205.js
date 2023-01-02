// k의 개수

function solution(i, j, k) {
    let answer = 0;  
    for(;i<=j;i++){
        answer += i.toString().split('').filter(v => v==k).length;
    }
    return answer
}

console.log(solution(1, 13, 1))
//console.log(solution(10, 50, 5))