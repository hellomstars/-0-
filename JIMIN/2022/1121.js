function solution(my_string) {
    var answer = my_string
        .split('')
        .filter(item => item != 'a' && item !='e'&& item !='o'&& item !='i'&& item !='u')
        .join('');
    return answer;
}

let my_string = "nice to meet you";
console.log(solution(my_string))