import java.util.Scanner;
public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int n = sc.nextInt();
		int out = n*(n+1)/2;
		System.out.print(out);
	}
}