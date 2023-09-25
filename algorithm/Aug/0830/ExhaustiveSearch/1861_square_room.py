# def solution(y, x, cnt):
#     if visited[y][x]:
#         return cnt
#
#     max_count = cnt  # 최대 연속된 수를 저장할 변수 추가
#     visited[y][x] = 1  # 현재 위치를 방문 처리
#
#     for dy, dx in directions:
#         ny, nx = y + dy, x + dx
#         if 0 <= ny < N and 0 <= nx < N:
#             if arr[ny][nx] - arr[y][x] == 1:
#                 # 현재 위치에서 다음 위치로 이동 가능한 경우
#                 max_count = max(max_count, solution(ny, nx, cnt + 1))
#
#     visited[y][x] = 0  # 백트래킹, 현재 위치를 다시 방문 가능하도록 처리
#     return max_count  # 최대 연속된 수 반환
#
#
#
# T = int(input())
# for tc in range(1, T + 1):
#     N = int(input())
#     arr = [list(map(int, input().split())) for _ in range(N)]
#     visited = [[0] * N for _ in range(N)]  # 수정된 부분
#     directions = [(1, 0), (0, -1), (-1, 0), (0, 1)]
#     max_result = 0
#     for i in range(N):
#         for j in range(N):
#             max_result = max(max_result, solution(i, j, 1))  # 모든 위치에서 최대 연속된 수 계산
#     print(f'#{tc} {i} {max_result}')

for tc in range(1, int(input()) + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    v = [0] * (N * N + 1)
    for i in range(N):
        for j in range(N):
            for r, c in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                if 0 <= i + r < N and 0 <= j + c < N and arr[i][j] + 1 == arr[i+r][j+c]:
                    v[arr[i][j]] = 1
    start, cnt, temp = 0, 1, 1
    for i in range(len(v) - 1, -1, -1):
        if v[i] == 1:
            temp += 1
        else:
            if cnt <= temp:
                cnt = temp
                start = i + 1
            temp = 1
    print(f'#{tc} {start} {cnt}')