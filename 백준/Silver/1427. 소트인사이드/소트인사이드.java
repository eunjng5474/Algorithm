import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        String n = br.readLine();
        int len = n.length();

        int[] num = new int[len];
        for (int i = 0; i < len; i++) {
            num[i] = Integer.parseInt(String.valueOf(n.charAt(i)));
        }

        Arrays.sort(num);
        for (int i = len - 1; i >= 0; i--) {
            sb.append(num[i]);
        }
        System.out.println(sb);
    }
}