
import java.util.PriorityQueue;
import java.util.Scanner;

class Solution {
    public static class Num implements Comparable<Num>{
        int count;
        int left;
        public Num(int count, int left){
            this.count = count;
            this.left = left;
        }
        @Override
        public int compareTo(Num n){
            return this.count - n.count;
        }
    }
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int TC = sc.nextInt();
        for(int tc = 1; tc <= TC; tc++){
            int N = sc.nextInt();
            int[] A = new int[N];
            for(int n = 0; n < N; n++){
                A[n] = sc.nextInt();
            }
            int K = sc.nextInt();
            PriorityQueue<Num> queue = new PriorityQueue<>();
            queue.add(new Num(0, K));
            while(queue.peek().left != 0){
                Num num = queue.poll();
                queue.add(new Num(num.count + num.left, 0));
                for(int n : A){
                    queue.add(new Num(num.count + num.left % n, num.left / n));
                }
            }
            System.out.printf("#%d %d\n", tc, queue.peek().count);
        }
    }

}
