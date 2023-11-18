import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int k = Integer.parseInt(br.readLine());

        int idx = -1;
        int[] arr = new int[k];

        for (int i = 0; i < k; i++) {
            int n = Integer.parseInt(br.readLine());
            if (n != 0) {
                idx++;
                arr[idx] = n;
            } else idx--;
        }
        int sum = 0;
        for (int i = 0; i <= idx; i++) {
            sum += arr[i];
        }
        System.out.println(sum);
    }
}