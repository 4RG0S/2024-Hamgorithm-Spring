import java.util.Scanner;
public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int a = sc.nextInt();
		if(a == 0) {
			System.out.print(1);
		}else {
			for(int i = a-1;i>0;i--) {
			a = a*i;
			}
			System.out.print(a);
		}
	}
}