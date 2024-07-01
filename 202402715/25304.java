import java.util.Scanner;
public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int total = sc.nextInt();
		int ea = sc.nextInt();
		int[] in = new int[2*ea];
		int[] arrtotal = new int[ea];
		int out = 0;
		int j = 0;
		for(int i = 0; i<in.length; i++) {
			in[i] = sc.nextInt();
		}
		
		for(int i=0; i<in.length;i++) {
			if(i%2==1) {
				arrtotal[j]=in[i-1]*in[i];
				j++;
			}
		}
		
		for(int i=0; i<arrtotal.length;i++) {
			out = out + arrtotal[i];

		}
		if(total == out) {
			System.out.print("Yes");
		}else {
			System.out.print("No");
		}
	}
}