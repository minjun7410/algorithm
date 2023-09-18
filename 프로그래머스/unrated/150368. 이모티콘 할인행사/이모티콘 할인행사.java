class Solution {
    private final int[] discounts = {10, 20, 30, 40};
    int maxCount = 0;
    int maxAmount = 0;
    int N;
    public int[] solution(int[][] users, int[] emoticons) {
        N = emoticons.length;
        int[] answer = new int[2];
        dfs(0, users, emoticons, new int[users.length]);
        answer[0] = maxCount;
        answer[1] = maxAmount;
        return answer;
    }
    private void dfs(int n, int[][] users, int[] emoticons, int[] userCounts){
        if(n == N){
            int count = 0;
            int amount = 0;
            for(int i = 0; i < users.length; i++){
                int[] user = users[i];
                int userCount = userCounts[i];
                if(user[1] <= userCount){
                    count++;
                }
                else{
                    amount += userCount;
                }
            }
            
            if(maxCount < count){
                maxCount = count;
                maxAmount = amount;
            }
            else if(maxCount == count) {
                maxAmount = Math.max(maxAmount, amount);
            }
            return;
        }
        for(int discount : discounts){
            int price = emoticons[n] - (discount * emoticons[n] / 100);
            for(int i = 0; i < users.length; i++){
                int[] user = users[i];
                if(discount >= user[0]) userCounts[i] += price;
            }
            dfs(n+1, users, emoticons, userCounts);
            
            for(int i = 0; i < users.length; i++){
                int[] user = users[i];
                if(discount >= user[0]) userCounts[i] -= price;
            }
        }
    }
}