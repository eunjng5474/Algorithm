import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        int n = Integer.parseInt(br.readLine());
        Stack<Integer> stack = new Stack<Integer>();

        for(int i = 0; i < n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            String str = st.nextToken();

            if(str.equals("push")) {
                stack.push(Integer.parseInt(st.nextToken()));
            } else if(str.equals("pop")) {
                if(stack.empty()) sb.append(-1).append("\n");
                else sb.append(stack.pop()).append("\n");
            } else if(str.equals("size")) {
                sb.append(stack.size()).append("\n");
            } else if(str.equals("empty")) {
                if(stack.empty()) sb.append(1).append("\n");
                else sb.append(0).append("\n");
            } else {
                if(stack.empty()) sb.append(-1).append("\n");
                else sb.append(stack.peek()).append("\n");
            }
        }
        System.out.println(sb);
    }
}