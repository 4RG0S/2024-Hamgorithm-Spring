import java.util.Scanner;
public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int num = sc.nextInt();
		for(int i = 0; i<num/4;i++) {
			System.out.print("long ");
		}
		System.out.print("int");
	}
}