import java.util.*;

class Solution {
    public int solution(int n, int[][] edge) {
        ArrayList<ArrayList<Integer>> graph = new ArrayList<>();
        for(int i = 0; i < n+1; i ++) {
            graph.add(new ArrayList<>());
        }
        
        // 인덱스에 해당하는 노드와 연결된 노드들 추가(양방향)
        for(int i = 0; i < edge.length; i++) {
            graph.get(edge[i][0]).add(edge[i][1]);
            graph.get(edge[i][1]).add(edge[i][0]);  
        }
        
        int[] visited = new int[n+1];
        
        Queue<Integer> q = new LinkedList<>();
        q.add(1);
        visited[1] = 1;
        
        while(!q.isEmpty()) {
            int now = q.poll();
            for(int i = 0; i < graph.get(now).size(); i++) {
                int next = graph.get(now).get(i);
                // now와 연결된 노드들 순회하면서
                // next에 방문한 적 없으면 이전까지의 거리 + 1해서 저장 후 q에 추가
                
                if(visited[next] == 0) {
                    visited[next] = visited[now] + 1;
                    q.add(next);
                }
            }
        }
        
        int answer = 0;
        int max = 1;
        
        for(int i = 1; i <= n; i++) {
            if(visited[i] > max) {
                max = visited[i];
                answer = 1;
            } else if (visited[i] == max) {
                answer++;
            }
        }
            
        return answer;
        
    }
}