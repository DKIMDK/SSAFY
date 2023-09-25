'''
첫 번째 줄에 지역의 수 N과 버스로 이동 가능한 관계의 수 M이 공백을 구분으로 주어집니다.(1 ≤ N≤ 10 , 0≤ M≤ 45)
지역의 번호는 1부터 N까지의 번호가 부여됩니다.
두 번째 줄부터 M개의 줄에 걸쳐 정수 A, B가 공백으로 구분되어 주어집니다.
A와 B는 한 버스의 이동 경로를 의미하며, A에서 B 방향으로, 또는 B에서 A방향으로 이동할 수 있습니다. (1≤ A, B≤ N,A =/= B)

마지막 줄에 직장이 존재하는 지역 R과 출근하기 편하다는기준이 되는 버스 탑승 횟수 K가 공백으로 구분되어 주어집니다.(1 ≤ R≤ N , 0≤ K≤9)

출력
민철이가 출근하기 편하다고 느끼는이사 후보 지역의 개수를 출력합니다.
'''
def solution(R, K):
    queue = [R]
    visited = [0] * (N + 1)
    distance = [0] * (N + 1)
    visited[R] = 1
    result = 0
    while queue:
        p = queue.pop(0)
        if not visited[p]:
            visited[p] = 1
        for j in arr[p]:
            if not visited[j]:
                queue.append(j)
                distance[j] = distance[p] + 1
    for k in distance:
        if k != 0 and k <= K:
            result += 1
    return result + 1

N, M = map(int, input().split())
arr = [[] for _ in range(N + 1)]
for _ in range(M):
    A, B = map(int, input().split())
    arr[A].append(B)
    arr[B].append(A)
R, K = map(int, input().split())
ans = solution(R, K)
print(ans)