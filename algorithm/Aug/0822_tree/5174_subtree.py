'''
트리의 일부를 서브 트리라고 한다.
주어진 이진 트리에서 노드 N을 루트로 하는 서브 트리에 속한 노드의 개수를 알아내는 프로그램을 만드시오.

주어지는 트리는 부모와 자식 노드 번호 사이에 특별한 규칙이 없고,
부모가 없는 노드가 전체의 루트 노드가 된다.

[입력]

첫 줄에 테스트케이스의 수 T가 주어진다. 1<=T<=50
다음 줄부터 테스트 케이스의 별로 첫 줄에 간선의 개수 E와 N이 주어지고, 다음 줄에 E개의 부모 자식 노드 번호 쌍이 주어진다.
노드 번호는 1번부터 E+1번까지 존재한다. 1<=E<=1000, 1<=N<=E+1

[출력]
각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.

'''

def sub_tree(node):         # 서브트리의 노드의 수를 찾는 함수
    global cnt
    for i in range(2):      # 왼쪽, 오른쪽
        if tree[i][node]:   # 해당 노드의 자식이 있다면
            cnt += 1
            n = tree[i][node]   # 자식 노드의 번호
            sub_tree(n)

T = int(input())
for tc in range(1, T + 1):
    E, N = map(int, input().split())
    temp = input().split()
    # 노드번호는 1번부터 E+1 번까지 존재 -> 이진트리 리스트 초기화
    tree = [[0 for _ in range(E+2)] for _ in range(2)]
    for i in range(E):
        p_node = int(temp[2*i])         # 부모 노드 번호 -> 짝수 번째
        c_node = int(temp[2*i + 1])     # 자식 노드 번호 -> 홀수 번째
        if tree[0][p_node] == 0:        # 왼쪽 자식이 없다면 할당, 왼쪽 자식이 있다면 오른쪽에 할당
            tree[0][p_node] = c_node
        else:
            tree[1][p_node] = c_node
    cnt = 1
    sub_tree(N)
    print(f'#{tc} {cnt}')