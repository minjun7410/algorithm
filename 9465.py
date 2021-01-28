# 동적계획법 문제
# 두개의 dp 리스트를 사용한다. (n번 인덱스에서 위를 선택할 경우의 최대값, 아래를 선택할경우..) 
# 2부터 n 까지 반복문을 도는데 dp1[n-1] 과 dp1[n-2] or dp2[n-2]을 선택할 수 있다.
for _ in range(int(input())):
    n = int(input())
    sticker1 = list(map(int, input().split()))
    sticker2 = list(map(int, input().split()))
    dp1 = [0 for _ in range(n)]
    dp2 = [0 for _ in range(n)]
    dp1[0], dp2[0] = sticker1[0], sticker2[0]
    dp1[1], dp2[1] = sticker1[1] + dp2[0], sticker2[1] + dp1[0]
    for i in range(2, n):
        pass_value = dp1[i-2] if dp1[i-2] > dp2[i-2] else dp2[i-2]
        up_value = dp1[i-1]
        down_value = dp2[i-1]
        dp1[i] = down_value + sticker1[i] if down_value > pass_value else pass_value + sticker1[i]
        dp2[i] = up_value + sticker2[i] if up_value > pass_value else pass_value + sticker2[i]
        
    result = dp1[-1] if dp1[-1] > dp2[-1] else dp2[-1]
    print(result)
    