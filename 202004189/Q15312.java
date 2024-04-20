import java.util.*;
import java.io.*;
import java.util.stream.IntStream;

public class Q15312 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        // input
        String p1 = br.readLine();
        String p2 = br.readLine();

        // data init
        int[] num = {3, 2, 1, 2, 3, 3, 2, 3, 3, 2, 2, 1, 2, 2, 1, 2, 2, 2, 1, 2, 1, 1, 1, 2, 2, 1};
        ArrayList<Integer> nums = new ArrayList<>();
        ArrayList<Character> combinedName = new ArrayList<>();

        for(int i=0;i<p1.length();i++){
            combinedName.add(p1.charAt(i));
            combinedName.add(p2.charAt(i));
        }


        // logic
        for(int i =0 ; i<combinedName.size()-1;i++){
            char pc1 = combinedName.get(i);
            char pc2 = combinedName.get(i+1);

            int combined = combined(num[idx(pc1)], num[idx(pc2)]);
            nums.add(combined);
        }

        while(nums.size() > 2){
            ArrayList<Integer> currentNums = new ArrayList<>();

            for(int i=0;i<nums.size()-1;i++){
                int n1 = nums.get(i);
                int n2 = nums.get(i+1);
                currentNums.add(combined(n1,n2));
            }

            nums = currentNums;
        }

        // result
        System.out.println((nums.get(0))+""+(nums.get(1)));
    }

    public static int idx(char c){
        return (c-'A');
    }
    public static int combined(int a, int b){
        return (a+b) % 10;
    }
}