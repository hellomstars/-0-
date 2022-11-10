const solution = (n, k) => {
    let answer = 0;
    let s = 0;
    if (n >= 10) {
        k -= n / 10;
    }
    answer = n*12000+k*2000;

    return answer;
}

console.log(solution(64, 6));