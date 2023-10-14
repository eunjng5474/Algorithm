import java.util.*;

class Solution {
    public int[] solution(int[] array, int[][] commands) {
        int[] answer = new int[commands.length];
        int idx = 0;
        
        for(int i = 0; i < commands.length; i++) {
            int n = commands[i][1] - commands[i][0] + 1;
            int[] lst = new int[n];
            int k = 0;
            
            for(int j = commands[i][0]; j <= commands[i][1]; j++) {
                lst[k++] = array[j - 1];
            }
            Arrays.sort(lst);
            answer[idx++] = lst[commands[i][2] - 1];
        }
        
        return answer;
    }
}