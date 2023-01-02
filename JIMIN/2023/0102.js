function solution(array) {
    var answer = array.map(v => v+v);
    return answer;
}

console.log(solution([1, 2, 7, 10, 11]));