import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int tc = Integer.parseInt(br.readLine());

        StringTokenizer st;
        StringBuilder sb = new StringBuilder();

        for (int i = 0; i < tc; i++) {
            st = new StringTokenizer(br.readLine());
            int n = Integer.parseInt(st.nextToken());
            int m = Integer.parseInt(st.nextToken());

            LinkedList<int[]> q = new LinkedList<>();
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < n; j++) {
                int[] set = {j, Integer.parseInt(st.nextToken())};
                q.add(set);
            }

            int cnt = 0;    // 출력 횟수
            while (!q.isEmpty()) {
                int[] check = q.poll();
                boolean flag = true;    // check가 가장 중요도 높은지 여부

                for (int[] p : q) {
                    if (p[1] > check[1]) {
                        flag = false;
                        break;
                    }
                }

                if(!flag) q.add(check);
                else {
                    cnt++;
                    if(check[0] == m) break;
                }
            }
            sb.append(cnt).append("\n");
        }
        System.out.println(sb);
    }
}