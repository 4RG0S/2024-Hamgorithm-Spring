package ilhacneonilhakgee;

import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in); //sc를 스캐너로 지정받기
		int N = sc.nextInt(); //입력받을 숫자의 갯수를 정하기
		String numbers = sc.next(); //문자열로 숫자열을 입력받기
		int sum = 0; //총합을 입력받을 변수 설정
		
		for (int i=0; i<N; i++) { 
			sum += Character.getNumericValue(numbers.charAt(i)); //i번쨰 문자를 합하여 대입 -> 반복
		}
		System.out.print(sum); //총합 출력
		sc.close();
	}

}