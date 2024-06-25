import java.util.Scanner;
public class Main{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int[] val = {1,1,2,2,2,8};
        int[] in = new int[6];
        for(int i = 0; i<6;i++) {
        	in[i]=sc.nextInt();
        }
        for(int i = 0; i<6;i++) {
        	System.out.print(val[i]-in[i]+" ");;
        }
        
    }
}