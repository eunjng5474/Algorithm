import java.util.*;

class Solution {
    public int[] solution(int[] answers) {
        int[] ans1 = {1, 2, 3, 4, 5};
        int[] ans2 = {2, 1, 2, 3, 2, 4, 2, 5};
        int[] ans3 = {3, 3, 1, 1, 2, 2, 4, 4, 5, 5};
        
        int cnt1 = 0;
        int cnt2 = 0;
        int cnt3 = 0;
        
        for(int i = 0; i < answers.length; i++) {
            if(answers[i] == ans1[i%5]) cnt1++;
            if(answers[i] == ans2[i%8]) cnt2++;
            if(answers[i] == ans3[i%10]) cnt3++;
        }
        
        int max = Math.max(Math.max(cnt1, cnt2), cnt3);
        
        List<Integer> ans = new ArrayList<>();
        if(cnt1 == max) ans.add(1);
        if(cnt2 == max) ans.add(2);
        if(cnt3 == max) ans.add(3);

        int[] answer = new int[ans.size()];
        for(int i = 0; i < ans.size(); i++) {
            answer[i] = ans.get(i);
        }
        
        return answer;
    }
}