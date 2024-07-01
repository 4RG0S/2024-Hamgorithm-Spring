import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        // input
        String inputs = br.readLine();

        // data init
        HashMap<String, String> pairs = new HashMap<>();
        Stack<String> stk = new Stack<>();

        long ans = 0;

        pairs.put(")","(");
        pairs.put("]","[");

        // logic
        logic : for(int i=0;i<inputs.length();i++){
            String c = String.valueOf(inputs.charAt(i));

            switch (c){
                case "(":
                case "[":
                    stk.push(c);
                    break;
                case ")":
                case "]":
                    long sum = 0;
                    while (!stk.isEmpty() && isNumber(stk.peek())){
                        sum += Integer.parseInt(stk.pop());
                    }

                    if(!stk.isEmpty() && stk.peek().equals(pairs.get(c))){
                        stk.pop();
                        int num = c.equals(")") ? 2 : 3;
                        sum = Math.max(1,sum);
                        stk.push(String.valueOf(sum*num));
                    }else{
                        break logic;
                    }
            }
        }

        // result
        while(!stk.isEmpty()) {
            String c = stk.pop();
            if (isNumber(c)) {
                ans+=Integer.parseInt(c);
            } else {
                ans = 0;
                break;
            }
        }

        System.out.println(ans);
    }

    public static boolean isNumber(String c){
        return !"([".contains(c);
    }


}