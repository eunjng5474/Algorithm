import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        StringBuilder sb = new StringBuilder();

        int m = Integer.parseInt(st.nextToken());
        int n = Integer.parseInt(st.nextToken());

        boolean[] prime = new boolean[n+1];
        prime[0] = true;    // 소수X
        prime[1] = true;

        for(int i = 2; i < n+1; i++) {
            if(prime[i]) continue;
            for (int j = i * 2; j < n + 1; j += i) {
                prime[j] = true;
            }
        }

        for (int i = m; i < n + 1; i++) {
            if(!prime[i]) sb.append(i).append("\n");
        }

        System.out.println(sb);
    }
}