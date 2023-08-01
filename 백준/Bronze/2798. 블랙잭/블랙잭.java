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
		
		int[] nums = new int[n];
		
		st = new StringTokenizer(br.readLine());
		for(int i=0; i<n; i++) {
			nums[i] = Integer.parseInt(st.nextToken());
		}
		
		int result = sol(nums, n, m);
		System.out.println(result);

	}
	
	static int sol(int[] nums, int n, int m) {
		int result = 0;
		
		for(int i=0; i<n-2; i++) {
			if(nums[i] > m) continue;
			
			for(int j=i+1; j<n-1; j++) {
				if (nums[j] > m) continue;
				
				for(int k=j+1; k<n; k++) {
					int sum = nums[i] + nums[j] + nums[k];
					if (sum > m) continue;
					result = Math.max(result, sum);
					
					if(result == m) {
						return result;
					}
				}
			}
		}
		
		return result;
	}

}