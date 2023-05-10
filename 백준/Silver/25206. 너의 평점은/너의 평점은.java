import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.StringTokenizer;

public class Main {

	public static void main(String[] args) throws IOException{
		double sum = 0;
		double sumGrade = 0;
		// 딕셔너리 -> hashmap
		HashMap<String, Double> scores = new HashMap<String, Double>();
		scores.put("A+", 4.5);
		scores.put("A0", 4.0);
		scores.put("B+", 3.5);
		scores.put("B0", 3.0);
		scores.put("C+", 2.5);
		scores.put("C0", 2.0);
		scores.put("D+", 1.5);
		scores.put("D0", 1.0);
		scores.put("F", 0.0);
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
//		StringTokenizer st;

		for (int i=0; i<20; i++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			String name = st.nextToken();
			double num = Double.parseDouble(st.nextToken());
			String score = st.nextToken();
			
//			System.out.println(score.getClass().getName());
//			System.out.println("P".getClass().getName());
			if(score.equals("P")) {
				continue;
			}
			sum += (num * scores.get(score));
			sumGrade += num; 
			
//			System.out.println(num * scores.get(score));
			
		}
		double avg = sum / sumGrade;
		System.out.printf("%.6f\n", avg);
		

	}

}