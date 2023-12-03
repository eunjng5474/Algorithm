import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        int[] nums = new int[n];
        for (int i = 0; i < n; i++) {
            nums[i] = Integer.parseInt(br.readLine());
        }
        Arrays.sort(nums);

        int out = (int) Math.round(n * 0.15);

        double sum = 0;
        for (int i = out; i < n - out; i++) {
            sum += nums[i];
        }

        int result = (int) Math.round(sum / (n - out * 2));
        System.out.println(result);
    }
}