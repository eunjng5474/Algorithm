import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        while (true) {
            String num = br.readLine();
            if (num.equals("0")) break;

            boolean flag = true;
            int n = num.length();
            for (int i = 0; i < n; i++) {
                if (num.charAt(i) != num.charAt(n - 1 - i)) {
                    flag = false;
                    break;
                }
            }

            if (flag) {
                sb.append("yes").append("\n");
            } else {
                sb.append("no").append("\n");
            }
        }
        System.out.println(sb);
    }
}