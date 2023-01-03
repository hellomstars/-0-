// 중앙값 구하기

function solution(array) {
    var answer = array.sort((a,b) => a-b);
    let mid = Math.floor(array.length/2)
    return answer[mid];
}

console.log(solution([9, -1, 0]));


const solution2 = (array) =>{
    return array.sort((a,b) => a-b)[Math.floor(array.length/2)]
}

console.log(solution2([9, -1, 0]));
