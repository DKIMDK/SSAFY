'''
첫 번째 줄에 지역의 수 N과 대중교통으로이동 가능한 관계의 수 M이 공백을 구분으로 주어집니다.(1 ≤ N ≤ 10 , 0≤ M≤ 45)
두 번째 줄부터 M개의 줄에 걸쳐에 정수 A, B가 공백을 구분으로 주어지며
A와 B는 서로간에 대중교통으로 1번의 환승으로 갈 수 있다는 것을 의미합니다. (1≤ A,B≤ N)
단, A와 B가 같은 경우는 존재하지 않습니다.
마지막 줄에 화재가 발생한 지역 T가 주어집니다.(1 < T)

출력
T번 지역을 피해 N번 지역으로 출근할 수 있는 최소 환승을 출력합니다.
단, 출근할 수 있는 방법이 없다면 -1을 출력합니다.
'''
def solution(N, T):
    queue = [(1, 0)]
    visited = [0] * (N+1)
    visited[1] = 1
    visited[T] = -1
    while queue:
        now, cnt = queue.pop(0)
        if not visited[now]:
            visited[now] = 1
        for next in arr[now]:
            if not visited[next] and next == N:
                return cnt + 1
            elif not visited[next]:
                queue.append((next, cnt + 1))
    return -1

N, M = map(int, input().split())
arr = [[] for _ in range(N + 1)]
for _ in range(M):
    A, B = map(int, input().split())
    arr[A].append(B)
    arr[B].append(A)
T = int(input())
ans = solution(N, T)
print(ans)