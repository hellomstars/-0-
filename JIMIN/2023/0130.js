//문자열 계산하기

function solution(my_string) {
   let answer = Number(my_string.split(' ')[0]);
   let result = my_string.split(' ');
   for(let i=0; i<my_string.length; i++){
        if(result[i] == '+') answer += Number(result[i+1]); //Number(result[i+1])
        else if(result[i] == '-')  answer -= Number(result[i+1]); 
   }
   return answer
}

console.log(solution("3 + 4"))