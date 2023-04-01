import java.util.Arrays;
import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int N = sc.nextInt();
		int M = sc.nextInt();
		
		int arr[] = new int[N];
		for(int i=0; i<N; i++) {
			arr[i] = 0;
		}
		
		
		for(int n=0; n<M; n++) {
			int i = sc.nextInt();
			int j = sc.nextInt();
			int k = sc.nextInt();
			
			for(int m=i-1; m<j; m++) {
				arr[m] = k;
			}
		}
		
		for(int num: arr) {
			System.out.print(num+" ");
		}
	}

}