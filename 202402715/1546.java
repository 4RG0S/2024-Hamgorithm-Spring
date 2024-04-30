import java.util.Scanner;
public class Main {
	public static void main(String[] args){
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt(); //과목 수
		double[] array = new double[n];
		double max = Double.MIN_VALUE;
		double sum = 0;
		
		for(int i =0; i<array.length;i++) {
			array[i]=sc.nextInt(); 
			if(array[i]>max) {
				max = array[i];
			}
		}
		
		for(int i = 0; i<array.length;i++) {
			array[i]= array[i]/max*100;
			sum = sum + array[i];
		}
		
		System.out.print(sum/n);
	
		
	}
}