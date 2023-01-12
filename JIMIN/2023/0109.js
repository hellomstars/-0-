// 편지

function solution(message) {
    return (message.split('').filter(v => v != "").length)*2
}

console.log(solution("I love you~"));