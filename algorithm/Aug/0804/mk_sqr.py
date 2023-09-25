'''
사각형 그리기 게임에는 N*N 크기의 게임판이 주어진다.
이 게임의 목표는 치ㅗ대한 면적이 큰 사각형을 몇 개 그릴 수 있는가?를 구하는 것이다.

사각형을 그리는 데에는 아래 두가지 조건을 충족해야 한다.
(1) 특정 좌표를 기준으로, "우측 하단"의 방향으로 사각형을 그릴 수 있다.
(2) 왼쪽 상단 표의 값과 우측 하단 좌표의 값이 동일해야 한다.

'최대 면적의 사각형의 총 개수'

입력
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

출력
#1 1
#2 3
#3 3
'''
T = int(input())
for tc in range(1, T+1):
    max_area = 0
    cnt = 0
    N = int(input())
    board = [int(i) for _ in range(N) for i in input().split()]
    for now in range(len(board)):
        x, y = now // N, now % N
        k = board[now]
        for next in range(now + 1, len(board)):
            k2 = board[next]
            x2, y2 = next // N, next % N
            if k2 == k:
                area = (x2 - x + 1) * (y2 - y + 1)
                if max_area < area:
                    max_area = area
                    cnt = 1
                elif max_area == area:
                    cnt += 1

    print(f'#{tc} {cnt}')