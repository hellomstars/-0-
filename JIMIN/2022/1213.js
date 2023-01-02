function solution(before, after) {
    return before.split('').reverse().join('') == after ? 1 :0;
}

console.log(solution("olleh","hello"));