import java.util.Scanner;
import java.util.Arrays;
public class Main{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt();
        int b = sc.nextInt();
        long[] v1 = new long[a];
        long[] v2 = new long[b];

        for(int i = 0; i<a;i++){
            v1[i]=sc.nextLong();
        }
        Arrays.sort(v1);
        for(int i = 0; i<b;i++){
            v2[i]=sc.nextLong();
        }
        Arrays.sort(v2);
        
        System.out.print(v1[a-1]+v2[b-1]);
    }
}