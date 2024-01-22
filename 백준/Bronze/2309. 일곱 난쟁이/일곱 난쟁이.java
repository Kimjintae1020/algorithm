import java.util.Arrays;
import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int[] a = new int[9];	//입력
		
		int sum9 = 0;
		
		for(int i = 0; i < 9; i++) {
			a[i] = sc.nextInt();
			sum9 = sum9 + a[i];
		}
		//sum = 140
		Arrays.sort(a);
		
		//100초과 걸러내는 변수
		int x = 0;
		int y = 0;
		
		for(int i = 0; i < a.length; i++) {
			for(int j = i+1; j < a.length; j++) {
				if(sum9 - a[i] - a[j] == 100) {
					x = a[i];
					y = a[j];
				}
			}
		}
		
		for(int i = 0; i < a.length; i++) {
			if(a[i] == x || a[i] == y) {
				continue;
			}
			System.out.println(a[i]);
		}
		
	}

}
