
import java.util.Arrays;
import java.util.Scanner;

public class Solution {
    public static int[] horses;
    public static int[] cows;
    public static int minDst, maxCnt;
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int TC = sc.nextInt();
        for(int tc = 1; tc <= TC; tc++){
            int N = sc.nextInt(); int M = sc.nextInt();
            int c1 = sc.nextInt(); int c2 = sc.nextInt();
            cows = new int[N];
            for(int i = 0; i < N; i++){
                cows[i] = sc.nextInt();
            }
            horses = new int[M];
            for(int i = 0; i < M; i++){
                horses[i] = sc.nextInt();
            }
            minDst = Integer.MAX_VALUE;
            maxCnt = 0;
            Arrays.sort(horses);
            for(int n = 0; n < N; n++){
                int cowLoc = cows[n];
                int start = 0; int end = M-1;
                while(start <= end){
                    int mid = start + (end - start) / 2;
                    if(horses[mid] < cowLoc){
                        start = mid + 1;
                    }
                    else if(horses[mid] > cowLoc){
                        end = mid - 1;
                    }
                    else{
                        if(minDst == 0){
                            maxCnt++;
                        }
                        else{
                            minDst = 0;
                            maxCnt = 1;
                        }
                        break;
                    }
                }
                if(minDst == 0) continue;
                if(start < M){
                    int dst = Math.abs(horses[start] - cowLoc);
                    if(dst < minDst){
                        minDst = dst;
                        maxCnt = 1;
                    }
                    else if(dst == minDst){
                        maxCnt++;
                    }
                }
                if(end >= 0){
                    int dst = Math.abs(horses[end] - cowLoc);
                    if(dst < minDst){
                        minDst = dst;
                        maxCnt = 1;
                    }
                    else if(dst == minDst){
                        maxCnt++;
                    }
                }
            }
            System.out.printf("#%d %d %d\n", tc, minDst+Math.abs(c1-c2), maxCnt);
        }
    }
}
