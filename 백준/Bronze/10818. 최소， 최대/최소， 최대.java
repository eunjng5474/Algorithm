import java.util.Scanner;
import java.util.Arrays;

public class Main {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int N = sc.nextInt();
		int[] lst = new int[N];
		
		for(int i = 0; i < N; i++) {
			lst[i] = sc.nextInt();
		}
		
		Arrays.sort(lst);  // 정렬 
		System.out.println(lst[0]+" "+lst[N-1]);
		

	}

}