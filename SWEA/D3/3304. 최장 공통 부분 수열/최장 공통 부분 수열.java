
import java.util.Scanner;

class Solution {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int TC = sc.nextInt();
        for(int tc = 1; tc <= TC; tc++){
            char[] A = sc.next().toCharArray();
            char[] B = sc.next().toCharArray();
            int[][] dp = new int[A.length+1][B.length+1];
            for(int a = 1; a <= A.length; a++){
                for(int b = 1; b <= B.length; b++){
                    if(A[a-1] == B[b-1]){
                        dp[a][b] = dp[a-1][b-1] + 1;
                    }
                    else{
                        dp[a][b] = Math.max(dp[a-1][b], dp[a][b-1]);
                    }
                }
            }
            System.out.printf("#%d %d\n", tc, dp[A.length][B.length]);
        }
    }
}
