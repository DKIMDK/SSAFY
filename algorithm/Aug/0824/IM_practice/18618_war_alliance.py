'''
춘추 전국 시대는 여러 국가간의 전쟁과 동맹이 난무하던 시대였습니다.
한 때에는 N개의 국가가 존재하며, 각 국가들은 P명의 인구 수를 가지고 있습니다.

아래 그림은 A부터 G까지의 총 7개의 나라를 나타낸 지도입니다.
각 국가의 인구 수는 다음과 같다고 가정합시다.

A : 10
B : 20
C : 30
D : 40
E : 50
F : 60
G : 70
B와 D는 동맹을 맺고, A와 C와 F가 동맹을 맺었다고 가정해 봅시다.
동맹을 맺은 국가끼리는 전쟁을 일으키지 않으며, 동맹을 파기하는 일 또한 없습니다.
이러한 상황에서, B연합군(D + B) 와 F연합군(A + C + F)가 전쟁을 하게 된다고 합시다.

이런 상황에서는 둘 중 연합군의 인구수가 더 큰 국가가 승리합니다.
B연합군의 인구 수는  60 (D + B), F연합군의 인구 수는 100 입니다. (A + C + F)
이 전쟁에서 B연합군의 국가들은 멸망하고, 살아남은 국가의 수는 5개가 됩니다. (A, C, E, F, G)

만약 두 국가의 인구 수가 동일하다면, 두 국가 모두 멸망합니다.


춘추 전국 시대의 여러 동맹과 전쟁 이후 살아남은 국가의 수를 출력해 주세요.

입력
첫번째 줄에 각 국가의 수 N을 입력받습니다. (2 <= N <= 25)
두번째 줄에 N개 각 국가의 인구 수를 입력 받습니다. 인구의 수는 0 이상, 100,000 이하입니다.
세번째 줄에 동맹과 전쟁의 상황의 개수 T를 입력 받습니다. (1 <= T <= 100)
그 후의 T개의 줄에는 상황, 국가 A, 국가 B를 한 줄로 입력 받습니다.
상황에서 "alliance"는 동맹, "war"은 전쟁을 의미합니다.

출력
첫번째 줄에 동맹과 전쟁 이후 살아남은 국가의 개수를 출력합니다.

'''

def find(node):
    if node != root[node]:          #노드의 부모가 자기 자신이 아니라면
        root[node] = find(root[node])   # 부모 노드를 찾아간다 -> 경로 압축 수행
    return root[node]

def union(x, y):
    root_x = find(x)                    # x의 루트 부모 찾기
    root_y = find(y)                    # y의 루트 부모 찾기
    if root_x == root_y:
        population[x] = population[y]
        return
    if rank[root_x] > rank[root_y]:     # x의 랭크가 더 크다면 y의 부모를 x의 루트부모로 설정
        root[root_y] = root_x
        population[root_x] += population[root_y]
        population[root_y] = population[root_x]
        group[root_x] += 1

    else:
        root[root_x] = root_y
        population[root_y] += population[root_x]
        population[root_x] = population[root_y]
        group[root_y] += 1

        if rank[root_x] == rank[root_y]:
            rank[root_y] += 1


N = int(input())
root = [i for i in range(N+1)]
rank = [0] * (N+1)
population = [0] + list(map(int, input().split()))
group = [1] * (N+1)
T = int(input())
for tc in range(T):
    situation, a, b = input().split()
    int_a, int_b = ord(a) - 64, ord(b) - 64
    if situation == 'alliance':
        union(int_a, int_b)

    else:
        if population[root[int_a]] > population[root[int_b]]:
            N -= group[root[int_b]]
        elif population[root[int_a]] < population[root[int_b]]:
            N -= group[root[int_a]]
        else:
            N -= group[root[int_a]] - group[root[int_b]]
print(N)
print(population)

