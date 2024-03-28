import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());

        int[] arr = new int[n];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }

        int[] cnt = new int[100001];
        int result = 0;

        int start = 0;
        int end = 0;
        while (end < n) {
            while (end < n && cnt[arr[end]] < k) {
                cnt[arr[end]]++;
                end++;
            }
            int tmp = end - start;
            result = Math.max(result, tmp);
            cnt[arr[start]]--;
            start++;
        }
        System.out.println(result);
    }
}