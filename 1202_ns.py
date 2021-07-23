# 우선 순위 큐 문제

# 1. 가방 최대 무게를 기준으로 오름차순으로 정렬한다.
# 2. 보석 무게를 기준으로 최대 힙을 만든다.
# 3. 가방 무게로 반복문을 돈다.
# 3-1. 우선 순위 큐를 도는데 if [가방 무게] < [보석 무게] continue
# 3-2. continue 하기 전에 다른 최소힙을 만들어서 저장한다.
# 3-3. 조건문을 통과하면 pop 하고 result += pop
# 3-4. 최소힙을 모두 pop해서 최대힙에 넣어줌 (가장 값이 큰 보석을 할당하고 힙에서 제외)
# 3-5. 힙을 모두 돌아도 조건문을 만족 못하면 break
# 4. return result
