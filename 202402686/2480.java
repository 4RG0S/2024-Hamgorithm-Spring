import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		int r1 =sc.nextInt();
		int r2 =sc.nextInt();
		int r3 =sc.nextInt();
		
		if(r1==r2&&r2==r3) {
			System.out.println(10000+r1*1000);
		}
		else if((r1==r2||r1==r3) && r2 != r3) {
			System.out.println(1000+r1*100);
		}
		else if(r2==r3&&r1!=r2) {
			System.out.println(1000+r2*100);
		}
		else if (r2!=r1&&r2!=r3) {
			int max = r1;
			if(max<r2) max = r2;
			if(max<r3) max = r3;
			System.out.println(max*100);
		}
	}
}
