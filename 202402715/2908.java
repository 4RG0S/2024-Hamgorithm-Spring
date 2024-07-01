import java.util.Scanner;
public class Main {
	public static void main(String[] args){
		Scanner sc = new Scanner(System.in);
		int a = sc.nextInt();
		int b = sc.nextInt();
		
		int a100 = a/100;
		int a10 = (a- a100*100)/10;
		int a1 = a- a100*100 - a10*10;
		
		int b100 = b/100;
		int b10 = (b- b100*100)/10;
		int b1 = b- b100*100 - b10*10;
		
		int aa = a100 + a10*10 + a1*100;
		int bb = b100 + b10*10 + b1*100;
		if(aa>bb) {
			System.out.print(aa);
		}else {
			System.out.print(bb);
		}
	}
}