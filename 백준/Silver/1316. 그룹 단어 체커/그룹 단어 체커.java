import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int result = 0;

        for (int i = 0; i < n; i++) {
            String word = br.readLine();
            if(check(word)) result++;
        }
        System.out.println(result);
    }

    static boolean check(String word) {
        boolean[] used = new boolean[26];
        int prev = 0;

        for (int i = 0; i < word.length(); i++) {
            int now = word.charAt(i);

            if (prev != now) {
                if (used[now - 97] == false) {
                    used[now - 97] = true;
                    prev = now;
                } else {
                    return false;
                }
            }
        }
        return true;
    }
}