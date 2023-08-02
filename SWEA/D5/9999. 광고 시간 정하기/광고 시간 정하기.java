
import java.util.Scanner;

public class Solution {
    public static int[][] peekTimes;
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int TC = sc.nextInt();
        for(int tc = 1; tc <= TC; tc++){
            int result = 0;
            int L = sc.nextInt(); int N = sc.nextInt();
            int sum = 0;
            peekTimes = new int[N][3];
            for(int n = 0; n < N; n++){
                int s = sc.nextInt();
                int e = sc.nextInt();
                sum += e - s;
                peekTimes[n][0] = s;
                peekTimes[n][1] = e;
                peekTimes[n][2] = sum;
            }

            for(int n = 0; n < N; n++){
                int start = peekTimes[n][0];
                int end = start + L;
                int[] closePeekTime = getClosePeekTime(end);
                sum = closePeekTime[2] - peekTimes[n][2] + (peekTimes[n][1] - peekTimes[n][0]);

                if(closePeekTime[1] > end) {
                    if (closePeekTime[0] < end) {
                        sum -= (closePeekTime[1] - end);
                    } else {
                        sum -= (closePeekTime[1] - closePeekTime[0]);
                    }
                }
                result = Math.max(result, sum);
            }
            System.out.printf("#%d %d\n", tc, result);
        }
    }
    public static int[] getClosePeekTime(int target){
        int start = 0;
        int end = peekTimes.length-1;
        while(start < end){
            int mid = start + (end - start) / 2;
            if(peekTimes[mid][1] < target){
                start = mid + 1;
            }
            else end = mid;
        }
        return peekTimes[end];
    }
}
