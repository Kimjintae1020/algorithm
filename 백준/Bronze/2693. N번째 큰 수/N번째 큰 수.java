import java.util.Arrays;
import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner in = new Scanner(System.in);
		
		int n = in.nextInt();
		
		int[] arr = new int[10];	// 10개 담을 배열
		int[] result = new int[n];	// 3번째 큰 자연수
		
		for(int i = 0; i < n; i++) {
			for(int j = 0; j < 10; j++) {
				arr[j] = in.nextInt();
			}
			Arrays.sort(arr);
			
			result[i] = arr[7];
		}
		
		
		for(int i = 0; i < n; i++) {
			System.out.println(result[i]);
		}
	}
}
