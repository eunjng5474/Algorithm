import java.util.Scanner;
import java.util.Arrays;

public class Main {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int T = sc.nextInt();
		int arr[] = new int[] {25, 10, 5, 1};

		
		for(int t=0; t<T; t++) {
			int money = sc.nextInt();
			
			int result[] = new int[4];
			for(int i=0; i<4; i++) {
				result[i] = money / arr[i];
				money %= arr[i];
			}
			
			for(int n: result) System.out.print(n+" ");
			System.out.println();
		}
		
	}

}