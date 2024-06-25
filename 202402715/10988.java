import java.util.Scanner;
public class Main{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        String in = sc.next();
        int len = in.length();
        int a = 0;
        int z = len-1;
        while(a<z) {
        	if(in.charAt(a)!=in.charAt(z)) {
        		System.out.println("0");
        		System.exit(0);
        	}
        	a++; z--;
        }
        System.out.println("1");
    }
}