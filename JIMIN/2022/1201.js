// 특정 문자 제거하기

function solution(my_string, letter) {
    return my_string.split('').filter(v => v!== letter).join('');
}

console.log(solution("BCBdbe", "B"));