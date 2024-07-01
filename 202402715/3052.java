import java.util.Scanner;
public class Main {
	public static void main(String[] args){
		Scanner sc = new Scanner(System.in);
		boolean[] array = new boolean[42];
		int [] numarray = new int[42];
		int count =0;
		
		for(int i = 0; i<42;i++) {
			numarray[i] = (i+1);
		}
		
		for (int i = 0; i<10;i++) {
			int a = sc.nextInt();
			a=a%42;
			array[a]=true;
		}
		
		for(int i = 0; i<42;i++) {
			if(array[i]==true) {
				count++;
			}
		}
		System.out.print(count);
		
	}
}