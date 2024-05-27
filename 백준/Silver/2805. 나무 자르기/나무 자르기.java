import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        int start = 0;
        int end = 0;
        int[] trees = new int[n];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            int h = Integer.parseInt(st.nextToken());
            trees[i] = h;
            end = Math.max(end, h);
        }

        while (start < end) {
            int mid = (start + end) / 2;
            long sum = 0;

            for (int tree : trees) {
                if(tree > mid) sum += (tree - mid);
            }

            if(sum < m) end = mid;
            else start = ++mid;
        }
        System.out.println(start - 1);
    }
}