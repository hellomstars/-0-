// 7의 개수
const solution = (arr) =>{
    return arr.toString().split('').filter(v => v=='7').length;
}

console.log(solution([7, 77, 17]));
console.log(solution([10,29]))