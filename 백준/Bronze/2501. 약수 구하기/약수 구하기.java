import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		int n = Integer.parseInt(st.nextToken());
		int k = Integer.parseInt(st.nextToken());
		
		int cnt = 0;
		int flag = 0;

		for(int i=1; i<=n; i++) {
			if(n%i == 0) {
				cnt += 1;
			}
			if(cnt==k) {
				System.out.println(i);
				flag = 1;
				break;
			}

		}
		if(flag==0) {
		System.out.println(0);

		}
	}

}