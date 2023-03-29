import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int h = sc.nextInt();
		int m = sc.nextInt();
		
		if(m-45 < 0) {
			h -= 1;
			m += 15;
		}
		else {
			m -= 45;
			}
		if(h>=24) {
			h -= 24;
		}
		if(h<0) {
			h += 24;
		}
		
		System.out.println(h+" "+m);
	}

}