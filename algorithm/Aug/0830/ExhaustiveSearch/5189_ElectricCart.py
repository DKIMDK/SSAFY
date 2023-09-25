def DFS(idx, now_sum):
    global result
    if result <= now_sum:
        return
    if idx == N:
        if result > now_sum:
            result = now_sum
            return
    for i in range(N):
        if not visited[i] and i != idx and i:    # 여기서 시작구역과 구분을 못하여 이상하게 나옴
            visited[i] = 1
            DFS(idx + 1, now_sum + arr[idx][i])
            visited[i] = 0


def cart(cur, start, total):
    global result
    if cur == N - 1:                                        # 모든 구역 다 돌았으면
        result = min(result, arr[start][0] + total)         # 총 배터리 사용량의 최소값 업데이트
        return
    for i in range(1, N):
        if visited[i] == 0 and start != i:                  # 아직 방문하지 않았고, 시작구역이랑 다르면
            visited[i] = 1                                  # 방문표시
            cart(cur + 1, i, total + arr[start][i])         # 다음 구역 이동
            visited[i] = 0                                  # 방문표시 지우기
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [0 for _ in range(N)]
    result = float('inf')
    cart(0, 0, 0)
    # DFS(0, 0)
    print(f'#{tc} {result}')