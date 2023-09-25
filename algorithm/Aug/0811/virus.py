'''
신종 바이러스인 웜 바이러스는 네트워크를 통해 전파됩니다.
한 컴퓨터가 웹 바이러스에 걸리면 그 컴퓨터와 네트워크 상에서 연결되어 있는 모든 컴퓨터는 웜 바이러스에 걸리게 됩니다.

예를 들어 7대의 컴퓨터가 그림과 같이 네트워크 상에서 연결되어 있다고 할 때
1번 컴퓨터가 웜 바이러스에 걸리면 웜 바이러스는 2번과 5번 컴퓨터를 걸쳐 3번과 6번까지 전파되며
2,3,5,6 네 대의 컴퓨터는 웜 바이러스에 걸리게 됩니다.
하지만 4번과 7번 컴퓨터는 네트워크 상에서 연결되어 있지 않기 때문에 영향을 받지 않습니다.
컴퓨터 수와 네트워크 상 연결되어 있는 정보가 주어질 때 웜 바이러스에 걸리게 되는 컴퓨터의 수를 출력하는 프로그램 작성

입력
첫째 줄에는 컴퓨터의 수 (1<=n<=100)
둘째 줄에는 네트워크 상에서 직접 연결되어 있는 컴퓨터 쌍의 수
이어서 그 수만큼 한 줄에 한 쌍 씩 네트어크 상에서 직접 연결되어 있는 컴퓨터의 번호 쌍이 주어집니다.

예시
7
6
1 2
2 3
1 5
5 2
5 6
4 7

출력예시
4
'''
N = int(input())
M = int(input())
arr = [[0] * N for _ in range(N)]
visited = [0] * N
for _ in range(M):
    i, j = map(int, input().split())
    arr[i-1][j-1] = arr[j-1][i-1] = 1


# def virus(start, c, adj):
#     stack = [start]  # path를 저장할 stack
#     visited = [False] * (c + 1)  # 노드를 방문했는지를 0, 1로 표현
#
#     while stack:  # 스택이 비어있으면 반복문 종료
#         now = stack.pop()  # 스택의 마지막 노드를 꺼냄
#         visited[now] = True  # 현재 노드를 방문
#         for next in range(1, c + 1):
#             if adj[now][next] and not visited[next]:  # 방문하지 않았고, 연결되어 있다면
#                 stack.append(next)
#     return

def DFS(v):
    visited[v] = 1
    for i in range(N):
        if arr[v][i] == 1 and not visited[i]:
            DFS(i)
DFS(0)

print(sum(visited) -1)