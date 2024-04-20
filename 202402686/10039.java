import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		
		int s1 =sc.nextInt();
		int s2 =sc.nextInt();
		int s3 =sc.nextInt();
		int s4 =sc.nextInt();
		int s5 =sc.nextInt();
		
		if (s1<40) s1 = 40;
		if (s2<40) s2 = 40;		
		if (s3<40) s3 = 40;		
		if (s4<40) s4 = 40;		
		if (s5<40) s5 = 40;
		
		int ev = s1+s2+s3+s4+s5;
				
		System.out.println(ev/5);
		
	
	}
}
