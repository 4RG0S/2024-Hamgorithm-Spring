import java.util.Scanner;
public class Main {
	public static void main(String[] args){
		Scanner sc = new Scanner(System.in);
		int boxnum = sc.nextInt();
		int[] box = new int[boxnum];
		int num = sc.nextInt(); //횟수
		int temp = 0;
		
		for(int j = 0; j<box.length;j++) {
			box[j]=j+1;
		}
			
		for(int i = 0; i<num; i++) {
			int a = sc.nextInt();
			int b = sc.nextInt();
			a = a-1;
			b = b-1;
			temp = box[b];
			box[b] = box[a];
			box[a] = temp;	
		}
		
		for(int j = 0; j<box.length;j++) {
			System.out.printf("%d ",box[j]);
			
	}
	}
}