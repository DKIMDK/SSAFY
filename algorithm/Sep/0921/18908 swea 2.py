import heapq

def find_set(x):
    if parents[x] == x:
        return x
    parents[x] = find_set(parents[x])
    return parents[x]


def union(x, y):
    x = find_set(x)
    y = find_set(y)

    if x == y:
        return
    if x > y:
        parents[x] = y
    else:
        parents[y] = x

T = int(input())
for tc in range(1, T+1):
    heap = []
    V, E = map(int, input().split())
    for _ in range(E):
        f, t, w = map(int, input().split())
        heapq.heappush(heap, [w, f, t])

    parents = [i for i in range(V + 1)]
    cnt = 0
    sum_weight = 0
    while heap:
        w, f, t = heapq.heappop(heap)
        if find_set(f) != find_set(t):
            cnt += 1
            sum_weight += w
            union(f, t)
            if cnt == V:
                break

    print(f'#{tc} {sum_weight}')
