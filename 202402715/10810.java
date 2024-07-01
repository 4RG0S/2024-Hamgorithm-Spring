import java.util.Scanner;
public class Main {
	public static void main(String[] args){
		Scanner sc = new Scanner(System.in);
		int in = sc.nextInt();
		int[] box = new int[in];
		int num = sc.nextInt(); //횟수
		
		for(int i = 0; i<num; i++) {
			int a = sc.nextInt();
			int b = sc.nextInt();
			int c = sc.nextInt();
			for(int k=a-1;k<=b-1;k++) {
				box[k]=c;
			}
			
		}
		for(int j = 0; j<in;j++) {
			System.out.printf("%d ",box[j]);
		}
	}
}