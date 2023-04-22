import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main {

	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		while(true) {
			int n = Integer.parseInt(br.readLine());
			if(n==-1) break;
			
			StringBuilder sb = new StringBuilder();
			
			int[] arr = new int[n+1];
			arr[0] = 1;
			int cnt = 1;
			for(int i=2; i<n; i++) {
				if(n%i==0) {
					arr[cnt] = i;
					cnt ++;
				}
			}
			int sum = Arrays.stream(arr).sum();
			if(sum == n) {
				sb.append(n).append(" = ");
				for(int i=0; i<cnt; i++) {
					sb.append(arr[i]);
					if(i==cnt-1) continue;
					sb.append(" + ");
				}
			} else {
				sb.append(n);
				sb.append(" is NOT perfect.");
			}
			System.out.println(sb);
		}

	}

}