//배열의 평균값
function solution1(numbers) {
    
    let answer = 0;
    let size = numbers.length;
    numbers.forEach(item => {
        answer += item;
    });
    answer = (answer / size).toFixed(1)
    return answer;
}

const solution2 = (numbers)=>{
    return numbers.reduce((a,b) => a+b ,0 )/ numbers.length;
}


let numbers= [89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99];
console.log(solution1(numbers));
console.log(solution2(numbers));
