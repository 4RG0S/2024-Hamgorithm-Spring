import java.util.Scanner;
public class Main{
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		String a = sc.next();
		String b = sc.next();
		int a1 = a.length();
		int b1 = b.length();
		
		if(a1>b1) {
			System.out.println("go");
		}else if(a1==b1) {
			System.out.println("go");
		}
		else {
			System.out.println("no");
		}
	}
}