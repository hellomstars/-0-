// 삼각형의 완성조건 (1)
function solution(sides) {
    var answer = sides.reduce((a, b) => a + b) - Math.max(...sides) > Math.max(...sides) ? 1 : 2
    return answer;
}
console.log(solution([1, 2, 3]));
console.log(solution([3, 6, 2]));
console.log(solution([199, 72, 222]));