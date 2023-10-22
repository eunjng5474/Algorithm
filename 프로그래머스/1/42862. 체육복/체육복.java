import java.util.Arrays;

class Solution {
    public int solution(int n, int[] lost, int[] reserve) {
        int answer = n - lost.length;
        
        Arrays.sort(reserve);
        Arrays.sort(lost);

        // 여벌 중 도난 당함
        for (int i = 0; i < lost.length; i++) {
			for (int j = 0; j < reserve.length; j++) {
				if (lost[i] == reserve[j]) {
					lost[i] = -1;
					reserve[j] = -1;
                    answer++;
                    break;
				}
			}
		}
        
        // 앞뒤로 빌려줌
        for (int i = 0; i < lost.length; i++) {
			for (int j = 0; j < reserve.length; j++) {
				if (lost[i] - 1 == reserve[j] || lost[i] + 1 == reserve[j]) {
					reserve[j] = -1;
                    answer++;
					break;
				}
			}
		}
        
        return answer;
    }
}