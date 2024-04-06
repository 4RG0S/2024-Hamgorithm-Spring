import java.util.*;
import java.io.*;
import java.util.stream.IntStream;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        // input
        StringTokenizer s=new StringTokenizer(br.readLine()," ");
        int N=Integer.parseInt(s.nextToken());
        int p1Num=Integer.parseInt(s.nextToken());
        int p2Num=Integer.parseInt(s.nextToken());

        // data init & logic
        ArrayList<Integer> p1Arr = predict(p1Num);
        ArrayList<Integer> p2Arr = predict(p2Num);

        int ans = -1;

        ArrayList<Integer> smaller = p1Arr.size()<p2Arr.size() ? p1Arr : p2Arr;
        IntStream.range(0, Math.max(p1Arr.size(),p2Arr.size()) - Math.min(p1Arr.size(),p2Arr.size()))
                .forEach(i->smaller.add(1));

        for(int i=0;i < smaller.size();i++){
            int p1 = p1Arr.get(i);
            int p2 = p2Arr.get(i);

            if(p1 - p2 ==0){
                ans = i;
                break;
            }
        }

        // result
        System.out.println(ans);
    }

    public static ArrayList<Integer> predict(int num){
        ArrayList<Integer> arr = new ArrayList<>();
        int pNum = num;
        arr.add(pNum);

        while(pNum > 1){
            pNum = (pNum / 2) + (pNum % 2);
            arr.add(pNum);
        }

        return arr;
    }
}