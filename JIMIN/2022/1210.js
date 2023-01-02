// 자릿수 더하기
function solution(n) {
   return n.toString().split('').map(Number).reduce((a,b) => a+b)
}

console.log(solution(930211));