# 에라토스테네스의 체
# min의 제한이 1조로 매우 크지만 min과 max 사이는 백만으로 비교적 작다.
# min의 값이 어떻든 간에 가장 작은 제곱수인 4부터 max와 가까운 제곱수의 리스트가 필요하다
import sys
input = sys.stdin.readline

# 백만까지의 제곱수 구하기
squares = [True for _ in range(1001)]
squares[0], squares[1] = False, False
for num in range(2, len(squares)):
    if not(squares[num]): continue
    times = 2
    while num * times <= 1000:
        squares[num * times] = False
        times += 1
squares = [pow(num, 2) for num in range(len(squares)) if squares[num]]

# input
min, max = map(int, input().split())
numbers = [num for num in range(min, max+1)]

result = 0
for square in squares:
    if square > max:    break
    for num in numbers:
        if not(num): continue
        if num % square == 0: # 나누어 떨어지면 square를 주기로 False 저장
            times = 0
            while num + (square * times) <= max:
                if not(numbers[num + (square * times) - min]):
                    times += 1
                    continue
                numbers[num + (square * times) - min] = False
                times += 1
                result += 1
            break
print(max - min - result + 1)