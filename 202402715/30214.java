import java.util.Scanner;
public class Main{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt();
        int b = sc.nextInt();
        a = a*2;
        if(a<b){
            System.out.print("H");
        }else{
            System.out.print("E");
        }
    }
}