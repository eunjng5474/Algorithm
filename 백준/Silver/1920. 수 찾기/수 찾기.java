import javax.lang.model.type.ArrayType;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        int n = Integer.parseInt(br.readLine());
        int[] nums = new int[n];

        StringTokenizer st = new StringTokenizer(br.readLine());
        for(int i = 0; i < n; i++) {
            nums[i] = Integer.parseInt(st.nextToken());
        }
        Arrays.sort(nums);

        int m = Integer.parseInt(br.readLine());
        int[] check = new int[m];

        st = new StringTokenizer(br.readLine());
        for(int i = 0; i < m; i++) {
            check[i] = Integer.parseInt(st.nextToken());
        }

        for(int c : check) {
            sb.append(search(nums, c)).append("\n");
        }
        System.out.println(sb.toString());
    }

    public static int search(int[] arr, int check) {
        int s = 0;
        int e = arr.length - 1;

        while(s <= e) {
            int m = (s + e) / 2;
            if(check == arr[m]) return 1;
            else if(check < arr[m]) e = m - 1;
            else s = m + 1;
        }
        return 0;
    }
}