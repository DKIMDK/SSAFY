def solution(y, x, route_sum):
    if y == N - 1 and x == N - 1:
        return route_sum + arr[y][x]

    if y < N and x < N:
        route_sum += arr[y][x]
        down_sum = solution(y + 1, x, route_sum)
        right_sum = solution(y, x + 1, route_sum)
        return min(down_sum, right_sum)

    return float('inf')


dir = [(0, 1), (1, 0)]

def dfs(x, y, sum_v):
    global result

    if sum_v >= result:
        return

    if x == N - 1 and y == N - 1:
        if sum_v < result:
            result = sum_v
        return
    for dx, dy in dir:
        nx, ny = x + dx, y + dy
        if -1 < nx < N and -1 < ny < N:
            dfs(nx, ny, sum_v + arr[nx][ny])

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    result = float('inf')
    dfs(0, 0, arr[0][0])
    ans = solution(0, 0, 0)
    print(f'#{tc} {result}')


