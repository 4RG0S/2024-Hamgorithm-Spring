import java.util.Scanner;
public class Main{
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		int F = sc.nextInt();
		
		String k = Integer.toString(N);
		int v1 = k.charAt(k.length()-1)-48;
		int v2 = k.charAt(k.length()-2)-48;
//		System.out.println(v1);
//		System.out.println(v2);
		
		int N2 = N -10*v2 -v1;
///		System.out.println(N2);
		
		for(int a = 0; a<10;a++) {
			for(int b = 0; b<10;b++) {
				int N3 = N2 + 10*a + b;
				if(N3%F==0) {
					System.out.print(a);
					System.out.print(b);
					System.exit(0);
				}
			}
		}
		
	}
}