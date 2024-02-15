import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static int N, r, c;
    static int cnt = 0;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        r = Integer.parseInt(st.nextToken());
        c = Integer.parseInt(st.nextToken());

        sol(r, c, (int) Math.pow(2, N));
        System.out.println(cnt);;
    }

    public static void sol(int x, int y, int n) {
        if(n == 1) return;
        int m = n / 2;

        if(x < m && y < m) sol(x, y, m);    // 좌상단
        else if (x < m && y >= m) {         // 우상단
            cnt += n * n / 4;       // 4분할 중 좌상단 1개만큼 더해줌
            sol(x, y - m, m);
        } else if (x >= m && y < m) {       // 좌하단
            cnt += n * n / 4 * 2;
            sol(x - m, y, m);
        } else {                                        // 우하단
            cnt += n * n / 4 * 3;
            sol(x - m, y - m, m);
        }
    }
}