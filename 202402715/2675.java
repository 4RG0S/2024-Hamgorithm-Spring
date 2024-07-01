import java.util.Scanner;
public class Main {
	public static void main(String[] args){
		Scanner sc = new Scanner(System.in);
		int num = sc.nextInt();
		for(int i = 0; i<num;i++) {
			int a = sc.nextInt();
			String line = sc.next();
			
			for(int j = 0; j<line.length();j++) {
				
				for(int k = 0; k<a;k++) {
					System.out.print(line.charAt(j));

				}
			}
			System.out.print("\n");
		}
	}
}