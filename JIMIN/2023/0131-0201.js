// 로그인 성공?

function solution(id_pw, db) {
    let answer = 'fail';
    db.forEach((item) =>{
        if(item[0] == id_pw[0]){
            item[1] == id_pw[1] ? answer = 'login': answer = 'wrong pw';
        }
    });
    return answer;
}

let id_pw = ["meosseugi", "1234"];
let db = [["rardss", "123"], ["yyoom", "1234"], ["meosseugi", "1234"]];
console.log(solution(id_pw, db));
