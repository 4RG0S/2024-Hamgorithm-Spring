import java.util.Scanner;
public class Main {
	public static void main(String[] args){
		Scanner sc = new Scanner(System.in);
		int[] array = new int[30];
		int[] count = new int[2];
		int k = 0;
		
		for(int i = 0; i<28; i++) {
			int a = sc.nextInt();
			array[a-1]=a;
		}
		
		for(int i = 0; i<array.length; i++) {
			if(array[i]==0) {
				count[k]=i+1;
				k++;
			}
		}
		
		if(count[0]>count[1]) {
			System.out.println(count[1]);
			System.out.print(count[0]);
		}else {
			System.out.println(count[0]);
			System.out.print(count[1]);
		}
		
	}
}