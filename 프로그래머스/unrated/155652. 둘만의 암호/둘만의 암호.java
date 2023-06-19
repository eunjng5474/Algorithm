import java.util.*;

class Solution {
    public String solution(String s, String skip, int index) {
        String answer = "";
        
        for(int i=0; i<s.length(); i++) {
            char ch = s.charAt(i);
            int cnt = 0;
            while(cnt < index) {
                ch++;
                if(ch > 'z') {
                    ch -= 26;
                }
                // ch가 skip에 있으면 cnt 증가x 
                if(skip.contains(Character.toString(ch))) {
                    continue;
                }
                cnt++;
            }
            answer += ch;
        }
        return answer;
    }
}