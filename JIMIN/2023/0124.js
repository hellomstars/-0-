// 가위 바위 보


function solution(rsp) {
    let answer = [];
    rsp .split('')
        .map((v) => {
            if (v == '2') answer.push(0);
            else if (v == '0') answer.push(5);
            else answer.push(2);
    });
    return answer.join('')

}

console.log(solution('205'))