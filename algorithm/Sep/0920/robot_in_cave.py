N, s, e = map(int, input().split())
al = [[] for _ in range(N + 1)]
visited = [0 for _ in range(N + 1)]
sum_v = 0
MIN = float('inf')
MAX = float('-inf')

def dfs(node, dest):
    global sum_v, MIN, MAX

    if node == dest:
        if sum_v - MAX < MIN:
            MIN = sum_v - MAX

        return
    for next in al[node]:
        if visited[next[0]] == 1:
            continue
        sum_v += next[1]
        visited[next[0]] = 1
        temp = MAX
        # 지금까지 방문한 통로중 가장 긴 것을 MAX에 저장
        if next[1] > MAX:
            MAX = next[1]
        dfs(next[0], dest)
        #dfs 호출 후 이전 상태로 복원
        visited[next[0]] = 0
        sum_v -= next[1]
        MAX = temp

for _ in range(N - 1):
    from_v, to_v, cost = map(int, input().split())
    al[from_v].append((to_v, cost))
    al[to_v].append((from_v, cost))
visited[s] = 1
dfs(s, e)
print(MIN if MIN != float('inf') else 0)