'''
오목인지 판정하라
N*N 바둑판에 돌이 없으면 '.', 있으면 'o'

입력
첫 줄에 T
각 Tc마다 바둑판 크기 N, N줄에 걸쳐 오목판 배열
4
5
....o
...o.
..o..
.o...
o....
5
...o.
ooooo
...o.
...o.
.....
5
.o.oo
oo.oo
.oo..
.o...
.o...
5
.o.o.
o.o.o
.o.o.
o.o.o
.o.o.

출력
#{tc} YES or NO
'''
# 답안
def omok():
    dy = [1, 0, 1, -1]
    dx = [0, 1, 1, 1]
    for y in range(N):
        for x in range(N):
            if arr[y][x] == 'o':
                for dir in range(4):
                    ny = y
                    nx = x
                    cnt = 0
                    while 0 <= ny < N and 0 <= nx < N and arr[ny][nx] == 'o':
                        cnt += 1
                        ny += dy[dir]
                        nx += dx[dir]
                    if cnt >= 5:
                        return 'YES'
    return 'NO'
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [input() for _ in range(N)]
    print(f'#{tc} {omok()}')