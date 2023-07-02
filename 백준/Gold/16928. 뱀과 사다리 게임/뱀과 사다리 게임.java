import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Deque;
import java.util.LinkedList;
import java.util.StringTokenizer;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		st = new StringTokenizer(br.readLine());
		int n = Integer.parseInt(st.nextToken());
		int m = Integer.parseInt(st.nextToken());
		
		int[] move = new int[101];
		for(int i=0; i<(n+m); i++) {
			st = new StringTokenizer(br.readLine());
			int a = Integer.parseInt(st.nextToken());
			int b = Integer.parseInt(st.nextToken());
			move[a] = b;
		}
		
		int[] visited = new int[101];
		Deque<Integer> q = new LinkedList<Integer>();
		q.offer(1);
		visited[1] = 1;
		
		while(!q.isEmpty()) {
			int now = q.poll();
			if(now == 100) {
				System.out.println(visited[100] - 1);
				break;
			}
			for(int i=1; i<7; i++) {
				int next = now + i;
				if(next <= 100 && move[next] != 0) {
					next = move[next];
				}
				if(next > 100 || visited[next] != 0) continue;
				
				visited[next] = visited[now] + 1;
				q.add(next);
			}
		}
		
	}

}