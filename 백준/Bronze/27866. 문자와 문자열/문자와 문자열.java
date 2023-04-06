import java.util.Scanner;
public class Main {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		String s = sc.next();
		int i = sc.nextInt();
		
		char sol = s.charAt(i-1);
		System.out.println(sol);
		
	}

}