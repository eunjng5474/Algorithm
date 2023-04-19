import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine(), " ");
		
		String a = st.nextToken();
		String b = st.nextToken();
		
		int max_len = Math.max(a.length(), b.length());
		
		// 덧셈 과정에서 올림되어 자릿수 늘어날 수 있으므로 +1 
		int [] A = new int[max_len + 1];
		int [] B = new int[max_len + 1];
		
		for(int i=a.length()-1; i>=0; i--) {
			A[a.length()-1-i] = a.charAt(i) - '0';  // 묵시적 형변환 
		}
		for(int j=b.length()-1; j>=0; j--) {
			B[b.length()-1-j] = b.charAt(j) - '0';  // 묵시적 형변환 
		}
		
		for(int i=0; i<max_len; i++) {
			int sum_n = A[i] + B[i];
			A[i] = sum_n % 10;
			A[i+1] += sum_n / 10; 
		}
		if(A[max_len] != 0) 
			System.out.print(A[max_len]);
		// 가장 첫자리가 0이 아닐 때만 출력 
		for(int i=max_len-1; i>=0; i--) {
			System.out.print(A[i]);
		}
		

	}

}