package algorithm;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Baekjoon3460 {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int n = Integer.parseInt(br.readLine());
		
		for(int i = 0; i < n; i++) {
			int k = Integer.parseInt(br.readLine());
			int index = 0;
			
			while(k > 0) {
				if(k%2 == 1) {
					
					System.out.print(index + " ");
					
				}
				k = k/2;
				index++;
			}
			
			System.out.println();
		}
		
	}

}
