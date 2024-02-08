import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
    static int m, n, h;
    static int result;
    static boolean chk = true;  // 처음부터 토마토 모두 익어있는지 체크

    static int[][][] arr;
    static int[][][] visited;
    static Queue<int[]> q;
    static int[] dz = {-1, 1, 0, 0, 0, 0};   // 위 아래 왼 오 앞 뒤
    static int[] dx = {0, 0, -1, 1, 0, 0};
    static int[] dy = {0, 0, 0, 0, -1, 1};

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        m = Integer.parseInt(st.nextToken());
        n = Integer.parseInt(st.nextToken());
        h = Integer.parseInt(st.nextToken());

        arr = new int[h][n][m];
        visited = new int[h][n][m];
        q = new LinkedList<>();

        for (int i = 0; i < h; i++) {
            for (int j = 0; j < n; j++) {
                st = new StringTokenizer(br.readLine());
                for (int k = 0; k < m; k++) {
                    arr[i][j][k] = Integer.parseInt(st.nextToken());
                    if (arr[i][j][k] == -1) visited[i][j][k] = -1;  // 토마토 없는 칸 visited에도 표시
                    else if (arr[i][j][k] == 1) {
                        q.add(new int[]{i, j, k});
                        visited[i][j][k] = 1;
                    } else if (chk && arr[i][j][k] == 0) chk = false; // 익지 않은 토마토 있으면 chk를 false로
                }
            }
        }

        if(chk) System.out.println(0);
        else {
            bfs();
            System.out.println(check());
        }
    }

    public static void bfs() {
        while (!q.isEmpty()) {
            int[] p = q.poll();
            int z = p[0];
            int x = p[1];
            int y = p[2];

            for (int d = 0; d < 6; d++) {
                int nz = z + dz[d];
                int nx = x + dx[d];
                int ny = y + dy[d];

                if(nz < 0 || nx < 0 || ny < 0 || nz >= h || nx >= n || ny >= m) continue;
                if (arr[nz][nx][ny] == 0 && visited[nz][nx][ny] == 0) {
                    q.add(new int[]{nz, nx, ny});
                    visited[nz][nx][ny] = visited[z][x][y] + 1;
                }
            }
        }
    }

    public static int check() {
        for (int i = 0; i < h; i++) {
            for (int j = 0; j < n; j++) {
                for (int k = 0; k < m; k++) {
                    if (visited[i][j][k] == 0) {
                        return -1;
                    } else if (visited[i][j][k] > result) result = visited[i][j][k];
                }
            }
        }
        return --result;    // 1부터 시작했으므로 1 빼줌
    }

}