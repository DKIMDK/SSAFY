'''
사각형 그리기 게임에는 N x N 크기의 게임판이 주어진다.
이 게임의 목표는 최대한 면적이 큰 사각형을 몇 개 그릴 수 있는가?를 구하는 것이다.

사각형을 그리는 데에는 아래 두가지 조건을 충족해야만 한다.
[1] 특정 좌표를 기준으로, "우측 하단"의 방향으로 사각형을 그릴 수 있다.
[2] 왼쪽 상단 좌표의 값과 우측 하단 좌표의 값이 동일해야 한다.

N x N 크기의 게임판이 주어졌을 때, 최대 면적의 사각형을 규칙대로 그릴 수 있는 총 사각형의 개수를 구하라.

입력 예시
3
3
1 1 1
1 1 1
1 1 1
3
1 2 3
3 2 1
2 1 3
3
1 2 3
1 2 3
1 2 3

출력 예시
#1 1
#2 3
#3 3

'''
def solution(arr):
    max_area = 0
    cnt = 0
    N = len(arr)
    for y in range(N):
        for x in range(N):
            now = arr[y][x]
            for dy in range(y, N):
                for dx in range(x, N):
                    next = arr[dy][dx]
                    if now == next:
                        area = (dy - y + 1) * (dx - x + 1)
                        if max_area < area:
                            max_area = area
                            cnt = 1
                        elif max_area == area:
                            cnt += 1
    return cnt

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    ans = solution(arr)
    print(f'#{tc} {ans}')
