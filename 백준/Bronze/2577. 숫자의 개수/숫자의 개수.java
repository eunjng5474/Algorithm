import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int a = Integer.parseInt(br.readLine());
		int b = Integer.parseInt(br.readLine());
		int c = Integer.parseInt(br.readLine());

		int val = a * b * c;
		int[] arr = new int[10];
		
		while(val!=0) {
			arr[val % 10]++;
			val/=10;
		}
		
		for (int num : arr) {
			System.out.println(num);
		}
	}

}