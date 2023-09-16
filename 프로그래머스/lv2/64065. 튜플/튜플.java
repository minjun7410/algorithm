import java.util.ArrayList;
import java.util.HashMap;

class Solution {
    private int[][] table;
    private int[] countList;
    public int[] solution(String s) {
        countList = new int[100001];
        s = s.substring(1, s.length()-1);
        int lastIndex = 0;
        ArrayList<String> arrayList = new ArrayList();
        for(int i = 0; i < s.length(); i++){
            if(s.charAt(i) == '{') lastIndex = i;
            if(s.charAt(i) == '}') arrayList.add(s.substring(lastIndex+1, i));
        }
        
        table = new int[arrayList.size()+1][arrayList.size()+1];
        
        for(int i = 0; i < arrayList.size(); i++){
            String substr = arrayList.get(i);
            String[] split = substr.split(",");
            for(int j = 0; j < split.length; j++) {
                table[split.length][j] = Integer.parseInt(split[j]);
            }
        }


        int[] answer = new int[arrayList.size()];

        for(int i = 1; i <= arrayList.size(); i++){
            int[] list_cpy = countList.clone();
            for(int j = 0; j < i; j++){
                int a = table[i][j];
                if(list_cpy[a] == 0){
                    answer[i-1] = a;
                    break;
                }
                else{
                    list_cpy[a]--;
                }
            }
            countList[answer[i-1]]++;
        }

        return answer;
    }
}