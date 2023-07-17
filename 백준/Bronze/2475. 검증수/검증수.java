import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		double ans = 0;
		
		for(int i=0; i<5; i++) {
			int a = Integer.parseInt(st.nextToken());
			ans += Math.pow(a, 2);
		}
		System.out.println((int) ans%10);

	}

}