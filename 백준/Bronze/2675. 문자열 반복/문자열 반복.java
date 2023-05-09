import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int t = Integer.parseInt(br.readLine());
		StringTokenizer st;
		
		for(int i=0; i<t; i++) {
			st = new StringTokenizer(br.readLine());
			int num = Integer.parseInt(st.nextToken());
			String str = st.nextToken();
			
			StringBuilder sb = new StringBuilder();
			for(int j=0; j<str.length(); j++) {
				for(int k=0; k<num; k++) {
					sb.append(str.charAt(j));
				}
			}
			System.out.println(sb);
		}
		
		

	}

}