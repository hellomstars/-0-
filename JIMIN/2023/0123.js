// 암호 해독


function solution(cipher, code) {
    var result = [];
    var answer = cipher.split('');
    for(let i=1; i<=cipher.length; i++){     
        result.push(answer[code*i-1])
    }

    return result.join('');
}

//더 간결하게
function solution2(cipher, code){
    return cipher.split('').filter((v, idx) => (idx+1)%code === 0).join('');
}


console.log(solution("dfjardstddetckdaccccdegk",4));
console.log(solution2("dfjardstddetckdaccccdegk",4));