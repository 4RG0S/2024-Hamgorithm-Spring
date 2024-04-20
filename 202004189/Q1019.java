import java.io.*;
import java.util.*;
import java.util.stream.IntStream;

public class Q1019 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        // input
        String originalNum = br.readLine();

        // data init
        int[] ans = new int[10];
        int currentDegreeIndex = originalNum.length()-1;
        int totalNumLength  = originalNum.length();

        // logic
        for(;currentDegreeIndex>=0;currentDegreeIndex--){
            int[] tempNumsArray = new int[10];
            int overNumber = getOverNumber(originalNum,currentDegreeIndex);
            int degree = getDegree(totalNumLength-currentDegreeIndex);
            int previousNumber = getPreviousNumber(originalNum,currentDegreeIndex);

            // f1
            tempNumsArray[0] = overNumber * degree;

            // f2
            for(int i=1;i<10;i++){
                tempNumsArray[i] = (overNumber+1) * degree;
            }

            // loss
            int currentNum = originalNum.charAt(currentDegreeIndex)-'0';

            tempNumsArray[currentNum] -= (degree - previousNumber - 1); // self num loss

            for(int i=currentNum+1;i<10;i++){
                tempNumsArray[i] -= degree;
            } // next num loss

            IntStream.range(0,ans.length).forEach(i->ans[i]+=tempNumsArray[i]);
        }


        // result
        StringBuilder writer = new StringBuilder();
        IntStream.range(0,ans.length).forEach(i->writer.append(ans[i]).append(" "));
        
        System.out.println(writer);
    }
    public static int getOverNumber(String numString, int untilIndex){
        if(untilIndex == 0){
            return 0;
        }

        return Integer.parseInt(numString.substring(0,untilIndex));
    }

    public static int getPreviousNumber(String numString, int startIndex){
        int untilIndex= numString.length();

        if(startIndex == untilIndex-1){
            return 0;
        }

        return Integer.parseInt(numString.substring(startIndex+1,untilIndex));
    }

    public static int getDegree(int tries){
        int result = 1;

        for(int i=0;i<tries-1;i++){
            result*=10;
        }

        return result;
    }
}
