import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int k = Integer.parseInt(st.nextToken());
        int n = Integer.parseInt(st.nextToken());

        long start = 0;
        long end = 0;

        int[] lines = new int[k];
        for (int i = 0; i < k; i++) {
            lines[i] = Integer.parseInt(br.readLine());
            if(lines[i] > end) end = lines[i];
        }
        end++;

        while (start < end) {
            long mid = (start + end) / 2;
            long cnt = 0;

            for (int line : lines) {
                cnt += (line / mid);
            }

            if(cnt < n) end = mid;
            else start = mid + 1;
        }
        System.out.println(start - 1);
    }
}