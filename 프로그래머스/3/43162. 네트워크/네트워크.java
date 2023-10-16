class Solution {
    public int solution(int n, int[][] computers) {
        int answer = 0;
        int[] visited = new int[n+1];
        
        for(int i = 0; i < n; i++) {
            if(visited[i] == 0) {
                dfs(computers, i, n, visited);
                answer++;
            }
        }
        
        return answer;
    }
    
    public void dfs(int[][] computers, int idx, int n, int[] visited) {
        visited[idx] = 1;
        
        for(int i = 0; i < n; i++) {
            if(computers[idx][i] == 1 && visited[i] == 0) {
                dfs(computers, i, n, visited);
            }
        }
    }
}