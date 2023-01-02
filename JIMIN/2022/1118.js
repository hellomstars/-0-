function solution(numbers) {
    let answer = []
    numbers.forEach((item) => {
        item *= 2;
        answer.push(item);
    });
    return answer
}

let numbers = [2, 4, 6, 8, 10];
console.log(solution(numbers));
