import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(br.readLine());
        StringBuilder sb = new StringBuilder();

        int[] dp = new int[41];
        dp[1] = 1;
        for (int i = 2; i <= 40; i++) {
            dp[i] = dp[i-2] + dp[i-1];
        }

        for (int i = 0; i < t; i++) {
            int n = Integer.parseInt(br.readLine());
            if (n == 0) {
                sb.append(1).append(" ").append(0).append("\n");
            } else if (n == 1) {
                sb.append(0).append(" ").append(1).append("\n");
            } else {
                sb.append(dp[n-1]).append(" ").append(dp[n]).append("\n");
            }
        }
        System.out.println(sb);
    }
}