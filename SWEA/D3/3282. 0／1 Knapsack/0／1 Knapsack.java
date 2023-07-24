
import java.util.Scanner;

class Solution {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int TC = sc.nextInt();
        for(int tc = 1; tc <= TC; tc++){
            int N = sc.nextInt();
            int K = sc.nextInt();
            int[][] weights = new int[N+1][2];
            for(int i = 1; i <= N; i++){
                weights[i][0] = sc.nextInt();
                weights[i][1] = sc.nextInt();
            }
            int[][] dp = new int[N+1][K+1];
            for(int i = 1; i <= N; i++){
                for(int j = 1; j <= K; j++){
                    if(j - weights[i][0] < 0) {
                        dp[i][j] = dp[i-1][j];
                        continue;
                    }
                    dp[i][j] = Math.max(dp[i-1][j], weights[i][1] + dp[i-1][j - weights[i][0]]);
                }
            }
            System.out.printf("#%d %d\n", tc, dp[N][K]);

        }
    }
}
