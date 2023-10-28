import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static int result = 64;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        // W면 0, B면 1
        int[][] arr = new int[n][m];

        for(int i = 0; i < n; i++) {
            String str = br.readLine();

            for (int j = 0; j < m; j++) {
                if(str.charAt(j) == 'W') arr[i][j] = 0;
                else arr[i][j] = 1;
            }
        }

        for (int i = 0; i < n - 7; i++) {
            for (int j = 0; j < m - 7; j++) {
                check(i, j, arr);
            }
        }
        System.out.println(result);
    }

    public static void check(int x, int y, int[][] arr) {
        int cnt = 0;
        int color = arr[x][y];  // 첫번째 칸 색 (W: 0, B: 1)

        for (int i = x; i < x + 8; i++) {
            for (int j = y; j < y + 8; j++) {
                if(arr[i][j] != color) cnt++;

                color = (color + 1) % 2;    // 다음 칸은 반대 색
            }
            color = (color + 1) % 2;
        }
        cnt = Math.min(cnt, 64 - cnt);
        result = Math.min(result, cnt);
    }
}