//배열의 평균값
function solution(numbers) {
    
    let answer = 0;
    let size = numbers.length;
    numbers.forEach(item => {
        answer += item;
    });
    answer = (answer / size).toFixed(1)
    return answer;
}

let numbers= [89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99];
console.log(solution(numbers));
