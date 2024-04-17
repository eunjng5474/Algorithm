import java.util.*;

class Solution {
    static ArrayList<Integer>[] graph;
    static int answer = 100;
    
    public int solution(int n, int[][] wires) {
        graph = new ArrayList[n+1];
        for(int i=0; i<n+1; i++) {
            graph[i] = new ArrayList<>();
        }
        
        for(int[] w : wires) {
            int v1 = w[0];
            int v2 = w[1];
            graph[v1].add(v2);
            graph[v2].add(v1);
        }
        
        for(int[] w : wires) {
            int i = w[0];
            int j = w[1];
            
            // wires 순회하면서 연결 하나씩 끊어서 bfs 돌려보기
            int cnt = bfs(n, i, j);
            answer = Math.min(answer, Math.abs(cnt - (n-cnt)));
        }
        
        return answer;
    }
    
    // n, 시작 지점, 자를 전선 번호 
    public int bfs(int n, int start, int cut) {        
        Queue<Integer> q = new LinkedList<>();
        boolean[] visited = new boolean[n+1];
        q.offer(start);
        visited[start] = true;
        int cnt = 1;
        
        while(!q.isEmpty()) {
            int now = q.poll();
            for(int next : graph[now]) {
                // 이미 방문한 곳이거나 자를 곳이면 continue 
                if(visited[next] == true || next == cut) continue;
                q.offer(next);
                visited[next] = true;
                cnt++;
            }
        }
        return cnt;
    }
}