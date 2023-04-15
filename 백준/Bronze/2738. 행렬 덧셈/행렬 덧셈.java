import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int N = sc.nextInt();
		int M = sc.nextInt();
		int arr[][] = new int[N][M];
		
		for(int i=0; i<2; i++) {
			for(int n=0; n<N; n++) {
				for(int m=0; m<M; m++) {
					arr[n][m] += sc.nextInt();
				}
			}
		}
		
		for(int n=0; n<N; n++) {
			for(int m=0; m<M; m++) {
				System.out.print(arr[n][m]+" ");
			}
			System.out.println();
		}

	}

}