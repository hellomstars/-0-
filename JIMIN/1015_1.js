const solution = (a,b) => {
    let answer = (a / b)*1000;
    return answer;
}

console.time()
console.log(solution(3,2))
console.timeEnd()