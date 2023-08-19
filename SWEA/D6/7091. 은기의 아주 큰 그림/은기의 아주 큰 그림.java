
import java.util.Arrays;
import java.util.Scanner;

class Solution {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int TC = scanner.nextInt();
        for (int tc = 1; tc <= TC; tc++) {
            int H = scanner.nextInt();
            int W = scanner.nextInt();
            int N = scanner.nextInt();
            int M = scanner.nextInt();

            int[][] smallPicture = new int[2000][2000];
            for (int h = 0; h < H; h++) {
                String str = scanner.next();
                for (int w = 0; w < W; w++) {
                    char a = str.charAt(w);
                    smallPicture[h][w] = (a == 'o') ? 1 : 0;
                }
            }
            int[][] bigPicture = new int[2000][2000];
            for (int n = 0; n < N; n++) {
                String str = scanner.next();
                for (int m = 0; m < M; m++) {
                    char a = str.charAt(m);
                    bigPicture[n][m] = (a == 'o') ? 1 : 0;
                }
            }

            int[][] tmp = new int[2000][2000];
            for (int i = 0; i < H; i++) {
                tmp[0][i] = calculateHash(smallPicture[i], W, 8);
            }
            int smallHash = calculateHash(tmp[0], H, 9);

            tmp = new int[2000][2000];
            int mulColumn = calculateMul(W, 8);
            int mulRow = calculateMul(H, 9);
            for (int i = 0; i < N; i++) {
                tmp[0][i] = calculateHash(bigPicture[i], W, 8);
                for (int j = 1; j < M - W + 1; j++) {
                    tmp[j][i] = calculateNext(tmp[j - 1][i], bigPicture[i][j - 1], mulColumn, bigPicture[i][j + W - 1], 8);
                }
            }

            int[][] bigHash = new int[2000][2000];
            for (int i = 0; i < M - W + 1; i++) {
                bigHash[0][i] = calculateHash(tmp[i], H, 9);
                for (int j = 1; j < N - H + 1; j++) {
                    bigHash[j][i] = calculateNext(bigHash[j - 1][i], tmp[i][j - 1], mulRow, tmp[i][j + H - 1], 9);
                }
            }

            int count = 0;
            for (int i = 0; i < N - H + 1; i++) {
                for (int j = 0; j < M - W + 1; j++) {
                    if (bigHash[i][j] == smallHash) count++;
                }
            }

            System.out.printf("#%d %d\n", tc, count);
        }
    }

    static int calculateMul(int num, int shift) {
        long rev = 1;
        for (int i = 1; i < num; i++) {
            rev = (rev << shift) + rev;
        }
        return (int) rev & ((1 << 30) - 1);
    }

    static int calculateHash(int[] piv, int num, int shift) {
        long hashValue = 0;
        for (int i = 0; i < num; i++) {
            hashValue = (hashValue << shift) + hashValue + piv[i];
        }
        return (int) hashValue & ((1 << 30) - 1);
    }

    static int calculateNext(int prev, int sub, int mul, int add, int shift) {
        long hashValue = prev - sub*mul;
        hashValue = (hashValue << shift) + hashValue + add;
        return (int) hashValue & ((1 << 30) - 1);
    }
}