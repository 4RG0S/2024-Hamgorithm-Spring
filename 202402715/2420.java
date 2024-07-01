import java.util.Scanner;
public class Main {
	public static void main(String[] args){
		Scanner sc = new Scanner(System.in);
		long a = sc.nextLong();
		long b = sc.nextLong();
		if(a>b) {
			if(a-b>0) {
				System.out.print(a-b);
			}else {
				System.out.print(-a+b);
			}
		}else if(a==b) {
			System.out.print('0');
		}else if(a<b) {
			if(b-a>0) {
				System.out.print(b-a);
			}else {
				System.out.print(-b+a);
			}
			
		}
	}
}