import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int a = sc.nextInt();
		int b = sc.nextInt();
		int c = sc.nextInt();
		
		int sum = 0;
		
		//모두 다를 경우
		if(a != b && b != c && a != c) {
			int max;
			
			if(a > b) {
				// c > a > b
				if(c > a) {
					max = c;
				}
				// a > b,c
				else {
					max = a;
				}
				
			}
			else {
				// c > b > a
				if(c > b) {
					max = c;
				}
				// b > c > a
				else {
					max = b;
				}
			}	
			System.out.println(max * 100);	
		}
		// 두개는 같음
		else {
			// 세개 다 같은 경우
			if(a == b && a == c) {
				System.out.println(10000 + a * 1000);
			}
			else {
				if(a == b || a == c) {
					System.out.println(1000 + a * 100);
				}
				// b == c랑 같은 경우
				else {
					System.out.println(1000 + b * 100);
				}
			}
		}			
	}
}

