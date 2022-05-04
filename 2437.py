# 2437 저울
# 수학

# concept

# 1 1 2 3 6 7 30
#
# 0 1
# 1
# 1(1) 1
# 1 1(2) 2
# 1 1 2 (4) 3
# 1 1 2 3 (7) 6
# 1 1 2 3 6 (13) 7
# 1 1 2 3 6 7 (20) 30 -> (x)
# -> 20 + 1 = 21


N = int(input())
chu = list(map(int, input().split()))
chu.sort()
summation = 1

for c in chu:
    if summation < c:
        break
    summation += c
print(summation)