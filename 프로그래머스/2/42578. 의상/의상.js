function solution(clothes) {
    var answer = 1;
    let map = new Map();
    clothes.forEach(([name, type]) => {
        if(map.has(type)) {
            map.set(type, map.get(type) + 1);
        } else map.set(type, 1);
    })
    
    map.forEach(value => {
        answer *= value + 1
    })
    
    return answer - 1;
}