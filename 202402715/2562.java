import java.util.Scanner;
public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int array[];
		int max = 0;
		int count = 0;
		array = new int[10];
		for (int i = 0; i<9; i++) {
			int a = sc.nextInt();
			array[i] = a;
		}
		for(int i = 0; i<9; i++) {
			if (array[i]>max) {
				max = array[i];
				count = i+1;
				
			}
		}
		System.out.println(max);
		System.out.println(count);
	}

}