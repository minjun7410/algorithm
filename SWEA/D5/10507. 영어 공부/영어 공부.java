
import java.util.Scanner;

public class Solution {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int TC = sc.nextInt();
        for(int tc = 1; tc <= TC; tc++){
            int N = sc.nextInt(); int P = sc.nextInt();
            int[] days = new int[N];
            boolean[] checked = new boolean[1000001];
            for(int n = 0; n < N; n++){
                int tmp = sc.nextInt();
                days[n] = tmp;
                checked[tmp] = true;
            }
            int maxCount = P+1;
            int currCount = 0;
            //int n = 0;
            int p = P;
            int start = 0; int end = 0;
            while(end < checked.length){
                if(checked[end]){
                    currCount++;
                    end++;
                    maxCount = Math.max(maxCount, currCount);
                    //n++;
                }
                else{
                    if(p == 0){
                        p += (checked[start]) ? 0 : 1;
                        start++;
                        currCount--;
                    }
                    else{
                        p--;
                        currCount++;
                        end++;
                        maxCount = Math.max(maxCount, currCount);
                    }
                }
            }
            System.out.printf("#%d %d\n", tc, maxCount);
        }
    }
}
