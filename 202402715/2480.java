import java.util.Arrays;
import java.util.Scanner;
public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int a = sc.nextInt();
		int b = sc.nextInt();
		int c = sc.nextInt();
		int[] array = {a,b,c};
	
		if(a==b) {
			if (a==c) {//a=b=c
				int out = 10000+a*1000;
				System.out.print(out);
			}else {//a=b!=c
				int out = 1000+a*100;
				System.out.print(out);
			}
		}else if (a==c){//a=c!=b
			int out = 1000+a*100;
			System.out.print(out);
		}else if (c==b) {//c=b!=a
			int out = 1000+b*100;
			System.out.print(out);
		}else {//a!=b!=c
			Arrays.sort(array);
			int k = array[array.length-1];
			int out = k*100;
			System.out.print(out);
		}
	}
}