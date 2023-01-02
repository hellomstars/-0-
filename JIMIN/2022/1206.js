// 문자열 정렬하기 (1)
function solution(my_string) {
    return my_string.split('').filter(v => v >47 || v<58).sort().map(Number);
}

console.log(solution("hi12392"));