import java.util.Scanner;
public class Main {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int N = sc.nextInt();
		int M = sc.nextInt();
		
		int arr[] = new int[N+1];
		for(int i=0; i<N+1; i++) {
			arr[i] = i;
		}
		
		for(int m=0; m<M; m++) {
			int i = sc.nextInt();
			int j = sc.nextInt();
			
			int tmp = arr[i];
			arr[i] = arr[j];
			arr[j] = tmp;
		}
		
		for(int i=1; i<N+1; i++) {
			System.out.print(arr[i]+" ");
		}

	}

}