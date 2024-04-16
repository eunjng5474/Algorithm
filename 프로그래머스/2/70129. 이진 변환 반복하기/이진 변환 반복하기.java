class Solution {
    public int[] solution(String s) {
        int cnt = 0;
        int zeroCnt = 0;
        
        while(!s.equals("1")) {
            String tmp = s.replace("0", "");
            zeroCnt += s.length() - tmp.length();
            s = Integer.toBinaryString(tmp.length());
            cnt++;
        }
        
        return new int[] {cnt, zeroCnt};
    }
}