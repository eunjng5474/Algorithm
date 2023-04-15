import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int arr[][] = new int[9][9];
		
		for(int i=0; i<9; i++) {
			String[] strArr = br.readLine().split(" ");
			for(int j=0; j < strArr.length; j++) {
				arr[i][j] = Integer.parseInt(strArr[j]);
			}
		}
		
		int max_n = 0;
		int row = 0;
		int col = 0;
		
		for(int i=0; i<9; i++) {
			for(int j=0; j<9; j++) {
				if(arr[i][j] > max_n) {
					max_n = arr[i][j];
					row = i;
					col = j;
				}
			}
		}
		
		System.out.println(max_n);
		System.out.println((row+1)+" "+(col+1));

	}

}