'''
N * N 사각형의 전투장에는 각 칸마다 몇 마리의 몬스터가 있는지 적혀 있다.
광대한 영역에 마법을 시전할 수 있는 마법사 Mort는 전투장에서 최대한 많은 몬스터를 잡으려 한다.

마법사 Mort는 대각선 방향으로 각 방향마다 K 칸만큼 마법을 시전할 수 있다.

마법은 마법사가 있는 지점에서 마법을 시전한 위치를 제외하고 대각선 방향으로 방향 변화 없이 시전된다.

입력예시:
5
1 2 3 5 10
9 7 2 2 9
0 0 1 5 7
5 2 3 2 2
1 1 1 1 1
2

출력예시: 26
'''

direction = [(-1, 1), (1, 1), (1, -1), (-1, -1)]
T = int(input())
arr = [list(map(int, input().split())) for _ in range(T)]
K = int(input())
answer = 0
for i in range(T):
    for j in range(T):
        cnt = 0
        for x, y in direction:
            for p in range(1, K + 1):
                dx, dy = i + x * p, j + y * p
                if 0 <= dx < T and 0 <= dy < T:
                    cnt += arr[dx][dy]

        if answer < cnt:
            answer = cnt
print(answer)

