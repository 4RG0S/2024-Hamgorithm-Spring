import java.util.Scanner;
public class Main{
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int a = sc.nextInt();
		for(int i = a; i>0;i--) {
			for(int j = i-1; j>0;j--) {
				System.out.print(" ");
			}for(int k= i-1;k<a;k++) {
				System.out.print("*");
			}for(int t = i;t<a;t++) {
				System.out.print("*");
			}
			System.out.println();
		}
	}
}