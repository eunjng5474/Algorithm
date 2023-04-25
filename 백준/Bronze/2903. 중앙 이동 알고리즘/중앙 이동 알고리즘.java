import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int n = Integer.parseInt(br.readLine());
		
		// (1 + (2**n))**2
		long num = 1 + (long) Math.pow(2, n);
		System.out.println((long)Math.pow(num, 2));

	}

}