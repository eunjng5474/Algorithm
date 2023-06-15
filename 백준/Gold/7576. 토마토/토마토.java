import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
	static int[] dx = {-1, 1, 0, 0};
	static int[] dy = {0, 0, -1, 1};
	
	static int m;
	static int n;
	static int result;
	
	static int[][] arr;
	static int[][] visited;
	static Queue<int[]> q;
	
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		st = new StringTokenizer(br.readLine());
		
		m = Integer.parseInt(st.nextToken());
		n = Integer.parseInt(st.nextToken());
		arr = new int[n][m];
		visited = new int[n][m];
		q = new LinkedList<>();
		
		for(int i=0; i<n; i++) {
			st = new StringTokenizer(br.readLine());
			for(int j=0; j<m; j++) {
				arr[i][j] = Integer.parseInt(st.nextToken());
//				visited[i][j] = -1;
				if(arr[i][j] == 1) {
					q.add(new int[] {i, j});
					// 시작 위치(1) q에 추가하고, visited에 1(시작점)  
					visited[i][j] = 1;
				} else if(arr[i][j] == -1) {
					visited[i][j] = -1;
					// visited에 -1로 저장해서 갈 수 없음을 표시 
					// 즉, visited에서 값이 0이면 갈 수 있는 곳, 1이면 시작점, -1이면 토마토 없는 곳 
				}
			}
		}
		
		bfs();
		System.out.println(result);
		
//		for(int i=0; i<n; i++) {
//			for(int j=0; j<m; j++) {
//				System.out.print(visited[i][j] + " ");
//			}
//			System.out.println();
//		}
	}
	
	
	public static void bfs() {
		
		while(!q.isEmpty()) {
			int[] rm = q.remove();
			int x = rm[0];
			int y = rm[1];
			
			for(int d=0; d<4; d++) {
				int nx = x + dx[d];
				int ny = y + dy[d];
				
				if(nx<0 || nx>=n || ny<0 || ny>=m) continue;
//				// arr[nx][ny] == 0 && 
				if(visited[nx][ny] == 0) {
					visited[nx][ny] = visited[x][y] + 1;
					q.add(new int[]{nx, ny});
				}
			}
		}
		if(!check()) {
			result = -1;
			// 다 익지 못하면 결과는 -1 
		} else {
			for(int i=0; i<n; i++) {
				for(int j=0; j<m; j++) {
					if (visited[i][j] > result) {
						result = visited[i][j];
						// visited 중 최대값이 토마토가 모두 익는 데까지 걸리는 날짜 수
					}
				}
			}
			result--; // 1부터 시작했기 때문에 1을 빼줌 
		}
	}
	
	// visited에 0이 있다면 토마토가 모두 익지 못하는 상황 
	// 따라서 boolean으로 체크 
	public static boolean check() {
		for(int i=0; i<n; i++) {
			for(int j=0; j<m; j++) {
				if(visited[i][j] == 0) return false;
			}
		}
		return true;
	}
	}

//}