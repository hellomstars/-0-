// 세균 증식 

function solution(n, t) {
    return new Array(t).fill(n).reduce((v) => v*2,n);
}

console.log(solution(7,15));