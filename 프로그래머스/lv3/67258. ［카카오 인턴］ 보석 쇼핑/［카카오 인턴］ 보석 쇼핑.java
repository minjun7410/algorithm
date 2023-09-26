import java.util.*;
class Solution {
    public int[] solution(String[] gems) {
        int[] answer = new int[2];
        HashMap<String, Integer> hashMap = new HashMap<>();
        int gemCount = new HashSet<>(Arrays.asList(gems)).size();
        int l = 0;
        int length = Integer.MAX_VALUE;
        for(int r = 0; r < gems.length; r++){
            hashMap.put(gems[r], hashMap.getOrDefault(gems[r], 0) + 1);
            while(hashMap.get(gems[l]) > 1){
                hashMap.put(gems[l], hashMap.get(gems[l]) - 1);
                l++;
            }
            if(hashMap.size() == gemCount && length > (r-l)) {
                answer[0] = l+1;
                answer[1] = r+1;
                length = r - l;
            }
            
        }
        
        return answer;
    }
}