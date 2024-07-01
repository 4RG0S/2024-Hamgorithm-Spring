import java.util.Scanner;
public class Main {
	public static void main(String[] args){
		Scanner sc = new Scanner(System.in);
		int num = sc.nextInt();//입력받을 개수
		int[] array = new int[num];//배열

		int count = 0;//카운트
		
		for(int i = 0; i<num; i++) {
			array[i] = sc.nextInt();//배열 채우기
			
		}
		
		int check = sc.nextInt();//비교할 수
		
		for(int i = 0; i<num; i++) {
			if(array[i]==check) {//
				count++;
			}
		}
		
		System.out.print(count);
	}
}