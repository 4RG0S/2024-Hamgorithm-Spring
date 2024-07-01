import java.util.Arrays;
import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
			int a = sc.nextInt();
			int[]num = new int[a];
			for(int i = 0; i<a;i++) {
				num[i]=sc.nextInt();
			}
			
			Arrays.sort(num);
			for(int i = 0; i<a; i++) {
				System.out.println(num[i]);
			}
	}
}