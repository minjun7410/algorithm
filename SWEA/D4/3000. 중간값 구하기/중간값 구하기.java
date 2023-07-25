
import java.util.Scanner;

class Solution {
    public static int[] minHeap;
    public static int[] maxHeap;
    public static int minIndex;
    public static int maxIndex;
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int TC = sc.nextInt();
        for(int tc = 1; tc <= TC; tc++){
            int N = sc.nextInt();
            int A = sc.nextInt();
            int result = 0;
            minHeap = new int[400001];
            maxHeap = new int[400001];
            minIndex = 0;
            maxIndex = 1;
            maxHeap[1] = A;
            for(int n = 0; n < N; n++){
                for(int i = 0; i < 2; i++){
                    int x = sc.nextInt();
                    if(maxHeap[1] >= x) maxPush(x);
                    else minPush(x);
                }
                if(maxIndex - minIndex == 3){
                    minPush(maxPop());
                }
                else if(maxIndex - minIndex == -1) {
                    maxPush(minPop());
                }
                result = ((result % 20171109) + (maxHeap[1] % 20171109)) % 20171109;
            }
            System.out.printf("#%d %d\n", tc, result);
        }
    }
    public static void minPush(int n){
        minHeap[++minIndex] = n;
        for(int i = minIndex; i > 1; i /= 2){
            if(minHeap[i] < minHeap[i/2]) swap(minHeap, i, i/2);
            else break;
        }
    }
    public static void maxPush(int n){
        maxHeap[++maxIndex] = n;
        for(int i = maxIndex; i > 1; i /= 2){
            if(maxHeap[i] > maxHeap[i/2]) swap(maxHeap, i, i/2);
            else break;
        }
    }
    public static int minPop(){
        int result = minHeap[1];
        minHeap[1] = minHeap[minIndex--];
        int i = 1;
        while(i * 2 <= minIndex){
            if(i*2 == minIndex || minHeap[i*2] < minHeap[i*2+1]){
                if(minHeap[i] > minHeap[i*2]) {
                    swap(minHeap, i, i * 2);
                    i = i * 2;
                }
                else break;
            }
            else{
                if(minHeap[i] > minHeap[i*2+1]){
                    swap(minHeap, i, i*2+1);
                    i = i * 2 + 1;
                }
                else break;
            }
        }
        return result;
    }
    public static int maxPop(){
        int result = maxHeap[1];
        maxHeap[1] = maxHeap[maxIndex--];
        int i = 1;
        while(i * 2 <= maxIndex){
            if(i*2 == maxIndex || maxHeap[i*2] > maxHeap[i*2+1]){
                if(maxHeap[i] < maxHeap[i*2]) {
                    swap(maxHeap, i, i * 2);
                    i = i * 2;
                }
                else break;
            }
            else{
                if(maxHeap[i] < maxHeap[i*2+1]){
                    swap(maxHeap, i, i*2+1);
                    i = i * 2 + 1;
                }
                else break;
            }
        }
        return result;
    }
    public static void swap(int[] array, int a, int b){
        int tmp = array[a];
        array[a] = array[b];
        array[b] = tmp;
    }
}
