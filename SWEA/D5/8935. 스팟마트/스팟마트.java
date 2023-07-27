import java.io.*;
import java.util.Arrays;
import java.util.Collections;

class Solution {

    public static int[] nList;
    public static Integer[] mList;
    static int[][][] dp = new int[3002][102][102];
    public static int N, M;


    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int TC = Integer.parseInt(br.readLine());

        for(int tc = 1; tc <= TC; tc++){
            N = Integer.parseInt(br.readLine());
            nList = new int[N];
            for(int i = 0; i < N; i++){
                nList[i] = Integer.parseInt(br.readLine());
            }
            M = Integer.parseInt(br.readLine());
            mList = new Integer[M];
            for(int i = 0; i < M; i++){
                mList[i] = Integer.parseInt(br.readLine());
            }
            Arrays.sort(mList, Collections.reverseOrder());
            for(int i = 0; i <= N; i++){
                for(int j = 0; j <= M; j++){
                    for(int k = 0; k <= M; k++){
                        dp[i][j][k] = -1;
                    }
                }
            }
            int result = recursive(0, 0, 0);
            System.out.printf("#%d %d\n", tc, result);
        }
    }

    public static int recursive(int nIndex, int mIndex, int mSkip){
        if(nIndex > N || mIndex + mSkip > M) return 0;
        if(dp[nIndex][mIndex][mSkip] != -1){
            return dp[nIndex][mIndex][mSkip];
        }
        int result = 0;
        if(nIndex < N) result = Math.max(result, recursive(nIndex+2, mIndex, mSkip) + nList[nIndex]);
        if(nIndex < N) result = Math.max(result, recursive(nIndex+1, mIndex, mSkip));
        if(nIndex < N && mIndex + mSkip < M) result = Math.max(result, recursive(nIndex+1, mIndex, mSkip+1) + nList[nIndex]);
        if(mIndex+mSkip < M) result = Math.max(result, recursive(nIndex, mIndex, mSkip+1));
        if(nIndex < N && mIndex + mSkip < M ) result= Math.max(result, recursive(nIndex + 1, mIndex + 1, mSkip) + mList[mIndex]);
        if(mIndex + mSkip + 1 < M) result = Math.max(result, recursive(nIndex, mIndex+1, mSkip +1) + mList[mIndex]);

        dp[nIndex][mIndex][mSkip] = result;
        return result;
    }
}


