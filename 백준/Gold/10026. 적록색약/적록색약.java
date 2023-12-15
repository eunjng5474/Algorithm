import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;

public class Main {
    static int n;
    static Character[][] arr;   // 적록색약 아님
    static boolean[][] visited;         // 적록색약X 방문 여부
    static boolean[][] colorVisited;    // 적록색약 방문 여부
    static int[] dx = {-1, 1, 0, 0};
    static int[] dy = {0, 0, -1, 1};

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());

        arr = new Character[n][n];
        for (int i = 0; i < n; i++) {
            String str = br.readLine();
            for (int j = 0; j < n; j++) {
                arr[i][j] = str.charAt(j);
            }
        }

        visited = new boolean[n][n];
        colorVisited = new boolean[n][n];

        int cnt = 0;
        int colorCnt = 0;

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (!visited[i][j]) {
                    bfs(i, j);
                    cnt++;
                }

                if (!colorVisited[i][j]) {
                    colorBfs(i, j);
                    colorCnt++;
                }
            }
        }

        System.out.println(cnt + " " + colorCnt);
    }

    static void bfs(int i, int j) {  // 적록색약 아님
        Queue<int[]> q = new LinkedList<>();
        q.add(new int[]{i, j});

        while (!q.isEmpty()) {
            int[] now = q.poll();
            int x = now[0];
            int y = now[1];

            for (int d = 0; d < 4; d++) {
                int nx = x + dx[d];
                int ny = y + dy[d];

                if(nx < 0 || nx >= n || ny < 0 || ny >= n) continue;

                if (!visited[nx][ny] && arr[nx][ny].equals(arr[x][y])) {
                    visited[nx][ny] = true;
                    q.add(new int[]{nx, ny});
                }
            }
        }
    }

    static void colorBfs(int i, int j) {    // 적록색약
        Queue<int[]> queue = new LinkedList<>();
        queue.add(new int[]{i, j});

        while (!queue.isEmpty()) {
            int[] now = queue.poll();
            int x = now[0];
            int y = now[1];

            Character color = arr[x][y];

            for (int d = 0; d < 4; d++) {
                int nx = x + dx[d];
                int ny = y + dy[d];

                if(nx < 0 || nx >= n || ny < 0 || ny >= n || colorVisited[nx][ny]) continue;

                if (color.equals('R') || color.equals('G')) {
                    if (arr[nx][ny].equals('R') || arr[nx][ny].equals('G')) {
                        colorVisited[nx][ny] = true;
                        queue.add(new int[]{nx, ny});
                    }
                } else if (arr[nx][ny].equals('B')) {
                    colorVisited[nx][ny] = true;
                    queue.add(new int[]{nx, ny});
                }
            }
        }
    }
}