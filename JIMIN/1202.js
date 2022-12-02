// k의 개수

function solution(i, j, k) {
    let answer = 0;
    let result=0;
    for (i; i <= j; i++) {
        result=i.toString().split('').filter(v => v == k.toString()); 
        if (result.length > 0) {
            answer++
            //console.log(result)
            for(let results of result){
                console.log(results)
            }
           
        }

        //console.log(i.toString().split(',').filter(v => v == k.toString()))
    }

    return answer
}

console.log(solution(1, 13, 1))