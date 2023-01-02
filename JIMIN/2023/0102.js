function solution(array) {
    var answer = array.sort((a,b) => a-b);
    return  Math.floor((array.reduce((acr, cur) => acr+cur))/array.length);
}

console.log(solution([1, 2, 7, 10, 11]));