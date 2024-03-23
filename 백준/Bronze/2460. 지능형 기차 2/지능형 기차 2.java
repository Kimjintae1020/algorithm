import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		st.nextToken();
		
		int max = Integer.parseInt(st.nextToken());	//사람 가장 많을 때
		int term = max;		//현재 사람의 수
		
		for(int i = 1; i <= 9; i++) {
			st = new StringTokenizer(br.readLine());
			int out = Integer.parseInt(st.nextToken());
			int in = Integer.parseInt(st.nextToken());
			
			term = term - out + in;
			max = Math.max(max, term);
		}
		
		System.out.println(max);
		
	}
}
