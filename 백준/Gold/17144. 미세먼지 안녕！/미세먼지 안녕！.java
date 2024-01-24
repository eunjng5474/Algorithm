import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static int r, c, t;
    static int[][] arr;
    static int[][] move;
    static int air = -1;     // 공기청정기 윗 행 좌표

    static int[] dx = {-1, 1, 0, 0};    // 상하좌우 이동
    static int[] dy = {0, 0, -1, 1};

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        r = Integer.parseInt(st.nextToken());
        c = Integer.parseInt(st.nextToken());
        t = Integer.parseInt(st.nextToken());

        arr = new int[r][c];
        for (int i = 0; i < r; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < c; j++) {
                int n =  Integer.parseInt(st.nextToken());
                arr[i][j] = n;
                if(air == -1 && n == -1) air = i;
            }
        }

        for (int k = 0; k < t; k++) {
            arr[air][0] = arr[air+1][0] = -1;
            move = new int[r][c];

            for (int i = 0; i < r; i++) {
                for (int j = 0; j < c; j++) {
                    if(arr[i][j] > 0) spread(i, j);
                }
            }

            cleaner_up(air-1, 0);
            cleaner_down(air+2, 0);
            arr = move;
        }

        int result = 0;
        for (int i = 0; i < r; i++) {
            for (int j = 0; j < c; j++) {
                result += move[i][j];
            }
        }
        System.out.println(result);
    }

    private static void spread(int x, int y) {
        int n = arr[x][y] / 5;
        int cnt = 0;

        for (int d = 0; d < 4; d++) {
            int nx = x + dx[d];
            int ny = y + dy[d];

            if (nx < 0 || nx >= r || ny < 0 || ny >= c || arr[nx][ny] == -1) continue;
            move[nx][ny] += n;
            cnt++;
        }
        move[x][y] += arr[x][y] - (n * cnt);
    }

    private static void cleaner_up(int x, int y) {
        int[] direct = {0, 3, 1, 2};     // 상우하좌 - 위쪽 공기 순환(우상좌하)의 역순의 반대 방향
        int d = 0;

        while (d < 4) {
            int nx = x + dx[direct[d]];
            int ny = y + dy[direct[d]];

            if (nx < 0 || nx > air || ny < 0 || ny >= c) {
                d++;
                continue;
            }
            if (nx == air && ny == 0) { // 다음 좌표가 공청기면 해당 위치 0으로 바꾸고 종료
                move[x][y] = 0;
                break;
            }
            move[x][y] = move[nx][ny];  // 다음 좌표의 값 가져오기(미세먼지 이동)
            x = nx;
            y = ny;
        }
    }

    private static void cleaner_down(int x, int y) {
        int[] direct = {1, 3, 0, 2};    // 하우상좌
        int d = 0;

        while (d < 4) {
            int nx = x + dx[direct[d]];
            int ny = y + dy[direct[d]];

            if (nx <= air || nx >= r || ny < 0 || ny >= c) {
                d++;
                continue;
            }
            if (nx == air + 1 && ny == 0) {
                move[x][y] = 0;
                break;
            }
            move[x][y] = move[nx][ny];
            x = nx;
            y = ny;
        }
    }
}