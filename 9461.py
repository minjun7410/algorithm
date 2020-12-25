T = int(input())
for _ in range(T):
    N = int(input())
    memory = [0 for _ in range(N+1)]
    for i in range(N+1):    
        if i <= 3:
            memory[i] = 1
        elif i <= 5:
            memory[i] = 2
        else:
            memory[i] = memory[i-1] + memory[i-5]
    print(memory[N])