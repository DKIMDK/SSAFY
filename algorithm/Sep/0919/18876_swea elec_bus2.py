'''
충전지를 교환하는 방식의 전기버스를 운행하려고 한다. 정류장에는 교체용 충전지가 있는 교환기가 있고, 충전지마다 최대로 운행할 수 있는 정류장 수가 정해져 있다.
충전지가 방전되기 전에 교체하며 운행해야 하는데 교체하는 시간을 줄이려면 최소한의 교체 횟수로 목적지에 도착해야 한다.
정류장과 충전지에 대한 정보가 주어질 때, 목적지에 도착하는데 필요한 최소한의 교환횟수를 출력하는 프로그램을 만드시오. 단, 출발지에서의 배터리 장착은 교환횟수에서 제외한다.
마지막 정류장에는 배터리가 없다.


[입력]
첫 줄에 테스트케이스의 수 T가 주어진다. 1<=T<=50
다음 줄부터 테스트 케이스의 별로 한 줄에 정류장 수 N, N-1개의 정류장 별 배터리 용량 Mi가 주어진다. 3<=N<=100, 0 ＜ Mi ＜ N

[출력]
각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다
'''

ans = []
# def sol(k):
#     global ans
    
#     if ans > N:
#         return
    
#     dist = Mi[k]
#     v = max(Mi[k + 1 : k + dist + 1])
#     ans.append(v)
    
#     sol(Mi.index(v))

def dfs(idx, sum_v):
    global answer
    if answer < sum_v:
        return
    # 현재 위치가 종점 이상이면 종점에 도달한 것이므로 최소 교환 횟수 갱신 및 종료
    if idx >= N:
        answer = sum_v
        return
    count = Mi[idx] # 현재 정류장의 배터리 용량을 가져옴
    for i in range(count, 0, -1):
        dfs(idx + i, sum_v + 1) # 현재 위치에서 i 만큼 이동, 교환 횟수 1 증가시켜 재귀


T = int(input())
for tc in range(1, T+1):
    answer = float('inf')
    Mi = list(map(int, input().split()))
    N = Mi.pop(0) - 1
    dfs(0, -1)
    print(f'#{tc} {answer}')
    
