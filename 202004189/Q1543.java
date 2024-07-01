import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Q1543 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        //input
        String file = br.readLine();
        String word = br.readLine();

        //data init
        int ans = 0;
        int i = 0;
        while(i < file.length()){
            int counted = 0;
            int startedIndex = i;
            for(int j=0; i < file.length() && j<word.length();j++){
                if(file.charAt(i)==word.charAt(j)){
                    counted++;
                    i++;
                }else{
                    i = startedIndex + 1;
                    break;
                }
            }

            if(counted == word.length()) ans++;
        }

        System.out.println(ans);
    }
}
