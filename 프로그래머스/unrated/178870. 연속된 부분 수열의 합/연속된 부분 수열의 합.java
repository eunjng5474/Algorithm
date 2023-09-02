class Solution {
    public int[] solution(int[] sequence, int k) {
        int n = sequence.length;
        int sum = 0;
        int r = 0;
        int minLength = n + 1;
        
        int left = 0;
        int right = 0;
        
        for(int l = 0; l < n; l++) {
            while(r < n && sum < k) {
                sum += sequence[r];
                r++;
            }
            
            if(sum == k) {
                if(r - l < minLength) {
                    left = l;
                    right = r - 1;
                    minLength = r - l;
                }
            }
            sum -= sequence[l];
        }
        
        int[] answer = {left, right};
        return answer;
    }
}