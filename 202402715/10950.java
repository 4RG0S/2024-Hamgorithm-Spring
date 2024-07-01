import java.util.Scanner;
public class Main{
    public static void main(String[] args){
    	Scanner sc = new Scanner(System.in);
    	int n = sc.nextInt();
    	int[] array = new int[n];
    	for(int i = 0; i<n; i++) {
    		int A = sc.nextInt();
    		int B = sc.nextInt();
    		array[i] = A+B;
    	}
    	for(int j = 0 ; j<n; j++) {
    		System.out.println(array[j]);
    	}
    }
}