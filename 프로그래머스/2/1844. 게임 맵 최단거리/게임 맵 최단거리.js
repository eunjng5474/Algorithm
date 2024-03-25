dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

function solution(maps) {
    var answer = 0;
    let visited = [maps.length];
    for(let i=0; i<maps.length; i++) {
        visited[i] = new Array(maps[0].length).fill(-1);
    }
    
    function bfs(x, y) {
        const q = [];
        q.push([x, y]);
        visited[x][y] = 1
        
        while(q.length !== 0) {
            let [x, y] = q.shift();
            for(let d=0; d<4; d++) {
                let nx = x + dx[d];
                let ny = y + dy[d];
                
                
                if(nx < 0 || nx >= maps.length || ny < 0 || ny >= maps[0].length) continue;
                if(maps[nx][ny] == 1 && visited[nx][ny] == -1) {
                    visited[nx][ny] = visited[x][y] + 1;
                    q.push([nx, ny]);
                }
            }
        }
    }
        
        
    bfs(0, 0);
    answer = visited[maps.length - 1][maps[0].length -1]
    return answer;
}