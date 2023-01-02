//369게임

function solution(order) {
    return order.toString().split('').filter(v => v%3 ==0 && v%10 !==0 ).length;
}

console.log(solution(29423));