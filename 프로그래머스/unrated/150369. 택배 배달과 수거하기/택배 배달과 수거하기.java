class Solution {
    public long solution(int cap, int n, int[] deliveries, int[] pickups) {
        long answer = 0;
        
        int deli = 0;
        int pick = 0;
        
        // 먼 곳부터 탐색
        for(int i=n-1; i>=0; i--) {
            deli += deliveries[i];
            pick += pickups[i];
            
            // deli <= 0 && pick <= 0이면 i번째 집은 안 가도 됨
            // 즉, 예제1 기준 5번 집(i=4)에서 2개 배달 0개 수거 후 cap을 각 빼준다면
            // deli == -2, pick == -4가 되고, 5번까지의 거리를 answer에 추가
            
            // 그 다음 i=3일 때, deli + 1 == -1, pick + 4 == 0
            // 이 경우 5번집 갔다오는 길에 모두 처리 가능하기 때문에 안 가도 됨
            // while문 통과하지 않아서 answer에 추가 안 됨
            
            // 즉 먼 곳부터 탐색해서 deli이나 pick이 양수여서 가야하는 경우만 answer에 추가 
            while(deli > 0 || pick > 0) {
                deli -= cap;
                pick -= cap;
                answer += (i+1)*2;
            }
        }
        
        return answer;
    }
}