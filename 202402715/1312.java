import java.util.Scanner;
public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int a = sc.nextInt();
		int b = sc.nextInt();
		int num = sc.nextInt();
		int out = a%b*10;
		for(int i = 1; i<num;i++) {
			out = out % b*10;
		}
		out/=b;
		System.out.print(out);
	}
}