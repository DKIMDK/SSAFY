'''
도깨비의 보자기에는 n개 황금이 들어있습니다.
이 보자기는 한번 꺼낼 때가장 가벼운 물건만 꺼내지는마법의 보자기입니다.
보자기에 있는 황금을 꺼내면 보자기의 무게는 점점 가벼워집니다.
도깨비에게 들키지 않도록, 황금을 2개씩 꺼낼 때 마다 무거운 짱돌 1개를 넣어두려고 합니다.


황금의 개수 n과
보자기에 들어있는 황금의 무게들을 입력 받습니다.
보자기에서 2 개의 내용물을 꺼냅니다. 그리고 마지막으로 꺼낸 황금의 2 배 무게를 가진 짱돌 1개 넣습니다.
꺼내어진 돌이 황금이 아닐 때까지위 동작을 반복 합니다.


[세부사항]
1.황금과 짱돌이 같은 무게일때는,황금이 먼저나와야 합니다.
2. 꺼낸 돌이 짱돌일 경우, 즉시 꺼내는 작업을 중단합니다.
'''
import heapq
n = int(input())
golds = list(map(int, input().split()))
que = []
cnt = 0
for i in range(n):
    heapq.heappush(que, [golds[i], -1]) # -1 : gold
while que:
    x, tp = heapq.heappop(que)
    if tp == 0: # 0 : stone
        break
    cnt += 1

    y, tp =heapq.heappop(que)
    if tp == 0:
        break
    else:
        heapq.heappush(que, [y*2, 0])
    cnt += 1
print(cnt)