import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		Scanner sc = new Scanner(System.in);
		
		int N =sc.nextInt();
		
		for(int i=1;i<=N;i++){
			for(int l=1; l<i; l++) {System.out.print(' ');};
			for(int k=N; k>=i; k--) {System.out.print('*');};
		System.out.println();
		}
		

	}
}
