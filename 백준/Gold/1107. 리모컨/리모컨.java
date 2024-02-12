import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int m = Integer.parseInt(br.readLine());
        int result = Math.abs(n - 100); // 우선 100까지 +/-로만 이동하는 횟수를 최소값으로 잡음
        boolean[] btns = new boolean[10];   

        if (m > 0) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            for (int i = 0; i < m; i++) {
                int btn = Integer.parseInt(st.nextToken());
                btns[btn] = true;   // 고장난 버튼의 경우 true로 
            }
        }

        for (int i = 0; i < 1000000; i++) {
            String str = String.valueOf(i);     // 모든 숫자를 자리별로 탐색하기 위해 String으로 변환
            boolean flag = false;

            for (int j = 0; j < str.length(); j++) {
                int num = str.charAt(j) - '0';  // str의 j번째 자릿수를 숫자로 변환 
                if (btns[num]) {
                    flag = true;
                    break;          // 고장난 버튼 포함되어 있으면 flag 바꾸고 해당 숫자 건너뜀 
                }
            }
            if(flag) continue;
            int cnt = str.length() + Math.abs(n - i);  
            // length만큼 숫자 버튼 클릭 횟수 + 채널 이동 횟수
            result = Math.min(result, cnt);
        }
        System.out.println(result);
    }
}