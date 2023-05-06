import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		int n = Integer.parseInt(st.nextToken());
		int m = Integer.parseInt(st.nextToken());
		
		int arr[] = new int[n+1];
		for(int i=0; i<n+1; i++) {
			arr[i] = i;
		}
		
		for(int k=0; k<m; k++) {
			st = new StringTokenizer(br.readLine());
			int i = Integer.parseInt(st.nextToken());
			int j = Integer.parseInt(st.nextToken());
			
			int tmp = arr[i];
			arr[i] = arr[j];
			arr[j] = tmp;
		}
		StringBuilder sb = new StringBuilder();
		for(int i=1; i<=n; i++) {
			sb.append(arr[i]);
			sb.append(" ");
		}
		System.out.println(sb);
	}

}