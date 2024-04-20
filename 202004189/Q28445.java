import java.util.*;
import java.io.*;

public class Main {
    static int N;
    static int M;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer x=new StringTokenizer(br.readLine()," ");
        StringTokenizer y=new StringTokenizer(br.readLine()," ");
        HashSet<String> colors = new HashSet<>();

        while(x.hasMoreTokens()){
            colors.add(x.nextToken());
            colors.add(y.nextToken());
        }

        ArrayList<String> arr = new ArrayList<>(colors);
        Collections.sort(arr);

        StringBuilder writer = new StringBuilder();

        for(int i=0;i<arr.size();i++){
            for(int j=0;j<arr.size();j++) {
                writer.append(arr.get(i)).append(" ").append(arr.get(j)).append("\n");
            }
        }


        System.out.println(writer);
    }
}