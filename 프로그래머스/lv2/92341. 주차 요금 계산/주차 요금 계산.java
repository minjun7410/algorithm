import java.util.*;
class Solution {
    private int cutLineTime;
    private int baseCharge;
    private int unitTime;
    private int unitCharge;
    private HashMap<Integer, Integer> comeInTimes;
    private int[] takedTimes;
    public int[] solution(int[] fees, String[] records) {
        int[] answer = {};
        comeInTimes = new HashMap<>();
        takedTimes = new int[10000];
        
        initFees(fees);
        takeRecords(records);
        calculRemainCar();
        ArrayList<Integer> list = new ArrayList<>();
        for(int i = 0; i < 10000; i++){
            if(takedTimes[i] != 0){
                int a = baseCharge;
                if(takedTimes[i] > cutLineTime){
                    
                    a += Math.ceil((takedTimes[i] - cutLineTime) / (double)unitTime) * unitCharge;
                }
                list.add(a);
            }
        }
        answer = list.stream()
            .mapToInt(Integer::intValue)
            .toArray();
        return answer;
    }
    private void calculRemainCar(){
        for(int key : comeInTimes.keySet()){
            takedTimes[key] += (23 * 60 + 59) - comeInTimes.get(key);
        }
    }
    private void takeRecords(String[] records){
        for(String record : records){
            String[] splited = record.split(" ");
            int time = hourToMinuit(splited[0]);
            int car = Integer.parseInt(splited[1]);
            if(splited[2].equals("IN")){
                comeInTimes.put(car, time);
            }
            else{
                int startTime = comeInTimes.get(car);
                takedTimes[car] += time - startTime;
                comeInTimes.put(car, 23*60 + 59);
            }
        }
    }
    private int hourToMinuit(String hour){
        String[] hourAndMinuit = hour.split(":");
        return Integer.parseInt(hourAndMinuit[0]) * 60 + Integer.parseInt(hourAndMinuit[1]);
    }
    private void initFees(int[] fees){
        cutLineTime = fees[0];
        baseCharge = fees[1];
        unitTime = fees[2];
        unitCharge = fees[3];
    }
}