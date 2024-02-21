import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.HashMap;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        int N = Integer.parseInt(br.readLine());
        int[] arr = new int[N];
        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }
        int[] sorted = arr.clone(); // 기존 arr 복사 후 정렬 
        Arrays.sort(sorted);

        HashMap<Integer, Integer> map = new HashMap<>();
        int idx = 0;
        for (int num : sorted) {
            if(!map.containsKey(num)) map.put(num, idx++);
            // key에 num 없으면 idx와 함께 넣고 idx++
        }

        for (int n : arr) sb.append(map.get(n)).append(" ");
        System.out.println(sb);
    }
}