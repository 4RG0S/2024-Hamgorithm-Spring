import java.util.Scanner;
public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int length = sc.nextInt();
		String num = sc.next();
		int sum = 0;
		for(int i = 0; i<length; i++) {
			char a = num.charAt(i);
			sum += a;
		}
		sum = sum - 48*length;
		System.out.print(sum);
	}
}