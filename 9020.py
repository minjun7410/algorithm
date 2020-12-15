import math

def Sieve(M):#에라토스테네스의 체
    lst = [True for _ in range(M+1)]
    for i in range(2, int(math.sqrt(M))+1):
        if lst[i]:
            j = 2
            while i*j <= M:
                lst[i*j] = False
                j += 1
    result = [i for i in range(2, M) if lst[i]] #소수만 result에 넣어준다
    return result

T = int(input())
for _ in range(T):
    M = int(input())
    lst = Sieve(M)
    result = []
    for i in lst:
        for j in lst:
            if i + j == M:#둘이 합이 M일 때
                result.append([i, j])
                break
    answer = None
    diff = None #두 요소의 차이
    for i in result:
        tmp = abs(i[0] - i[1])
        if diff == None or tmp < diff: #현재 tmp가 차이가 제일 적었던 수(diff)보다 적으면 tmp로 넣어주기
            diff = tmp
            answer = i
    print(' '.join(map(str, answer)))