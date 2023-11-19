import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        while (true) {
            String str = br.readLine();
            if(str.equals(".")) break;
            boolean flag = true;

            Stack<Character> stack = new Stack<>();

            for (int i = 0; i < str.length(); i++) {
                char c = str.charAt(i);
                if (c == '(' || c == '[') stack.push(c);
                else if (c == ')') {
                    if (stack.empty() || stack.peek() != '(') {
                        sb.append("no");
                        flag = false;
                        break;
                    } else stack.pop();
                } else if (c == ']') {
                    if (stack.empty() || stack.peek() != '[') {
                        sb.append("no");
                        flag = false;
                        break;
                    } else stack.pop();
                }
            }
            if (flag) {
                if(stack.empty()) sb.append("yes");
                else sb.append("no");
            }
            sb.append("\n");
        }
        System.out.println(sb);
    }
}