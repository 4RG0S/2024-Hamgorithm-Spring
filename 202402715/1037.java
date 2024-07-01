import java.util.Arrays;
import java.util.Scanner;
public class Main{
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		int[] num = new int[N];
		
		for(int i = 0; i<N; i++) {
			num[i] = sc.nextInt();
		}
		
		Arrays.sort(num);
		
//		System.out.println(num[0]);
//		System.out.println(num[num.length-1]);
		System.out.println(num[0]*num[num.length-1]);
		
	}
}