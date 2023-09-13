class Solution {
    static int answer = 0;
    
    public int solution(int[] numbers, int target) {
        dfs(0, 0, target, numbers);
        return answer;
    }
    
    public void dfs(int idx, int tmp, int target, int[] numbers) {
        if(idx == numbers.length) {
            if(tmp == target) {
                answer++;
            }
        } else {
            dfs(idx+1, tmp+numbers[idx], target, numbers);
            dfs(idx+1, tmp-numbers[idx], target, numbers);
        }
    }
}