import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		int tc = Integer.parseInt(br.readLine());
		
		for (int i=0; i<tc; i++) {
			st = new StringTokenizer(br.readLine());
			int d = Integer.parseInt(st.nextToken());
			int n = Integer.parseInt(st.nextToken());
			double arr[] = new double[n];
			st = new StringTokenizer(br.readLine());

			for(int j=0; j<n; j++) {
				arr[j] = Double.parseDouble(st.nextToken());
			}
			
			double mod[] = new double[d];
			for(int j=0; j<d; j++) {
				mod[j] = 0;
			}
			int cnt = 0;
			int sum = 0;
			
			for (double num : arr) {
				sum += num;
				sum %= d;
				
				cnt += mod[sum];
				mod[sum] += 1;
			}
			cnt += mod[0];
//			for(int k=0; k<d; k++) {
//				System.out.print(mod[k] + " ");	
//			}
			System.out.println(cnt);
		}
	}

}