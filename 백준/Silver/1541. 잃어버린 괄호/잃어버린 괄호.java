import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String str = br.readLine();
        String[] strs = str.split("-");
        int answer = 0;

        for (int i = 0; i < strs.length; i++) {
            String[] split = strs[i].split("\\+");
            int sum = 0;
            for (String sp : split) {
                sum += Integer.parseInt(sp);
            }
            if (i == 0) answer += sum;
            else answer -= sum;
        }
        System.out.println(answer);
    }
}