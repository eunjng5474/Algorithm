import java.util.Scanner;
public class Main {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int tc = sc.nextInt();
		for(int t=0; t<tc; t++) {
			String str = sc.next();
			int len_str = str.length();
			
			System.out.print(str.charAt(0));
			System.out.print(str.charAt(len_str-1));
			System.out.println();
		}
		
	}

}