import java.util.Scanner;
public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int hour = sc.nextInt();
		int min = sc.nextInt();
		int time = sc.nextInt();
		int hour2 = hour+((min+time)/60);
		int min2 = ((min+time)%60);
		if (hour2>=24) {
			if(min2>60) {
				System.out.printf("%d %d",hour2-24, min2-60);
			}else {
				System.out.printf("%d %d",hour2-24, min2);
			}
		}else {
			if(min2>=60) {
				System.out.printf("%d %d",hour2, min2-60);
			}else {
				System.out.printf("%d %d",hour2, min2);
			}
		}
	}
}