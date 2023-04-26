import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		StringBuilder sb = new StringBuilder();
		
		int n = Integer.parseInt(st.nextToken());
		int m = Integer.parseInt(st.nextToken());
		
		int[] arr = new int[n+1];
		int[] tmp = new int[n+1];
		for(int i=0; i<=n; i++) {
			arr[i] = i;
			tmp[i] = i;
		}
		int i, j, k;
		String input;
		StringTokenizer str;
		
		for(int a=0; a<m; a++) {
//			BufferedReader bfr = new BufferedReader(new InputStreamReader(System.in));
//			StringTokenizer stn = new StringTokenizer(bfr.readLine());
			
			input = br.readLine();
			str = new StringTokenizer(input);
			i = Integer.parseInt(str.nextToken());
			j = Integer.parseInt(str.nextToken());
			k = Integer.parseInt(str.nextToken());
			int idx = i;
			
			for(int b=0; b<=j-i; b++) {
				if(k+b<=j) {
					tmp[i+b] = arr[k+b];
				} else {
					tmp[i+b] = arr[idx];
					idx ++;
				}
			}
			for(int q=1; q<=n; q++) {
				arr[q] = tmp[q];
			}
		}
		for(int p=1; p<=n; p++) {
			sb.append(arr[p] + " ");
		}
		System.out.println(sb);
	}

}