# 에라토스테네스의 체
# min의 제한이 1조로 매우 크지만 min과 max 사이는 백만으로 비교적 작다.
# min의 값이 어떻든 간에 가장 작은 제곱수인 4부터 max와 가까운 제곱수의 리스트가 필요하다
# 이후 제곱수를 반복문으로 돌 때 "가장 작은 min이상 max이하 제곱수"를 찾아서 등차수열로 리스트를 갱신시킨다.

# 이때 나는 가장 작은 min 이상 max 이하 제곱수를 찾는데 다시 반복문을 써서 시간초과가 나왔다.
# 사실 가장 작은 min 이상 max 이하 제곱수는
# ((min - 1) // square + 1) * square
# 이렇게 몫을 구하고 다시 곱하면 쉽게 구할 수 있다.
# 참조: https://haedallog.tistory.com/179  SM_Haedal
import sys
input = sys.stdin.readline

# 백만까지의 제곱수 구하기
squares = [True for _ in range(1000001)]
squares[0], squares[1] = False, False
for num in range(2, len(squares)):
    if not(squares[num]): continue
    times = 2
    while num * times <= 1000000:
        squares[num * times] = False
        times += 1
squares = [pow(num, 2) for num in range(len(squares)) if squares[num]]

# input
min, max = map(int, input().split())
numbers = [num for num in range(min, max+1)]

result = 0
for square in squares:
    if square > max:    break
    mini = ((min - 1) // square + 1) * square  # 가장 작은 수보다 1이 적은 수(이유는 가장 작은수가 가장 작은 제곱수임을 고려)를
    # 제곱수로 나누고(몫만 남김) 1을 더해 다시 제곱수를 곱하면 가장 작은 제곱수가 된다.
    ''' 시간을 줄이기 위해 가장 작은 제곱수를 구하는 과정을 하나의 수식으로 대체함
    for num in numbers:
        if not(num): continue
        if num % square == 0: # 나누어 떨어지면 square를 주기로 False 저장
        '''
    for num in range(mini, max+1, square):
        if numbers[num - min]:
            numbers[num - min] = False
            result += 1

print(max - min - result + 1)