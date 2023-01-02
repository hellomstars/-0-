const solution = (my_string) =>{
  let answer = '';
  for(let x of my_string){
    x == x.toUpperCase()? answer += x.toLowerCase(): answer += x.toUpperCase();
  }
  return answer;
    
}

console.log(solution('cccCCC'));