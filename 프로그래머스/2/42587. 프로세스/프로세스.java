import java.util.*;

class Solution {
    public int solution(int[] priorities, int location) {
        int answer = 0;
        PriorityQueue<Integer> pq = new PriorityQueue<>(Collections.reverseOrder());
        for(int p : priorities) {
            pq.offer(p);
        }
        
        while(!pq.isEmpty()) {
            for(int i=0; i<priorities.length; i++) {
                
                if(pq.peek() == priorities[i]) {
                    pq.poll();
                    answer++;
                    
                    if(i == location) return answer;
                }
            }
        }
        
        
        return answer;
    }
}