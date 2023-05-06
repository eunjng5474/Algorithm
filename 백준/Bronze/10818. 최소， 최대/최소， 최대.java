import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
//import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
	////////// sol 1
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int n = Integer.parseInt(br.readLine());
		int max = - 1000001;
		int min = 1000001;
		
		StringTokenizer st = new StringTokenizer(br.readLine());
		while(st.hasMoreTokens()) {
			int num = Integer.parseInt(st.nextToken());
			if(num > max) {
				max = num;
			}
			if(num < min) {
				min = num;
			}
		}
		System.out.println(min + " " + max);
	}
	
	
	
//	//////// sol 2
//	public static void main(String[] args) throws IOException {
//		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
//		
//		int n = Integer.parseInt(br.readLine());
//		int[] lst = new int[n];
//		int idx = 0;
//		
//		StringTokenizer st = new StringTokenizer(br.readLine());
//		while(st.hasMoreTokens()) {
//			lst[idx] = Integer.parseInt(st.nextToken());
//			idx++;
//		}
//		
//
//		Arrays.sort(lst);
//		System.out.println(lst[0] + " " + lst[n-1]);
//	}

}