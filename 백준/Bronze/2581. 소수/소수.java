import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {

	// 에라토스테네스의 체 방법 
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int m = Integer.parseInt(br.readLine());
		int n = Integer.parseInt(br.readLine());
		primeNumber(m, n);
	}
		
	static void primeNumber(int m, int n) {
		int[] arr = new int[n+1];
		
		// 2부터 arr에 해당 인덱스 값 넣기 
		for(int i=2; i<=n; i++) {
			arr[i] = i;
		}
		
		for(int i=2; i<=n; i++) {
			if(arr[i] == 0) continue;
			
			for(int j=i*2; j<=n; j+=i) {
				arr[j] = 0;
				// j에 i씩 더해가면서 i의 배수인 j의 인덱스값을 0으로 
			}
		}
		int min = 0;
		int sum = 0;
		
		for(int k=m; k<=n; k++) {
			if(arr[k]==0) continue;
			
			if(sum==0) {
				min = k;
			}
			sum += k;
		}
		
		if(sum==0) {
			System.out.println(-1);
		} else {
			System.out.println(sum);
			System.out.println(min);
		}
		
	}

		

}