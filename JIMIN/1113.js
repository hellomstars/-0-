function solution(n, numlist) {
    let answer = [];
    numlist.forEach((item) => {
        if(item % n == 0) answer.push(item);
    });
    return answer;
}

let numlist = [4, 5, 6, 7, 8, 9, 10, 11, 12];
console.log(solution(3,numlist))