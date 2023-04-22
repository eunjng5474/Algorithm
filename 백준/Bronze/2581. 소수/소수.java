import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int m = Integer.parseInt(br.readLine());
		int n = Integer.parseInt(br.readLine());
		int sum = 0;
		int min = 0;
		
		for(int i=m; i<=n; i++) {
			if(i==1) continue;
			if(i==2) {
				sum += i;
				min = i;
				continue;
			}
			
			int flag = 0;
			for(int j=2; j<i; j++) {
				if(i%j==0) {
					flag = 1;
					break;
				}
			}
			if(flag==0) {
				if(sum==0) {
					min = i;
				}
				sum += i;
			}
			
		}
		int result = -1;
		
		if(sum!=0) {
			System.out.println(sum);
			result = min;
		}
		System.out.println(result);
	}

}