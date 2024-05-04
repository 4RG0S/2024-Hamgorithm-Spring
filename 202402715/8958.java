import java.util.Scanner;
public class Main {
	public static void main(String[] args){
		Scanner sc = new Scanner(System.in);
		int num = sc.nextInt();
		String[] arr = new String[num];
		
		for(int i = 0; i<arr.length;i++) {
			arr[i] = sc.next();
		}
		
		for(int i = 0; i<arr.length;i++) {
			
			int dus = 0;
			int count = 0;
			
			String line = arr[i];
			
			for(int j = 0; j<line.length();j++){
				
				if(line.charAt(j)=='O') {
					dus++;
				}
				else {
					dus=0;
				}	
				count += dus;
			}
			System.out.println(count);
		}
	}
}