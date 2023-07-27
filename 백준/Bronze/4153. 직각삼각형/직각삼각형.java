import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();

		while(true) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			
			int[] nums = new int[3];
			for(int i=0; i<3; i++) {
				nums[i] = Integer.parseInt(st.nextToken());
			}
			
			if(nums[0] == 0 && nums[1] == 0 && nums[2] == 0) break;
			
			Arrays.sort(nums);
			
			if(nums[2]*nums[2] == nums[1]*nums[1] + nums[0]*nums[0]) {
				sb.append("right").append("\n");
			} else {
				sb.append("wrong").append("\n");
			}
		}
		System.out.println(sb);
		

	}

}