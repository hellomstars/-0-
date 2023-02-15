// 최빈값 구하기

function solution(array) {
    let map = new Map();

    if(array.length ==1) return array[0];

    console.log(array[0]);

    //Map 초기화
    for(let i=0; i<array.length; i++) map.set(i,0);

    for(let i=0; i<array.length; i++){
        map.set(array[i], map.get(array[i])+1);
    }

    let arr = Array.from(map.values());
    console.log(arr);
    let max = Math.max(...arr);

    if(arr.indexOf(max) !== arr.lastIndexOf(max)){
        return -1;
    }else{
        return arr.indexOf(max);
    }

}

let array = [1, 2, 3, 3, 3, 4];
console.log(solution(array));
