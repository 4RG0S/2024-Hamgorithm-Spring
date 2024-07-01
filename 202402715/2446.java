import java.util.Scanner;
public class Main{
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int a = sc.nextInt();
		int b = 0;
		for(int i = a; i>0;i--) {
			for(int j = 0;j<b;j++) {
				System.out.print(" ");
			}
			for(int k = 2*i-1;k>0;k--) {
				System.out.print("*");
			}
			System.out.println();
			b++;
		}
		b=a;
		for(int i = 1; i<a;i++) {
			for(int j = 1;j<b-1;j++) {
				System.out.print(" ");
			}
			for(int k = 0;k<2*i+1;k++) {
				System.out.print("*");
			}
			System.out.println();
			b--;
		}
		
	}
}