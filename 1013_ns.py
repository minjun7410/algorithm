# 구현문제
# 구현 문제는 나에게 쥐약인것 같다.
# 처음 푸는데 아래 주석같이 복잡하게 설계했기 때문에 신경써야할 부분이 많았는데
# 구글링으로 다른사람의 풀이를 보니 오토마타, DFA를 이용해서 푸는것을 보고 직접 메모장에 적어가면서 다시 풀었더니 AC
# *DFA: data flow analysis: 데이터 흐름 분석
# 이 문제처럼 현재 상태와 방향, 즉 흐름이 주된 구현문제는 DFA를 생각해보도록 해야겠다.
import sys
input = sys.stdin.readline
# solution
'''def solution(signal):
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
'''

def get_state(num, state):
    if signal[num] == '0':
        if state == 'a': return 'g'
        elif state == 'b': return 'c'
        elif state == 'c': return 'd'
        elif state == 'd': return 'd'
        elif state == 'e': return 'g'
        elif state == 'f': return 'h'
        elif state == 'g': return -1
        elif state == 'h': return 'd'
    else:
        if state == 'a': return 'b'
        elif state == 'b': return -1
        elif state == 'c': return -1
        elif state == 'd': return 'e'
        elif state == 'e': return 'f'
        elif state == 'f': return 'f'
        elif state == 'g': return 'a'
        elif state == 'h': return 'a'
def solution():
    state = 'a'
    for num in range(len(signal)):
        state = get_state(num, state)
        if state == -1: return False
    if state in ['a', 'e', 'f']:
        return True
    else:
        return False

# input
for _ in range(int(input())):
    signal = input().rstrip()
    print("YES" if solution() else "NO")

