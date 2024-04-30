import java.util.Scanner;
public class Main {
	public static void main(String[] args){
		Scanner sc = new Scanner(System.in);
		String in = sc.next();
		int num = in.length();
		int sum = 0;
		for(int i = 0; i<num;i++) {
			int a = in.charAt(i);
			switch((a-65)/3){
				case 0 : sum += 3; //ABC
				break;
				case 1 : sum += 4; //DEF
				break;
				case 2 : sum += 5; //GHI
				break;
				case 3 : sum += 6; //JKL
				break;
				case 4 : sum += 7; //MNO
				break;
				case 5 : sum += 8;
				break;
				case 6 :
					if(in.charAt(i)== 'S') {
						sum += 8; //PGR S
					}else {
						sum += 9; //PGR S
					}
				break;
				case 7 :
					if(in.charAt(i)== 'V') {
						sum += 9; //PGR S
					}else {
						sum += 10; //PGR S
					}
				break;
				case 8 : sum += 10;
				break;
				
			}
		}
		System.out.print(sum);
	}
}