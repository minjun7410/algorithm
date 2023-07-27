import java.util.HashMap;
import java.util.Scanner;
 
public class Solution {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int TC = sc.nextInt();
        for(int tc = 1; tc <= TC; tc++){
            int N = sc.nextInt();
            int M = sc.nextInt();
            HashMap<String, Integer> hashMap = new HashMap<>();
            for(int n = 0; n < N; n++){
                hashMap.put(sc.next(), 0);
            }
            for(int m = 0; m < M; m++){
                String str = sc.next();
                if(hashMap.containsKey(str)){
                    hashMap.put(str, hashMap.get(str)+1);
                }
                else{
                    hashMap.put(str, 0);
                }
            }
            int result = 0;
            for(String str : hashMap.keySet()){
                if(hashMap.get(str) > 0){
                    result++;
                }
            }
            System.out.printf("#%d %d\n", tc, result);
        }
    }
}