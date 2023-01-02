/*
첫 번째 분수의 분자와 분모를 뜻하는 denum1, num1, 
두 번째 분수의 분자와 분모를 뜻하는 denum2, num2가 매개변수로 주어집니다. 
두 분수를 더한 값을 기약 분수로 나타냈을 때 분자와 분모를 순서대로 담은 배열을 return 하도록
solution 함수를 완성해보세요.
*/


function solution(denum1, num1, denum2, num2) {
    var answer = [];
    let bunja = num1 * denum2 + num2 * denum1;
    let bunmo  = num1* num2;
    
    let gcd = (a, b) =>( a% b === 0  ? b : gcd(b, a%b));
    let min = gcd(bunja, bunmo);
    answer.push(bunja/min);
    answer.push(bunmo/min);
    return answer;
}




console.log(solution(1,2,3,4));
console.log(solution(9,2,1,3));
console.log(solution(512,512,512,512));
console.log(solution(3,5,2,4));
console.log(solution(13, 10, 12, 5));
console.log(solution(1,1,1,1));
