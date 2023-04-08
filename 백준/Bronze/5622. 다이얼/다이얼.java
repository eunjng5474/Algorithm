import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		String str = sc.next();
		int len_str = str.length();
		int result = 0;
		char tmp;
		
		for(int i=0; i<len_str; i++) {
			tmp = str.charAt(i);
			
			if(tmp>='A' && tmp<='C') {
				result += 3;
			} else if (tmp>='D' && tmp<='F') {
				result += 4;
			} else if (tmp>='G' && tmp<='I') {
				result += 5;
			} else if (tmp>='J' && tmp<='L') {
				result += 6;
			} else if (tmp>='M' && tmp<='O') {
				result += 7;
			} else if (tmp>='P' && tmp<='S') {
				result += 8;
			} else if (tmp>='T' && tmp<='V') {
				result += 9;
			} else if (tmp>='W' && tmp<='Z') {
				result += 10;
			}
		}
		System.out.println(result);
	}

}