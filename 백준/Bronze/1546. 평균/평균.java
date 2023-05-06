import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int n = Integer.parseInt(br.readLine());
		double arr[] = new double[n];
		double max = 0;
		
		StringTokenizer st = new StringTokenizer(br.readLine());
		for(int i=0; i<n; i++) {
			double num = Double.parseDouble(st.nextToken());
			arr[i] = num;
			if(num > max) {
				max = num;
			}
		}
		
		double sum = 0;
		for(int i=0; i<n; i++) {
			sum += (arr[i] / max * 100);
		}
		System.out.println(sum / n);
	}

}