# 구현문제
import sys
input = sys.stdin.readline
# solution
def solution(signal):
    signal_len = len(signal) - 1
    if signal_len <= 1: return False  # 길이가 1인 신호는 TRUE가 될 수 없다.
    location = 0
    while location < signal_len:  # '1'의 경우 마지막에 1을 남기고 continue 시킨다.
        if signal[location] == '1':  # case 1001
            if location + 2 >= signal_len or signal[location+1] == '1' or signal[location+2] == '1':
                return False  # 1다음 0이 두개 있는 지 검사
            location += 3
            while location < signal_len and signal[location] == '0':
                location += 1
            if location == signal_len: return False  # 시그널이 0으로 끝날 경우
            while location < signal_len and signal[location] == '1':
                if location + 2 < signal_len and signal[location+1] == '1' and signal[location+2] == '0':
                    location += 1  # 앞으로 1다음 0이 있는지 검사
                    break
                location += 1
        else:
            location += 1
            if location >= signal_len or signal[location] == '0': return False
            location += 1
    return True



# input
for _ in range(int(input())):
    signal = input()
    print("YES" if solution(signal) else "NO")

