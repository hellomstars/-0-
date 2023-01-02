const solution = (a,b) => {
    let answer = Math.floor((a / b)*1000);
    return answer;
}

console.time()
console.log(solution(7,3))
console.timeEnd()