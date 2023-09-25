'''
바이러스가 한 마을을 집어삼켰다.
여기에 차르봄바라는 백신 폭탄을 떨어뜨려, 최대한 많은 바이러스를 제거하려고 한다.
차르봄바는 P 크기만큼으로 가로, 세로 방향으로 퍼져나가면서 해당 영역의 바이러스를 제거할 수 있다.
N * N 크기의 마을의 한 위치에 차르봄바를 떨어뜨려, 가장 많은 바이러스를 제거했을 때 제거된 바이러스의 수를 구하여라

입력
첫 번째 줄에는 테스트 케이스의 개수 T가 주어진다.
두 번째 줄부터 각 테스트 케이스가 주어진다.
각 테스트 케이스의 첫 번째 줄에는 마을의 크기 N, 차르봄바의 파워 P가 공백으로 구분되어 주어진다.
각 테스트 케이스의 두 번째 줄부터 N개의 줄에 걸쳐 각 좌표의 바이러스의 개수가 공백으로 구분되어 주어진다.

출력
각 테스트 케이스 tc에 대한 결과를 각 줄에 #tc을 출력하고 한 칸을 띄운 다음 정답을 출력한다.

입력 예시
4
7 3
1 8 1 4 2 5 1
1 5 2 6 7 2 3
7 9 5 5 1 9 8
3 7 0 9 8 0 7
5 5 3 9 5 1 4
2 5 9 3 3 6 8
0 1 4 1 8 4 0
7 2
3 3 8 8 5 5 0
4 3 9 6 0 2 5
0 8 6 2 0 3 8
5 1 0 8 2 9 6
1 7 5 3 9 2 0
8 4 2 9 5 5 3
2 3 6 2 9 1 4
5 3
9 3 0 4 0
3 9 4 0 4
0 4 9 4 0
4 0 4 9 3
0 4 0 3 9
5 4
1 2 3 4 9
2 3 4 5 9
3 4 5 6 9
4 5 6 7 9
9 9 9 9 9

'''

def vac(arr, P):
    direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    answer = 0
    N = len(arr)
    for i in range(N):
        for j in range(N):
            cnt = arr[i][j]
            for x, y in direction:
                for p in range(1, P+1):
                    dx, dy = i + x * p, j + y * p
                    if 0 <= dx < N and 0 <= dy < N:
                        cnt += arr[dx][dy]
            answer = max(answer, cnt)
    return answer

T = int(input())
for tc in range(1, T+1):
    N, P = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    answer = vac(arr, P)
    print(f'#{tc} {answer}')