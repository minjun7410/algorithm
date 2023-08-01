
import java.util.Scanner;

public class Solution {
    public static long[] candyPocket;
    public static long start, end, mid;
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int TC = sc.nextInt();
        for(int tc = 1; tc <= TC; tc++){
            int N = sc.nextInt();
            long M = sc.nextLong();
            candyPocket = new long[N];
            start = 1;
            for(int n = 0; n < N; n++){
                candyPocket[n] = sc.nextLong();
            }
            end = Long.MAX_VALUE;
            while(start <= end){
                mid = start + (end - start) / 2;
                long candyCnt = getCandyCnt(mid);
                if(candyCnt < M){
                    end = mid-1;
                }
                else{
                    start = mid+1;
                }
            }
            System.out.printf("#%d %d\n", tc, end);
        }
    }
    public static long getCandyCnt(long pocketCnt){
        long result = 0;
        for(int i = 0; i < candyPocket.length; i++){
            result += candyPocket[i] / pocketCnt;
        }
        return result;
    }
}
