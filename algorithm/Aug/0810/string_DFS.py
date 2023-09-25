'''
8개의 알파벳으로 구성된 문자열과 대응되는 인접 행렬을 입력받아주세요.
0번 알파벳으로부터 DFS로 노드들을 탐색하면서 출력해 주세요.

입력
첫 번째에 8개의 알파벳으로 이루어진 문자열이 주어집니다.
이어지는 8개의 줄에 걸쳐 인접행렬에 대한 정보가 주어집니다.
각 인접 행렬의 줄 번호 i, 칸 번호 j, 해당 위치의 값 Aij라고 할 때
Aij가 1이면 i번 알파벳에서 j번 알파벳으로 갈 수 있다는 것을 의미합니다.

출력
방문한 순서대로 노드 출력

입력예시
RKFCBICM
0 1 1 1 0 0 0 0
0 0 0 0 1 1 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 1 1
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0

출력
RKBIFCCM
'''


def dfs(chars, adj_m, start_node):
    stack = [start_node]  # stack 생성
    visited = [False] * len(chars)  # visited 생성
    result = []

    while stack:
        now = stack.pop()
        if not visited[now - 1]:  # 현재 정점 now에 인접하고 미방문 next
            visited[now - 1] = True
            result.append(chars[now - 1])

            for next_node in range(len(chars)):
                if adj_m[now - 1][next_node] and not visited[next_node]:
                    stack.append(next_node + 1)

    return result



chars = list(input())
arr = [list(map(int, input().split())) for _ in range(len(chars))]
print(dfs(chars, arr, 0))


# visited = [False for _ in range(N)] # 방문 여부를 저장하는 리스트, 처음에는 False로 초기화
def DFS(lst, v, adj):
    N = len(lst)
    visited = [False for _ in range(N)]
    print(lst[v], end='')
    visited[v] = True

    for i in range(N):
        if adj[v][i] and not visited[i]:        # 연결, 아직 방문 x
            DFS(lst, i, adj)                    # 탐색 계속
#
# lst2 = list(input())
# N = len(lst2)
# adj2 = [list(map(int, input().split())) for _ in range(N)]
# DFS(lst2, 0, adj2)