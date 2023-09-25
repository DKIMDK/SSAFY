n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
parent = [i for i in range(n)]

def Find(node):
    if node == parent[node]:
        return node
    parent[node] = Find(parent[node])
    return parent[node]

def Union(a, b):
    pa = Find(a)
    pb = Find(b)
    if pa != pb:
        parent[pb] = pa


for i in range(n):
    for j in range(i+1, n):
        if arr[i][j] == 0:
            continue
        if Find(i) == Find(j):
            print('WARNING')
            exit()
        Union(i, j)
print('STABLE')

