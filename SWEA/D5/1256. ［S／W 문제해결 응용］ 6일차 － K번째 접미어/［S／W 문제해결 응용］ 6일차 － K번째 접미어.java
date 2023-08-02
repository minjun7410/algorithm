
import java.util.Scanner;

public class Solution {
    static class TrieNode{
        int count;
        boolean isEnd;
        TrieNode[] nextNodes;
        public TrieNode(){
            this.count = 0;
            this.isEnd = false;
            this.nextNodes = new TrieNode[26];
        }
    }
    public static TrieNode head;
    public static void init(){
        head = new TrieNode();
    }
    public static void insert(String str){
        TrieNode node = head;
        for(char c : str.toCharArray()){
            if(node.nextNodes[c - 'a'] == null){
                node.nextNodes[c-'a'] = new TrieNode();
            }
            node.count++;
            node = node.nextNodes[c - 'a'];
        }
        node.count++;
        node.isEnd = true;
    }
    public static void find(int n){
        TrieNode node = head;
        if(node.count < n) System.out.print("none");

        while(true){
            if(node.isEnd) n--;
            if(n == 0) return;
            int remain = n;
            for(int i = 0; i < 26; i++){
                n = remain;
                if(node.nextNodes[i] != null) remain -= node.nextNodes[i].count;
                if(remain <= 0){
                    node = node.nextNodes[i];
                    System.out.print((char)(i+'a'));
                    break;
                }
            }

        }
    }
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int TC = sc.nextInt();
        for(int tc = 1; tc <= TC; tc++){
            init();
            int n = sc.nextInt();
            String str = sc.next();
            int strLen = str.length();
            for(int i = 0; i < strLen; i++){
                insert(str.substring(i, strLen));
            }
            System.out.printf("#%d ", tc);
            find(n);
            System.out.println();
        }
    }
}
