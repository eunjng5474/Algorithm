import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.math.BigInteger;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int l = Integer.parseInt(br.readLine());
		String str = br.readLine();
		
		BigInteger num = new BigInteger("0");
		for(int i=0; i<l; i++) {
			BigInteger tmp = BigInteger.valueOf(str.charAt(i) - 96).multiply(BigInteger.valueOf(31).pow(i));
			num = num.add(tmp);
		}
		System.out.println(num.remainder(BigInteger.valueOf(1234567891)));

	}

}