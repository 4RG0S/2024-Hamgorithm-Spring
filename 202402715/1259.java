import java.util.Scanner;
public class Main {
	public static void main(String[] args){
		Scanner sc = new Scanner(System.in);
		A:
		while(true) {
			String val = sc.next();
			if(val.equals("0")) {
				break A;
			}
			int k = val.length()-1;
			int count = 0;
			
			while(true) {
				if(k>=count) {
//					System.out.println("t1");
					if(val.charAt(count) == val.charAt(k)) {
						if((count == k)||count+1==k) {
								System.out.println("yes");
								break;
						}
						
						count++;
						k--;
						
					}else{
//						System.out.println("t3");
						System.out.println("no");
						break;
					}
				}
			}

		}
	
	}
}