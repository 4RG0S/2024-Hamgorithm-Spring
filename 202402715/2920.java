import java.util.Scanner;
public class Main {
	public static void main(String[] args){
		Scanner sc = new Scanner(System.in);
		int[] in = new int[8];
		for(int i = 0; i<in.length; i++) {
			in[i]=sc.nextInt();
		}
		
		if(in[0]==8) {
			for(int i = 1;i<8;i++) {
				if(in[i]==in[i-1]-1) {
					if(i==7&&in[i]==1) {
						System.out.print("descending");
					}else {
						continue;
					}
				}else {
					System.out.print("mixed");
					break;
				}
			}
		}else if(in[0]==1) {
			for(int i = 1;i<8;i++) {
				if(in[i]==in[i-1]+1) {
					if(i==7&&in[i]==8) {
						System.out.print("ascending");
					}else {
						continue;
					}
				}else {
					System.out.print("mixed");
					break;
				}
			}
		}else {
			System.out.print("mixed");
		}
	}
}