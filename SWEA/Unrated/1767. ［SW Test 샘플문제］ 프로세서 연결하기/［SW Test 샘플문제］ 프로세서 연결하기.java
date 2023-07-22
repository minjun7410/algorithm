import java.util.Scanner;

 class Solution {
    public static Scanner sc;
    public static int N;
    public static int[][] map;
    public static int[][] nodePool;
    public static int lineNum;
    public static int minNum;
    public static int poolNum;
    public static int[] dx = {1, 0, -1, 0};
    public static int[] dy = {0, 1, 0, -1};

    public static void main(String[] args){
        sc = new Scanner(System.in);
        int TC = sc.nextInt();
        for(int tc = 1; tc <= TC; tc++){
            N = sc.nextInt();
            map = new int[N][N];
            nodePool = new int[N*N][2];
            poolNum = 0;
            for(int i = 0; i < N; i++){
                for(int j = 0; j < N; j++){
                    map[i][j] = sc.nextInt();
                    if(i != 0 && i != N && j != 0 && j != N && map[i][j] == 1){
                        nodePool[poolNum][0] = i;
                        nodePool[poolNum][1] = j;
                        poolNum++;
                    }
                }
            }
            System.out.printf("#%d %d\n", tc, dfs());
        }
    }

    public static int dfs(){
        minNum = 9999999;
        maxCoreNum = 0;
        lineNum = 0;
        // init
        for(int d = 0; d < 4; d++){
            recursion(0, d, 0);
        }

        return minNum;
    }
    public static int maxCoreNum;
    public static void recursion(int nodeIndex, int nodeDirection, int coreNum){
        if(nodeIndex == poolNum) return;
        recursion(nodeIndex+1, nodeDirection, coreNum);
        int nodeX = nodePool[nodeIndex][1];
        int nodeY = nodePool[nodeIndex][0];
        if(!installLine(nodeY, nodeX, nodeDirection)) return;
        if(coreNum > maxCoreNum) {
            maxCoreNum = coreNum;
            minNum = lineNum;
        }
        else if(coreNum == maxCoreNum){
            minNum = (minNum > lineNum) ? lineNum : minNum;
        }
        for(int d = 0; d < 4; d++){
            recursion(nodeIndex+1, d, coreNum+1);
        }
        removeLine(nodeY, nodeX, nodeDirection);
    }

    public static boolean installLine(int y, int x, int d){
        boolean result = true;
        int nx = x + dx[d];
        int ny = y + dy[d];
        while(nx >= 0 && ny >= 0 && nx < N && ny < N){
            if(map[ny][nx] != 0){
                result = false;
                break;
            }
            lineNum++;
            map[ny][nx] = 2;
            nx = nx + dx[d];
            ny = ny + dy[d];
        }
        if(!result){
            nx = nx - dx[d];
            ny = ny - dy[d];
            while(map[ny][nx] == 2){
                lineNum--;
                map[ny][nx] = 0;
                nx = nx - dx[d];
                ny = ny - dy[d];
            }
            return false;
        }
        else return true;
    }
    public static void removeLine(int y, int x, int d){
        int nx = x + dx[d];
        int ny = y + dy[d];
        while(nx >= 0 && ny >= 0 && nx < N && ny < N && map[ny][nx] == 2){
            lineNum--;
            map[ny][nx] = 0;
            nx = nx + dx[d];
            ny = ny + dy[d];
        }
    }
}
