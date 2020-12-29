first = input()
second = input()

target, none_target = (first, second) if len(first) > len(second) else (second, first)

dp = [0 for _ in range(len(target))]

for n_index in range(len(none_target)):
    for t_index in range(len(target)):
        if t_index and none_target[n_index] == target[t_index]:
            dp[t_index] = max(dp[0:t_index]) + 1
        elif not(t_index) and none_target[n_index] == target[t_index]:
            dp[t_index] = 1
print(max(dp))

    