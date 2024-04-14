import java.util.*;

class Solution {
    public String solution(String s) {
        StringBuilder sb = new StringBuilder();
        s = s.toLowerCase();
        boolean flag = true;
        
        for(int i=0; i<s.length(); i++) {
            char c = s.charAt(i);
            if(c == ' ') {
                flag = true;
            }
            else if(flag) {
                // 공백 다음인데 문자열이면 대문자로 바꾸고 flag = false 
                c = Character.toUpperCase(c);
                flag = false;
            }
            sb.append(c);
        }
    
        return sb.toString();

    }
}