// 아이스 아메리카노

function solution(money) {
    var answer = [];
    answer.push(Math.floor(money / 5500));
    answer.push(money % 5500);
    return answer;
}

console.log(solution(5500));
