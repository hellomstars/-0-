function solution(n, k) {
    return n * 12000 + (k - Math.floor(n/10)) * 2000
}

console.log('10 이상',solution(64, 6));
console.log('10 미만',solution(3,3));