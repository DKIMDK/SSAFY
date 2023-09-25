'''
NxN 크기의 미로에서 출발지 목적지가 주어진다.
이때 최소 몇 개의 칸을 지나면 출발지에서 도착지에 다다를 수 있는지 알아내는 프로그램을 작성하시오.

경로가 있는 경우 출발에서 도착까지 가는데 지나야 하는 최소한의 칸 수를, 경로가 없는 경우 0을 출력한다.

[입력]
첫 줄에 테스트 케이스 개수 T가 주어진다.  1<=T<=50
다음 줄부터 테스트 케이스의 별로 미로의 크기 N과 N개의 줄에 걸쳐 미로의 통로와 벽에 대한 정보가 주어진다. 5<=N<=100
0은 통로, 1은 벽, 2는 출발, 3은 도착이다.

[출력]
각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.

3
5
13101
10101
10101
10101
10021
5
10031
10111
10101
10101
12001
5
00013
01110
21000
01111
00000


#1 5
#2 5
#3 0
'''

def bfs(arr):
    direction = [(0, -1), (-1, 0), (0, 1), (1, 0)]
    N = len(arr)
    queue = []
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                queue.append([i, j, 0])
    while queue:
        y, x, cnt = queue.pop(0)
        for dy, dx in direction:
            ny, nx = y + dy, x + dx
            if 0 <= ny < N and 0 <= nx < N:
                if arr[ny][nx] == 3:
                    return cnt
                elif arr[ny][nx] == 0:
                    arr[ny][nx] = -1
                    queue.append([ny, nx, cnt + 1])
    return 0


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    ans = bfs(arr)
    print(f'#{tc} {ans}')