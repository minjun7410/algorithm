
import java.util.Scanner;

public class Solution {
    public static int A, B;
    public static int sum;
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int TC = sc.nextInt();
        for(int tc = 1; tc <= TC; tc++){
            A = sc.nextInt();
            B = sc.nextInt();
            sum = A + B;
            int K = sc.nextInt();
            long result = (pow(K, 2) * A) % sum;
            result = Math.min(result, sum - result);
            System.out.printf("#%d %d\n", tc, result);
        }
    }
    public static long pow(int n, int k){
        if(n == 0) return 1;
        if(n == 1) return k;
        int isEven = (n % 2 == 0) ? 1 : k;
        long small = pow(n/2, k) % sum;
        small = (small * small) % sum;
        return small * isEven % sum;
    }
}