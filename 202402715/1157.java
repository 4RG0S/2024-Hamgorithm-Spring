import java.util.Scanner;
public class Main {
	public static void main(String[] args){
		Scanner sc = new Scanner(System.in);
		String in = sc.next();
		in = in.toUpperCase();
		int count = 0;
		int a = 0;
		int max = Integer.MIN_VALUE;
		int[] alpha = new int[26];
		
		for(int i = 0; i<in.length();i++) {
//			System.out.print(in.charAt(i));
			alpha[in.charAt(i)-65]++;
		}
//		System.out.print("\n");

		for(int i = 0; i<alpha.length;i++) {
//			System.out.print(alpha[i]);

			if(alpha[i]>max) {
				max = alpha[i];
				a=i;
			}
//			System.out.println(max);

		}
//		System.out.print("\n");

		for(int i = 0; i<alpha.length;i++) {
			if(alpha[i] == max) {
				count++;
			}
		}
//		System.out.println(max);
//		System.out.println(count);
		if(count!=1) {
			System.out.print('?');
		}
		else {
			System.out.print((char)(a+65));
		}
		
	}
}