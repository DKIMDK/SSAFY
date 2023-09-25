tree = [[-1, -1] for _ in range(1001)]
N = 0
preorder = []
inorder = []
postorder = []

def dfs(now):

    if now == -1:
        return
    #전위순회
    preorder.append(now)
    #왼쪽탐색
    dfs(tree[now][0])

    #중위순회
    inorder.append(now)
    #오른쪽탐색
    dfs(tree[now][1])

    #후위순회
    postorder.append(now)

N = int(input())
for _ in range(N):
    root, left, right = map(int, input().split())
    tree[root][0] = left
    tree[root][1] = right
dfs(1)
print(' '.join(map(str, inorder)))
print(' '.join(map(str, preorder)))
print(' '.join(map(str, postorder)))