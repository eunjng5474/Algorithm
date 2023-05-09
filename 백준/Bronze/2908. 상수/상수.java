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

		int changeA = 0;
		int changeB = 0;
		
		for(int i=0; i<3; i++) {
			changeA += ((a.charAt(i) - 48) * (int) Math.pow(10, i));
			changeB += ((b.charAt(i) - 48) * (int) Math.pow(10, i));
		}
		
		if(changeA > changeB) {
			System.out.println(changeA);
		} else {
			System.out.println(changeB);
		}
	}

}