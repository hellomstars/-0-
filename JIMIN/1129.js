// 머쓱이보다 키 큰 사람

function solution(array, height) {
    var answer = array.filter(v => v> height).length;
    return answer;
}

function solution2(arr, height){
    var answer = 0;
    arr.forEach((item) => {
        if(item > height) answer++;
    });
    return answer;
}
console.log(solution([180, 120, 140], 130));
console.log(solution2([180, 120, 140], 130));