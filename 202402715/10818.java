import java.util.Scanner;
public class Main {
	public static void main(String[] args){
		Scanner sc = new Scanner(System.in);
		int num = sc.nextInt();//입력받을 개수
		int[] array = new int[num];//배열
		int max = -1000000;
		int min = 1000000;
		
		for(int i = 0; i<num; i++) {
			array[i] = sc.nextInt();//배열 채우기
		}
		
		
		for(int i = 0; i<num; i++) {
			if(array[i]>max) {//
			max = array[i];
			}
		}
		for(int i = 0; i<num; i++) {
			if(array[i]<min) {//
			min = array[i];
			}
		}
		System.out.printf("%d ",min);
		System.out.print(max);
	}
}