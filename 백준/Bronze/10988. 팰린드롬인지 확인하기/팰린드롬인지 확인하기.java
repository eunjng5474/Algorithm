import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String str = br.readLine();
		int len_str = str.length();
		int result = 1;
		
		for(int i=0; i<(len_str/2); i++) {
			if(str.charAt(i) != str.charAt(len_str-i-1)) {
				result = 0;
				break;
			} 
		}
		System.out.println(result);
	}

}