import java.util.*;

class Solution {
    public int[] solution(String s) {
        int[] answer = {};
        String[] strs = s.replaceAll("[{}]", " ").trim().split(" , ");
        // "[{}]" -> 정규표현식 사용. "{"와 "}" 모두 공백으로 바꿔줌
        // 공백 제거 후 " , "을 기준으로 split
        Arrays.sort(strs, (a, b) -> (a.length() - b.length()));
        // 문자열 길이 순으로 정렬(짧은 것 먼저)
        
        answer = new int[strs.length];
        HashSet<Integer> hs = new HashSet<Integer>();
        
        int i=0;
        for(String str : strs) {
            for(String sr : str.split(",")) {
                int num = Integer.parseInt(sr);
                // str이 2 | 2,1 | 1,2,3 | 2,1,3,4 식으로 되어있으므로
                // ,를 기준으로 split하고 정수로 변환
                if (!hs.contains(num)) {
                    hs.add(num);
                    answer[i++] = num;
                }
            }
        }
            
        return answer;
    }
}