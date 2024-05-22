import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        StringBuilder sb = new StringBuilder();

        int m = Integer.parseInt(br.readLine());
        int set = 0;

        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            String str = st.nextToken();
            int n;
            switch (str) {
                case "add":
                    n = Integer.parseInt(st.nextToken());
                    set = set | (1 << n);
                    break;
                case "remove":
                    n = Integer.parseInt(st.nextToken());
                    set = set & ~(1 << n);
                    break;
                case "check":
                    n = Integer.parseInt(st.nextToken());
                    if((set & (1 << n)) > 0) sb.append("1\n");
                    else sb.append("0\n");
                    break;
                case "toggle":
                    n = Integer.parseInt(st.nextToken());
                    set = set ^ (1 << n);
                    break;
                case "all":
                    set = (1 << 21) - 1;
                    break;
                case "empty":
                    set = 0;
                    break;
            }
        }
        System.out.println(sb);
    }
}