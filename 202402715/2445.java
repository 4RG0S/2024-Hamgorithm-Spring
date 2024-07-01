import java.util.Scanner;
public class Main{
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int a = sc.nextInt();
		int b=1;
		for(int i = a; i>0;i--) {
			for(int j = 0;j<b;j++) {
				System.out.print("*");
			}
			for(int k = i-1;k>0;k--) {
				System.out.print(" ");
			}for(int k = i-1;k>0;k--) {
				System.out.print(" ");
			}for(int j = 0;j<b;j++) {
				System.out.print("*");
			}
			System.out.println();
			b++;
		}
		b=a;
		for(int i = 0; i<a;i++) {
			for(int j = 0;j<b-1;j++) {
				System.out.print("*");
			}
			for(int k = 0;k<i+1;k++) {
				System.out.print(" ");
			}for(int k = 0;k<i+1;k++) {
				System.out.print(" ");
			}for(int j = 0;j<b-1;j++) {
				System.out.print("*");
			}
			System.out.println();
			b--;
		}
		
	}
}
