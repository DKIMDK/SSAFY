'''
첫째 줄에 결혼정보회사에 가입된 사람의 수 N과  ( 2 <= N <= 100)
서로 연관됨을 나타내는 관계수 T 가 입력됩니다. ( 1 <= T <= N(N-1)/2 )
둘째 줄에는 T 줄에 걸쳐 서로 연관이 있는 사람들의 정보가 주어집니다.
사람들 지인 관계 정보는 A B 형태로 입력되며, A 번 사람과 B번 사람이 서로 지인 임을 나타냅니다. ( 1 <= A, B <= N, A=/=B)

마지막 줄에는 코코씨와 결혼 상대로 적합한지 확인해볼 상대 번호가 입력됩니다. ( 1 <= 번호 <= N)

출력
연관이 있는 상대이면 YES연관이 없는 상대이면 NO를 출력해주세요.

'''
def solution(a, b):
    queue = [a]
    visited[a] = 1
    while queue:
        p = queue.pop(0)
        if not visited[p]:
            visited[p] = 1
        for n in arr[p]:
            if not visited[n] and n == b:
                return 'YES'
            elif not visited[n]:
                queue.append(n)
    return 'NO'


N = int(input())
T = int(input())
arr =[[] for _ in range(N + 1)]
visited = [0] * (N + 1)
for _ in range(T):
    i, j = map(int, input().split())
    arr[i].append(j)
    arr[j].append(i)
c = int(input())
p = int(input())
ans = solution(c, p)
print(ans)