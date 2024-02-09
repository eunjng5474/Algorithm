import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        long[] dp = new long[n];
        int[] stairs = new int[n];
        for (int i = 0; i < n; i++) {
            stairs[i] = Integer.parseInt(br.readLine());
        }

        if (n < 3) {
            long result = 0;
            for (int i = 0; i < n; i++) result += stairs[i];
            System.out.println(result);
        } else {
            dp[0] = stairs[0];
            dp[1] = stairs[0] + stairs[1];
            dp[2] = Math.max(stairs[0] + stairs[2], stairs[1] + stairs[2]);

            for (int i = 3; i < n; i++) {
                dp[i] = Math.max(dp[i - 3] + stairs[i - 1] + stairs[i], dp[i - 2] + stairs[i]);
            }
            System.out.println(dp[n-1]);
        }
    }
}