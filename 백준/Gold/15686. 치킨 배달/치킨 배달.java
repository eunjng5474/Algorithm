import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class Main {
    static int N, M;
    static int result = Integer.MAX_VALUE;
    static ArrayList<int[]> house = new ArrayList<>();;
    static ArrayList<int[]> chicken = new ArrayList<>();;
    static boolean[] selected;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        // 집, 치킨집의 좌표 담은 배열
        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < N; j++) {
                int num = Integer.parseInt(st.nextToken());
                if(num == 1) house.add(new int[]{i, j});
                else if(num == 2) chicken.add(new int[]{i, j});
            }
        }
        // 선택 여부 확인 위한 치킨집 개수만큼의 배열 selected 생성
        selected = new boolean[chicken.size()];

        sol(0, 0);
        System.out.println(result);
    }

    static void sol(int cnt, int idx) {
        // M개만큼 선택되었다면 각 집별로 선택된 치킨집에 대한 치킨 거리 계산 및 최소값 판단
        if (cnt == M) {
            int sum = 0;
            for (int[] h : house) {
                int dist = Integer.MAX_VALUE;
                for (int j = 0; j < chicken.size(); j++) {
                    if (selected[j]) {
                        int tmp = Math.abs(chicken.get(j)[0] - h[0]) + Math.abs(chicken.get(j)[1] - h[1]);
                        dist = Math.min(dist, tmp);
                    }
                }
                sum += dist;
            }
            result = Math.min(result, sum);
            return;
        }

        for (int i = idx; i < chicken.size(); i++) {
            selected[i] = true;
            sol(cnt+1, i+1);
            selected[i] = false;
        }
    }
}