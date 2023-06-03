import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		int arr[] = new int[8];
		String result = "";
		
		for(int i=0; i<8; i++) {
			int n = Integer.parseInt(st.nextToken());
			arr[i] = n;
		}
		for(int i=0; i<7; i++) {
			if(arr[i+1] == arr[i] + 1) {
				result = "ascending";
			} else if(arr[i+1] == arr[i] - 1) {
				result = "descending";
			} else {
				// 한 번이라도 아니면 mixed 후 break 
				result = "mixed";
				break;
			}
		}
		System.out.println(result);

	}

}