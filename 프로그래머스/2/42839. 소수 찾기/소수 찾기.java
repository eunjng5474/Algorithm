import java.util.*;

class Solution {
    static ArrayList<Integer> arr = new ArrayList<>();
    static boolean[] used = new boolean[7];
    
    public int solution(String numbers) {
        int answer = 0;
        
        for(int i = 1; i <= numbers.length(); i++) {
            dfs(numbers, "", i);
        }
        
        for(int num : arr) {
            if(check(num)) answer++;
        }
        
        return answer;
    }
    
    public boolean check(int num) {
        if(num < 2) return false;
        for(int i = 2; i < num; i++) {
            if(num % i == 0) return false;
        }
        return true;
    }
    
    public static void dfs(String str, String tmp, int n) {
        if(tmp.length() == n) {
            int num = Integer.parseInt(tmp);
            if(!arr.contains(num)) arr.add(num);
        }
        
        for(int i = 0; i < str.length(); i++) {
            if(!used[i]) {
                used[i] = true;
                tmp += str.charAt(i);
                dfs(str, tmp, n);
                used[i] = false;
                tmp = tmp.substring(0, tmp.length() - 1);
            }
        }
    }
}