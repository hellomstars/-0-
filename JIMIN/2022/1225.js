// 피자 나눠 먹기
const solution = (n) => {
   return n % 7 == 0 ? n/7 : Math.floor(n/7)+1
}

console.log(solution(15))