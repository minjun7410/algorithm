
import java.util.ArrayList;
import java.util.PriorityQueue;
import java.util.Scanner;

class Solution {
    public static class Island implements Comparable<Island>{
        int destination;
        long weight;
        public Island(int destination, long weight){
            this.destination = destination;
            this.weight = weight;
        }
        @Override
        public int compareTo(Island o){
            return Long.compare(this.weight, o.weight);
        }
    }
    public static int[][] islands;
    public static long result;
    public static ArrayList<Island>[] adjust;
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int TC = sc.nextInt();
        for(int tc = 1; tc <= TC; tc++){
            result = 0;
            int N = sc.nextInt();
            islands = new int[N][2];
            for(int i = 0; i < N; i++){
                islands[i][1] = sc.nextInt();
            }
            for(int i = 0; i < N; i++){
                islands[i][0] = sc.nextInt();
            }
            double E = sc.nextDouble();
            adjust = new ArrayList[N];
            for(int i = 0; i < N; i++){
                adjust[i] = new ArrayList<>();
                for(int j = 0; j < N; j++){
                    if(i == j) continue;
                    long distanceX = Math.abs(islands[i][1] - islands[j][1]);
                    long distanceY = Math.abs(islands[i][0] - islands[j][0]);
                    adjust[i].add(new Island(j,distanceY*distanceY + distanceX*distanceX));

                }
            }
            prim(N);
            System.out.printf("#%d %d\n", tc, Math.round(result * E));
        }
    }
    public static void prim(int N){
        boolean[] visited = new boolean[N];
        PriorityQueue<Island> queue = new PriorityQueue<>();
        queue.add(new Island(0, 0));
        int visitNum = 0;
        while(!queue.isEmpty()){
            Island island = queue.poll();
            if(visited[island.destination]) continue;
            visited[island.destination] = true;

            result += island.weight;

            visitNum++;
            if(visitNum == N) break;
            for(int i = 0; i < adjust[island.destination].size(); i++){
                Island nextIsland = adjust[island.destination].get(i);
                if(visited[nextIsland.destination]) continue;
                queue.add(nextIsland);
            }
        }
    }
}
