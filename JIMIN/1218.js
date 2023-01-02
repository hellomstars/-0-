// 최댓값 만들기 (1)

function solution(numbers) {
    let answer = numbers.sort(function(a,b){
        return b-a;
    })

    return answer[0] * answer[1]
}


console.log(solution([0, 31, 24, 10, 1, 9]));