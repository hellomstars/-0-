// 개미 군단

function solution(hp) {
    var answer = 0;
    if( hp!=0){
        answer = Math.floor(hp/5)+Math.floor((hp%5)/3)+Math.floor(((hp%5)%3)/1);
    }else answer =0;
    return answer;
}

console.log(solution(999));