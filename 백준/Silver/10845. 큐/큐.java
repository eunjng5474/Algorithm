import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        Queue<Integer> q = new LinkedList<>();
        int num = 0;

        int n = Integer.parseInt(br.readLine());
        for(int i = 0; i < n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            String str = st.nextToken();

            if(str.equals("push")) {
                num = Integer.parseInt(st.nextToken());
                q.add(num);
            } else if(str.equals("pop")) {
                if(q.isEmpty()) {
                    sb.append(-1).append("\n");
                } else {
                    sb.append(q.poll()).append("\n");
                }
            } else if(str.equals("size")) {
                sb.append(q.size()).append("\n");
            } else if(str.equals("empty")) {
                if(q.isEmpty()) {
                    sb.append(1).append("\n");
                } else {
                    sb.append(0).append("\n");
                }
            } else if(str.equals("front")) {
                if(q.isEmpty()) {
                    sb.append(-1).append("\n");
                } else {
                    sb.append(q.peek()).append("\n");
                }
            } else if(str.equals("back")) {
                if(q.isEmpty()) {
                    sb.append(-1).append("\n");
                } else {
                    sb.append(num).append("\n");
                }
            }
        }
        System.out.println(sb);
    }
}