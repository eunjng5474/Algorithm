import java.util.*;

class Solution {
    public int solution(int[][] maps) {
        int answer = 0;
        int[][] visited = new int[maps.length][maps[0].length];
		
		bfs(maps, visited);
		answer = visited[maps.length-1][maps[0].length-1];
		if(answer==0)
			answer = -1;
        return answer;
    }
    
	static void bfs(int[][] maps, int[][] visited) {
		int[] dx = {-1, 1, 0, 0};
		int[] dy = {0, 0, -1, 1};
		
		visited[0][0] = 1;
		Queue<int[]> q = new LinkedList<>();
		q.add(new int[]{0, 0});
		
		while(!q.isEmpty()) {
			int[] rm = q.remove();
			int x = rm[0];
			int y = rm[1];
			
			for(int d=0; d<4; d++) {
				int nx = x + dx[d];
				int ny = y + dy[d];
				
				if(nx<0 || nx>=maps.length || ny<0 || ny>=maps[0].length)
					continue;
				
				if(visited[nx][ny]==0 && maps[nx][ny]==1) {
					visited[nx][ny] = visited[x][y] + 1;
					q.add(new int[] {nx, ny});
				}
			}
		}
	}
}