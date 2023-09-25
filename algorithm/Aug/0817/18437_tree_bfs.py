'''
트리 자료구조에서 너비 우선 탐색법으로 각 노드를 탐색해주세요.

시작 지점 부터, 노드에 방문할 때마다 값을 출력 해주세요.
출발지점은 입력으로 주어 집니다.
한번 방문 했던 노드는 방문할 수 없습니다.
트리 자료구조는 인접행렬로 하드코딩 해주세요.

입력
탐색을 시작할 노드 번호 K가 주어집니다.

출력
K부터 시작하여 너비 우선 탐색을 진행하여 방문한 순서대로 노드 번호를 출력합니다.
단, 다양한 방법이 가능한 경우 더 작은 번호의 노드를 먼저 들리는 방법을 출력합니다.

'''
from collections import deque

arr = [[0, 1, 0, 0, 1, 0],
       [0, 0, 1, 0, 0, 1],
       [0, 0, 0, 1, 0, 0],
       [0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0]]
queue = [0]
for i in range(6):
    for j in range(6):
        if arr[i][j] == 1:
            queue.append(j)
print(*queue)

k = int(input())
def bfs(now):
    q = deque()
    q.append(now)
    while q:
        now = q.popleft()
        print(now, end = ' ')
        for i in range(6):
            if arr[now][i] == 1:
                q.append(i)

bfs(k)