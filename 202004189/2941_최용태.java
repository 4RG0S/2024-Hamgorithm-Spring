import java.util.*;
import java.io.*;

public class 2941_최용태 {
    static int ptr = 0;
    public static void main(String[] args) throws IOException {
        HashSet<String> dict =initDictionary();

        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));

        char[] context = br.readLine().toCharArray();
        int ans = 0;


        while(ptr< context.length){
            String case1 = getLetter(ptr,context)+getLetter(ptr+1,context);
            String case2 = case1+getLetter(ptr+2,context);

            if(dict.contains(case2)){
                ptr+=3;
            } else if(dict.contains(case1)){
                ptr+=2;
            } else{
                ptr++;
            }

            if(!(case1.charAt(0)>='a' && case1.charAt(0)<='z')) continue;

            ans++;
        }


        System.out.println(ans);
    }

    public static String getLetter(int ptr,char[] context){
        return ptr < context.length ? context[ptr]+"":"";
    }
    public static HashSet initDictionary(){
        // 사전에 등록된 크로아티아 알파벳
        HashSet<String> dict = new HashSet<>();

        dict.add("c-");
        dict.add("dz=");
        dict.add("d-");
        dict.add("lj");
        dict.add("nj");
        dict.add("s=");
        dict.add("z=");

        return dict;
    }


}