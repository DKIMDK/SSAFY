def solution(arr):
    direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]                      # 방향 설정
    N = len(arr)                                                        # 풍선게임 맵 크기
    maximum = 0                                                         # 최대점수
    minimum = 99999                                                     # 최소점수 임의설정 N <=20, Aij <= 9이므로 모든 칸 다 더해도 3600
    for y in range(N):
        for x in range(N):                                              # 맵의 각 칸 순회
            power = arr[y][x]                                           # 풍선이 터질 범위
            point = arr[y][x]                                           # 현재 점수
            for dy, dx in direction:
                for i in range(1, power + 1):
                    ny, nx = y + i * dy, x + i * dx                     # 각 방향을 power만큼 순회
                    if 0 <= ny < N and 0 <= nx < N:                     # 맵을 벗어나지 않는 선에서
                        point += arr[ny][nx]                            # 점수 계산
            if maximum <= point:
                maximum = point                                         # 최대점수 계산
            if minimum >= point:
                minimum = point                                         # 최소점수 계산
    result = maximum - minimum                                          # 최종점수 계산
    return result

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    ans = solution(arr)
    print(f'#{tc} {ans}')