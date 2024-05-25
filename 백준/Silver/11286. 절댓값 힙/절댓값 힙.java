import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Comparator;
import java.util.PriorityQueue;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        int n = Integer.parseInt(br.readLine());

        PriorityQueue<Integer> pq = new PriorityQueue<>(new Comparator<Integer>() {
            @Override
            public int compare(Integer o1, Integer o2) {
                int a = Math.abs(o1);
                int b = Math.abs(o2);
                if(a > b) return a - b;
                else if (a == b) {
                    if(o1 > o2) return 1;
                    else return -1;
                }
                else return -1;
            }
        });

        while (n > 0) {
            int x = Integer.parseInt(br.readLine());
            if (x == 0) {
                if (!pq.isEmpty()) sb.append(pq.poll()).append("\n");
                else sb.append(0).append("\n");
            } else {
                pq.offer(x);
            }
            n--;
        }
        System.out.println(sb);
    }
}