import java.util.*;
class Solution {
    static class Pair{
        String uid;
        boolean isEnter;
        Pair(String uid, boolean isEnter){
            this.uid = uid;
            this.isEnter = isEnter;
        }
    }
    public String[] solution(String[] record) {
        String[] answer = {};
        ArrayList<Pair> beforeAnswer = new ArrayList<>();
        HashMap<String, String> hashMap = new HashMap<>();
        for(String rec : record){
            String[] splited = rec.split(" ");
            if(splited.length == 3){
                hashMap.put(splited[1], splited[2]);
                if(splited[0].equals("Enter")){
                    beforeAnswer.add(new Pair(splited[1], true));
                }
            }
            else{
                beforeAnswer.add(new Pair(splited[1], false));
            }
        }
        answer = new String[beforeAnswer.size()];
        int a = 0;
        for(Pair pair : beforeAnswer){
            if(pair.isEnter){
                answer[a] = hashMap.get(pair.uid) + "님이 들어왔습니다.";
            }
            else{
                answer[a] = hashMap.get(pair.uid) + "님이 나갔습니다.";
            }
            a++;
        }
        return answer;
    }
}