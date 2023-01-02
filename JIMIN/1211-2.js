//문자 반복 출력하기

function solution(my_string, n) {
    return my_string.split('').map(v => v.repeat(n)).join('');
}

console.log(solution("hello",3));
