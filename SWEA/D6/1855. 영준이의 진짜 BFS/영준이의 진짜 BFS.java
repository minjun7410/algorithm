import java.util.*;

class Solution {
    public static ArrayList<ArrayList<Integer>> adjacency;
    public static List<Integer> bfsResults;
    public static int[] depths;
    public static int[][] parents;
    public static long result;
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int TC = sc.nextInt();
        for(int tc = 1; tc <= TC; tc++){
            result = 0;
            int N = sc.nextInt();
            adjacency = new ArrayList<>();
            for(int i = 0; i <= N; i++){
                adjacency.add(new ArrayList<>());
            }
            bfsResults = new ArrayList<>();
            parents = new int[N+1][20];
            depths = new int[N+1];
            for(int child = 2; child <= N; child++){
                int parent = sc.nextInt();
                adjacency.get(child).add(parent);
                adjacency.get(parent).add(child);
            }
            bfs(N);

            for(int i = 1; i < 20; i++){
                for(int j = 1; j <= N; j++){
                    parents[j][i] = parents[parents[j][i-1]][i-1];
                }
            }

            for(int i = 1; i < bfsResults.size(); i++){
                int a = bfsResults.get(i-1); int b = bfsResults.get(i);
                int parent = LCA(a, b);
                result += depths[a] - depths[parent];
                result += depths[b] - depths[parent];

            }

            System.out.printf("#%d %d\n", tc, result);
        }
    }
    public static void bfs(int N){
        Queue<Integer> queue = new LinkedList<>();
        boolean[] visited = new boolean[N+1];
        queue.add(1);
        visited[1] = true;

        while(!queue.isEmpty()){
            int node = queue.poll();
            bfsResults.add(node);
            int size = adjacency.get(node).size();
            for(int i = 0; i < size; i++){
                int child = adjacency.get(node).get(i);
                if(visited[child]) continue;
                visited[child] = true;
                parents[child][0] = node;
                depths[child] = depths[node] + 1;
                queue.add(child);
            }
        }
    }
    public static int LCA(int a, int b){
        if(depths[a] > depths[b]){
            int tmp = a;
            a = b;
            b = tmp;
        }
        for(int i = 19; i >= 0; i--){
            if(depths[a] <= depths[parents[b][i]]){
                b = parents[b][i];
            }
        }
        if(a == b) return a;
        for(int i = 19; i >= 0; i--){
            if(parents[a][i] != parents[b][i]){
                a = parents[a][i];
                b = parents[b][i];
            }
        }
        return parents[a][0];
    }
}