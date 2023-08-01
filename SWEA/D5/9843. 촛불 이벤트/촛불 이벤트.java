
import java.util.Scanner;

public class Solution {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int TC = sc.nextInt();
        for(int tc = 1; tc <= TC; tc++){
            int result = binarySearch(sc.nextLong());
            System.out.printf("#%d %d\n", tc, result);
        }
    }
    public static int binarySearch(long n){
        int start = 0;
        int end = Integer.MAX_VALUE;
        int mid;
        while(start <= end){
            mid = start + (end-start)/2;

            long candle = ((long) mid *mid + mid)/2;
            if(n < candle){
                end = mid-1;
            }
            else if(n > candle){
                start = mid+1;
            }
            else{
                return mid;
            }
        }
        return -1;
    }
}
