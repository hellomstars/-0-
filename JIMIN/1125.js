function solution(s){
    let p_cnt =0, y_cnt = 0;
    let answer = s.split('');
    answer.forEach((item) => {
        if(item.toUpperCase() == 'P') p_cnt++
        else if (item.toUpperCase() == 'Y') y_cnt++
    });

    if(p_cnt == y_cnt) answer =true;
    else answer =false;


    return answer;
}