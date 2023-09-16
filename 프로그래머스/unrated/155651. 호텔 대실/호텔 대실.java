class Solution {
    private int[] times;
    public int solution(String[][] book_time) {
        times = new int[24 * 61];
        for(String[] book : book_time){
            int start = parseTime(book[0]);
            int end = parseTime(book[1]) + 10;
            times[start]++;
            times[end]--;
        }
        int answer = 0;
        int count = 0;
        for(int i = 0; i < 24 * 60; i++){
            count += times[i];
            if(times[i] > 0) answer = Math.max(answer, count);
        }
        return answer;
    }
    private int parseTime(String s){
        String[] startEnd = s.split(":");
        return hourToMinuit(Integer.parseInt(startEnd[0])) + Integer.parseInt(startEnd[1]);
    }
    private int hourToMinuit(int hour){
        return hour * 60;
    }
}