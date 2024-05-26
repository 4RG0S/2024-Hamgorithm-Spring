import java.util.Scanner;
public class Main{
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int a = sc.nextInt();
		for(int i = 0; i<=a;i++) {
			for(int j = 0; j<i;j++) {
				System.out.print(" ");
			}for(int k= a;k>i;k--) {
				System.out.print("*");
			}for(int t = a-1;t>i;t--) {
				System.out.print("*");
			}
			System.out.println();
		}
	}
}