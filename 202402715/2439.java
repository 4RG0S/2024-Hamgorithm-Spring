import java.util.Scanner;
public class Main{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int star = sc.nextInt();
        for(int i = 0; i<star; i++){
        	for(int k = 1; k < star - i; k++){
                System.out.print(" ");
        	}
            for(int j = 0; j<=i; j++){
                System.out.print("*");
            }
            System.out.printf("\n");
        }
    }
}