import java.util.Arrays;
import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int a = sc.nextInt();
		int b = sc.nextInt();
		int c = sc.nextInt();
		
		if(a == b && b == c && c == a) {
			System.out.println(10000+a*1000); 
		}
		else if(a == b || b == c ) {
			System.out.println(1000+b*100);
		}
		else if(a == c) {
			System.out.println(1000+a*100);
		}
		else {
			int arr[] = new int[3];
			arr[0] = a;
			arr[1] = b;
			arr[2] = c;
			
			Arrays.sort(arr);
			System.out.println(arr[2]*100);

		}

	}

}