import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        int n = Integer.parseInt(br.readLine());

        int[] nums = new int[n];
        int[] cnt = new int[8001];
        int sum = 0;
        int max = -4000;
        int min = 4000;

        for (int i = 0; i < n; i++) {
            int num = Integer.parseInt(br.readLine());
            nums[i] = num;
            cnt[num + 4000]++;
            sum += num;

            if(num > max) max = num;
            if(num < min) min = num;
        }

        Arrays.sort(nums);

        int maxCnt = 0;
        int mode = 0;
        boolean flag = false;   // 최빈값 한 번 등장하면 true

        for (int i = 0; i < 8001; i++) {
            if (cnt[i] > maxCnt) {
                maxCnt = cnt[i];
                mode = i - 4000;
                flag = true;
            } else if (cnt[i] == maxCnt && flag) {
                mode = i - 4000;
                flag = false;
            }
        }

        sb.append((int) Math.round((double) sum / n)).append("\n");
        sb.append(nums[n / 2]).append("\n");
        sb.append(mode).append("\n");
        sb.append(max - min);

        System.out.println(sb);
    }
}