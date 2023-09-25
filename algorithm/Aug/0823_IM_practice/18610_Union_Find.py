# Union-Find
## 노드간의 집합 관계를 빠르게 파악하고 관리해야 하는 경우
## Union -> 두 그룹을 하나로 합친다.
# Find -> 특정 노드가 어디에 속해있는지 찾는다.
'''
1번부터 N번까지의 노드가 있습니다.
연결 된 노드 끼리는 같은 그룹으로 취급합니다.

Query 명령어에 따라 두 개의 노드를 연결하고, 같은 그룹인지 출력하는 프로그램을 작성 해주세요.

입력
첫 번째 줄에 N과 Query의 개수 Q가 입력됩니다. (1 <= N, Q <= 1,000)
두 번째 줄부터 [K, A, B] 형태로 입력이 주어집니다. (1 <= A, B <= N, A ≠ B)

[0, A, B] : 노드 A, B가 서로 같은 그룹 이라면 YES, 아니면 NO 를 출력합니다.
[1, A, B] : 노드 A, B를 연결합니다.

출력
Query의 순서에 따라 YES 또는 NO를 출력합니다.
'''
#
# def find(A, B):
#     queue = [A]
#     visited = [0] * (N + 1)
#     visited[A] = 1
#     while queue:
#         p = queue.pop(0)
#         if not visited[p]:
#             visited[p] = 1
#         for n in arr[p]:
#             if not visited[n] and n == B:
#                 return('YES')
#             elif not visited[n]:
#                 queue.append(n)
#     return('NO')
#
# N, Q = map(int, input().split())
#
# arr = [[] for _ in range(N+1)]
# for tc in range(Q):
#     K, A, B = map(int, input().split())
#     if K == 0:
#         print(find(A, B))
#     elif K == 1:
#         arr[A].append(B)
#         arr[B].append(A)


## 답안 코드
def find(node):
    if node != root[node]:          #노드의 부모가 자기 자신이 아니라면
        root[node] = find(root[node])   # 부모 노드를 찾아간다 -> 경로 압축 수행
    return root[node]

def union(x, y):
    root_x = find(x)                    # x의 루트 부모 찾기
    root_y = find(y)                    # y의 루트 부모 찾기
    if rank[root_x] > rank[root_y]:     # x의 랭크가 더 크다면 y의 부모를 x의 루트부모로 설정
        root[root_y] = root_x
    else:
        root[root_x] = root_y
        if rank[root_x] == rank[root_y]:
            rank[root_y] += 1

N, Q = map(int, input().split())
rank = [0] * (N + 1)
root = [i for i in range(N + 1)]    # 각 노드의 루트 부모를 저장하는 리스트
for _ in range(Q):
    K, A, B = map(int, input().split())
    if K == 0:
        if find(A) == find(B):
            print('YES')
        else:
            print('NO')
    else:
        union(A, B)