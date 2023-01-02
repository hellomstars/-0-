//중복된 숫자 개수
const solution = (array, n) =>{
    let answer =0;
    array.filter(v => {
        if(v==n) answer++;
    });
    return answer
}


console.log(solution([0, 2, 3, 4],1));
