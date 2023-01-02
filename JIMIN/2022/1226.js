// 숨어있는 숫자의 덧셈 (1)

function solution(my_string) {
    return my_string.split('').filter(v => Number(v)).map(Number).reduce((a,b) => a+b)
}

console.log(solution('1a2b3c4d123'));