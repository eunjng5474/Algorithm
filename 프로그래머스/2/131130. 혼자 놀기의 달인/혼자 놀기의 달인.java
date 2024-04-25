import java.util.*;

class Solution {
    static List<Integer> arr;
    static boolean[] visited;
    static int cnt;
    
    public int solution(int[] cards) {
        int len = cards.length;
        arr = new ArrayList<>();
        visited = new boolean[len + 1];
        
        for(int i=0; i<len; i++) {
            if(!visited[i+1]) {
                visited[i+1] = true;
                cnt = 1;
                dfs(cards[i], cards);
                arr.add(cnt);
            }
        }
        
        if(arr.size() == 1) return 0;
        
        Collections.sort(arr, Collections.reverseOrder());
        int answer = arr.get(0) * arr.get(1);
        
        return answer;
    }
    
    static void dfs(int now, int[] cards) {
        if(!visited[now]) {
            visited[now] = true;
            cnt++;
            dfs(cards[now-1], cards);
        }
    }
}