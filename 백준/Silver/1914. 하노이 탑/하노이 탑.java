import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.math.BigInteger;

public class Main {
	static StringBuilder sb = new StringBuilder();

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int n = Integer.parseInt(br.readLine());
		
//		System.out.println((int)Math.pow(2, n) - 1);
		//n이 클 경우 long 초과 -> BigInteger 사용 
		BigInteger bi = new BigInteger("2");
		BigInteger cnt = (bi.pow(n)).subtract(BigInteger.ONE);
		// 2**n - 1 (pow : 제곱, subtract : 뺄셈) 
		System.out.println(cnt);
		
		if(n <= 20) {
			hanoi(n, 1, 3, 2);
			System.out.println(sb);
		}
	}
	
	public static void hanoi(int n, int start, int end, int tmp) {
		if(n == 1) {
			sb.append(start + " " + end + "\n");
//			System.out.println(start + " " + end);
			return;
		}
		
		hanoi(n-1, start, tmp, end);
		sb.append(start + " " + end + "\n");
		hanoi(n-1, tmp, end, start);
	}
}