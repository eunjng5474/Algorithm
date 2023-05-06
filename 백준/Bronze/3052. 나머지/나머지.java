import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int arr[] = new int[42];
		int cnt = 0;
		
		for(int i=0; i<10; i++) {
			int num = Integer.parseInt(br.readLine());
			if(arr[num % 42] == 0) {
				cnt ++;
			}
			arr[num % 42] = 1;
		}
		System.out.println(cnt);
	}

}