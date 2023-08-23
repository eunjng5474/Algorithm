import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        int b = Integer.parseInt(st.nextToken());

        int[][] arr = new int[n][m];

        for(int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            for(int j = 0; j < m; j++) {
                arr[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        int time = 99999999;
        int height = 0;

        for(int i = 0; i < 257; i++) {
            int removed = 0;
            int added = b;

            for(int j = 0; j < n; j++) {
                for(int k = 0; k < m; k++) {
                    if(arr[j][k] > i) {
                        added += (arr[j][k] - i);
                    } else {
                        removed += (i - arr[j][k]);
                    }
                }
            }
            if(removed > added) continue;

            int tmp = (added - b) * 2 + removed;
            if(tmp <= time) {
                time = tmp;
                height = i;
            }
        }
        System.out.println(time + " " + height);
    }
}