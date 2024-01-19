package algorithm;

import java.util.ArrayList;
import java.util.Scanner;

public class Baekjoon2501 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
            int n = scanner.nextInt();
            int k = scanner.nextInt();

        ArrayList<Integer> list = new ArrayList<>();

        // list 안에 a의 약수 넣기
        for (int i = 1; i <= n; i++) {
            if (n%i == 0){
                list.add(i);
            }
        }

        // b-1번째 인덱스 꺼내기. 만약 b보다 list.size 가 작으면 0 출력
        if (list.size() <= k-1) {
            System.out.println(0);
        }else {
            System.out.println(list.get(k-1));
        }


    }
}