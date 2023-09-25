'''
사다리 게임이 지겨워진 알고리즘 반 학생들이 새로운 게임을 만들었다. 가위바위보가 그려진 카드를 이용해 토너먼트로 한 명을 뽑는 것이다.
게임 룰은 다음과 같다.
1번부터 N번까지 N명의 학생이 N장의 카드를 나눠 갖는다.
전체를 두 개의 그룹으로 나누고, 그룹의 승자끼리 카드를 비교해서 이긴 사람이 최종 승자가 된다.
그룹의 승자는 그룹 내부를 다시 두 그룹으로 나눠 뽑는데, i번부터 j번까지 속한 그룹은 파이썬 연산으로 다음처럼 두개로 나눈다.
start ~ (start+end)//2
(start+end)//2 + 1 ~ end

두 그룹이 각각 1명이 되면 양 쪽의 카드를 비교해 승자를 가리고, 다시 더 큰 그룹의 승자를 뽑는 방식이다.
숫자 1은 가위, 2는 바위, 3은 보를 나타낸다.
만약 같은 카드인 경우 편의상 번호가 작은 쪽을 승자로 하고, 처음 선택한 카드는 바꾸지 않는다.

N명이 학생들이 카드를 골랐을 때 1등을 찾는 프로그램을 만드시오.

[입력]
첫 줄에 테스트 케이스 개수 T가 주어진다.  1≤T≤50
다음 줄부터 테스트 케이스의 별로 인원수 N과 다음 줄에 N명이 고른 카드가 번호순으로 주어진다. 4≤N≤100
카드의 숫자는 각각 1은 가위, 2는 바위, 3은 보를 나타낸다.

[출력]
각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 1등의 번호를 출력한다.
'''
def solution(group, start, end):
    if start == end:
        return start
    mid = (start + end) // 2
    left = solution(group, start, mid)
    right = solution(group, mid + 1, end)
    return winner(group, left, right)

def winner(group, a, b):
    if group[a] == group[b]:
        return a
    elif (group[a] - group[b] == 1) or (group[a] - group[b] == -2):
        return a
    else:
        return b




T = int(input())
for tc in range(1, T+1):
    N = int(input())
    group = list(map(int, input().split()))
    ans = solution(group, 0, N-1) + 1
    print(f'#{tc} {ans}')