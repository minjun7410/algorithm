import java.util.*;
class Solution {
    String[] user_id;
    String[] banned_id;
    HashSet<HashSet<String>> hashSet;
    public int solution(String[] user_id, String[] banned_id) {
        this.user_id = user_id;
        this.banned_id = banned_id;
        this.hashSet = new HashSet<>();
        int answer = recursion(0, new boolean[user_id.length], new HashSet<String>());
        
        return answer;
    }
    private int recursion(int b, boolean[] visited, HashSet<String> hash){
        if(b == banned_id.length){
            if(hashSet.contains(hash)){
                return 0;
            }
            hashSet.add(new HashSet<>(hash));
            return 1;
        }
        else{
            int result = 0;
            for(int v = 0; v < visited.length; v++){
                if(visited[v]) continue;
                if(!isMatched(user_id[v], banned_id[b])) continue;
                visited[v] = true;
                hash.add(user_id[v]);
                result += recursion(b+1, visited, hash);
                hash.remove(user_id[v]);
                visited[v] = false;
            }
            return result;
        }
    }
    
    private boolean isMatched(String a, String b){
        if(a.length() != b.length()) return false;
        
        for(int i = 0; i < a.length(); i++){
            if(b.charAt(i) == '*') continue;
            if(b.charAt(i) != a.charAt(i)) return false;
        }
        
        return true;
    }
}