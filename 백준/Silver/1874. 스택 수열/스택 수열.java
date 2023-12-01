import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.Stack;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int[] sequence = new int[n];
        for (int i = 0; i < n; i++) {
            sequence[i] = Integer.parseInt(br.readLine());
        }

        Stack<Integer> stack = new Stack<>();
        int[] arr = new int[n];
        StringBuilder sb = new StringBuilder();

        int check = 0;
        int idx = 0;

        for (int num : sequence) {
            if (num >= check) {
                for (int i = check + 1; i <= num; i++) {
                    stack.push(i);
                    sb.append("+").append("\n");
                }
                arr[idx] = stack.pop();
                sb.append("-").append("\n");
                check = num;
            } else {
                arr[idx] = stack.pop();
                sb.append("-").append("\n");
            }
            idx++;
        }
        boolean flag = true;
        for (int i = 0; i < n; i++) {
            if (sequence[i] != arr[i]) {
                flag = false;
                break;
            }
        }

        if(flag){ System.out.println(sb);}
        else System.out.println("NO");

    }
}