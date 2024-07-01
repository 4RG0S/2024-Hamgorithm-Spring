import java.util.Scanner;
public class Main{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt();
        int b = sc.nextInt();
        
        String B = ""+b;
        int t = (int)B.charAt(0)-48;
        int k = (int)B.charAt(1)-48;
        int j = (int)B.charAt(2)-48;
        
        System.out.println(a*j);
        System.out.println(a*k);
        System.out.println(a*t);
        System.out.println(a*b);

        
    }
}