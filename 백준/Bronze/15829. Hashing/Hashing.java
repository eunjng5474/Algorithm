import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.math.BigInteger;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int L = Integer.parseInt(br.readLine());
		String str = br.readLine();
		long result = 0;
		long r = 1;
		for(int i=0; i<L; i++) {
			result += (str.charAt(i) - 96)*r;
			r = (r*31) % 1234567891;
		}
		System.out.println(result % 1234567891);
	}

}