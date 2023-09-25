# T = int(input())
# for tc in range(1, T+1):
#     N, M = map(int, input().split())
#     m = N // 2
#     arr = [list(map(int, input().split())) for _ in range(N)]
#
#     for K in range(1, m + 1):
#         profit = -(K * K + (K-1) * (K-1))
#         max_profit = 0
#         for y in range(N):
#             for x in range(N):
#                 # K와 관련해서 방범 서비스 범위를 설정하는 코드를 이 줄에 짜야 함
#                 for i in range(K):
#                     for j in range(x - K - i, x + K - i):
#                         if 0 <= y+i < N and 0 <= y-i < N and 0 <= j < N:
#                             profit += arr[y+i][j] * M
#                             profit += arr[y-i][j] * M
#                             break
#                 profit -= sum(arr[y])
#
#     if max_profit < profit:
#         max_profit = profit
#         tmp = [K, max_profit]
#     # 내가 구해야 하는 것은 max_profit일 때 집의 수
#     print(f'{tmp}')

## answer code

def solution():
    ans = 0
    K = N
    for k in range(K, 0, -1):
        cost = k * k + (k - 1) * (k - 1)
        for y in range(N):
            for x in range(N):
                cnt = 0
                for hy, hx in houses:
                    dist = abs(hy - y) + abs(hx - x)
                    if dist < k:
                        cnt += 1
                if cnt * M - cost >= 0:
                    ans = max(ans, cnt)
        if ans != 0:
            return ans
    return ans

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    houses = []
    for i in range(N):
        for j in range(N):
            if arr[i][j]:
                houses.append([i, j])
    result = solution()
    print(f'#{tc} {result}')
