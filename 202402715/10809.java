import java.util.Scanner;
public class Main {
	public static void main(String[] args){
		Scanner sc = new Scanner(System.in);
		String line = sc.next();
		int[] array = new int['z'-'a'+1];
		char[] arr1 = new char['z'-'a'+1];
		int[] arr2 = new int['z'-'a'+1];
		
		for(int i = 0; i<='z'-'a';i++) {
			array[i]=-1;
			arr1[i]=(char)('a'+i);
			arr2[i]=i;
		}
		
//		for(int i = 0; i<array.length; i++) {
//			System.out.print(arr[i]);
//		}
		
		for(int i = 0; i<line.length();i++) {
			int a = arr2[line.charAt(i)-'a'];
//			System.out.println(line.charAt(i));
//			System.out.println(arr2[line.charAt(i)-'a']);
//			System.out.print(a);
			array[a]=line.indexOf(line.charAt(i));
//			System.out.print(array[a]);
		}
		
		for(int i = 0; i<array.length; i++) {
			System.out.printf("%d ",array[i]);
		}
	}
}