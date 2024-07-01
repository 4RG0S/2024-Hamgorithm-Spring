import java.util.Scanner;
public class Main {
	public static void main(String[] args){
		Scanner sc = new Scanner(System.in);
		int num = sc.nextInt();
		
		for(int i =0; i<num;i++) {
			String line = sc.next();
			System.out.print(line.charAt(0));
			System.out.println(line.charAt(line.length()-1));
		}
	}
}