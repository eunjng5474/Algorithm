import java.util.*;

class Solution {
    public String solution(String number, int k) {
        StringBuilder sb = new StringBuilder();
        int idx = 0;
        // 최대값을 추가하고, 그 다음 인덱스부터 탐색하기 위해 인덱스 저장 
        
        for (int i=0; i<number.length()-k; i++) {
            // (number길이 - k)번 만큼 숫자를 추가해야 한다  
            char maxNum = 0;
            for (int j=idx; j<=i+k; j++) {
                // idx부터 i+k번째 값 중 최대값 찾기 
                // 예제3) 0<=i<6 -> 6번 반복
                // i=0, idx=0이면 j는 0부터 4까지 5개의 수 중 최대값 찾기
                // 이 때 j=2일 때 7로 최대값이므로 sb에 7이 추가되고, idx=3
                // 그 다음 i=1일 때 j는 3부터 5까지 중에서 최대값 추가 
                if(number.charAt(j) > maxNum) {
                    maxNum = number.charAt(j);
                    idx = j+1;
                }
            }
            sb.append(maxNum);
        }
        String answer = sb.toString();
        return answer;
    }
}