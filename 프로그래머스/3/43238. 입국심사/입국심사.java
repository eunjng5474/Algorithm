import java.util.*;

class Solution {
    public long solution(int n, int[] times) {
        long answer = Long.MAX_VALUE;
        Arrays.sort(times);
        
        long start = 1;
        long end = (long) times[times.length - 1] * n;
        long mid;
        long num;
        
        while(start <= end) {
            mid = (start + end) / 2;
            num = 0;    // 인원 수 
            
            for(int time : times) {
                num += mid/time;
            }
            
            if(num < n) start = mid + 1;
            else {
                end = mid - 1;
                answer = mid;
            }
        }
        
        return answer;
    }
}