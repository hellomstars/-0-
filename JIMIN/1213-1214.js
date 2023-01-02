// 잘라서 배열로 저장하기

function solution(my_str, n) {
    let str = my_str.split('');
    let answer = [];

    while (str.length > 0) {
        answer.push(str.splice(0, n).join(''));
    }

    return answer;
}
console.log(solution("abcdef123abcdef123", 6));


/*
function solution(my_str, n) {
    let answer =[];
    answer.push(my_str.substring(0,n));
    answer.push(my_str.substring(n,n+n));
    answer.push(my_str.substring(n+n, ));
    return answer;
}
*/