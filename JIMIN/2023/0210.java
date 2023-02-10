// 직각삼각형

import java.util.Scanner;

public class Solution {
      public static void main(String[] args) {
          Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        String x = "*";
        
        // 0부터 시작하면 "*" * 0 이어서 아무것도 안나옴 주의
        for(int i=1; i<=n; i++) {
        	System.out.println(x.repeat(i));
        }
      }
}
