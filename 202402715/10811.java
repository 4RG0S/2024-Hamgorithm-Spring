import java.util.Scanner;
public class Main {
	public static void main(String[] args){
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt(); //바구니 갯수
		int m = sc.nextInt(); //횟수
		int[] array = new int[n];
		
		for(int i =0; i<n;i++) {
			array[i]=i+1; 
		}
		
		for(int i = 0; i<m;i++) {
			int a = sc.nextInt()-1;
			int b = sc.nextInt()-1;
			int temp = 0;
		
			while(b-a>0) {
				temp = array[a];
				array[a++] = array[b];
				array[b--] = temp;
				}
		}
		for(int p = 0; p<n;p++) {
			System.out.printf("%d ",array[p]);
		}
	}
}