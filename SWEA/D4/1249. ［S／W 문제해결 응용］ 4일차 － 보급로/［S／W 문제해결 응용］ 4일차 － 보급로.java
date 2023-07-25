
import java.util.LinkedList;
import java.util.PriorityQueue;
import java.util.Scanner;

class Solution {
    public static int[] dx = {1, 0, -1, 0};
    public static int[] dy = {0, 1, 0, -1};
    static class Space implements Comparable<Space>{
        int y; int x;
        int distance;
        public Space(int y, int x, int distance){
            this.y = y;
            this.x = x;
            this.distance = distance;
        }
        @Override
        public int compareTo(Space s){
            return this.distance - s.distance;
        }
    }
    public static int[][] map;
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int TC = sc.nextInt();
        for(int tc = 1; tc <= TC; tc++) {
            int N = sc.nextInt();
            map = new int[N][N];
            for (int i = 0; i < N; i++) {
                char[] line = sc.next().toCharArray();
                for (int j = 0; j < N; j++) {
                    map[i][j] = line[j] - '0';
                }
            }
            System.out.printf("#%d %d\n", tc, prim(N));
        }
    }
    public static int prim(int N){
        int result = 0;
        boolean[][] visited = new boolean[N][N];
        PriorityQueue<Space> queue = new PriorityQueue<>();
        queue.add(new Space(0, 0, 0));
        while(!queue.isEmpty()){
            Space space = queue.poll();
            int curr_y = space.y;
            int curr_x = space.x;
            int curr_distance = space.distance;
            visited[curr_y][curr_x] = true;
            if(curr_x == N-1 && curr_y == N-1){
                result = curr_distance;
                break;
            }
            for(int d = 0; d < 4; d++){
                int ny = curr_y + dy[d];
                int nx = curr_x + dx[d];
                if(ny < 0 || nx < 0 || ny >= N || nx >= N || visited[ny][nx]) continue;
                int nd = map[ny][nx] + curr_distance;
                queue.add(new Space(ny, nx, nd));
            }
        }
        return result;
    }
}
