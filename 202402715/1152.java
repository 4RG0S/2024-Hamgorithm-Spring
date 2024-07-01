import java.util.Scanner;
public class Main {
	public static void main(String[] args){
		Scanner sc = new Scanner(System.in);
		String line = sc.nextLine();
		int count = 0;
		
		for(int i = 0; i<line.length();i++) {
			if(line.charAt(i)==' ') {
				count++;
			}
		}
		
		if(line.charAt(0)==' '&&line.charAt(line.length()-1)==' ') {
			System.out.print(count-1);
		}else if(line.charAt(0)==' '||line.charAt(line.length()-1)==' ') {
			System.out.print(count);
		}else {
			System.out.print(count+1);
		}
	}
}