import java.util.*;

class Solution {
    public int solution(String[] want, int[] number, String[] discount) {
        int answer = 0;
        Map<String, Integer> map = new HashMap<>();
        
        for(int i=0; i<want.length; i++) {
            map.put(want[i], number[i]);
        }
    
        for(int i=0; i<discount.length - 9; i++) {
            Map<String, Integer> tmp = new HashMap<>();
            
            for(int j=i; j<i+10; j++) {
                tmp.put(discount[j], tmp.getOrDefault(discount[j], 0)+1);
            }
            
            boolean flag = true;
            for(String m : map.keySet()) {
                if(map.get(m) != tmp.get(m)) {
                    flag = false;
                    break;
                }
            }
            
            if(flag) answer++;
        }
        
        return answer;
    }
}