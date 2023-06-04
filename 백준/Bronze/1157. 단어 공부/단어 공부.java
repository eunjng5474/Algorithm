import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String str = br.readLine();
		int[] arr = new int[26];

		for(int i=0; i<str.length(); i++) {
			char st = str.charAt(i);
			if('A' <= st && st <= 'Z') {
				arr[st - 65] += 1;
			} else {
				arr[st - 97] += 1;
			}
		}
		
		int max = 0;
		char result = '?';
		for(int i=0; i<26; i++) {
			if (arr[i] > max) {
				max = arr[i];
				result = (char) (i+65);
			} else if (arr[i] != 0 && arr[i] == max) {
				result = '?';
			}
		}
		System.out.println(result);

	}

}