import java.util.*;

class Solution {
    public int solution(int[] A, int[] B) {
        int answer = 0;
        Arrays.sort(A);
        Arrays.sort(B);
        int idx = 0;
        
        for(int b : B) {
            if(b > A[idx]) {
                answer++;
                idx++;
            }
        }
        
        return answer;
    }
}