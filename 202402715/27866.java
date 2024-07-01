import java.util.Scanner;
public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		String line = sc.nextLine();
		int i = sc.nextInt();
		char k = line.charAt(i-1);
		System.out.print(k);
	}
}
