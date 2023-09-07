import java.util.*;

class Solution {
    public int solution(int[][] sizes) {
        int maxX = 0;
        int maxY = 0;
        
        for(int i = 0; i < sizes.length; i++) {
            if(sizes[i][1] > sizes[i][0]) {
                maxX = Math.max(sizes[i][1], maxX);
                maxY = Math.max(sizes[i][0], maxY);
            } else {
                maxX = Math.max(sizes[i][0], maxX);
                maxY = Math.max(sizes[i][1], maxY);
            }
        }
        
        int answer = maxX * maxY;
        
        return answer;
    }
}