import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int n = sc.nextInt();
		int m = sc.nextInt();
		
		int result1 = gcd(n, m);
		
		int result2 = (m * n) / result1;
		System.out.println(result1);	//최대공약수
		System.out.println(result2);
		}
	
	public static int gcd(int a, int b) {
		
		while(b != 0) {
			int r = a % b;
			
			//(a, b) = (b, r) 변경
			a = b;
			b = r;
		}
		return a;
	}
	
}
