import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner in = new Scanner(System.in);
		
		int n = in.nextInt();	
		int num;
		int count = 0;
		
		for(int i = 0; i < n; i++) {
			num = in.nextInt();
			
			//1은 소수 아님
			for(int j = 2; j <= num; j++) {
				
				if(j == num) {
					count++;
				}
					
				//소수 아님
				if(num % j == 0) {
					break;
				}
			}
			
		}
		System.out.println(count);
		
	}

}
