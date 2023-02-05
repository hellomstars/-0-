// 숫자 찾기

function solution(num, k) {
   return num.toString().split('').indexOf(k+'') == -1 ? -1 : [...num+''].findIndex((v) => v == k.toString())+1;
}

// pretty
const solution2 = (num,k)=>{ 
    return num.toString().split('').findIndex((v) => v ==k )+1 || -1
}

console.log(solution(29183,0));
console.log(solution2(29183,1));
