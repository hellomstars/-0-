// 숫자 찾기

function solution(num, k) {
   return num.toString().split('').indexOf(k+'') == -1 ? -1 : [...num+''].findIndex((v) => v == k.toString())+1;
}
console.log(solution(29183,0));
