import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Collections;
import java.util.PriorityQueue;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        int n = Integer.parseInt(br.readLine());
        PriorityQueue<Integer> hq = new PriorityQueue<>(Collections.reverseOrder());    // 내림차순

        for (int i = 0; i < n; i++) {
            int x = Integer.parseInt(br.readLine());
            if (x == 0) {
                if(hq.isEmpty()) sb.append(0).append("\n");
                else sb.append(hq.poll()).append("\n");
            } else hq.offer(x);
        }
        System.out.println(sb);
    }
}