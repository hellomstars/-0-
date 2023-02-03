// A로 B 만들기

function solution(before, after) {
    console.log(after.split('').sort().join(''));
    return before.split('').sort().join('') === after.split('').sort().join('') ? 1 : 0
}

// 참고할 풀이
let solution1=(b,a)=>([...b].sort().join("")==[...a].sort().join(""))+0

console.log(solution1("olleh","hello"));

