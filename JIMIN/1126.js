//자연수 뒤집어 배열로 만들기
const solution =(n) =>{
    return n.toString().split('').reverse('').map(v => parseInt(v,10));
}

console.log(solution(12345));