'''
인디언 족장님은 전통악기를 이용한 오케스트라를 하려고 합니다.
족장님은 총 26명의 인디언 연주자를 선별하였고,
26명의 연주자들에게는 'A' ~ 'Z' 의 닉네임을 부여하였습니다.
이제, 음색이 비슷한 사람끼리 팀을 구성하고자 합니다.

연주자들을 여러 개의  팀으로 묶었을 때
몇 개의 팀이 존재하는 지 출력 하세요.
그리고 팀이 조직되지 못한 남은 개인 연주자가 몇 명인지 출력해 주세요.

입력
첫 줄에는 N 개의 명령이 들어옵니다. (1 <= N <= 10,000)
다음 N 개의 줄에는 알파벳 2개씩 팀으로 묶을 인디언들의 닉네임이 입력됩니다.
입력 받은 두 인디언이 이미 같은 팀인경우, 명령을 무시합니다.


만약 족장이 A, B 가 음색이 비슷하고, B, C가 음색이 비슷하다고 판단되면
{A,B} / {B,C} 로 입력이 주어집니다. 이런 경우 A, B, C 는 한 팀입니다.

출력
첫 줄에는 조직된 팀의 수를 출력하세요.
다음 줄에는 팀으로 구성되지 못한 개인 연주자 인디언들의 수를 출력합니다.
'''
'''
def ctoi(letter):
    letter = letter.upper()
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    if letter in alphabet:
        return ord(letter) - ord('A') + 1

def find(node):
    if node != root[node]:          #노드의 부모가 자기 자신이 아니라면
        root[node] = find(root[node])   # 부모 노드를 찾아간다 -> 경로 압축 수행
    return root[node]

def union(x, y):
    root_x = find(x)                    # x의 루트 부모 찾기
    root_y = find(y)                    # y의 루트 부모 찾기
    if rank[root_x] > rank[root_y]:     # x의 랭크가 더 크다면 y의 부모를 x의 루트부모로 설정
        root[root_y] = root_x
    else:
        root[root_x] = root_y
        if rank[root_x] == rank[root_y]:
            rank[root_y] += 1

T = int(input())
rank = [0] * (26 + 1)
root = [i for i in range(26 + 1)]    # 각 노드의 루트 부모를 저장하는 리스트
for _ in range(T):
    x, y = input().split()
    x, y = ctoi(x), ctoi(y)
    union(x, y)

count_dict = {}
team = 0

for num in root:
    if num != 0:
        if num in count_dict:
            count_dict[num] += 1
            if count_dict[num] == 2:
                team += 1
        else:
            count_dict[num] = 1

single = sum(1 for count in count_dict.values() if count == 1)
print(team)
print(single)
'''
## 답안 코드
def find(node):
    if node != root[node]:          #노드의 부모가 자기 자신이 아니라면
        root[node] = find(root[node])   # 부모 노드를 찾아간다 -> 경로 압축 수행
    return root[node]

def union(x, y):
    root_x = find(x)                    # x의 루트 부모 찾기
    root_y = find(y)                    # y의 루트 부모 찾기
    if root_x == root_y:                # 입력 받은 두 인디언이 이미 같은 팀인 경우, 명령을 무시
        return
    if rank[root_x] > rank[root_y]:     # x의 랭크가 더 크다면 y의 부모를 x의 루트부모로 설정
        root[root_y] = root_x
    else:
        root[root_x] = root_y
        if rank[root_x] == rank[root_y]:
            rank[root_y] += 1

N = int(input())
rank = [0] * 26
root = [i for i in range(26)]
for _ in range(N):
    a, b = input().split()
    union(ord(a) - 65, ord(b) - 65) # 닉네임을 숫자로 바꾸고 연결

for i in range(26):
    find(i)
DAT = [0] * 26

for i in range(26):
    DAT[root[i]] += 1
team = 0
indi = 0
for data in DAT:
    if data > 1:
        team += 1
    elif data == 1:
        indi += 1
print(team)
print(indi)
