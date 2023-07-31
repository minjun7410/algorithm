
import java.util.Scanner;

public class Solution {
    public static String[] array;
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int TC = sc.nextInt();
        for(int tc = 1; tc <= TC; tc++){
            int N = sc.nextInt();
            array = new String[N];
            for(int i = 0; i < N; i++){
                array[i] = sc.next();
            }
            dc(0, N);
            System.out.println("#"+tc);
            String last = "";
            for(int i = 0; i < N; i++){
                if(last.equals(array[i])) continue;
                last = array[i];
                System.out.println(array[i]);
            }
        }
    }
    public static int dc(int start, int end){
        if(end - start == 1) return 1;
        int mid = (start + end)/2;
        int leftSize = dc(start, mid);
        int rightSize = dc(mid, end);

        String[] tmpArray = new String[end - start];
        int i = start, j = mid;
        int t = 0;
        int size = (end - start);
        while(i < start+leftSize && j < mid + rightSize){
            if(array[i].length() > array[j].length()){
                tmpArray[t++] = array[j++];
            }
            else if(array[i].length() == array[j].length()){
                switch(compareStr(array[i], array[j])){
                    case -1:
                        tmpArray[t++] = array[i++];
                        break;
                    case 0:
                        tmpArray[t++] = array[j++];
                        break;
                    case 1:
                        tmpArray[t++] = array[i++];
                        break;
                    default:
                        break;
                }
            }
            else{
                tmpArray[t++] = array[i++];
            }
        }
        while(i < start+leftSize){
            tmpArray[t++] = array[i++];
        }
        while(j < mid + rightSize){
            tmpArray[t++] = array[j++];
        }
        for(int k = 0; k < size; k++){
            array[start + k] = tmpArray[k];
        }
        return size;
    }
    public static int compareStr(String a, String b){
        int leng = a.length();
        for(int i = 0; i < leng; i++){
            char ac = a.charAt(i);
            char bc = b.charAt(i);
            if(ac > bc) return 0;
            else if(ac < bc) return 1;
        }
        return -1;
    }
}
