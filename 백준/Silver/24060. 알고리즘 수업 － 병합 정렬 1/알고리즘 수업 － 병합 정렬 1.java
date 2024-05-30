import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static int n, k, cnt;
    static int result = -1;
    static int[] a, tmp;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        k = Integer.parseInt(st.nextToken());
        a = new int[n];
        tmp = new int[n];

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            a[i] = Integer.parseInt(st.nextToken());
        }

        mergeSort(a, 0, n - 1);
        System.out.println(result);
    }

    static void mergeSort(int[] a, int p, int r) {
        if (p < r) {
            int q = (p + r) / 2;
            mergeSort(a, p, q);
            mergeSort(a, q + 1, r);
            merge(a, p, q, r);
        }
    }

    static void merge(int[] a, int p, int q, int r) {
        int i = p;
        int j = q + 1;
        int t = 0;

        while (i <= q && j <= r) {
            if(a[i] <= a[j]) tmp[t++] = a[i++];
            else tmp[t++] = a[j++];
        }
        while (i <= q) {
            tmp[t++] = a[i++];
        }
        while (j <= r) {
            tmp[t++] = a[j++];
        }
        i = p;
        t = 0;
        while (i <= r) {
            cnt++;
            if (cnt == k) {
                result = tmp[t];
                break;
            }
            a[i++] = tmp[t++];
        }
    }
}