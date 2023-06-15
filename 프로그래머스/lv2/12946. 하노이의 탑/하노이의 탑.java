class Solution {
    public int idx = 0;
    public int[][] solution(int n) {
        int num = (int)Math.pow(2, n) - 1;
        int[][] answer = new int[num][2];
        hanoi(n, 1, 3, 2, answer);
        return answer;
    }
    
    
    public void hanoi(int n, int start, int end, int tmp, int[][] answer) {
        if(n == 1) {
            int[] move = new int[] {start, end};
            answer[idx++] = move;
            return;
        }
        
        hanoi(n-1, start, tmp, end, answer);
        answer[idx++] = new int[] {start, end};
        hanoi(n-1, tmp, end, start, answer);
    }
}