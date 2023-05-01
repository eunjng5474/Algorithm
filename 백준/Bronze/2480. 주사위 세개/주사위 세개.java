import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		int a = Integer.parseInt(st.nextToken());
		int b = Integer.parseInt(st.nextToken());
		int c = Integer.parseInt(st.nextToken());
		
		if (a==b && b==c && c==a) {
			System.out.println(10000+a*1000);
		} else if (a==b || b==c) {
			System.out.println(1000+b*100);
		} else if (a==c) {
			System.out.println(1000+a*100);
		} else {
			int[] arr = new int[3];
			arr[0] = a;
			arr[1] = b;
			arr[2] = c;
			Arrays.sort(arr);
			System.out.println(arr[2]*100);
		}

	}

}