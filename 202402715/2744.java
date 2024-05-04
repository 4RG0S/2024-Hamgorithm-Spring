import java.util.Scanner;
public class Main {
	public static void main(String[] args){
		Scanner sc = new Scanner(System.in);
		String in = sc.nextLine();
		for(int i = 0; i<in.length();i++) {
			if(in.charAt(i)>='A'&&in.charAt(i)<='Z') {
				System.out.print((char)(in.charAt(i)+32));
			}else if(in.charAt(i)>='a'&&in.charAt(i)<='z') {
				System.out.print((char)(in.charAt(i)-32));
			}
		}
	}
}