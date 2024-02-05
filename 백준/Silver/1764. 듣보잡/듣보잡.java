import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.HashSet;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        StringBuilder sb = new StringBuilder();
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        HashSet<String> set = new HashSet<>();
        ArrayList<String> arr = new ArrayList<>();

        for (int i = 0; i < n; i++) set.add(br.readLine());
        for (int i = 0; i < m; i++) {
            String str = br.readLine();
            if(set.contains(str)) arr.add(str);
        }

        Collections.sort(arr);
        sb.append(arr.size()).append("\n");
        for(String str : arr) sb.append(str).append("\n");
        System.out.println(sb);
    }
}