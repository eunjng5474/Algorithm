class Solution {
    static int[] answer;
    static int[][] arr;
    
    public int[] solution(int rows, int columns, int[][] queries) {
        answer = new int[queries.length];
        arr = new int[rows][columns]; 
        
        // 첫 행렬 만들기 
        int n = 1;
        for(int i=0; i<rows; i++) {
            for(int j=0; j<columns; j++) {
                arr[i][j] = n++;
            }
        }
        
        int idx = 0;
        for(int[] q : queries) {
            int num = turn(q[0]-1, q[1]-1, q[2]-1, q[3]-1);
            answer[idx++] = num;
        }
        
        return answer;
    }
    
    
    static int turn(int x1, int y1, int x2, int y2) {
        int tmp = arr[x1][y1];
        int minVal = tmp;
        
        // 첫번째 값은 따로 저장해두고, 변경 전 값 가져오기 위해 역순으로 회전 
        // 위로 회전 -> x1, y1부터 아래값 가져옴
        for(int i=x1; i<x2; i++) {
            arr[i][y1] = arr[i+1][y1];
            minVal = Math.min(minVal, arr[i][y1]);
        }
        
        // <- : x2, y1부터 오른쪽 값 가져옴
        for(int i=y1; i<y2; i++) {
            arr[x2][i] = arr[x2][i+1];
            minVal = Math.min(minVal, arr[x2][i]);
        }
        
        // 아래로 회전
        for(int i=x2; i>x1; i--) {
            arr[i][y2] = arr[i-1][y2];
            minVal = Math.min(minVal, arr[i][y2]);
        }
        
        // ->
        for(int i=y2; i>y1+1; i--) {
            arr[x1][i] = arr[x1][i-1];
            minVal = Math.min(minVal, arr[x1][i]);
        }
        arr[x1][y1+1] = tmp;
        
        return minVal;
        
    }
}