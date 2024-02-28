import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static int N;
    static int[][] arr;
    static int white = 0;
    static int blue = 0;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        N = Integer.parseInt(br.readLine());
        arr = new int[N][N];
        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < N; j++) {
                arr[i][j] = Integer.parseInt(st.nextToken());
            }
        }
        sol(0, 0, N);
        System.out.println(white);
        System.out.println(blue);
    }

    public static void sol(int x, int y, int n) {
        boolean flag = true;    // 종이가 모두 같은 색인지 확인
        for (int i = x; i < x + n; i++) {
            for (int j = y; j < y + n; j++) {
                if (arr[i][j] != arr[x][y]) {
                    flag = false;
                    break;
                }
            }
            if(!flag) break;
        }

        if (flag) {
            if (arr[x][y] == 0) white++;
            else blue++;
        } else {
            // 분할
            sol(x, y, n / 2);
            sol(x, y + n / 2, n / 2);
            sol(x + n / 2, y, n / 2);
            sol(x + n / 2, y + n / 2, n / 2);
        }
    }
}