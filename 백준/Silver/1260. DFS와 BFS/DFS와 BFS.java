import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
    static int n, m, v;
    static int[][] graph;
    static boolean[] visited;
    static StringBuilder sb = new StringBuilder();

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        v = Integer.parseInt(st.nextToken());

        graph = new int[n + 1][n + 1];

        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            graph[a][b] = 1;
            graph[b][a] = 1;
        }

        visited = new boolean[n + 1];
        dfs(v);
        sb.append("\n");

        visited = new boolean[n + 1];
        bfs(v);
        System.out.println(sb);
    }

    public static void dfs(int now) {
        visited[now] = true;
        sb.append(now).append(" ");

        for (int i = 0; i <= n; i++) {
            if(graph[now][i] == 1 && !visited[i]) dfs(i);
        }
    }

    public static void bfs(int now) {
        Queue<Integer> q = new LinkedList<>();
        q.add(now);
        visited[now] = true;

        while (!q.isEmpty()) {
            now = q.poll();
            sb.append(now).append(" ");

            for (int i = 0; i <= n; i++) {
                if (graph[now][i] == 1 && !visited[i]) {
                    visited[i] = true;
                    q.add(i);
                }
            }
        }
    }
}