import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		String a = st.nextToken();
		String b = st.nextToken();
		
		int changeA = Integer.parseInt(new StringBuilder(a).reverse().toString());
		int changeB = Integer.parseInt(new StringBuilder(b).reverse().toString());
		
		System.out.print(changeA > changeB ? changeA : changeB);
	}

}