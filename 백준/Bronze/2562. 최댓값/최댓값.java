import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int max_num = 0;
		int max_idx = 0;
		
		for(int i = 0; i < 9; i++) {
			int x = sc.nextInt();
			
			if(x > max_num) {
				max_num = x;
				max_idx = i+1;
			}
		}
		
		System.out.println(max_num);
		System.out.println(max_idx);

	}

}